from manim import *

class Balanced(Scene):
    def construct(self):
        self.wait(5)

        mass = Circle(radius=1)
        mass.set_fill(RED, opacity=0.5)

        fg_arrow = Arrow(start=DOWN, end=(DOWN * 3))
        art_fg_arrow = Arrow(start=UP, end=(UP * 3))

        self.play(Create(mass))
        self.play(Create(fg_arrow), Create(art_fg_arrow))

        fg_label = MathTex(r"\vec{F_{g}}")
        art_fg_label = MathTex(r"\vec{F_{ga}}")

        self.wait(1)

        fg_label.shift(2 * DOWN + 1 * RIGHT)
        art_fg_label.shift(2 * UP + 1 * RIGHT)

        self.play(Write(fg_label), Write(art_fg_label))

        self.wait(1)

        self.play(
            mass.animate.shift(4 * LEFT),
            fg_arrow.animate.shift(4 * LEFT),
            art_fg_arrow.animate.shift(4 * LEFT),
            fg_label.animate.shift(4 * LEFT),
            art_fg_label.animate.shift(4 * LEFT),
        )
        self.wait(1)

        eq = MathTex(r"F_{ga} = F_{g}")

        net = MathTex(r"\vec{F_{net}} = \vec{F_{ga}} + \vec{F_{g}}")

        self.play(Write(eq))
        self.play(eq.animate.shift(3 * UP))

        self.play(Write(net))
    
        # self.play(Write(net))
        self.wait(1)
        self.play(
            Transform(net, MathTex(r"\vec{F_{net}} = 0"))
        )

        self.wait(5)
