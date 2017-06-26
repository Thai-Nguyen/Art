'''
Circle and Asteroid
Creates an MP4 video of an curve going from a circle to asteroid

Thai Nguyen
June 19, 2017
'''
import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


# Calculate k parameter
def calculate_k(time):
    freq = 1 / video_duration
    angular_freq = 2 * np.pi * freq
    amplitude = 5
    return amplitude * np.sin(angular_freq * time)


# Calculate parametric curve
def calculate_curve(k):
    x = np.cos(theta) * (1 - k * np.sin(theta) ** 2)
    y = np.sin(theta) * (1 - k * np.cos(theta) ** 2)
    return x, y


# Plot curve
def plot_curve(x, y, k):
    ax.plot(x, y, antialiased=True)
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    str = '$k = %1.2f$\n' % k
    str += '$x = \\cos \\theta(1-k\\sin(\\theta))$\n'
    str += '$y = \\sin \\theta(1-k\\cos(\\theta))$'
    ax.text(-3.75, -3.75, str)
    return fig


# Make frame
def make_frame(time):
    ax.clear()
    k = calculate_k(time)
    x, y = calculate_curve(k)
    fig = plot_curve(x, y, k)
    return mplfig_to_npimage(fig)


if __name__ == '__main__':
    # Initial parameters
    fig = plt.figure()
    ax = fig.gca()
    theta = np.linspace(0, 2 * np.pi, 250)
    video_duration = 10  # time in seconds

    # Create video file
    animation = VideoClip(make_frame, duration=video_duration)
    animation.write_videofile('circle_and_asteroid.mp4', fps=60)
