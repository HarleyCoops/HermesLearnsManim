# Starter Prompts

These prompts were pulled from the old `Math-To-Manim` repo and kept here as jumpstart material.

They are included in full text form so you can paste them directly into Hermes.
A few broken characters from older files were normalized for readability.

## Cinematic Cosmology

Source: `examples/cosmology/Claude37Cosmic.py`, `docs/AGENT_ARCHITECTURE.md`

```text
Create a gorgeous, cinematic Manim animation called "Cosmology: The Story of Our Universe".

Goal:
Build an awe-filled reverse-knowledge-tree style explanation of cosmology. Start from spacetime and observational clues, then expand outward into the history of the universe: expansion, redshift, the cosmic microwave background, and the Friedmann equation. The result should feel like a premium science documentary opening, not a dry classroom diagram.

Visual style:
- Use ThreeDScene.
- Background should be deep black or near-black with subtle blue cosmic gradients.
- Open with a dense star field with depth, twinkling, and slow parallax camera motion.
- Use elegant glowing text, clean MathTex, and consistent color coding.
- Favor deliberate camera moves, ambient rotation, and layered compositions over fast cuts.
- Keep the aesthetic cinematic and cosmic: volumetric-feeling space, luminous equations, and careful transitions.

Color language:
- spacetime / geometry: blue and cyan
- matter / density: orange
- curvature: purple
- radiation / light: gold
- observational evidence / labels: white or pale yellow

Narrative requirements:
1. Opening cosmic vista.
   - Fade in a star field representing the observable universe.
   - Reveal the title "Cosmology: The Story of Our Universe" in large glowing text.
   - Make the first 5-10 seconds feel expansive and prestigious.

2. Spacetime as the stage.
   - Introduce a 3D spacetime coordinate system or wireframe.
   - Show the Minkowski metric:
     ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2
   - Use color coding to distinguish temporal and spatial parts.
   - Briefly establish that cosmology is built on the geometry of spacetime.

3. Light, causality, and observation.
   - Show a light cone or expanding spherical light front.
   - Connect the idea that astronomy is seeing light from the past.
   - Make the viewer feel that looking farther away means looking farther back in time.

4. Cosmic expansion.
   - Transition from static stars to galaxies embedded in an expanding grid or fabric.
   - Show galaxies separating as the scale factor grows.
   - Include Hubble's Law:
     v = H_0 d
   - Make it visually clear that space itself is stretching, not just galaxies flying through empty space.

5. Redshift as evidence.
   - Animate wavelengths stretching as the universe expands.
   - Include a redshift relation such as:
     1 + z = lambda_observed / lambda_emitted
   - Link the stretched wavelength directly to cosmic expansion.
   - Use color changes to show light moving toward the red end of the spectrum.

6. The early universe and the CMB.
   - Rewind from the large modern universe into a hot dense early state.
   - Show the universe becoming opaque plasma, then transitioning to transparency.
   - Introduce the cosmic microwave background as an afterglow shell or sky map.
   - Suggest tiny primordial fluctuations that later seed structure formation.

7. The Friedmann equation as the governing law.
   - Present the Friedmann equation prominently:
     ((dot a)/a)^2 = (8 pi G / 3) rho - (k c^2 / a^2)
   - Optionally include a simplified version first, then the fuller form.
   - Color code:
     - dot a / a in cyan
     - rho in orange
     - k in purple
   - Explain visually that expansion rate depends on energy density and curvature.

8. Timeline of cosmic history.
   - Show a clean visual progression:
     Big Bang -> rapid expansion -> plasma era -> recombination / CMB -> first stars -> galaxies -> large-scale structure -> present universe
   - Use icons, labels, or a glowing timeline in space.
   - Keep the pacing smooth and cumulative.

9. Modern cosmic composition.
   - Briefly visualize ordinary matter, dark matter, and dark energy as distinct components.
   - This should be elegant and suggestive, not overly cluttered.
   - If helpful, show a pie chart transforming into large-scale structure and accelerated expansion motifs.

10. Ending shot.
   - Return to a majestic wide cosmic view.
   - Re-show the Friedmann equation or the title in a refined final composition.
   - End with a sense that cosmology unifies geometry, light, and cosmic history.

Technical guidance:
- Use raw string MathTex for all LaTeX.
- Prefer 3D camera work and layered depth over flat slides.
- Keep text readable against the dark background.
- Use smooth fades, transforms, and scale transitions.
- Make the animation long enough to feel like a journey, not a quick demo.

Deliverable:
Generate complete, runnable Manim Community Edition code for a cinematic cosmology scene or scene sequence that combines observational evidence, spacetime geometry, and universe evolution into one coherent narrative.
```

## Epic QED Journey

Source: `examples/misc/ULTRAQED.py`, `examples/cosmology/Claude37Cosmic.py`

```text
Create an epic cinematic 3D Manim animation explaining Quantum Electrodynamics as a journey from spacetime and classical electromagnetism to gauge symmetry, particle interactions, and the running coupling.

Core objective:
Make QED feel visually inevitable. The viewer should start with light and spacetime, then watch Maxwell theory compress into relativistic form, then see the QED Lagrangian emerge as the compact law governing electrons, photons, and their interactions.

Visual style:
- Use ThreeDScene with a deep black cosmic background.
- Open with a star field and premium title treatment.
- Use glow, contrast, and restrained neon colors rather than cartoon colors.
- Keep the visuals elegant, high-end, and physics-forward.
- Camera should drift, orbit, and reframe smoothly to give a sense of scale.

Color language:
- photons / electromagnetic field: gold
- fermions / electrons: orange or blue-orange contrast
- gauge structure / covariant derivative: green
- spacetime / geometry: blue and cyan
- symmetry highlights: violet

Required structure:
1. Cosmic opening.
   - Begin with a star field and a strong title, such as:
     "Quantum Electrodynamics"
     "A Journey into the Electromagnetic Interaction"
   - The opening should feel large and cinematic.

2. Spacetime arena.
   - Build a 3D spacetime grid or wireframe.
   - Show a future and past light cone.
   - Display the Minkowski metric:
     ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2
   - Use color coding to distinguish time from space.

3. Electromagnetic wave emergence.
   - Zoom into the spacetime arena and show orthogonal E and B field oscillations.
   - Clearly indicate propagation direction.
   - Make the wave feel alive and physical, not just symbolic.

4. Maxwell equations to relativistic compression.
   - Present the classical Maxwell equations first:
     div E = rho / epsilon_0
     div B = 0
     curl E = - dB/dt
     curl B = mu_0 J + mu_0 epsilon_0 dE/dt
   - Then transform them into a compact relativistic form:
     partial_mu F^{mu nu} = mu_0 J^nu
   - Emphasize the conceptual payoff: four equations condense into elegant spacetime structure.

5. QED Lagrangian reveal.
   - Make this the centerpiece.
   - Display:
     L_QED = psi_bar ( i gamma^mu D_mu - m ) psi - 1/4 F_{mu nu} F^{mu nu}
   - Put it on a refined dark panel or luminous plane.
   - Color code the fermion term, gauge-field term, and interaction structure.
   - Explicitly highlight the covariant derivative:
     D_mu = partial_mu + i e A_mu
   - Explain visually that this is where interaction enters.

6. Gauge symmetry.
   - Show the local U(1) gauge transformation:
     psi(x) -> e^{i alpha(x)} psi(x)
     A_mu(x) -> A_mu(x) - (1/e) partial_mu alpha(x)
   - Make the animation communicate that the Lagrangian remains unchanged.
   - Use circular motion, phase rotation, or local phase markers to make symmetry feel dynamic.

7. Feynman interaction layer.
   - Introduce multiple Feynman diagrams, not just one.
   - Include at least:
     - electron-electron scattering
     - pair annihilation
     - pair creation
   - Label the electron, positron, and photon lines clearly.
   - The diagrams should emerge as visual consequences of the interaction term, not as disconnected clip art.

8. Fine structure constant.
   - Present:
     alpha = e^2 / (4 pi epsilon_0 hbar c) approximately 1/137
   - Explain that this is the coupling strength of electromagnetic interaction.
   - Add a few concise interpretations:
     - dimensionless constant
     - controls interaction strength
     - appears in atomic fine structure

9. Running coupling and vacuum polarization.
   - Show a graph of alpha(Q) versus energy scale.
   - The curve should rise gently with energy.
   - Add labeled scales such as m_e, M_W, M_Z, or Planck scale if useful.
   - Explain visually that vacuum polarization from virtual pairs modifies the effective coupling.
   - If you include caption text, keep it concise and elegant.

10. Final synthesis.
   - Build a final collage or unified composition containing:
     - spacetime / light cone
     - electromagnetic wave
     - QED Lagrangian
     - Feynman diagram motifs
     - running coupling graph
   - End with a strong concluding title such as:
     "QED: Unifying Light and Matter Through Gauge Theory"

Technical requirements:
- Use raw string MathTex for equations.
- Keep the visual pacing premium and deliberate.
- Avoid clutter even though the subject is dense.
- Prefer clean transformations that show one idea becoming the next.
- Make the code runnable in Manim Community Edition.

Deliverable:
Generate complete, polished Manim code for a cinematic multi-part QED animation that moves from classical electromagnetism to gauge theory and quantum interactions with strong visual continuity.
```

## Brownian Motion to Black-Scholes

Source: `examples/finance/optionskew.py`, `Gemini3/finance_pipeline_output.json`

```text
Create a cinematic 3D Manim animation that connects randomness, diffusion, and finance through the chain:

standard deviation -> Brownian motion -> heat equation -> Black-Scholes PDE -> implied volatility surface

Goal:
Make quantitative finance feel visually deep and mathematically coherent. The animation should not look like a corporate dashboard. It should feel like a cosmic mathematical journey from microscopic randomness to a full volatility surface.

Visual style:
- Use ThreeDScene.
- Start with a dark celestial background and a field of stars or luminous particles.
- Use elegant camera motion and premium color grading.
- Let the animation move from abstract stochastic motion into structured geometry and surfaces.
- Keep the aesthetic cinematic and mathematically serious.

Color language:
- randomness / particles: white and pale blue
- volatility / sigma objects: yellow
- diffusion / heat flow: blue-green
- pricing surface: teal to blue
- implied volatility skew / stress regions: yellow to red

Required sequence:
1. Celestial opening.
   - Begin with a star field or particle field.
   - Reveal a title such as:
     "Brownian Motion to Black-Scholes"
     or
     "A Cosmic Journey Through Financial Mathematics"
   - The opening should feel atmospheric rather than business-like.

2. Variability and standard deviation.
   - Transform the star field into a point cloud or spherical cloud around a center.
   - Display:
     sigma = sqrt((1/N) sum_{i=1}^N (x_i - mu)^2)
   - Show the mean mu at the center and visually indicate dispersion around it.
   - Make this feel like the first organizing principle extracted from randomness.

3. Brownian motion.
   - Morph the point cloud into multiple 3D random paths.
   - Display a stochastic-process expression such as:
     S_t = S_0 exp((r - 1/2 sigma^2)t + sigma W_t)
   - Emphasize that the motion is pathwise, noisy, and cumulative.
   - Highlight endpoints or trajectories so the viewer feels the spread of possible outcomes.

4. Diffusion / heat equation bridge.
   - Let the random paths melt or blend into a smooth evolving surface.
   - Display the diffusion equation:
     partial f / partial t = (1/2) sigma^2 partial^2 f / partial x^2
   - Make the visual transformation communicate that many random microscopic paths aggregate into a smooth PDE-level description.

5. Black-Scholes emergence.
   - Introduce 3D axes for asset price, time, and option value.
   - Display the Black-Scholes PDE:
     partial C / partial t + (1/2) sigma^2 S^2 partial^2 C / partial S^2 + r S partial C / partial S - r C = 0
   - Grow a pricing surface from the diffusion-like geometry.
   - Make it clear that the pricing PDE is the finance analogue of diffusion under the right change of interpretation.

6. Implied volatility surface.
   - Transform the pricing surface into an implied volatility surface:
     sigma(K, T)
   - Use a shape that suggests skew or smile rather than a flat plane.
   - Label axes clearly and orbit the camera around the surface.
   - Color the surface by value so the geometry feels informative and alive.

7. Finale: convergence of concepts.
   - Bring back ghosted traces of the earlier stages:
     - dispersion cloud
     - Brownian paths
     - diffusion surface
   - Compose them around the final volatility surface.
   - End with a concluding line that connects probability, PDEs, and pricing.

Conceptual requirements:
- The story must clearly communicate why the sequence is meaningful, not just visually flashy.
- Show that volatility is first statistical dispersion, then stochastic forcing, then diffusion, then derivative pricing, then an observed market surface.
- Keep the tone educational but sophisticated.

Technical guidance:
- Use raw string MathTex.
- Keep equations readable and stable while the 3D camera moves.
- Prefer smooth transformations and layered staging over abrupt cuts.
- Make the final implied vol surface visually striking enough to serve as a thumbnail moment.

Deliverable:
Generate complete runnable Manim Community Edition code for a cinematic finance animation that unifies Brownian motion, diffusion, Black-Scholes, and volatility skew in one coherent visual narrative.
```

## Geodesic Equation

Source: `Gemini3/geodesic_prompt.txt`

```text
Create a gorgeous, cinematic 3D Manim animation explaining the Geodesic Equation.

Visual Style:
- Use a 3D scene (ThreeDScene).
- Set the background color to an elegant off-white (e.g., "#F0F0F0" or similar) with dark text/math (BLACK or darker gray) for high contrast.
- Use smooth camera movements (ambient_camera_rotation) to showcase the 3D nature.

Content to Animate:
1. Title: "Geodesic Equation" (bold, elegant font).
2. The Main Equation:
   $\frac{d^2x^\alpha}{d\tau^2} + \Gamma^\alpha_{\beta\gamma} \frac{dx^\beta}{d\tau} \frac{dx^\gamma}{d\tau} = 0$
   - Explain that this describes a particle's motion under gravity in General Relativity.
   - Highlight the terms:
     - $\frac{d^2x^\alpha}{d\tau^2}$: Acceleration / 4-acceleration.
     - $\Gamma^\alpha_{\beta\gamma}$: Christoffel symbols (encodes curvature).
     - $\frac{dx^\beta}{d\tau}, \frac{dx^\gamma}{d\tau}$: Velocity / 4-velocity components.

3. The Christoffel Symbol Definition:
   $\Gamma^\alpha_{\beta\gamma} = \frac{1}{2}g^{\alpha\delta}(\frac{\partial g_{\delta\beta}}{\partial x^\gamma} + \frac{\partial g_{\delta\gamma}}{\partial x^\beta} - \frac{\partial g_{\beta\gamma}}{\partial x^\delta})$
   - Show this appearing below or connected to the main equation.
   - Annotate "spacetime metric" ($g_{\alpha\delta}$) and its derivatives.

4. 3D Visualization:
   - Illustrate the concept with a curved surface (e.g., a sphere or a parametric surface) in 3D.
   - Show a "particle" (a dot) moving along a geodesic (shortest path) on this surface vs a non-geodesic path.
   - Visualize tangent vectors or normal vectors if it helps explain the "straightest possible line" concept in curved space.

Make the transitions smooth and the explanation clear. Use colors to link equation terms to the visual elements on the 3D surface.
```

## Whiskering Exchange Law

Source: `Gemini3/whiskering_prompt.txt`

```text
Explain and visualize the Whiskering Exchange Law (Interchange Law) in 2-categories.

Concept:
In a 2-category, the whiskering exchange law describes the compatibility between horizontal and vertical composition of 2-cells. It states that composing 2-cells vertically and then horizontally yields the same result as composing them horizontally and then vertically.

Visual Requirements:
- The animation must be made within an off-white 3D space.
- Use orange and blue highlights for the 2-cells and their compositions to clearly distinguish the two paths of composition (horizontal then vertical vs vertical then horizontal).
- The style should be clean, modern, and mathematically precise.

Technical Details / LaTeX from Image:
The concept generalizes the following composition in a 2-category:
$$A(a,b)(f,g) \times A(a,b)(g,h) \xrightarrow{\circ} A(a,b)(f,h)$$

The Whiskering Exchange Law diagram involves:
- Maps $\eta_j: \prod_{i=1}^n P_{ij}(a_{i-1}, a_i) \to Q_j(La_0, Ra_n)$
- Map $\alpha: \prod_{i=1}^n X_i(f_{ij-1}, f_{ij}) \to Y(\eta_0(f_{i0}), \eta_1(f_{i1}))$

The core commutative diagram to visualize is:
$$A(a,b)(f,g) \times A(a,b)(g,h) \xrightarrow{\circ_0} A(a,c)(f' \circ f, g' \circ g) \times A(a,c)(g' \circ g, h' \circ h)$$
$$\times A(b,c)(f',g') \times A(b,c)(g',h')$$

Please generate a Manim scene `WhiskeringExchangeScene` that visualizes this concept.
- Start with the basic objects (0-cells), morphisms (1-cells), and 2-morphisms (2-cells).
- Illustrate the two different ways to compose the 2-cells (vertical then horizontal vs horizontal then vertical).
- Use the 3D camera to show the structure clearly.
- Render the LaTeX equations clearly in the off-white space.
```

## Klein Bottle and Mobius Strip

Source: `Gemini3/complex_prompt.txt`

```text
Create a Manim animation illustrating the topological concept of a Klein Bottle and its relation to a Mobius Strip.
The animation should:
1. Start by visualizing a 2D Mobius Strip being formed from a rectangular strip.
2. Evolve into a 3D visualization of a Klein Bottle, showing its "impossible" self-intersection in 3D space.
3. Use a grid or parametric surface to clearly show the curvature and single-sided nature.
4. Animate a small particle traversing the surface to demonstrate that it can visit both "sides" without crossing an edge (non-orientability).
5. Include mathematical annotations for the parametric equations of the Klein Bottle.
6. Use a color scheme that highlights the geometry (e.g., semi-transparent surface with wireframe).
7. End with the object rotating to show all angles.
```

## Taylor Series Topology of Convergence

Source: `Gemini3/taylor_prompt.txt`

```text
Create an educational 3D animation on the Taylor Series.
Use the provided image (which contains various Taylor series expansions) as a reference for the specific mathematical formulas to visualize.
The key goal is to specifically demonstrate the topology of convergence.
- Show how the approximation surface "hugs" the target function surface closer and closer as terms are added.
- Use 3D surfaces, not just 2D lines.
- Make it visually gorgeous with high-quality rendering, lighting, and camera movements.
- Include a maximum topology demonstration where we see the domain of convergence or the function manifold being approximated.
- The tone should be awe-inspiring and educational.
```

## Pythagorean Theorem Verbose Teaching Prompt

Source: `.claude/plugins/math-to-manim/skills/math-to-manim/examples/pythagorean-theorem/verbose-prompt.txt`

```text
# Manim Animation: Pythagorean Theorem

## Overview
This animation builds the Pythagorean theorem from first principles through a carefully
constructed knowledge tree. Each concept is explained with mathematical rigor
and visual clarity, building from foundational ideas to advanced understanding.

**Total Concepts**: 7
**Progression**: angles -> sides of a triangle -> right triangle -> multiplication -> squares and area -> equality -> Pythagorean theorem
**Estimated Duration**: 100 seconds (1:40)

## Animation Requirements
- Use Manim Community Edition (manim)
- All LaTeX must be in raw strings: r"$\frac{a}{b}$"
- Use MathTex() for equations, Text() for labels
- Maintain color consistency throughout
- Ensure smooth transitions between scenes
- Include voiceover-friendly pacing (2-3 seconds per concept introduction)

## Scene Sequence

### Scene 1: Angles
**Timestamp**: 0:00 - 0:10

Begin by fading in a simple angle visualization to establish our geometric foundation. Create two Line() objects meeting at a point, forming an angle. Use YELLOW for the angle arc created with Arc() and WHITE for the label. Display the notation r"$\theta$" using MathTex() positioned next to the arc with .next_to().

Draw the angle arc using Create(arc) over 1 second, then Write() the theta symbol. Briefly indicate that angles measure rotation between lines. Use FadeIn for the explanatory Text("Angles measure rotation") in WHITE, positioned at the bottom.

Wait 2 seconds for comprehension, then FadeOut all elements except leave a subtle indication that we'll build on this concept.

---

### Scene 2: Sides of a Triangle
**Timestamp**: 0:10 - 0:22

Transition by creating a triangle using Polygon() in BLUE. Position it at ORIGIN. Clearly label each side with Text() objects: "a", "b", and "c" in GREEN color. Use .next_to() to position labels adjacent to their respective sides.

Animate the triangle creation using Create(triangle) over 2 seconds. Then sequentially Write() each label with 0.5 second delays between them. This establishes the naming convention we'll use throughout.

Emphasize that these are the three sides of any triangle. Display Text("Every triangle has three sides") at the bottom. Wait 1 second, then prepare for the next scene by shifting the triangle to the LEFT.

---

### Scene 3: Right Triangle
**Timestamp**: 0:22 - 0:37

Transform the general triangle into a right triangle using ReplacementTransform(). The right triangle should have the right angle at the lower-left corner. Create a small square marker using Square(side_length=0.2) in YELLOW to indicate the 90-degree angle.

Display r"$\angle C = 90^\circ$" using MathTex() in YELLOW, positioned at the top. FadeIn the right angle marker. Use Indicate() to highlight the marker and the equation simultaneously.

Add labels Text("hypotenuse") next to side c (the longest side, opposite the right angle) and Text("legs") next to sides a and b. Color the hypotenuse label BLUE and the legs label GREEN.

This scene establishes the special property of right triangles that makes the theorem possible.

---

### Scene 4: Multiplication and Area
**Timestamp**: 0:37 - 0:47

Shift focus to area calculation. Create a simple square using Square() in GREEN to demonstrate that area equals side times side. Display r"$A = s \times s = s^2$" using MathTex() in WHITE at the top.

Fill the square with a semi-transparent color using set_fill(GREEN, opacity=0.5). Write the equation, then use Indicate() on the s^2 term to emphasize the squared connection.

This establishes the foundation for understanding squares built on triangle sides.

---

### Scene 5: Squares and Area
**Timestamp**: 0:47 - 1:07

This is a crucial visual scene. Start with the right triangle from Scene 3. Now grow three squares from each side of the triangle using GrowFromEdge():

1. Square on side a: RED with opacity 0.5, grows from the side
2. Square on side b: GREEN with opacity 0.5, grows from the side
3. Square on side c (hypotenuse): BLUE with opacity 0.5, grows from the side

Display the area equations sequentially:
- r"$A_a = a^2$" in RED at upper left
- r"$A_b = b^2$" in GREEN at upper right
- r"$A_c = c^2$" in BLUE at bottom

Use a VGroup() to organize the equations. The visual shows clearly that each side has a corresponding square.

---

### Scene 6: Equality
**Timestamp**: 1:07 - 1:15

Prepare for the key insight. Display r"$a^2 + b^2 = c^2$" in GOLD color using MathTex(), centered and large. This is the Pythagorean theorem equation.

Use Write() animation over 2 seconds. Then use Circumscribe() with GOLD color to highlight the entire equation, drawing attention to this fundamental relationship.

Add Text("The sum of squares on the legs equals the square on the hypotenuse") below, in WHITE.

---

### Scene 7: Pythagorean Theorem - Visual Proof
**Timestamp**: 1:15 - 1:40

This is the culminating scene that brings everything together.

Start by showing the right triangle with all three squares attached (from Scene 5). Now demonstrate the proof visually:

1. Highlight the squares on sides a and b using Indicate() with YELLOW
2. Show their combined area by animating the equation r"$a^2 + b^2$"
3. Transform or morph these two squares to fill the area of the square on side c
4. This visual transformation shows that r"$a^2 + b^2 = c^2$"

Display the final theorem statement in GOLD, large and centered:
r"$a^2 + b^2 = c^2$"

Below it, show the alternative form:
r"$c = \sqrt{a^2 + b^2}$"

Use Circumscribe() on the entire diagram to conclude. Add final text:
Text("The Pythagorean Theorem") in WHITE at the top.

Hold for 3 seconds, then gracefully FadeOut all elements.

---

## Final Notes

This animation is designed to be pedagogically sound and mathematically rigorous.
The progression from angles to Pythagorean theorem ensures that viewers
have all necessary prerequisites before encountering the main concept.

All visual elements, colors, and transitions have been specified to maintain
consistency and clarity throughout the 100-second animation.

Generate complete, working Manim Community Edition Python code that implements
this scene sequence with all specified mathematical notation, visual elements,
colors, and animations.
```
