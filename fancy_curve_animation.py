'''
Fancy Curve Animation
Creates an MP4 video showing a closed loop being twisted back and forth

Thai Nguyen
June 18, 2017
'''
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


# Calculate k parameter
def calculate_k(time):
    freq = 1 / video_duration
    angular_freq = 2 * np.pi * freq
    amplitude = 2 * np.pi
    return amplitude * np.sin(angular_freq * time)


# Calculate parametric curve
def calculate_curve(k):
    f = k * np.cos(t)
    x = 5 * np.cos(f) * np.sin(t)
    y = 5 * np.sin(f) * np.sin(t)
    z = 5 * np.cos(t)
    return x, y, z


# Plot curve
def plot_curve(x, y, z, k):
    ax.plot(x, y, z, antialiased=True)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(-5, 5)
    ax.set_axis_off()
    str  = '$k = %1.2f$\n' %k
    str += '$x = 5\cos(f(t))\sin(t)$\n'
    str += '$y = 5\sin(f(t))\cos(t)$\n'
    str += '$z = 5\cos(t)$'
    ax.text(0.1, 0.1, 5, str, transform=ax.transAxes)
    return fig


# Make frame
def make_frame(time):
    ax.clear()
    k = calculate_k(time)
    x, y, z = calculate_curve(k)
    fig = plot_curve(x, y, z, k)
    return mplfig_to_npimage(fig)


if __name__ == '__main__':
    # Initial parameters
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    t = np.linspace(0, 2 * np.pi, 250)
    video_duration = 10  # time in seconds

    # Create video file
    animation = VideoClip(make_frame, duration=video_duration)
    animation.write_videofile('fancy_curve.mp4', fps=60)
