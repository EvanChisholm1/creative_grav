from manim import *

class Calculation(Scene):
    def construct(self):

        center_circle = Circle(radius=0.5)
        center_circle.set_fill(PINK, opacity=0.5)

        # Create a second circle that will orbit around the center circle
        orbiting_circle = Circle(radius=0.2)
        orbiting_circle.set_fill(PINK, opacity=0.5)
        orbiting_circle.move_to(center_circle.get_center() + [3, 0, 0])

        self.play(Create(center_circle), Create(orbiting_circle), run_time=1)

        self.play(
            Rotate(mobject=orbiting_circle, about_point=(0.0, 0.0, 0.0), angle=30 * PI),
            run_time=16,
            rate_func=linear,
        )

        self.play(
            FadeOut(orbiting_circle),
            FadeOut(center_circle),
            run_time=1
        )

        given = Tex(r"""$G_a = 5.00 \frac{Nm^2}{kg^2}\break$$m_1 = 10.00 kg\break$$m_2 = 1.00 kg\break$$r = 0.500 m\break$$v = \mathord{?}$""", font_size=36)

        
        self.play(Write(given))
        self.wait(20)
        self.play(given.animate.shift(4 * LEFT))

        fg = MathTex(r"\vec{F_{ag}}", font_size=48)

        uni_grav_formula = MathTex(r"F_{ag} = \frac{G_Am_1m_2}{r^2}", font_size=36)
        disclaimer = Tex(r"let $F_{ag}$ represent force of artificial gravity")
        disclaimer.shift(3 * UP)
        self.play(Write(uni_grav_formula), Write(disclaimer), run_time=1)
        self.wait(10)
        
        fc_formula = MathTex(r"F_{c} = \frac{m_2v^2}{r}", font_size=36)
        self.play(uni_grav_formula.animate.shift(4 * RIGHT), FadeOut(disclaimer), run_time=1)
        self.play(Write(fc_formula), run_time=1)
        uni_grav_formula_fc = MathTex(r"F_{c} = \frac{G_Am_1m_2}{r^2}", font_size=36)
        uni_grav_formula_fc.shift(4 * RIGHT)
        self.wait(10)

        self.play(Transform(uni_grav_formula, uni_grav_formula_fc))
        self.play(FadeOut(uni_grav_formula_fc), FadeOut(uni_grav_formula))

        self.wait(1)
        joined_formula = MathTex(r"\frac{G_Am_1m_2}{r^2} = \frac{m_2v^2}{r}", font_size=36)
        self.play(Transform(fc_formula, joined_formula))
        self.wait(2)

        gross_v = MathTex(r"v = \pm\sqrt{\frac{G_Am_1m_2}{r^2m_2}}", font_size=36)
        self.play(Transform(fc_formula, gross_v))
        self.wait(2)

        v_formula = MathTex(r"v = \pm\sqrt{\frac{G_Am_1}{r}}", font_size=36)
        self.play(Transform(fc_formula, v_formula))

        self.wait(1)
        plugged_in_v = MathTex(r"v = \pm\sqrt{\frac{5.00 \frac{Nm^2}{kg^2} \cdot 10.00 kg}{0.500 m}}", font_size=36)
        self.play(Transform(fc_formula, plugged_in_v))
        self.wait(2)

        answer = MathTex(r"v = 14.1 \frac{m}{s}", font_size=36)
        disclaimer = Text("*We get rid of the negative sign because speed is a scalar quantity", font_size=24)
        disclaimer.shift(3 * DOWN)
        self.play(Transform(fc_formula, answer), Write(disclaimer))

        self.wait(5)

        # conclusion = Tex(r"""$\\therefore$ The velocity of the object is 14.14 $\frac{m}{s}$""", font_size=36)



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

        fg = MathTex(r"\vec{F_{ag}}", font_size=48)
        fg.shift(2 * LEFT)
        uni_grav_formula = MathTex(r"\vec{F_{ag}} = \frac{Gm_1m_2}{r^2}", font_size=48)
        uni_grav_formula.shift(2 * LEFT)

        m1_label = MathTex(r"m_1", font_size=48)
        m1_label.shift(2*RIGHT)

        m2_label = MathTex(r"m_2", font_size=48)
        m2_label.shift(2*RIGHT + [3, 0.4, 0])

        self.play(
            Write(fg),
            Write(m1_label),
            Write(m2_label)
        )
        self.wait(1)

        self.play(
            Transform(fg, uni_grav_formula),
        )
        # self.remove_foreground_mobjects()

        
