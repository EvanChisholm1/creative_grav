from manim import *

class Explainer(Scene):
    def construct(self):
        mass_a = Circle(radius=1, color=RED)
        mass_b = Circle(radius=1, color=RED)

        mass_a.set_fill(RED, opacity=0.5)
        mass_b.set_fill(RED, opacity=0.5)

        mass_a.shift(3 * LEFT)
        mass_b.shift(3 * RIGHT)

        self.play(
            Create(mass_a),
            Create(mass_b)
        )

        BIG_G = MathTex(r"G")
        BIG_G.shift(2 * DOWN)

        arrow_a = Arrow(start=(2 * LEFT), end=([0, 0, 0]), color=RED)
        arrow_b = Arrow(start=(2 * RIGHT), end=([0, 0, 0]), color=BLUE)

        self.play(
            Create(arrow_a),
            Create(arrow_b)
        )

        self.wait(5)

        label = MathTex(r"\vec{F_{ga}}")

        label.shift(UP)

        self.play(
            Write(label),
            Write(BIG_G)
        )

        self.wait(5)

        self.play(
            Transform(arrow_a, Arrow(start=(2 * LEFT), end=(2 * RIGHT), color=RED)),
            Transform(arrow_b, Arrow(start=(2 * RIGHT), end=(2 * LEFT), color=BLUE)),
            Transform(BIG_G, MathTex(r"G", font_size=350).shift(2 * DOWN))
        )

        self.wait(5)

        self.play(
            Transform(arrow_a, Arrow(start=(2 * LEFT), end=(1 * LEFT), color=RED)),
            Transform(arrow_b, Arrow(start=(2 * RIGHT), end=(1 * RIGHT), color=BLUE)),
            Transform(BIG_G, MathTex(r"G", font_size=20).shift(2 * DOWN))
        )

        self.wait(5)