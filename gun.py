from manim import *

class Gun(Scene):
    def construct(self):
        bullet = Circle(radius=0.5)
        accelerator = Circle(radius=1)
        accelerator.set_fill(RED, opacity=0.5)
        bullet.set_fill(RED, opacity=0.5)
        bullet.shift(4 * LEFT)
        accelerator.shift(2 * RIGHT)

        self.play(
            Create(bullet),
            Create(accelerator)
        )

        f_ag_arrow = Arrow(start=3*LEFT, end = RIGHT)

        f_ag_arrow_label = MathTex(r"\vec{F_{ag}}")
        f_ag_arrow_label.shift(2 * LEFT + 0.5 * UP)
        self.play(Create(f_ag_arrow), Write(f_ag_arrow_label))

        n_up = 2
        self.play(
            bullet.animate.shift(n_up * UP),
            accelerator.animate.shift(n_up * UP),
            f_ag_arrow.animate.shift(n_up * UP),
            f_ag_arrow_label.animate.shift(n_up * UP),
        )

        given = VGroup()
        given.add(
            
            MathTex("v = [insert vel]"),
            MathTex(r"G = \mathord{?}")
        )

        self.play(
            Write(given.arrange(DOWN))
        )
