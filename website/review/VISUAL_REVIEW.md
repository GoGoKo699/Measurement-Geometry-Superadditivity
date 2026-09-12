# Visual review of the implemented reader

These are the assistant's screenshot inspections, not external user testing. The images came from the actual Chromium loopback HTTP run on implementation commit `4dba83be51ca8113f7082edf06a7e04b999f4a27`. The downloaded artifact digest and individual screenshot hashes are in [ci/ARTIFACT_VERIFICATION.json](ci/ARTIFACT_VERIFICATION.json). No Preskill page image or copied figure is included.

| Screenshot inspected | Observation |
|---|---|
| Overview, mobile | Physical result precedes the background assignment. The expert bypass is visible before the explanatory route. Ordinary prose and inline mathematics remain legible. Figure 1 has a direct link to its atlas view. |
| Background, desktop and mobile | The pinned source, focused map, notation crosswalk, source-specific sign note and optional reading are distinct. Desktop navigation and the page contents remain plain. The mobile tables use horizontal scroll containers; all columns are not visible simultaneously. |
| Channel, mobile | The operation budget, reference calculation, coherent encoder and finite witness form one continuous explanation. Wide equations use the existing scroll containers. |
| Proof guide, desktop | The three steps and their distinct roles are visible. The sufficient band, common-error qualification, computer-assisted obligation and known-background distinction remain next to the relevant explanation. |
| Figure atlas, desktop and mobile | All three accepted-palette figures appear with their canonical captions and separate original/download links. The palette is confined to figures. The witness bar, sufficient strip and controlled-limit asymptote retain their original geometry. Mobile figures fit the column and link to full-size vector/raster downloads for detailed inspection. |

The browser record separately confirms 17 routes at 1440 × 1000 and 390 × 844, no whole-page overflow, source downloads, navigation, search, keyboard controls, figure-color controls and the recorded no-JavaScript subset. Screenshots at the initial scroll position do not establish that every wide table or equation fits simultaneously. Horizontal scroll gestures were not separately exercised. This was not a full accessibility audit.

The generated GitHub-compatible Markdown and its anchors were checked separately by the native-preview and presentation tests. GitHub's authenticated renderer was not inspected. No Safari or Firefox result is claimed. No public site was deployed.
