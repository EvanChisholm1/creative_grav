from manim import *

class Orbit(Scene):
    def construct(self):
        center_circle = Circle(radius=0.5, color=PINK)
        center_circle.set_fill(PINK, opacity=0.5)
        # self.add(center_circle)

        # Create a second circle that will orbit around the center circle
        orbiting_circle = Circle(radius=0.2)
        orbiting_circle.set_fill(PINK, opacity=0.5)
        orbiting_circle.move_to(center_circle.get_center() + [3, 0, 0])

        self.play(Create(center_circle), Create(orbiting_circle))

        # Animate the orbiting circle
        
        self.play(
            # orbiting_circle.animate.orbit(2 * PI, about_point=center_circle.get_center()),
            Rotate(mobject=orbiting_circle, about_point=(0.0, 0.0, 0.0), angle=4 * PI),
            run_time=5,
            rate_func=linear,
        )

        self.play(
            center_circle.animate.shift(2 * RIGHT),
            orbiting_circle.animate.shift(2 * RIGHT),
        )

        uni_grav_formula = MathTex(r"\vec{F_ag}")
        self.play(
            Create(uni_grav_formula)
        )