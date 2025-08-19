from manim import *
import numpy as np

class ProjectileMotion(Scene):
    def construct(self):
        # --- Axes Section ---
        axes = Axes(
            x_range=[0, 12, 2],
            y_range=[0, 6, 1],
        )
        x_label = Text("x").next_to(axes.x_axis, RIGHT)
        y_label = Text("y").next_to(axes.y_axis, UP)
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label))
        # --- End Axes Section ---

        # Parameters
        v0 = 10
        angle_deg = 45
        g = 9.8

        angle_rad = np.deg2rad(angle_deg)
        t_flight = 2 * v0 * np.sin(angle_rad) / g

        # Ball (Dot)
        def trajectory(t):
            x = v0 * np.cos(angle_rad) * t
            y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
            return np.array([x, y, 0])

        ball = Dot(trajectory(0), color=YELLOW)
        self.play(FadeIn(ball))

        # Trajectory path
        path = ParametricFunction(trajectory, t_range=[0, t_flight], color=BLUE)
        self.play(Create(path))

        # Animate ball along path
        self.play(MoveAlongPath(ball, path), run_time=3, rate_func=linear)
        self.wait()

