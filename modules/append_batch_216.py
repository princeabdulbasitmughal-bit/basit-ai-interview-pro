# -*- coding: utf-8 -*-
"""
Append Batch 216: Quasicrystal Photoemission Spectroscopy, Variable-Range Hopping, and Speculative Decoding
"""
import json
import os

new_pairs = [
    {
        "instruction": "Evaluate candidate knowledge of experimental photoemission spectroscopy (UPS/XPS) used to verify the Hume-Rothery pseudogap.",
        "input": "Candidate states: 'The electronic pseudogap in quasicrystals is purely a theoretical concept derived from simple free electron models and has never been confirmed experimentally.'",
        "output": "Critique: The candidate's assertion is completely false. The existence of a deep electronic pseudogap in stable icosahedral quasicrystals (e.g. Al63Cu25Fe12, Al70Pd20Mn10, and Zn-Mg-Y) has been extensively confirmed through high-resolution ultraviolet and X-ray photoemission spectroscopy (UPS and XPS) by Stadnik, Belin-Ferré, and Mori et al. Their ultra-high vacuum photoemission spectra show a dramatic suppression of intensity right at the Fermi edge—revealing that N(Ef) is reduced to approximately 20-25% of the free-electron value (g = N(Ef)/N0(Ef) ~ 0.20 - 0.25). Furthermore, tunneling spectroscopy (STM/STS) at liquid helium temperatures directly maps the dip in differential conductance (dI/dV) across a ~0.8 eV energy window centered on Ef. Ask the candidate how surface oxidation and phason defects affect photoemission measurements."
    },
    {
        "instruction": "Assess candidate understanding of Variable-Range Hopping (VRH) and weak localization in quasicrystalline electronic transport.",
        "input": "Candidate explains: 'Since quasicrystals have no periodic lattice, their electrical resistivity must be governed by classical Drude scattering with mean free path l >> lattice constant.'",
        "output": "Critique: The candidate misapplies classical Drude transport theory. In quasicrystals, the electronic mean free path l estimated from classical Drude formula is smaller than the interatomic distance (l < a ~ 2-3 Angstroms)—violating the Ioffe-Regel criterion for ordinary diffusive transport. Instead, conduction occurs in the critical regime between extended and localized states. Transport is dominated by quantum interference (weak localization) and variable-range hopping (VRH) between self-similar hierarchical clusters. As thermal energy increases, inelastic electron-phonon scattering breaks phase coherence, reducing quantum backscattering and lowering the resistivity (resulting in the famous anomalous negative temperature coefficient d*rho/dT < 0). Probe the candidate on how Mott's T^(-1/4) vs Efros-Shklovskii T^(-1/2) hopping laws apply in low-temperature quasicrystal transport."
    },
    {
        "instruction": "Evaluate candidate understanding of Speculative Decoding architectures for accelerating sovereign LLM inference on workstations.",
        "input": "Candidate claims: 'Speculative decoding cannot improve inference speed on a single GPU because running two models always takes twice as much compute.'",
        "output": "Critique: The candidate fundamentally misunderstands the memory-bandwidth bottleneck of autoregressive LLM decoding. In single-batch LLM inference, GPU utilization is bound by memory bandwidth (reading model weights from VRAM to SRAM), not raw compute. A small, fast draft model (e.g. Qwen 2.5 0.5B consuming <1 GB VRAM) generates K speculative candidate tokens (e.g. K=4) sequentially at extremely high speed. The large target model (e.g. Qwen 2.5 Coder 32B) then evaluates all K tokens in a single parallel forward pass (which takes essentially the same wall-clock time as generating a single token). If 3 of the 4 tokens are accepted, effective throughput increases by 2.5x to 3x with zero loss in mathematical accuracy. Challenge the candidate to calculate acceptance rates in structured code generation vs creative prose."
    },
    {
        "instruction": "Analyze candidate design for an automated continuous self-healing loop in autonomous coding agents.",
        "input": "Candidate suggests: 'An autonomous agent loop should automatically execute fixes without running regression suites, relying on LLM self-confidence to ensure correctness.'",
        "output": "Critique: The candidate promotes dangerous, uncontrolled autonomous drift. An enterprise-grade autonomous engineering loop must enforce deterministic verification gates: 1) Every code modification must trigger an automated regression test suite; 2) Static analysis and type checking (e.g. tsc --noEmit, ruff, mypy) must verify zero syntax/type errors; 3) All external daemon endpoints must pass automated pre-flight health pings; 4) Git commits must be performed atomically only upon 100% test pass rates; and 5) If any test fails, the agent must inspect stack traces, apply targeted self-healing diffs, and re-verify before proceeding. Probe the candidate on designing rollback checkpoints when an agent introduces a regression."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")
    
    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
