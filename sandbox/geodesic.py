from manim import *
import numpy as np


class GeodesicEquation(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.camera.background_color = "#F0F0F0"

        # --- Title ---
        title = Text("Geodesic Equation", font_size=56, color=BLACK, weight=BOLD)
        title.to_edge(UP).shift(DOWN * 0.3)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=2)
        self.wait(1)

        # --- Main Equation ---
        eq = MathTex(
            r"\frac{d^2 x^\alpha}{d\tau^2}",
            r"+",
            r"\Gamma^\alpha_{\beta\gamma}",
            r"\frac{dx^\beta}{d\tau}",
            r"\frac{dx^\gamma}{d\tau}",
            r"= 0",
            font_size=40,
            color=BLACK,
        )
        eq.next_to(title, DOWN, buff=0.4)

        # Color code the terms
        eq[0].set_color("#D32F2F")   # acceleration - red
        eq[2].set_color("#1565C0")   # Christoffel - blue
        eq[3].set_color("#2E7D32")   # velocity beta - green
        eq[4].set_color("#2E7D32")   # velocity gamma - green

        self.add_fixed_in_frame_mobjects(eq)
        self.play(Write(eq), run_time=3)
        self.wait(1)

        # --- Labels for terms ---
        accel_label = Text("acceleration", font_size=18, color="#D32F2F")
        accel_label.next_to(eq[0], DOWN, buff=0.25)

        christoffel_label = Text("curvature", font_size=18, color="#1565C0")
        christoffel_label.next_to(eq[2], DOWN, buff=0.25)

        vel_label = Text("velocity", font_size=18, color="#2E7D32")
        vel_label.next_to(eq[3:5], DOWN, buff=0.25)

        self.add_fixed_in_frame_mobjects(accel_label, christoffel_label, vel_label)
        self.play(
            FadeIn(accel_label),
            FadeIn(christoffel_label),
            FadeIn(vel_label),
            run_time=1.5,
        )
        self.wait(2)

        # Fade out labels, keep equation
        self.play(
            FadeOut(accel_label),
            FadeOut(christoffel_label),
            FadeOut(vel_label),
        )
        self.remove(accel_label, christoffel_label, vel_label)

        # Shift equation and title up smaller
        title2 = Text("Geodesic Equation", font_size=28, color=BLACK, weight=BOLD)
        title2.to_corner(UL)
        eq2 = MathTex(
            r"\frac{d^2 x^\alpha}{d\tau^2} + \Gamma^\alpha_{\beta\gamma}"
            r"\frac{dx^\beta}{d\tau} \frac{dx^\gamma}{d\tau} = 0",
            font_size=26,
            color=BLACK,
        )
        eq2.to_corner(UR)

        self.add_fixed_in_frame_mobjects(title2, eq2)
        self.play(
            ReplacementTransform(title, title2),
            ReplacementTransform(eq, eq2),
            run_time=1.5,
        )

        # --- 3D Curved Surface (sphere) ---
        sphere = Surface(
            lambda u, v: np.array([
                2 * np.cos(u) * np.cos(v),
                2 * np.cos(u) * np.sin(v),
                2 * np.sin(u),
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            resolution=(32, 64),
            fill_opacity=0.3,
            stroke_width=0.5,
            stroke_color=GREY,
            checkerboard_colors=["#B3E5FC", "#81D4FA"],
        )

        self.play(Create(sphere), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(1)

        # --- Geodesic path (great circle arc) ---
        def great_circle(t):
            phi = -PI / 3 + t * (2 * PI / 3)
            theta = PI / 4 + 0.3 * np.sin(2 * t)
            return np.array([
                2 * np.cos(phi) * np.cos(theta),
                2 * np.cos(phi) * np.sin(theta),
                2 * np.sin(phi),
            ])

        geodesic_path = ParametricFunction(
            great_circle,
            t_range=[0, 1],
            color="#FF6F00",
            stroke_width=4,
        )

        geodesic_label = Text("geodesic", font_size=22, color="#FF6F00")
        geodesic_label.to_edge(DOWN).shift(UP * 0.5)
        self.add_fixed_in_frame_mobjects(geodesic_label)

        self.play(Create(geodesic_path), FadeIn(geodesic_label), run_time=2)
        self.wait(1)

        # --- Non-geodesic (wobbly) path ---
        def non_geodesic(t):
            phi = -PI / 3 + t * (2 * PI / 3)
            theta = PI / 4 + 0.3 * np.sin(2 * t) + 0.4 * np.sin(5 * t)
            return np.array([
                2 * np.cos(phi) * np.cos(theta),
                2 * np.cos(phi) * np.sin(theta),
                2 * np.sin(phi),
            ])

        non_geodesic_path = ParametricFunction(
            non_geodesic,
            t_range=[0, 1],
            color="#7B1FA2",
            stroke_width=3,
            stroke_opacity=0.8,
        )

        non_geo_label = Text("non-geodesic", font_size=22, color="#7B1FA2")
        non_geo_label.next_to(geodesic_label, RIGHT, buff=1)
        self.add_fixed_in_frame_mobjects(non_geo_label)

        self.play(Create(non_geodesic_path), FadeIn(non_geo_label), run_time=2)
        self.wait(1)

        # --- Moving particle along geodesic ---
        particle = Sphere(radius=0.08, color="#FF6F00").set_fill("#FF6F00")
        self.play(FadeIn(particle))

        self.play(
            MoveAlongPath(particle, geodesic_path),
            run_time=4,
            rate_func=smooth,
        )
        self.wait(1)

        # --- Christoffel symbol definition ---
        christoffel_eq = MathTex(
            r"\Gamma^\alpha_{\beta\gamma} = \frac{1}{2} g^{\alpha\delta}"
            r"\left( \frac{\partial g_{\delta\beta}}{\partial x^\gamma}"
            r"+ \frac{\partial g_{\delta\gamma}}{\partial x^\beta}"
            r"- \frac{\partial g_{\beta\gamma}}{\partial x^\delta} \right)",
            font_size=28,
            color=BLACK,
        )
        christoffel_eq.to_edge(DOWN, buff=0.3)

        self.play(
            FadeOut(geodesic_label),
            FadeOut(non_geo_label),
            run_time=0.5,
        )
        self.remove(geodesic_label, non_geo_label)
        self.add_fixed_in_frame_mobjects(christoffel_eq)
        self.play(Write(christoffel_eq), run_time=3)
        self.wait(2)

        # --- Tangent vector on geodesic ---
        t_val = 0.4
        pos = great_circle(t_val)
        dt = 0.001
        tangent_dir = (great_circle(t_val + dt) - great_circle(t_val - dt)) / (2 * dt)
        tangent_dir = tangent_dir / np.linalg.norm(tangent_dir) * 0.8

        arrow = Arrow3D(
            start=pos,
            end=pos + tangent_dir,
            color="#D32F2F",
        )

        tangent_label = Text("tangent vector", font_size=20, color="#D32F2F")
        tangent_label.move_to(UP * 2.5 + RIGHT * 3)
        self.add_fixed_in_frame_mobjects(tangent_label)

        self.play(Create(arrow), FadeIn(tangent_label), run_time=1.5)
        self.wait(3)

        # --- Final rotation and fade ---
        self.play(
            FadeOut(christoffel_eq),
            FadeOut(tangent_label),
            run_time=1,
        )
        self.remove(christoffel_eq, tangent_label)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2,
        )
