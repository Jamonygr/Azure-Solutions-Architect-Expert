# Third-party notices

The project-authored source, diagrams, documentation, and original raster
illustrations are licensed under the repository MIT license. The official
Microsoft product icons listed below are not part of that MIT grant.

## Microsoft Azure architecture icons

- Copyright and rights holder: Microsoft Corporation.
- Official terms and source: <https://learn.microsoft.com/en-us/azure/architecture/icons/>
- Official package: <https://arch-center.azureedge.net/icons/Azure_Public_Service_Icons_V24.zip>
- Acquired: 2026-09-02.
- Package SHA-256: `921594ccd1bf3d9c0a1bd7b6d924e050551a59342f2b353bb74bdcf761c35141`.
- Permitted project use: architectural diagrams, training materials, and
  documentation. The icons must not be cropped, flipped, rotated, distorted,
  changed in shape, or used to represent this project as a Microsoft product.

Only the 47 Azure SVG files actually embedded by the registered lab diagrams
are vendored under `docs/site-assets/icons/azure/`. Their individual original
byte hashes and every lab usage are recorded in the generated
`docs/site-assets/visual-asset-manifest.json`.

## Microsoft Entra architecture icons

- Copyright and rights holder: Microsoft Corporation.
- Official terms and source: <https://learn.microsoft.com/en-us/entra/architecture/architecture-icons>
- Official package: <https://download.microsoft.com/download/3/1/a/31a56038-856a-4489-88e4-ee5a1c4352be/Microsoft%20Entra%20architecture%20icons%20-%20Oct%202023.zip>
- Acquired: 2026-09-02.
- Package SHA-256: `4e07536706a2d092e6524e5417e2c861333fdbdb41c36f78d44dfa07ccc5eedc`.
- Permitted project use: architectural diagrams, training materials, and
  documentation. The icons must not be cropped, flipped, rotated, distorted,
  changed in shape, used as this project's product mark, or used in marketing
  communications.

Only the Microsoft Entra ID and Microsoft Entra ID Governance color SVGs used
by the registered topology diagrams are vendored under
`docs/site-assets/icons/entra/`. Their individual original byte hashes and
every lab usage are recorded in the generated visual-asset manifest.

The final lab topology SVGs embed unchanged icon bytes as local data resources
and place the corresponding service name beside each icon. No runtime request
to Microsoft or another external host is made.
