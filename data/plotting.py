import matplotlib.pyplot as plt

import plotly.graph_objects as go
from plotly.subplots import make_subplots


### PLOTTING
## MATPLOTLIB
def plot_with_matplotlib(t_real, alt_meas, kalman_alt, alt_real, kalman_vel, vel_real, acc_noise, acc_real, P_trace):
    # altitude
    plt.subplot(4, 1, 1)
    plt.plot(t_real, alt_meas, '.g', label="altitude measurements")     #noised altitiude
    plt.plot(t_real, kalman_alt, 'b', label="estimated altitude")  #kalman altitiude
    plt.plot(t_real, alt_real, 'r', label="real height (ZOH)")      #measured altitiude
    plt.xlabel("Time [s]")
    plt.ylabel("Altitude [m]")
    plt.legend()
    plt.grid()

    # velocity
    plt.subplot(4, 1, 2)
    plt.plot(t_real, kalman_vel, 'b', label="estimated velocity")
    plt.plot(t_real, vel_real, '--r', label="real velocity")
    plt.xlabel("Time [s]")
    plt.ylabel("velocity [m/s]")
    plt.legend()
    plt.grid()

    # acceleration
    plt.subplot(4, 1, 3)
    plt.plot(t_real, acc_noise, '.m', label="acceleration with noise")
    plt.plot(t_real, acc_real, 'g', label="real acceleration")
    plt.xlabel("Time [s]")
    plt.ylabel("Acceleration [m/s^2]")
    plt.legend()
    plt.grid()

    # p trace
    plt.subplot(4, 1, 4)
    plt.plot(t_real, P_trace, 'b', label="P matrix trace")
    plt.xlabel("Time [s]")
    plt.ylabel("P matrix trace")
    plt.legend()
    plt.grid()

    plt.show()

### PLOTLY
def plot_with_plotly(t_real, alt_meas, kalman_alt, alt_real, kalman_vel, vel_real, acc_noise, acc_real):
    # Create subplots
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True, subplot_titles=("Altitude", "Velocity", "Acceleration"))

    # Altitude
    fig.add_trace(go.Scatter(x=t_real, y=alt_meas, mode='markers', name='altitude measurements', marker=dict(color='green')), row=1, col=1)
    fig.add_trace(go.Scatter(x=t_real, y=alt_real, mode='lines', name='real height (ZOH)', line=dict(color='red')), row=1, col=1)
    fig.add_trace(go.Scatter(x=t_real, y=kalman_alt, mode='lines', name='estimated altitude', line=dict(color='blue', dash='dash')), row=1, col=1)


    # Velocity
    fig.add_trace(go.Scatter(x=t_real, y=kalman_vel, mode='lines', name='estimated velocity', line=dict(color='blue')), row=2, col=1)
    fig.add_trace(go.Scatter(x=t_real, y=vel_real, mode='lines', name='real velocity', line=dict(color='red', dash='dash')), row=2, col=1)

    # Acceleration
    fig.add_trace(go.Scatter(x=t_real, y=acc_noise, mode='markers', name='acceleration with noise', marker=dict(color='magenta')), row=3, col=1)
    fig.add_trace(go.Scatter(x=t_real, y=acc_real, mode='lines', name='real acceleration', line=dict(color='green')), row=3, col=1)

    # Update layout
    fig.update_layout(height=900, width=800, title_text="Kalman Filter Data", showlegend=True)
    fig.update_xaxes(title_text="Time [s]", row=3, col=1)
    fig.update_yaxes(title_text="Altitude [m]", row=1, col=1)
    fig.update_yaxes(title_text="Velocity [m/s]", row=2, col=1)
    fig.update_yaxes(title_text="Acceleration [m/s^2]", row=3, col=1)

    fig.show()
