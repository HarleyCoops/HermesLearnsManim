# Starter Prompts

These prompts were pulled from the old `Math-To-Manim` repo and kept here as jumpstart material.

They are included in full text form so you can paste them directly into Hermes.
A few broken characters from older files were normalized for readability.

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
