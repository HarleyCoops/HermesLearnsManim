"""
Artemis II - Lunar Flyby
A cinematic 3D Manim scene telling the story of the 2026 Artemis II mission:
the first crewed lunar flyby in over 50 years, a free-return trajectory,
and a new human-spaceflight distance record of 252,756 miles.
"""

from manim import *
import numpy as np


# ──────────────────────────────────────────────
# Color language (from analysis.json.cinematic_defaults)
# ──────────────────────────────────────────────
DEEP_BG = "#050510"
STAR_WHITE = "#E8EAF6"
PALE_BLUE = "#90CAF9"
GOLD_TEXT = "#FFE082"
EARTH_BLUE = "#1E88E5"
MOON_GREY = "#BDBDBD"
ARTEMIS_ORANGE = "#FF7043"
APOLLO_GHOST = "#9E9E9E"
RECORD_RED = "#E53935"


# ──────────────────────────────────────────────
# Trajectory helpers
# ──────────────────────────────────────────────
def artemis_path(t):
    """Artemis II free-return. t in [0, 1]. Out, around Moon, back to Earth."""
    angle = PI * t
    x = 2.0 * (1 - np.cos(angle)) + 0.3 * np.sin(2 * PI * t)
    y = 1.8 * np.sin(angle) * (1 - 0.25 * np.sin(PI * t))
    z = 0.35 * np.sin(2 * PI * t)
    return np.array([x, y, z])


def apollo_path(t):
    """Apollo 13 ghost arc — slightly smaller apex, otherwise similar shape."""
    angle = PI * t
    x = 1.85 * (1 - np.cos(angle)) + 0.25 * np.sin(2 * PI * t)
    y = 1.6 * np.sin(angle) * (1 - 0.25 * np.sin(PI * t))
    z = 0.28 * np.sin(2 * PI * t) - 0.15
    return np.array([x, y, z])


class ArtemisIiLunarFlyby(ThreeDScene):
    """Full cinematic scene — five acts in one continuous take."""

    def construct(self):
        self.camera.background_color = DEEP_BG
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES)

        # ════════════════════════════════════════
        # ACT 1 — Cold Open: "A record set in silence"
        # ════════════════════════════════════════

        # Starfield — lightweight Dot objects with 3D points (NOT Dot3D)
        np.random.seed(42)
        n_stars = 90
        star_positions = np.random.uniform(-6, 6, (n_stars, 3))
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

        # Earth at origin
        earth = Sphere(
            radius=1.0,
            resolution=(24, 48),
            fill_opacity=0.9,
            stroke_width=0.3,
            stroke_color=PALE_BLUE,
            checkerboard_colors=[EARTH_BLUE, "#1565C0"],
        )
        self.play(FadeIn(earth), run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.10)

        # Title + subtitle (fixed in frame)
        title = Text(
            "Artemis II",
            font_size=52, color=GOLD_TEXT, weight=BOLD,
        )
        subtitle = Text(
            "252,756 miles from home",
            font_size=26, color=PALE_BLUE,
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, subtitle).move_to(ORIGIN).shift(UP * 0.2)
        self.add_fixed_in_frame_mobjects(title_group)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=1.2)
        self.play(FadeIn(subtitle), run_time=0.9)
        self.wait(1.2)

        subtitle2 = Text(
            "A new human-spaceflight record",
            font_size=24, color=GOLD_TEXT,
        )
        subtitle2.move_to(subtitle.get_center())
        self.add_fixed_in_frame_mobjects(subtitle2)
        self.play(ReplacementTransform(subtitle, subtitle2), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle2), run_time=1.0)
        self.remove(title, subtitle2)

        # ════════════════════════════════════════
        # ACT 2 — The Players: Earth, Moon, Orion
        # ════════════════════════════════════════
        act2_label = Text("I.  The Players", font_size=24, color=GOLD_TEXT)
        act2_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act2_label)
        self.play(FadeIn(act2_label), run_time=0.6)

        # Moon slides in from the right
        moon = Sphere(
            radius=0.27,
            resolution=(18, 36),
            fill_opacity=0.95,
            stroke_width=0.2,
            stroke_color=WHITE,
            checkerboard_colors=[MOON_GREY, "#9E9E9E"],
        )
        moon.move_to(np.array([6.5, 0, 0]))
        self.add(moon)
        self.play(
            moon.animate.move_to(np.array([4.0, 0, 0])),
            run_time=2.0, rate_func=smooth,
        )

        # Dashed Earth-Moon line
        em_line = DashedLine(
            start=np.array([1.05, 0, 0]),
            end=np.array([3.73, 0, 0]),
            color=PALE_BLUE, stroke_width=2, dash_length=0.12,
        )
        em_eq = MathTex(
            r"r_{EM} \approx 238{,}855\ \text{mi}",
            font_size=28, color=PALE_BLUE,
        )
        em_eq.to_edge(UP, buff=0.8)
        self.add_fixed_in_frame_mobjects(em_eq)
        self.play(Create(em_line), Write(em_eq), run_time=1.8)
        self.wait(1.2)

        # Crew caption strip
        crew_caption = Text(
            "Reid Wiseman  \u00b7  Victor Glover  \u00b7  "
            "Christina Koch  \u00b7  Jeremy Hansen",
            font_size=20, color=STAR_WHITE,
        )
        crew_caption.to_edge(DOWN, buff=0.4)
        self.add_fixed_in_frame_mobjects(crew_caption)
        self.play(FadeIn(crew_caption), run_time=1.0)
        self.wait(2.0)

        self.play(
            FadeOut(em_line), FadeOut(em_eq), FadeOut(crew_caption),
            FadeOut(act2_label),
            run_time=1.0,
        )
        self.remove(em_line, em_eq, crew_caption, act2_label)

        # ════════════════════════════════════════
        # ACT 3 — The Trajectory: free-return geometry
        # ════════════════════════════════════════
        act3_label = Text("II.  Free-Return Trajectory", font_size=24, color=ARTEMIS_ORANGE)
        act3_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act3_label)
        self.play(FadeIn(act3_label), run_time=0.6)

        # Artemis II orange parametric path
        artemis_curve = ParametricFunction(
            artemis_path,
            t_range=[0, 1],
            color=ARTEMIS_ORANGE,
            stroke_width=5,
        )

        self.play(Create(artemis_curve), run_time=4.0, rate_func=smooth)
        self.wait(0.5)

        # Orion particle traverses the path
        orion = Sphere(radius=0.09, color=ARTEMIS_ORANGE).set_fill(ARTEMIS_ORANGE, opacity=1.0)
        orion.move_to(artemis_path(0.0))
        self.play(FadeIn(orion), run_time=0.5)
        self.play(
            MoveAlongPath(orion, artemis_curve),
            run_time=4.5, rate_func=smooth,
        )

        # Newton's second law / two-body equation of motion
        motion_eq = MathTex(
            r"\ddot{\mathbf{r}} = -\tfrac{\mu}{r^3}\,\mathbf{r}",
            font_size=30, color=WHITE,
        )
        motion_eq.to_edge(UP, buff=0.8)
        self.add_fixed_in_frame_mobjects(motion_eq)
        self.play(Write(motion_eq), run_time=1.8)

        fail_safe = Text(
            "If the engines failed, geometry alone would bring them home.",
            font_size=20, color=GOLD_TEXT,
        )
        fail_safe.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(fail_safe)
        self.play(FadeIn(fail_safe), run_time=1.2)
        self.wait(2.2)

        self.play(
            FadeOut(motion_eq), FadeOut(fail_safe),
            FadeOut(orion), FadeOut(act3_label),
            run_time=1.0,
        )
        self.remove(motion_eq, fail_safe, orion, act3_label)

        # ════════════════════════════════════════
        # ACT 4 — The Record: Apollo 13 vs Artemis II
        # ════════════════════════════════════════
        act4_label = Text("III.  The Record", font_size=24, color=RECORD_RED)
        act4_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act4_label)
        self.play(FadeIn(act4_label), run_time=0.6)

        # Apollo 13 ghost arc
        apollo_curve = ParametricFunction(
            apollo_path,
            t_range=[0, 1],
            color=APOLLO_GHOST,
            stroke_width=3,
            stroke_opacity=0.45,
        )

        apollo_label_3d = Text("Apollo 13 (1970)", font_size=18, color=APOLLO_GHOST)
        apollo_label_3d.to_corner(UR).shift(DOWN * 0.2)
        self.add_fixed_in_frame_mobjects(apollo_label_3d)

        artemis_label_3d = Text("Artemis II (2026)", font_size=18, color=ARTEMIS_ORANGE)
        artemis_label_3d.next_to(apollo_label_3d, DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(artemis_label_3d)

        self.play(
            Create(apollo_curve),
            FadeIn(apollo_label_3d), FadeIn(artemis_label_3d),
            run_time=2.5,
        )
        self.wait(0.6)

        # Pulsing red dot at the Artemis II apex (midpoint of path)
        apex_pt = artemis_path(0.5)
        apex_dot = Dot(point=apex_pt, radius=0.12, color=RECORD_RED).set_fill(RECORD_RED, opacity=1.0)
        apex_ring = Circle(radius=0.22, color=RECORD_RED, stroke_width=3).move_to(apex_pt)

        # Record label (fixed in frame for readability)
        record_label = MathTex(
            r"252{,}756\ \text{mi}",
            font_size=30, color=RECORD_RED,
        )
        record_label.to_edge(UP, buff=0.8)
        self.add_fixed_in_frame_mobjects(record_label)

        self.play(
            FadeIn(apex_dot), Create(apex_ring),
            Write(record_label),
            run_time=1.2,
        )
        # Pulse the ring twice
        self.play(
            apex_ring.animate.scale(1.6).set_stroke(opacity=0.1),
            run_time=1.0, rate_func=smooth,
        )
        self.play(
            apex_ring.animate.scale(1 / 1.6).set_stroke(opacity=1.0),
            run_time=0.8, rate_func=smooth,
        )

        # Delta equation
        delta_eq = MathTex(
            r"d_{A2} - d_{A13} = 252{,}756 - 248{,}645 = 4{,}111\ \text{mi}",
            font_size=30, color=GOLD_TEXT,
        )
        delta_eq.to_edge(DOWN, buff=0.5)
        self.add_fixed_in_frame_mobjects(delta_eq)
        self.play(Write(delta_eq), run_time=2.5)
        self.wait(2.5)

        self.play(
            FadeOut(record_label), FadeOut(delta_eq),
            FadeOut(apex_ring), FadeOut(apex_dot),
            FadeOut(apollo_curve),
            FadeOut(apollo_label_3d), FadeOut(artemis_label_3d),
            FadeOut(act4_label),
            run_time=1.2,
        )
        self.remove(
            record_label, delta_eq, apex_ring, apex_dot,
            apollo_curve, apollo_label_3d, artemis_label_3d, act4_label,
        )

        # ════════════════════════════════════════
        # ACT 5 — The Return: splashdown
        # ════════════════════════════════════════
        act5_label = Text("IV.  Splashdown", font_size=24, color=EARTH_BLUE)
        act5_label.to_corner(UL)
        self.add_fixed_in_frame_mobjects(act5_label)
        self.play(FadeIn(act5_label), run_time=0.6)

        # Orion returns — small orange dot traversing the back half of the arc
        orion_return = Sphere(radius=0.09, color=ARTEMIS_ORANGE).set_fill(ARTEMIS_ORANGE, opacity=1.0)
        orion_return.move_to(artemis_path(0.5))
        self.play(FadeIn(orion_return), run_time=0.4)

        # Build a tail segment of the trajectory (apex back to Earth)
        return_curve = ParametricFunction(
            artemis_path,
            t_range=[0.5, 1.0],
            color=ARTEMIS_ORANGE,
            stroke_width=4,
            stroke_opacity=0.9,
        )
        self.play(
            MoveAlongPath(orion_return, return_curve),
            run_time=3.5, rate_func=smooth,
        )

        # Splashdown caption (fixed in frame)
        splashdown = Text(
            "Splashdown \u2014 2026-04-10, 5:07 PM PDT, Pacific Ocean",
            font_size=22, color=GOLD_TEXT,
        )
        splashdown.to_edge(DOWN, buff=0.6)
        self.add_fixed_in_frame_mobjects(splashdown)
        self.play(FadeIn(splashdown, shift=UP * 0.2), run_time=1.2)

        # Roll credits: crew names
        credits = Text(
            "Reid Wiseman  \u00b7  Victor Glover  \u00b7  "
            "Christina Koch  \u00b7  Jeremy Hansen",
            font_size=18, color=PALE_BLUE,
        )
        credits.next_to(splashdown, UP, buff=0.3)
        self.add_fixed_in_frame_mobjects(credits)
        self.play(FadeIn(credits), run_time=1.0)
        self.wait(3.0)

        # Graceful fade
        self.stop_ambient_camera_rotation()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2.5,
        )
