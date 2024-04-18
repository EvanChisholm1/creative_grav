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
            MathTex(r"v_1 = 0"),
            MathTex(r"v_2 = 375\frac{m}{s}"),
            MathTex(r"\vec{\Delta d} = 0.114m"),
            MathTex(r"r = \vec{\Delta d}"),
            MathTex(r"m_1 = 0.00745kg"),
            MathTex(r"m_2 = 1.00kg"),
            MathTex(r"G = \mathord{?}")
        )

        let_Ga_rep = Tex(r"let $G_a$ represent the artificial gravitational constant")
        let_Ga_rep.shift(3 * DOWN)

        self.play(
            Write(given.arrange(DOWN, aligned_edge=LEFT).scale(0.75)),
            Write(let_Ga_rep)
        )

        self.wait(1)

        self.play(
            given.animate.shift(5 * LEFT).scale(0.8),
            FadeOut(let_Ga_rep)
        )

        newton_motion = MathTex(r"\vec{v_2^2} = \vec{v_1^2} + 2\vec{a}\vec{\Delta d}")
        self.play(Write(newton_motion))

        self.wait(1)

        newton_motion_rearranged = MathTex(r"\vec{a} = \frac{\vec{v_2^2} - \vec{v_1^2}}{2\vec{\Delta d}}")
        self.play(Transform(newton_motion, newton_motion_rearranged))

        newton_motion_substituted = MathTex(r"\vec{a} = \frac{(375\frac{m}{s})^2 - 0}{2(0.114kg)}")
        self.wait(1)

        self.play(Transform(newton_motion, newton_motion_substituted))
        self.wait(1)

        newton_motion_calculated = MathTex(r"\vec{a} = 616776.3158\frac{m}{s^2}")
        self.play(Transform(newton_motion, newton_motion_calculated))

        self.wait(1)

        self.play(
            newton_motion.animate.shift(2 * DOWN + 5 * LEFT).scale(0.8 * 0.75),
        )

        f_net = MathTex(r"\vec{F_{net}} = m_1\vec{a}")

        self.play(Write(f_net))

        self.wait(1)

        self.play(
            f_net.animate.shift(5 * RIGHT)
        )
        self.wait(1)

        f_ga = MathTex(r"\vec{F_{ga}} = \frac{G_am_1m_2}{r^2}")
        let_f_ga_rep = Tex(r"let $F_{ga}$ represent the force of artificial gravity")
        let_f_ga_rep.shift(3 * DOWN)
        self.play(Write(f_ga), Write(let_f_ga_rep))
        self.wait(1)

        self.play(
            f_ga.animate.shift(5 * RIGHT + 2 * DOWN),
            FadeOut(let_f_ga_rep)
        )

        f_ga_eq_f_net = MathTex(r"\vec{F_{ga}} = \vec{F_{net}}")
        self.play(Write(f_ga_eq_f_net))
        self.wait(1)

        f_ga_eq_f_net_equations = MathTex(r"\frac{G_am_1m_2}{r^2} = m_1\vec{a}")
        self.play(
            Transform(f_ga_eq_f_net, f_ga_eq_f_net_equations)
        )
        self.wait(1)

        rearanged_f_ga_eq_f_net_equations = MathTex(r"G_a = \frac{m_1\vec{a}r^2}{m_1m_2}")
        self.play(
            Transform(f_ga_eq_f_net, rearanged_f_ga_eq_f_net_equations)
        )

        simplified_f_ga_eq_f_net_equations = MathTex(r"G_a = \frac{\vec{a}r^2}{m_2}")

        self.wait(1)
        self.play(
            Transform(f_ga_eq_f_net, simplified_f_ga_eq_f_net_equations)
        )

        self.wait(1)
        subbed_f_ga_eq_f_net_equations = MathTex(r"G_a = \frac{616776.3158\frac{m}{s^2}(0.114m)^2}{1.00kg}")

        self.play(
            Transform(f_ga_eq_f_net, subbed_f_ga_eq_f_net_equations)
        )

        self.wait(1)

        calculated_f_ga_eq_f_net_equations = MathTex(r"G_a = 70312.5\frac{Nm^2}{kg}")

        self.play(
            Transform(f_ga_eq_f_net, calculated_f_ga_eq_f_net_equations)
        )

        self.wait(1)

        conclusion = Tex(r"$\therefore$ the artificial gravitational constant between our acceleration and our bullet at 0.114m away from each other should be $70300\frac{Nm^2}{kg}$ to get the same force as a glock shooting a bullet.", font_size=24)
        conclusion.shift(3 * DOWN)

        self.play(
            Write(conclusion)
        )


        # f_ga = MathTex(r"\vec{F_{ga}} = \vec{F_{net}}")
