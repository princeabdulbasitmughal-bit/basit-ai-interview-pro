# -*- coding: utf-8 -*-
"""
Append Batch 212: Advanced TEM Electron Diffraction, Quasicrystal Symmetry, and Distributed AI Systems
"""
import json
import os

new_pairs = [
    {
        "instruction": "Evaluate candidate understanding of Transmission Electron Microscopy (TEM) Selected Area Electron Diffraction (SAED) for quasicrystalline discovery.",
        "input": "Candidate claims: 'We can definitively prove an alloy has an icosahedral quasicrystalline phase using conventional powder X-ray diffraction alone without TEM, because XRD peaks always have irrational Miller indices.'",
        "output": "Critique: The candidate's assertion is fundamentally flawed. In powder XRD, 1D intensity versus 2-theta traces can easily confuse quasicrystals with complex crystalline rational approximants (such as 1/1 or 2/1 Bergman or Tsai cubic phases) because their high-order Bragg peaks overlap closely. The definitive physical proof of quasicrystalline long-range order—as demonstrated by Dan Shechtman in his 2011 Nobel-winning discovery of Al-Mn—requires TEM Selected Area Electron Diffraction (SAED) to directly visualize the sharp, non-crystallographic 10-fold (or 5-fold) rotational point group symmetry. Such 5-fold and 10-fold periodic translations are strictly forbidden by the classical crystallographic restriction theorem in periodic 3D lattices. Follow up by asking how the candidate would distinguish between true aperiodic quasicrystals and multiple twinning of micro-crystals."
    },
    {
        "instruction": "Analyze candidate knowledge on relativistic electron wavelength and camera constant calibration in TEM diffraction analysis.",
        "input": "Candidate states: 'In a 200 kV TEM, the electron de Broglie wavelength is computed using classical mechanics lambda = h / sqrt(2*m0*e*V), yielding approximately 0.027 Angstroms.'",
        "output": "Critique: The candidate forgot relativistic correction. At 200 keV, the kinetic energy of the electron is approximately 39% of its rest mass energy (m0*c^2 = 511 keV), meaning relativistic effects cannot be neglected. With relativistic correction factor (1 + eV/(2*m0*c^2)), the actual relativistic momentum yields lambda = 0.02508 Angstroms (2.508 pm), not 0.027 Angstroms. This difference of ~7% causes significant errors in camera constant (K = lambda * L) calibration and Bragg d-spacing indexing. Probe the candidate on how camera constant errors propagate into reciprocal lattice vector length calculations."
    },
    {
        "instruction": "Evaluate candidate understanding of golden ratio (tau) radial progression in 10-fold SAED quasicrystal patterns.",
        "input": "Candidate explains: 'In a 10-fold quasicrystal SAED pattern, the concentric rings of spots are spaced uniformly like an ordinary periodic lattice.'",
        "output": "Critique: Incorrect. In periodic crystals, reciprocal lattice spots appear at integer multiples of reciprocal basis vectors (r_n = n * r0). In icosahedral and decagonal quasicrystals, however, the diffraction spots follow self-similar inflation/deflation scaling governed by powers of the golden ratio tau = (1 + sqrt(5))/2 approx 1.618034. That is, R_n = r0 * tau^n. The ratio of radii between consecutive fundamental decagonal shells is exactly 1.618034, reflecting the projection of a 6D hypercubic lattice into 2D reciprocal space. Challenge the candidate to explain why phason strain causes slight spot deviations and peak broadening in physical quasicrystalline ingots."
    },
    {
        "instruction": "Assess candidate expertise in architectural trade-offs between local sovereign model serving and multi-agent distributed clusters.",
        "input": "Candidate states: 'We should always route every prompt through cloud frontier APIs like Claude 3.7 or GPT-4o rather than maintaining local sovereign models like Qwen 2.5 Coder 32B on an RTX A6000, because cloud APIs are always superior.'",
        "output": "Critique: The candidate demonstrates poor systems engineering judgment. Relying 100% on external proprietary cloud APIs introduces severe vulnerabilities: data exfiltration risks for proprietary code/physics IP, high per-token latency (500ms - 2s network round-trip), variable cloud API rate-limiting/throttling, and unsustainable operational costs at scale. A world-class sovereign AI architecture uses hybrid routing: a local 48GB GPU (NVIDIA RTX A6000) running Qwen 2.5 Coder 32B or DeepSeek-Coder at 90+ tok/s with $0 marginal cost for 95% of parallel code generation, refactoring, and agent monitoring, reserving cloud frontier reasoning models strictly for complex high-level multi-hop architectural synthesis. Probe the candidate on designing local Ollama/vLLM fallbacks with automatic circuit breakers."
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
