import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
from typing import Tuple, Optional
import logging


class Preprocessor:
    """
    Data preprocessing for ML models:
    - Feature engineering
    - Scaling
    - Handling missing values
    """

    def __init__(self, scaler_type: str = "minmax"):
        """
        scaler_type: 'minmax' or 'standard'
        """
        self.scaler_type = scaler_type
        self.scaler = None

        if scaler_type == "minmax":
            self.scaler = MinMaxScaler()
        elif scaler_type == "standard":
            self.scaler = StandardScaler()
        else:
            raise ValueError("Invalid scaler_type, choose 'minmax' or 'standard'")

        self.imputer = SimpleImputer(strategy="mean")
        logging.info(f"Preprocessor initialized with {scaler_type} scaler.")

    # ────────────────────────────────────────────────
    # CLEAN DATA
    # ────────────────────────────────────────────────
    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fills missing values and removes duplicates.
        """
        df = df.copy()
        df = df.drop_duplicates()
        df.iloc[:, :] = self.imputer.fit_transform(df)
        return df

    # ────────────────────────────────────────────────
    # FEATURE ENGINEERING
    # ────────────────────────────────────────────────
    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Creates derived features commonly used for stock prediction.
        Example: Returns, moving averages, volatility
        """
        df = df.copy()

        if "close" in df.columns:
            df["return"] = df["close"].pct_change().fillna(0)
            df["log_return"] = np.log1p(df["return"])

        if "volume" in df.columns:
            df["volume_change"] = df["volume"].pct_change().fillna(0)

        # Rolling features
        if "close" in df.columns:
            df["ma_5"] = df["close"].rolling(window=5).mean().fillna(method="bfill")
            df["ma_10"] = df["close"].rolling(window=10).mean().fillna(method="bfill")
            df["volatility_5"] = df["close"].rolling(window=5).std().fillna(0)

        return df

    # ────────────────────────────────────────────────
    # SCALE FEATURES
    # ────────────────────────────────────────────────
    def scale_features(self, df: pd.DataFrame, fit: bool = True) -> pd.DataFrame:
        """
        Scales numeric features using the chosen scaler
        """
        df = df.copy()
        numeric_cols = df.select_dtypes(include=np.number).columns

        if fit:
            df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        else:
            df[numeric_cols] = self.scaler.transform(df[numeric_cols])

        return df

    # ────────────────────────────────────────────────
    # FULL PIPELINE
    # ────────────────────────────────────────────────
    def process(
        self, df: pd.DataFrame, fit_scaler: bool = True
    ) -> pd.DataFrame:
        """
        Clean, engineer, and scale data in one step
        """
        df = self.clean_data(df)
        df = self.engineer_features(df)
        df = self.scale_features(df, fit=fit_scaler)
        return df

    # ────────────────────────────────────────────────
    # SEQUENCE CREATION FOR LSTM
    # ────────────────────────────────────────────────
    def create_sequences(self, data: pd.DataFrame, seq_length: int, target_col: str) -> Tuple[np.ndarray, np.ndarray]:
        """
        Converts DataFrame to sequences for LSTM training
        """
        sequences = []
        targets = []
        values = data[target_col].values

        for i in range(len(values) - seq_length):
            seq = values[i:i+seq_length]
            label = values[i+seq_length]
            sequences.append(seq)
            targets.append(label)

        return np.array(sequences).reshape(-1, seq_length, 1), np.array(targets)
