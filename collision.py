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
            MathTex(r"m_1 = 70.0kg"),
            MathTex(r"m_2 = 60.0kg"),
            MathTex(r"\vec{v_{1}} = 7.5 \frac{m}{s} \text{[forward]}"),
            MathTex(r"\vec{v_{2}} = 6.75 \frac{m}{s} \text{[backward]}"),
            MathTex(r"\vec{v'}} = ?"),
            MathTex(r"E_{ktotal}' = ?"),
        )

        self.play(
            Write(given.arrange(DOWN, aligned_edge=LEFT).scale(0.75))
        )

        self.wait(1)

        self.play(
            given.animate.shift(5 * LEFT + 2 * UP).scale(0.8)
        )

        self.wait(1)

        completely_inelastic_disclaimer = VGroup(
            MathTex(r"\text{Completely Inelastic Collision}"),
            MathTex(r"\vec{v_{1}'} = \vec{v_{2}'} = \vec{v'}"),
        )

        self.play(
            Write(completely_inelastic_disclaimer.arrange(DOWN).scale(0.75))
        )

        self.wait(1)
        self.play(
            completely_inelastic_disclaimer.animate.shift(3 * UP).scale(0.8)
        )

        conservation_of_momentum = MathTex(r"\vec{P_{total}} = \vec{P_{total}'}")

        self.play(
            Write(conservation_of_momentum)
        )

        self.wait(1)

        self.play(
            Transform(conservation_of_momentum, MathTex(r"\vec{P_1} + \vec{P_2} = \vec{P_1'} + \vec{P_2'}"))
        )

        self.play(
            Transform(conservation_of_momentum, MathTex(r"\vec{P_1} + \vec{P_2} = \vec{P_1'} + \vec{P_2'}"))
        )

        self.wait(1)

        self.play(
            Transform(conservation_of_momentum, MathTex(r"m_1\vec{v_1} + m_2\vec{v_2} = m_1\vec{v'} + m_2\vec{v'}"))
        )

        self.wait(1)

        self.play(
            Transform(conservation_of_momentum, MathTex(r"m_1\vec{v_1} + m_2\vec{v_2} = (m_1 + m_2)\vec{v'}"))
        )

        self.wait(1)

        self.play(
            Transform(conservation_of_momentum, MathTex(r"\vec{v'} = \frac{m_1\vec{v_1} + m_2\vec{v_2}}{m_1 + m_2}"))
        )

        self.wait(1)

        positive_direction = MathTex(r"\text{[forward]+ve}")
        positive_direction.shift(2 * UP)

        self.play(
            Write(positive_direction),
            Transform(conservation_of_momentum, MathTex(r"\vec{v'} = \frac{(70.0kg)(7.5\frac{m}{s}\text{[forward]}) + (60.0kg)(6.75\frac{m}{s}\text{[backward]})}{70.0kg + 60.0kg}", font_size=30))
        )

        self.wait(1)

        self.play(
            Transform(conservation_of_momentum, MathTex(r"\vec{v'} = \frac{(70.0kg)(7.5\frac{m}{s}) + (60.0kg)(-6.75\frac{m}{s})}{70.0kg + 60.0kg}", font_size=30))
        )

        self.wait(1)

        self.play(
            Transform(conservation_of_momentum, MathTex(r"\vec{v'} = 0.9230769 \frac{m}{s} \text{[forward]}"))
        )

        self.wait(1)

        self.play(
            conservation_of_momentum.animate.shift(1 * DOWN + 5 * LEFT).scale(0.8 * 0.75)
        )

        self.wait(1)

        Ek_total_prime = MathTex(r"E_{ktotal}' = \frac{1}{2}m_1{v'}^2 + \frac{1}{2}m_2{v'}^2")

        self.play(
            Write(Ek_total_prime)
        )

        self.wait(1)

        self.play(
            Transform(Ek_total_prime, MathTex(r"E_{ktotal}' = \frac{1}{2}(m_1 + m_1)v'^2"))
        )

        self.wait(5)

        self.play(
            Transform(Ek_total_prime, MathTex(r"E_{ktotal}' = \frac{1}{2}(70.0kg + 60.0kg)(0.9230769\frac{m}{s})^2"))
        )

        self.wait(1)

        self.play(
            Transform(Ek_total_prime, MathTex(r"E_{ktotal}' = 55.38461538J"))
        )

        self.wait(1)

        therefore = Tex(r"$\therefore$ we can conclude that the final velocity of the two 'gravball' players is $0.9230769\frac{m}{s}$ [forward] and the final total kinetic energy of the two players is $55.38461538J$", font_size=24)
        therefore.shift(3 * DOWN)

        self.play(
            Write(therefore)
        )

        self.wait(1)
