<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
  <img src="./assets/hero-dark.svg" alt="Pranjal Sailwal — Software Engineer Generalist" width="100%"/>
</picture>

</div>

<br/>

<div align="center">

[![](https://img.shields.io/badge/backend%20systems-2DD4BF?style=flat-square&logoColor=white&labelColor=0C1220&color=2DD4BF)](#selected-systems)&nbsp;
[![](https://img.shields.io/badge/scientific%20software-A78BFA?style=flat-square&logoColor=white&labelColor=0C1220&color=A78BFA)](#selected-systems)&nbsp;
[![](https://img.shields.io/badge/interactive%20web-60A5FA?style=flat-square&logoColor=white&labelColor=0C1220&color=60A5FA)](#selected-systems)&nbsp;
[![](https://img.shields.io/badge/Dehradun%2C%20India-F59E0B?style=flat-square&logoColor=white&labelColor=0C1220&color=F59E0B)](#contact)

</div>

<div align="center">

[`selected systems`](#selected-systems)&emsp;·&emsp;[`my stack`](#my-stack)&emsp;·&emsp;[`things i've measured`](#things-ive-measured)&emsp;·&emsp;[`what i work on`](#what-i-work-on)&emsp;·&emsp;[`get in touch`](#get-in-touch)

</div>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/divider-light.svg">
  <img src="./assets/divider-dark.svg" alt="" width="100%"/>
</picture>

<br/>

## Selected Systems

I picked these five because they each pushed me into territory I hadn't been in before — not just "used a new library" but actually had to think differently about the problem.

<br/>

<div align="center">
<a href="https://github.com/sailwalpranjal/AetherScan">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/cards/aetherscan-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/cards/aetherscan-light.svg">
  <img src="./assets/cards/aetherscan-dark.svg" alt="AetherScan" width="100%"/>
</picture>
</a>
</div>

<br/>

<div align="center">
<a href="https://github.com/sailwalpranjal/Neurotract">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/cards/neurotract-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/cards/neurotract-light.svg">
  <img src="./assets/cards/neurotract-dark.svg" alt="NeuroTract" width="100%"/>
</picture>
</a>
</div>

<br/>

<table width="100%">
<tr>
<td width="50%" align="center">
<a href="https://github.com/sailwalpranjal/spectral-monte-carlo-raytracer">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/cards/spectralpathtracer-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/cards/spectralpathtracer-light.svg">
  <img src="./assets/cards/spectralpathtracer-dark.svg" alt="SpectralMC" width="100%"/>
</picture>
</a>
</td>
<td width="50%" align="center">
<a href="https://github.com/sailwalpranjal/SyncState">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/cards/syncstate-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/cards/syncstate-light.svg">
  <img src="./assets/cards/syncstate-dark.svg" alt="SyncState" width="100%"/>
</picture>
</a>
</td>
</tr>
</table>

<br/>

<div align="center">
<a href="https://solque-oli7.vercel.app/">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/cards/solque-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/cards/solque-light.svg">
  <img src="./assets/cards/solque-dark.svg" alt="Solque" width="100%"/>
</picture>
</a>
</div>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/divider-light.svg">
  <img src="./assets/divider-dark.svg" alt="" width="100%"/>
</picture>

<br/>

## My Stack

These bars reflect how comfortable I actually am using each thing in a real project, not just whether I've touched it. I tend to go pretty deep on fewer tools rather than broad and shallow across many.

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/stack-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/stack-light.svg">
  <img src="./assets/stack-dark.svg" alt="My stack — depth indicators across domains" width="100%"/>
</picture>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/divider-light.svg">
  <img src="./assets/divider-dark.svg" alt="" width="100%"/>
</picture>

<br/>

## Things I've Measured

I try to profile before optimising. These are a few cases where I actually sat down with real numbers instead of guessing.

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/metrics-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/metrics-light.svg">
  <img src="./assets/metrics-dark.svg" alt="Things I've measured" width="100%"/>
</picture>

<br/>

| What I was working on | What I did | What changed |
| :--- | :--- | :--- |
| AetherScan — 500-record sync batch | switched from sequential writes to bulk inserts | 78 s → 52 s &nbsp;`−33%` |
| AetherScan — FastAPI backend | separated CPU-bound work from I/O using `ProcessPoolExecutor` | 30+ endpoints, 8 live integrations |
| Yantra Byte internship | coordinated across a 6-month project, wrote up architecture decisions | ~1,050 team dev-hours |
| Spectral path tracer | built BVH acceleration, checked Monte Carlo output against analytical results | validated numerically |
| SyncState | CRDT merge with vector clocks, WebRTC mesh, IndexedDB persistence | works offline, no conflict on merge |

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/divider-light.svg">
  <img src="./assets/divider-dark.svg" alt="" width="100%"/>
</picture>

<br/>

## What I Work On

I mostly sit somewhere between backend systems, scientific/numerical software, and interactive web. None of these feel like separate worlds to me — a lot of my projects end up touching two or three of them at once.

<br/>

<table width="100%">
<tr>
<td width="50%" align="center">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/signals/backend-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/signals/backend-light.svg">
  <img src="./assets/signals/backend-dark.svg" alt="Backend Systems" width="100%"/>
</picture>
</td>
<td width="50%" align="center">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/signals/science-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/signals/science-light.svg">
  <img src="./assets/signals/science-dark.svg" alt="Scientific Computing" width="100%"/>
</picture>
</td>
</tr>
<tr>
<td width="50%" align="center">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/signals/interactive-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/signals/interactive-light.svg">
  <img src="./assets/signals/interactive-dark.svg" alt="Interactive Systems" width="100%"/>
</picture>
</td>
<td width="50%" align="center">
<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/signals/writing-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/signals/writing-light.svg">
  <img src="./assets/signals/writing-dark.svg" alt="Technical Writing" width="100%"/>
</picture>
</td>
</tr>
</table>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/divider-light.svg">
  <img src="./assets/divider-dark.svg" alt="" width="100%"/>
</picture>

<br/>

## Writing

I only write something up when the implementation itself is the interesting part. These are pieces I put out because I wanted a record of the thinking, not just the code.

<br/>

<table>
<tr>
<td><strong>Spectral Monte Carlo Path Tracer</strong></td>
<td>wrote about the C++ renderer I built — BVH construction, spectral sampling, how I checked the output was actually correct</td>
</tr>
<tr>
<td><strong>Geodesic Flow via WebAssembly</strong></td>
<td>numerical integration of geodesics, compiling to WASM and running it directly in the browser</td>
</tr>
<tr>
<td><strong>Wavelength-Resolved Geodesic</strong></td>
<td>extending the geodesic work with curvature-aware sampling — more of a note-to-self that turned into a write-up</td>
</tr>
</table>

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/divider-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/divider-light.svg">
  <img src="./assets/divider-dark.svg" alt="" width="100%"/>
</picture>

<br/>

## Get in Touch

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)"  srcset="./assets/contact-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/contact-light.svg">
  <img src="./assets/contact-dark.svg" alt="Contact" width="100%"/>
</picture>

<br/>

<div align="center">

[`pranjalsailwal09@gmail.com`](mailto:pranjalsailwal09@gmail.com)&emsp;
[`github.com/sailwalpranjal`](https://github.com/sailwalpranjal)&emsp;
[`linkedin.com/in/pranjal-sailwal`](https://linkedin.com/in/pranjal-sailwal)&emsp;
[`orcid.org/0009-0009-5936-3512`](https://orcid.org/0009-0009-5936-3512)

</div>

<br/>

<div align="center">
<sub>I'm a generalist, but not in a way where everything is shallow. The through-line is: backend work, some maths, and making it observable enough that you can tell when something breaks.</sub>
</div>

<br/>
