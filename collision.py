from manim import *

class Collision(Scene):
    def construct(self):
        object_a = Circle(radius=0.5)
        object_b = Circle(radius=0.5)
        object_a.set_fill(RED, opacity=0.5)
        object_b.set_fill(RED, opacity=0.5)
        object_a.shift(4 * LEFT)
        object_b.shift(2 * RIGHT)

        self.play(
            Create(object_a),
            Create(object_b)
        )

        self.play(
            object_a.animate.shift(5 * RIGHT),
            rate_func=linear
        )
        self.play(
            object_b.animate.shift(7 * RIGHT),
            object_a.animate.shift(7 * RIGHT),
            run_time=2.5,
            rate_func=linear
        )

        self.wait(1)

        given = VGroup(
            MathTex(r"m_a = 60.0kg"),
            MathTex(r"m_b = 70.0kg"),
            MathTex(r"")
        )
