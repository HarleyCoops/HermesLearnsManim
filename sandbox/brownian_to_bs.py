"""
Brownian Motion to Black-Scholes
A Cosmic Journey Through Financial Mathematics

7-act cinematic animation connecting:
  standard deviation → Brownian motion → heat equation →
  Black-Scholes PDE → implied volatility surface
"""

from manim import *
import numpy as np


# ──────────────────────────────────────────────
# Color language
# ──────────────────────────────────────────────
STAR_WHITE = "#E8EAF6"
PALE_BLUE = "#90CAF9"
SIGMA_YELLOW = "#FFD54F"
DIFFUSION_TEAL = "#4DB6AC"
PRICING_BLUE = "#0288D1"
STRESS_RED = "#EF5350"
DEEP_BG = "#050510"
GOLD_TEXT = "#FFE082"
GHOST_ALPHA = 0.18


class BrownianToBlackScholes(ThreeDScene):
    """Full cinematic scene — seven acts in one continuous take."""

    def construct(self):
        self.camera.background_color = DEEP_BG

        # ════════════════════════════════════════
        # ACT 1 — Celestial Opening
        # ════════════════════════════════════════
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES)

        # Star field — lightweight Dot objects (NOT Dot3D)
        np.random.seed(42)
        n_stars = 90
        star_positions = np.random.uniform(-5, 5, (n_stars, 3))
        star_sizes = np.random.uniform(0.02, 0.05, n_stars)
        star_colors = [
            STAR_WHITE if np.random.random() > 0.35 else PALE_BLUE
            for _ in range(n_stars)
        ]

        stars = VGroup(*[
            Dot(point=pos, radius=sz, color=col).set_fill(opacity=0.85)
            for pos, sz, col in zip(star_positions, star_sizes, star_colors)
        ])

        self.play(FadeIn(stars), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.08)
        self.wait(0.5)

        # Title
        title = Text(
            "Brownian Motion to Black-Scholes",
            font_size=42, color=GOLD_TEXT, weight=BOLD,
        )
        subtitle = Text(
            "A Cosmic Journey Through Financial Mathematics",
            font_size=22, color=PALE_BLUE,
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, subtitle).move_to(ORIGIN)
        self.add_fixed_in_frame_mobjects(title_group)

        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(2.5)
        self.play(FadeOut(title_group), run_time=1.5)
        self.remove(title_group)

        # ════════════════════════════════════════
        # ACT 2 — Variability & Standard Deviation
        # ════════════════════════════════════════
        act2_label = Text("I.  Variability", font_size=26, color=SIGMA_YELLOW)
        act2_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act2_label)
        self.play(FadeIn(act2_label), run_time=0.8)

        # Collapse star field into a spherical cloud around origin
        cloud_positions = np.random.normal(0, 1.0, (n_stars, 3))
        cloud_dots = VGroup(*[
            Dot(point=pos, radius=0.035, color=PALE_BLUE).set_fill(opacity=0.8)
            for pos in cloud_positions
        ])

        self.play(
            ReplacementTransform(stars, cloud_dots),
            run_time=2.5,
            rate_func=smooth,
        )
        self.wait(0.5)

        # Mean marker — a small glowing dot, not a full Sphere
        mean_dot = Dot3D(point=ORIGIN, radius=0.08, color=SIGMA_YELLOW)
        mean_label = MathTex(r"\mu", font_size=34, color=SIGMA_YELLOW)
        mean_label.to_edge(RIGHT).shift(UP * 2)
        self.add_fixed_in_frame_mobjects(mean_label)

        self.play(FadeIn(mean_dot), FadeIn(mean_label), run_time=0.8)

        # Standard deviation equation
        sigma_eq = MathTex(
            r"\sigma = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(x_i - \mu)^2}",
            font_size=34, color=SIGMA_YELLOW,
        )
        sigma_eq.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(sigma_eq)
        self.play(Write(sigma_eq), run_time=2.5)
        self.wait(2.5)

        self.play(
            FadeOut(sigma_eq), FadeOut(mean_label), FadeOut(mean_dot),
            FadeOut(act2_label),
            run_time=1.2,
        )
        self.remove(sigma_eq, mean_label, act2_label)

        # ════════════════════════════════════════
        # ACT 3 — Brownian Motion
        # ════════════════════════════════════════
        act3_label = Text("II.  Brownian Motion", font_size=26, color=PALE_BLUE)
        act3_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act3_label)
        self.play(FadeIn(act3_label), run_time=0.8)

        # Generate Brownian paths (geometric Brownian motion)
        n_paths = 10
        n_steps = 100
        dt = 0.05
        mu_drift = 0.05
        sigma_vol = 0.3

        paths_data = []
        np.random.seed(7)
        for _ in range(n_paths):
            path = [np.array([0.0, 0.0, 0.0])]
            s = 1.0
            for step in range(n_steps):
                dw = np.random.normal(0, np.sqrt(dt))
                s *= np.exp((mu_drift - 0.5 * sigma_vol**2) * dt + sigma_vol * dw)
                t_coord = step * dt * 3 - 3       # x: time spread [-3, 3]
                y_val = (s - 1.0) * 2              # y: log-price displacement
                z_val = np.random.normal(0, 0.12)  # slight z dispersion
                path.append(np.array([t_coord, y_val, z_val]))
            paths_data.append(path)

        # Build path curves
        path_colors = [
            interpolate_color(ManimColor(PALE_BLUE), ManimColor(STAR_WHITE), i / n_paths)
            for i in range(n_paths)
        ]
        brownian_paths = VGroup()
        for i, pdata in enumerate(paths_data):
            curve = VMobject(color=path_colors[i], stroke_width=1.5, stroke_opacity=0.7)
            curve.set_points_smoothly([p for p in pdata[::4]])  # subsample
            brownian_paths.add(curve)

        # Transform cloud into paths
        self.play(FadeOut(cloud_dots), run_time=1)
        self.play(
            *[Create(p) for p in brownian_paths],
            run_time=3.5,
            rate_func=smooth,
        )

        # GBM equation
        gbm_eq = MathTex(
            r"S_t = S_0 \exp\!\left[\left(r - \tfrac{1}{2}\sigma^2\right)t"
            r"+ \sigma W_t\right]",
            font_size=32, color=WHITE,
        )
        gbm_eq.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(gbm_eq)
        self.play(Write(gbm_eq), run_time=2.5)
        self.wait(2)

        # Highlight endpoints — spread of outcomes
        endpoints = VGroup(*[
            Dot(point=paths_data[i][-1], radius=0.06, color=SIGMA_YELLOW)
            for i in range(n_paths)
        ])
        self.play(FadeIn(endpoints), run_time=1)
        self.wait(1.5)

        self.play(
            FadeOut(gbm_eq), FadeOut(act3_label), FadeOut(endpoints),
            run_time=1.2,
        )
        self.remove(gbm_eq, act3_label)

        # ════════════════════════════════════════
        # ACT 4 — Diffusion / Heat Equation
        # ════════════════════════════════════════
        act4_label = Text("III.  Diffusion", font_size=26, color=DIFFUSION_TEAL)
        act4_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act4_label)
        self.play(FadeIn(act4_label), run_time=0.8)

        # Smooth Gaussian diffusion surface
        def diffusion_surface(u, v):
            x = u
            t = v + 0.5
            sigma_t = 0.4 * np.sqrt(t + 0.3)
            z = (1.0 / (sigma_t * np.sqrt(2 * PI))) * np.exp(-x**2 / (2 * sigma_t**2))
            return np.array([x, v * 2 - 2, z * 3])

        diff_surface = Surface(
            diffusion_surface,
            u_range=[-3, 3],
            v_range=[0, 2],
            resolution=(40, 24),
            fill_opacity=0.6,
            stroke_width=0.3,
            stroke_color=DIFFUSION_TEAL,
            checkerboard_colors=[DIFFUSION_TEAL, "#26A69A"],
        )

        self.play(
            FadeOut(brownian_paths, run_time=1.5),
            Create(diff_surface, run_time=3.5),
        )
        self.wait(0.5)

        # Heat / diffusion equation
        heat_eq = MathTex(
            r"\frac{\partial f}{\partial t} = \frac{1}{2}\sigma^2 "
            r"\frac{\partial^2 f}{\partial x^2}",
            font_size=34, color=DIFFUSION_TEAL,
        )
        heat_eq.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(heat_eq)
        self.play(Write(heat_eq), run_time=2.5)
        self.wait(1)

        # Bridge annotation
        bridge_text = Text(
            "many random paths  →  one smooth PDE",
            font_size=20, color=WHITE,
        )
        bridge_text.next_to(heat_eq, UP, buff=0.3)
        self.add_fixed_in_frame_mobjects(bridge_text)
        self.play(FadeIn(bridge_text), run_time=1)
        self.wait(2.5)

        self.play(
            FadeOut(heat_eq), FadeOut(bridge_text), FadeOut(act4_label),
            run_time=1.2,
        )
        self.remove(heat_eq, bridge_text, act4_label)

        # ════════════════════════════════════════
        # ACT 5 — Black-Scholes Emergence
        # ════════════════════════════════════════
        act5_label = Text("IV.  Black-Scholes", font_size=26, color=PRICING_BLUE)
        act5_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act5_label)
        self.play(FadeIn(act5_label), run_time=0.8)

        # Pricing surface C(S, t)
        def pricing_surface(u, v):
            S = np.exp(u * 0.8 + 0.5)
            T = 1.0 - v * 0.45 + 0.1
            K = 1.5
            r_rate = 0.05
            sig = 0.3
            sqrt_T = np.sqrt(np.maximum(T, 0.01))
            d1 = (np.log(S / K) + (r_rate + 0.5 * sig**2) * T) / (sig * sqrt_T)
            nd1 = 0.5 * (1 + np.tanh(d1 * 0.7978845608))
            d2 = d1 - sig * sqrt_T
            nd2 = 0.5 * (1 + np.tanh(d2 * 0.7978845608))
            C = S * nd1 - K * np.exp(-r_rate * T) * nd2
            C = np.clip(C, 0, 5)
            return np.array([u, v * 4 - 2, C * 0.8])

        price_surface = Surface(
            pricing_surface,
            u_range=[-2, 3],
            v_range=[0, 2],
            resolution=(40, 24),
            fill_opacity=0.65,
            stroke_width=0.3,
            stroke_color=PRICING_BLUE,
            checkerboard_colors=[PRICING_BLUE, "#0277BD"],
        )

        self.play(
            ReplacementTransform(diff_surface, price_surface),
            run_time=3.5,
            rate_func=smooth,
        )

        # Axis labels
        s_label = Text("Stock Price (S)", font_size=16, color=WHITE)
        t_label = Text("Time (t)", font_size=16, color=WHITE)
        c_label = Text("Option Value C(S,t)", font_size=16, color=PRICING_BLUE)
        s_label.to_edge(RIGHT, buff=0.4).shift(DOWN * 1.5)
        t_label.to_edge(LEFT, buff=0.4).shift(DOWN * 1.5)
        c_label.to_edge(UP, buff=1.0).shift(RIGHT * 2)
        self.add_fixed_in_frame_mobjects(s_label, t_label, c_label)
        self.play(FadeIn(s_label), FadeIn(t_label), FadeIn(c_label), run_time=0.8)

        # Black-Scholes PDE
        bs_eq = MathTex(
            r"\frac{\partial C}{\partial t}"
            r"+ \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}"
            r"+ rS\frac{\partial C}{\partial S}"
            r"- rC = 0",
            font_size=28, color=WHITE,
        )
        bs_eq.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(bs_eq)
        self.play(Write(bs_eq), run_time=3.5)
        self.wait(3.5)

        self.play(
            FadeOut(bs_eq), FadeOut(act5_label),
            FadeOut(s_label), FadeOut(t_label), FadeOut(c_label),
            run_time=1.2,
        )
        self.remove(bs_eq, act5_label, s_label, t_label, c_label)

        # ════════════════════════════════════════
        # ACT 6 — Implied Volatility Surface
        # ════════════════════════════════════════
        act6_label = Text("V.  Implied Volatility", font_size=26, color=SIGMA_YELLOW)
        act6_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act6_label)
        self.play(FadeIn(act6_label), run_time=0.8)

        # IV surface σ(K, T) with skew and smile
        def iv_surface(u, v):
            K_moneyness = u
            T = v * 1.5 + 0.1
            base_vol = 0.25
            skew = -0.08 * K_moneyness
            smile = 0.03 * K_moneyness**2
            term_effect = 0.05 / (T + 0.2)
            sigma_iv = base_vol + skew + smile + term_effect
            sigma_iv = np.clip(sigma_iv, 0.08, 0.6)
            return np.array([u, v * 4 - 2, sigma_iv * 6 - 1])

        vol_surface = Surface(
            iv_surface,
            u_range=[-2.5, 2.5],
            v_range=[0, 2],
            resolution=(48, 24),
            fill_opacity=0.75,
            stroke_width=0.3,
            stroke_color=SIGMA_YELLOW,
        )
        vol_surface.set_color_by_gradient(
            PRICING_BLUE, DIFFUSION_TEAL, SIGMA_YELLOW, STRESS_RED,
        )

        self.play(
            ReplacementTransform(price_surface, vol_surface),
            run_time=3.5,
            rate_func=smooth,
        )

        # Axis labels
        k_label = Text("Strike (K)", font_size=16, color=WHITE)
        t2_label = Text("Expiry (T)", font_size=16, color=WHITE)
        iv_label = MathTex(
            r"\sigma_{\mathrm{imp}}(K, T)",
            font_size=28, color=SIGMA_YELLOW,
        )
        k_label.to_edge(RIGHT, buff=0.4).shift(DOWN * 1.5)
        t2_label.to_edge(LEFT, buff=0.4).shift(DOWN * 1.5)
        iv_label.to_edge(UP, buff=1.0).shift(RIGHT * 2)
        self.add_fixed_in_frame_mobjects(k_label, t2_label, iv_label)
        self.play(FadeIn(k_label), FadeIn(t2_label), FadeIn(iv_label), run_time=0.8)
        self.wait(2)

        # Skew annotation
        skew_note = Text(
            "volatility skew — deep OTM puts carry higher implied vol",
            font_size=17, color=STRESS_RED,
        )
        skew_note.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(skew_note)
        self.play(FadeIn(skew_note), run_time=1)
        self.wait(3)

        self.play(
            FadeOut(skew_note), FadeOut(act6_label),
            FadeOut(k_label), FadeOut(t2_label), FadeOut(iv_label),
            run_time=1.2,
        )
        self.remove(skew_note, act6_label, k_label, t2_label, iv_label)

        # ════════════════════════════════════════
        # ACT 7 — Finale: Convergence of Concepts
        # ════════════════════════════════════════
        act7_label = Text("VI.  Convergence", font_size=26, color=GOLD_TEXT)
        act7_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act7_label)
        self.play(FadeIn(act7_label), run_time=0.8)

        # Bring back ghosted Brownian paths (offset left, faded)
        ghost_paths = VGroup()
        for i, pdata in enumerate(paths_data[:5]):
            curve = VMobject(
                color=PALE_BLUE,
                stroke_width=1.0,
                stroke_opacity=GHOST_ALPHA,
            )
            curve.set_points_smoothly(
                [p * 0.4 + np.array([-3.5, -1.0, 0]) for p in pdata[::5]]
            )
            ghost_paths.add(curve)

        # Ghosted diffusion surface (small, offset)
        def ghost_diffusion(u, v):
            base = diffusion_surface(u * 0.5, v * 0.5)
            return base * 0.35 + np.array([-3.0, 1.5, 0])

        ghost_diff = Surface(
            ghost_diffusion,
            u_range=[-3, 3],
            v_range=[0, 2],
            resolution=(20, 12),
            fill_opacity=GHOST_ALPHA,
            stroke_width=0.2,
            stroke_color=DIFFUSION_TEAL,
            checkerboard_colors=[DIFFUSION_TEAL, "#26A69A"],
        )

        self.play(
            *[Create(p) for p in ghost_paths],
            Create(ghost_diff),
            run_time=2.5,
        )
        self.wait(1.5)

        # Final synthesis chain
        synthesis = MathTex(
            r"\text{Dispersion}",
            r"\;\xrightarrow{\;\sigma\;}\;",
            r"\text{Brownian Motion}",
            r"\;\xrightarrow{\;\text{PDE}\;}\;",
            r"\text{Black-Scholes}",
            r"\;\xrightarrow{\;\text{market}\;}\;",
            r"\sigma_{\mathrm{imp}}(K,T)",
            font_size=24, color=WHITE,
        )
        synthesis[0].set_color(PALE_BLUE)
        synthesis[2].set_color(STAR_WHITE)
        synthesis[4].set_color(PRICING_BLUE)
        synthesis[6].set_color(SIGMA_YELLOW)
        synthesis.to_edge(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(synthesis)
        self.play(Write(synthesis), run_time=3.5)
        self.wait(3)

        # Concluding title
        final_title = Text(
            "From randomness to structure — volatility is the thread.",
            font_size=22, color=GOLD_TEXT,
        )
        final_title.move_to(ORIGIN)
        self.add_fixed_in_frame_mobjects(final_title)
        self.play(FadeIn(final_title, shift=UP * 0.2), run_time=2)
        self.wait(4)

        # Graceful fadeout
        self.stop_ambient_camera_rotation()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            FadeOut(synthesis), FadeOut(final_title), FadeOut(act7_label),
            run_time=3,
        )
