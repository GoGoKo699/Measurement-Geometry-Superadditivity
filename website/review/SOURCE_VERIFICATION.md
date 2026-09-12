# Selected tutorial source verification

Checked directly on 12 September 2026: John Preskill, *Quantum Shannon Theory*, Chapter 10 of *Quantum Information*, [arXiv:1604.07450v5](https://arxiv.org/abs/1604.07450v5), [official pinned PDF](https://arxiv.org/pdf/1604.07450v5). The arXiv version date is 8 July 2025; the PDF title says updated June 2025. The inspected 697,152-byte PDF has SHA-256 `c1228be6d7547ee51451616e5646cf276cea33e0effe452765238c87e286b104`.

The PDF has 103 viewer pages. Printed page k is one-based viewer page k+6, or zero-based PDF index k+5. Section 10.7.1 occupies printed pp. 51–53; 10.7.2 pp. 53–56; 10.7.4 pp. 58–60; 10.9.4 pp. 75–76. Section 10.2.4 is printed p. 19 only. All assigned and optional subsection locations and equation pages were checked in the actual edition and are recorded once in [learning_bridge.json](../learning_bridge.json); the two reader interfaces expand that map.

Visual inspection covered the title page, the repetition test state on printed p. 60, and printed pp. 53, 75 and 76 for the sign question. Equation (10.368) visibly reverses the entropy difference. Its rate must use H(B)-H(E), consistent with definition (10.275) and the exponent of the decoupling bound (10.367). The reader note is confined to that confirmed sign issue. It is not a chapter audit.

The check also confirmed that Preskill already gives a qualitative threshold improvement from repetition followed by outer coding. His depolarizing parameter and symmetry argument are not imported to this channel. The crosswalk distinguishes the input register from its state, H from S, Q1 from the project's optimized Q^(1), and physical report noise from accuracy tolerances. The project supplies its own hidden-outcome reduction, geometric bound, certificate and witness.

The front-matter redistribution notice was read at viewer page 5. No PDF, textbook screenshot, copied figure or chapter extract is included in this repository. Temporary inspection files were kept outside the checkout. The website has no tutorial-fetch step or remotely loaded tutorial asset. This is an assistant source check and editorial review, not external user testing or a new scientific audit.
