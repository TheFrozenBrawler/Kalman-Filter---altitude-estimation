import numpy as np

class KalmanFilter:
    def __init__(self, A, B, H, Q, R, P, x):
        self.A = A  # State transition matrix
        self.B = B  # Control input matrix
        self.H = H  # Observation matrix
        self.Q = Q  # Process noise covariance
        self.R = R  # Measurement noise covariance
        self.P = P  # Estimate error covariance
        self.x = x  # State estimate

    def predict(self, u):
        # Predict the state and estimate covariance
        # x = A*X + B*u
        self.x = self.A @ self.x + self.B * u

        # P_pred = A*P*A_T + Q
        self.P = self.A @ self.P @ self.A.T + self.Q

    def update(self, z):
        # Kalman gain
        # K = P*H.T * inv(H * P * H.T + R)
        K = self.P @ self.H.T / (self.H @ self.P @ self.H.T + self.R)
        # K = 0

        # Update the state estimate
        # x_curr = x*K*(z-H*x)
        self.x = self.x + K * (z - self.H @ self.x)

        # Update the estimate covariance
        # P_curr = (I-K*H) * P (I-KH).T + K*R*K.T
        self.P = (np.eye(self.P.shape[0]) - K * self.H) @ self.P @ (np.eye(self.P.shape[0]) - K * self.H).T + (K*self.R@K.T)

        return self.x[0][0]
    