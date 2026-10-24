# -*- coding: utf-8 -*-
"""
Append Batch 218: 6D Phason Strain Elasticity, Bancel-Heiney Peak Broadening,
Rational Approximant Transitions, and Dual-Node GPU Tensor Parallelism.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in 6D Phason Strain Elasticity and Bancel-Heiney anisotropic peak broadening in quasicrystals.",
        "input": "Candidate claims: 'X-ray diffraction peak broadening in quasicrystals is identical to ordinary polycrystalline microstrain and affects all Bragg peaks equally.'",
        "output": "Critique: The candidate fails to distinguish ordinary phonon strain from higher-dimensional phason strain. In conventional crystals, microstrain causes symmetric peak broadening proportional to physical momentum transfer q_parallel (Delta q / q = const). In contrast, in icosahedral quasicrystals (as experimentally discovered by Bancel & Heiney in 1986 and modeled by Lubensky et al.), peak broadening and shifts are strictly proportional to the perpendicular (phason) momentum vector q_perp: FWHM(q) = Gamma_0 + kappa * gamma * |q_perp|. Consequently, reflections with large physical diffraction angles (high q_par) but low internal momentum (small q_perp, such as the iconic (54, 86) reflection) remain exceptionally sharp (FWHM ~ 0.13 deg), whereas low-angle reflections with large internal momentum (high q_perp, such as (34, 54)) exhibit severe anisotropic broadening (FWHM > 0.18 deg). This inverse scaling is the definitive diagnostic fingerprint distinguishing true quasicrystals with frozen phason disorder from microcrystalline twins. Probe the candidate on how phason elastic constants K_4 and K_6 are determined experimentally from diffuse X-ray scattering."
    },
    {
        "instruction": "Evaluate candidate knowledge of the structural phase transition from Icosahedral Quasicrystals to Rational Approximants.",
        "input": "Candidate states: 'Rational approximants are completely unrelated compounds that accidentally form near quasicrystal compositions.'",
        "output": "Critique: The candidate fundamentally misunderstands the topological and crystallographic relationship between quasicrystals and rational approximants. Rational approximants are periodic crystals whose unit cells are exact local packing analogues of the quasicrystal. In the 6D cut-and-project formalism, applying a uniform linear phason strain M_ij to the irrational projection matrix P_par replaces the golden ratio tau = (1+sqrt(5))/2 approx 1.618034 with rational Fibonacci fractions F_(n+1)/F_n. For example: a strain of gamma approx 0.20-0.25 locks the Fibonacci ratio at F_2/F_1 = 1/1 = 1.000, collapsing the quasiperiodic lattice into the 1/1 cubic approximant (alpha-AlMnSi or beta-AlCuFe type, space group Pm-3, lattice parameter a ~ 12.3 Angstroms) containing identical 54-atom Mackay icosahedra. Similarly, intermediate strains yield the 2/1 approximant (F_3/F_2 = 2.0). Above the critical annealing temperature Tc (~620 deg C), thermal phason hops can unfreeze these approximant domains back into the ideal icosahedral ground state. Ask the candidate how transmission electron microscopy (TEM) electron diffraction patterns reveal the rational modulation vector."
    },
    {
        "instruction": "Assess candidate understanding of Dual-Node Multi-GPU Tensor Parallelism vs Pipeline Parallelism for enterprise LLM workloads.",
        "input": "Candidate suggests: 'When running a large model across two different GPU workstations over Ethernet, Tensor Parallelism is always faster than Pipeline Parallelism.'",
        "output": "Critique: The candidate proposes a severe distributed architectural mistake. Tensor Parallelism (TP) splits individual weight matrices (such as GEMMs in multi-head attention and MLP layers) and requires two All-Reduce communication barriers per transformer layer! Over commodity 1 GbE or 10 GbE local networking (with latencies of 50-200 microseconds), the network communication overhead of TP completely dwarfs GPU compute, causing GPUs to sit idle in synchronization locks. Tensor Parallelism strictly requires high-bandwidth, ultra-low-latency interconnects (such as NVLink at 900 GB/s or InfiniBand RDMA). For heterogeneous dual-node workstations connected over local networks (e.g. Node 1 with RTX A6000 and Node 2 with RTX 5090), Pipeline Parallelism (PP) with micro-batching or Speculative Disaggregated Serving (where the fast workstation acts as speculative draft proposer and the high-VRAM workstation verifies) is the correct architecture, minimizing cross-node network transfers to compact KV-cache activations or token IDs. Challenge the candidate to calculate All-Reduce latency per token across a 1 Gbps link."
    },
    {
        "instruction": "Analyze candidate design of an automated regression test gate enforcing 100% test pass rates before Git auto-commits in autonomous AI agent pipelines.",
        "input": "Candidate explains: 'If a test fails during an autonomous build loop, the agent should simply skip that test and commit anyway to maintain deployment velocity.'",
        "output": "Critique: The candidate advocates catastrophic software engineering practices that guarantee production downtime and technical debt accumulation. In autonomous multi-agent pipelines (such as BasitLoop / Antigravity), regression suites represent non-negotiable invariant boundaries: 1) Every single test (e.g. all 45 automated unit/integration tests) must pass with 100% success; 2) If any assertion fails, the commit must be aborted immediately; 3) The agent must inspect the failure traceback, perform localized root-cause analysis (RCA), apply targeted code repairs, and re-run the entire test harness; 4) Git staging and atomic commits must only execute once the test suite returns exit code 0; and 5) System telemetry, test logs, and artifact manifests must be persisted for full operational auditability. Probe the candidate on how they would implement automated bisection debugging when a regression occurs."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 218. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
