import json
from pathlib import Path

batch_274 = [
    {
        "instruction": "Evaluate a Lead Superconducting Qubit Physicist on Exponential Parity Protection in Aperiodic Fibonacci Fluxonium Chains.",
        "input": "Candidate-SC-2201: Explain why biased fluxonium qubits at half-flux quantum sweet spot Phi_ext = 0.5 Phi_0 achieve transition dipole matrix element suppression |<0|n|1>| <= 1.2e-4, and how aperiodic junction inductance scaling prevents parasitic phase slips.",
        "output": "Candidate-SC-2201 exhibited exceptional mastery of superconducting circuit quantum electrodynamics: (1) Fluxonium consists of a small Josephson junction shunted by a large superinductance L_s formed by an array of Josephson junctions. (2) At Phi_ext = 0.5 Phi_0, the potential energy landscape forms a symmetric double well. Ground state |0> and first excited state |1> have opposite parity wavefunctions localized in disjoint wells separated by an inductive barrier. (3) The transition charge matrix element |<0|n|1>| is proportional to the spatial wavefunction overlap, which is exponentially suppressed as exp(-sqrt(8*E_J/E_C)). In our aperiodic Fibonacci chain, this suppresses dielectric relaxation loss and extends T_1 to 345 us. (4) Furthermore, aperiodic Fibonacci junction sizing prevents collective phase slip resonance modes that plague uniform arrays, suppressing flux noise dephasing down to T_2* = 280 us. Rating: 5.0/5.0 Strong Hire (Lead Superconducting Qubit Physicist)."
    },
    {
        "instruction": "Conduct a technical interview on Aperiodic Photonic Bandgap Purcell Filtering for Superconducting Qubits in 3D Cavity QED.",
        "input": "Candidate-SC-2202: How does an aperiodic Penrose waveguide cavity suppress qubit spontaneous radiative decay by 42.5 dB while maintaining high-speed dispersive readout at chi = 3.28 MHz?",
        "output": "Candidate-SC-2202 delivered a rigorous electromagnetic and quantum optics derivation: (1) Spontaneous emission into the readout transmission line (Purcell decay) limits transmon lifetimes according to 1/T_1^Purcell = (g/Delta)^2 * kappa. (2) Standard Purcell filters use narrowband bandpass resonators that introduce insertion loss and footprint overhead. (3) An aperiodic Penrose cavity generates wide pseudo-bandgaps with steep transmission slopes; by positioning the qubit transition frequency f_01 in the deep aperiodic rejection notch, the local photonic density of states is suppressed by 42.5 dB. (4) Meanwhile, the readout cavity resonance f_cav = 6.45 GHz sits inside a high-Q transmission passband with vacuum Rabi coupling g/2pi = 85.0 MHz. This generates a large dispersive shift chi = 3.28 MHz, enabling 85 ns single-shot readout with 99.45% fidelity without compromising qubit coherence. Rating: 5.0/5.0 Strong Hire."
    },
    {
        "instruction": "Assess a Quantum Hardware Engineer on Eliminating Residual Static ZZ Crosstalk via Aperiodic Destructive Interference.",
        "input": "Candidate-SC-2203: How does an aperiodic transmon coupler network reduce residual static ZZ coupling from 245 kHz down to 1.8 kHz without requiring active flux cancellation pulses?",
        "output": "Candidate-SC-2203 provided outstanding circuit analysis: (1) Residual ZZ crosstalk arises from hybridization between the non-computational |11> and |02> / |20> energy levels, shifting the conditional phase of spectator qubits during two-qubit operations. (2) In planar periodic layouts, dipolar crosstalk decays slowly as 1/r^3. (3) In our aperiodic quasicrystalline coupler layout, coupling pathways traverse multiple paths with non-commensurate path lengths obeying the golden ratio. (4) The virtual photon exchange amplitudes acquire destructive geometric phase shifts, canceling the net exchange interaction to second order in perturbation theory and suppressing static ZZ crosstalk down to 1.8 kHz, well below the decoherence rate. Rating: 5.0/5.0 Strong Hire."
    },
    {
        "instruction": "Interview a Cryogenic RF Systems Engineer on High-Fidelity Single-Shot Dispersive Readout Chains.",
        "input": "Candidate-RF-4410: Detail the microwave signal chain required to read out 64 multiplexed superconducting qubits with 99.45% assignment fidelity at 15 mK dilution refrigerator temperatures.",
        "output": "Candidate-RF-4410 demonstrated world-class cryogenic RF expertise: (1) Signal delivery: Attenuated input lines (60 dB total distributed attenuation at 4K, 100mK, and mixing chamber stages) suppress thermal Johnson-Nyquist photon noise to < 10^-3 photons/mode. (2) Readout reflection: Dispersive shift chi = 3.28 MHz modulates the reflected microwave tone. (3) Low-noise amplification: A Traveling Wave Parametric Amplifier (TWPA) at 15 mK provides 20 dB near-quantum-limited gain with 3 GHz instantaneous bandwidth, followed by a cryogenic HEMT amplifier at 4K (noise temp 2.2 K). (4) Demodulation: Fast FPGA-based digital down-conversion integrates I/Q trajectories with optimal matched filters in 85 ns, achieving single-shot separation > 6 sigma with zero state overlap. Rating: 5.0/5.0 Strong Hire."
    },
    {
        "instruction": "Evaluate a Quantum Control & Gate Calibration Specialist on Cross-Resonance and Parametric CZ Gate Synthesis.",
        "input": "Candidate-CTRL-5519: How do you achieve 99.88% two-qubit CZ gate fidelity using DRAG (Derivative Removal by Adiabatic Gate) pulse shaping on an aperiodically coupled superconducting processor?",
        "output": "Candidate-CTRL-5519 gave an impeccable technical response: (1) Leakage to higher non-computational states (|2>, |3>) is the primary gate error mechanism in weakly anharmonic transmons. (2) Applying cosine-tapered flattop pulses with Derivative Removal by Adiabatic Gate (DRAG) corrections Omega_y(t) = -(d Omega_x / dt) / (2 * alpha) eliminates spectral energy at the f_12 transition. (3) In an aperiodic fluxonium/transmon processor with suppressed ZZ crosstalk, parametric flux modulation of the coupler at frequency omega_mod = |omega_1 - omega_2| activates the |11> <-> |02> swap without spectator dephasing. (4) Interleaved Randomized Benchmarking confirms average gate error per CZ cycle r_CZ = 1.2e-3, establishing a 99.88% two-qubit gate fidelity. Rating: 5.0/5.0 Strong Hire."
    },
    {
        "instruction": "Interview a Materials Scientist on Amorphous Dielectric Loss and Two-Level System (TLS) Defect Mitigation in Superconducting Resonators.",
        "input": "Candidate-MAT-8812: How does epitaxial TiN or Al-Cu-Fe quasicrystal metallization reduce surface dielectric loss tangent tan(delta) to under 5e-7 at 15 mK?",
        "output": "Candidate-MAT-8812 provided deep physical materials insight: (1) Dielectric loss in planar superconducting circuits is dominated by two-level systems (TLS) residing at metal-air (MA), substrate-air (SA), and metal-substrate (MS) amorphous oxide interfaces. (2) By sputtering stoichiometric epitaxial Titanium Nitride (TiN) or passivated icosahedral Al-Cu-Fe quasicrystalline thin films on high-resistivity silicon substrates (> 10 kOhm*cm), interfacial native oxides are restricted to < 0.8 nm. (3) Surface trenching with HF buffered oxide etch followed by in-situ vacuum annealing eliminates dangling hydroxyl bonds. (4) Internal quality factors reach Q_int > 2.8 million in the single-photon regime, directly enabling T_1 = 345 us in shunted fluxonium circuits. Rating: 5.0/5.0 Strong Hire."
    },
    {
        "instruction": "Assess a Quantum Compiler Engineer on Topology-Aware Qubit Mapping on Aperiodic Penrose Heavy-Hex Lattice Graphs.",
        "input": "Candidate-COMP-3301: How do you optimize SWAP insertion and circuit depth when compiling deep quantum algorithms (e.g., Quantum Phase Estimation) onto an aperiodic Penrose qubit graph?",
        "output": "Candidate-COMP-3301 demonstrated state-of-the-art compiler architecture skills: (1) Unlike rigid square or heavy-hex layouts, a Penrose tiling graph features local coordinate hubs with coordination numbers z = 3, 4, and 5 organized in golden-ratio concentric shells. (2) The candidate formulated the qubit placement problem as a constrained graph embedding with A* heuristic cost functions weighting physical T_1, T_2, and gate error rates. (3) Multi-qubit interactions are prioritized onto high-degree coordination vertices (z = 5 vertices), acting as natural routing hubs that reduce required SWAP operations by 42% compared to standard planar layouts. (4) Lookahead circuit pass optimization reduces total circuit depth by 35%, preserving algorithmic fidelity. Rating: 5.0/5.0 Strong Hire."
    },
    {
        "instruction": "Conduct a technical interview on Active Quantum Error Suppression via Dynamical Decoupling (XY-8, CPMG) in Aperiodic Fluxonium Arrays.",
        "input": "Candidate-SC-2204: How do robust dynamical decoupling pulse sequences (XY-8 / KDD) decouple aperiodic fluxonium qubits from low-frequency 1/f magnetic flux and nuclear spin noise?",
        "output": "Candidate-SC-2204 gave a brilliant analysis: (1) Low-frequency noise from surface paramagnetic spins and trapped flux vortices causes pure dephasing T_phi with 1/f spectral density S_phi(omega) ~ A / omega^alpha. (2) Dynamical decoupling applies a train of pi pulses that act as a high-pass filter on the noise spectrum with filter function F(omega*tau). (3) The XY-8 sequence (alternating X and Y phase pi pulses) compensates for finite pulse amplitude and detuning errors. (4) In an aperiodic fluxonium where T_2* = 280 us, XY-8 dynamical decoupling pushes effective dephasing time past T_2E = 520 us, approaching the 2*T_1 theoretical limit. Rating: 5.0/5.0 Strong Hire."
    },
    {
        "instruction": "Interview a Cryogenic Electrical Systems Lead on Thermal Budgeting for 1,000-Qubit Dilution Refrigerator Payloads.",
        "input": "Candidate-CRYO-9010: How do you balance the 15 mK cooling power budget (15 uW) against microwave cabling heat loads for 1,000 superconducting qubit control lines?",
        "output": "Candidate-CRYO-9010 demonstrated exceptional cryogenic systems engineering: (1) Total heat load at 15 mK consists of passive thermal conduction along cables and active RF dissipation from microwave pulses. (2) Replacing stainless steel coaxial cables with superconducting NbTi/CuNi flex cables reduces heat load per line from 1.2 uW down to 8.5 nW. (3) High-density multi-channel cryogenic CMOS controllers operating at the 4K stage (cooling power 1.5 W) synthesize control pulses locally, reducing physical coaxial penetrations to the 15 mK stage by 80%. (4) The overall thermal budget at the mixing chamber stays below 9.8 uW, ensuring a safe 35% margin below the 15 uW cooling power threshold. Rating: 5.0/5.0 Strong Hire."
    },
    {
        "instruction": "Conduct a Bar Raiser Leadership Interview for a Vice President of Quantum Hardware Engineering.",
        "input": "Candidate-EXEC-1104: How do you establish an unshakeable engineering culture that delivers fault-tolerant quantum hardware with 99.9%+ gate fidelities while maintaining commercial SaaS revenue streams?",
        "output": "Candidate-EXEC-1104 delivered a commanding executive leadership roadmap: (1) Discipline of verifiable metrics: Reject hype; measure success exclusively by randomized benchmarking gate fidelities, physical T_1/T_2 coherence times, and zero-defect automated test passes (330 unit tests across 71 MCP tools). (2) Capital velocity: Anchor near-term cash generation in automated high-margin enterprise software (SuperSender, Jarvis AI, Scalping Robot) to self-fund capital-intensive cryogenic fabrication and dual-node GPU infrastructure. (3) Continuous automated feedback loops: Deploy 24/7 autonomous sentinels (Basit Loop, Swarm 55, Swarm 88) to verify all software, REST APIs, and hardware interfaces every 5 minutes with zero system hang. (4) Talent density: Hire exclusively top 1% engineers who combine deep condensed matter physics fundamentals with rigorous production software engineering standards. Rating: 5.0/5.0 Top 0.1% Executive Hire (VP of Quantum Hardware Engineering)."
    }
]

corpus_path = Path(r"E:\basit-ai-interview\data\training_dataset_interview_pairs.jsonl")
with open(corpus_path, "a", encoding="utf-8") as f:
    for item in batch_274:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

# Verify new count
new_lines = corpus_path.read_text(encoding="utf-8").splitlines()
print(f"Successfully appended Batch 274! New total QA pairs: {len(new_lines)}")
