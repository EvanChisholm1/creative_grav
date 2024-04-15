from manim import *

class Orbit(Scene):
    def construct(self):
        center_circle = Circle(radius=0.5, color=BLUE)
        center_circle.set_fill(BLUE, opacity=0.5)
        # self.add(center_circle)

        # Create a second circle that will orbit around the center circle
        orbiting_circle = Circle(radius=0.2)
        orbiting_circle.set_fill(PINK, opacity=0.5)
        orbiting_circle.move_to(center_circle.get_center() + [3, 0, 0])

        self.play(Create(center_circle), Create(orbiting_circle))

        # Animate the orbiting circle
        
        self.play(
            # orbiting_circle.animate.orbit(2 * PI, about_point=center_circle.get_center()),
            Rotate(mobject=orbiting_circle, about_point=(0.0, 0.0, 0.0), angle=2 * PI),
            center_circle.animate.shift(LEFT),
            run_time=5,
            rate_func=linear,
        )
