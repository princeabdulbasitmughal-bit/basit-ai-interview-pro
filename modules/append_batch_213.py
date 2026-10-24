# -*- coding: utf-8 -*-
"""
Append Batch 213: Meteoritic Shock Kinetics, HRTEM Quasicrystal Verification, and GPU Tensor Core Systems
"""
import json
import os

new_pairs = [
    {
        "instruction": "Evaluate candidate knowledge of planetary impact shock synthesis and Rankine-Hugoniot jump conditions in mineral physics.",
        "input": "Candidate states: 'Shock synthesis of natural quasicrystals in meteorites is simply high-temperature thermal annealing over millions of years inside a differentiated asteroid core.'",
        "output": "Critique: The candidate's understanding is completely wrong. Natural quasicrystals (such as icosahedrite Al63Cu24Fe13 and decagonite Al71Ni24Fe5 found in the Khatyrka meteorite) could not have formed through slow equilibrium cooling in an asteroid core, because under equilibrium conditions Al-Cu-Fe decomposes into ordinary crystalline intermetallics (theta-Al2Cu, lambda-Al13Fe4, and beta-phase). Instead, natural quasicrystals require violent, hypervelocity planetesimal collision shocks (Stage S6, P = 5-25 GPa, T = 1200-1800 K) followed by ultra-fast rarefaction wave decompression quenching (quench rates dT/dt > 10^6 K/s). This rapid cooling kinetically traps the high-energy icosahedral aperiodic state before crystalline intermetallics can nucleate. Follow up by asking how the candidate computes Hugoniot shock pressure P = rho0 * Us * up."
    },
    {
        "instruction": "Assess candidate ability to distinguish between genuine quasicrystals and nano-twinned crystalline approximants in HRTEM.",
        "input": "Candidate claims: 'If a transmission electron micrograph displays a 10-fold ring of diffraction spots, that is 100% conclusive evidence of a true quasicrystal.'",
        "output": "Critique: Not necessarily. A major historical trap in crystallography is multiple micro-twinning: five or ten micro-crystals of an ordinary periodic cubic or orthorhombic phase (such as monoclinic Al13Fe4 or cubic alpha-AlMnSi) oriented at 72-degree angles to one another can produce a composite Selected Area Electron Diffraction (SAED) pattern that mimics 10-fold or 5-fold symmetry. To definitively prove true quasicrystalline order, one must perform high-resolution transmission electron microscopy (HRTEM) and convergent beam electron diffraction (CBED) with a sub-nanometer probe to demonstrate that individual nanometer-scale coherence domains themselves lack periodic translation and exhibit continuous golden-ratio tau scaling without inter-twin grain boundaries. Ask the candidate how phason flips manifest in Fourier transforms of HRTEM lattice images."
    },
    {
        "instruction": "Evaluate candidate expertise in optimizing local sovereign LLM training pipelines on high-VRAM single/dual-GPU workstations.",
        "input": "Candidate suggests: 'To fine-tune a 32B model like Qwen 2.5 Coder on a single 48GB NVIDIA RTX A6000, we should run standard FP32 full-parameter AdamW without any memory optimizations.'",
        "output": "Critique: The candidate demonstrates severe ignorance of LLM training memory footprints. A 32-billion parameter model in FP32 weights requires 128 GB of VRAM just to hold the model parameters, plus ~256 GB for AdamW optimizer states (first and second moments in FP32) and substantial additional VRAM for activations and gradients. Training on a 48GB GPU requires parameter-efficient fine-tuning (PEFT) such as QLoRA (4-bit NF4 quantized base model consuming ~18 GB VRAM), activation checkpointing (gradient checkpointing), FlashAttention-2/3, and 16-bit LoRA adapter weights (rank r=16 or 32, alpha=32). Challenge the candidate to calculate exact activation memory for a 4,096 sequence length batch."
    },
    {
        "instruction": "Analyze candidate strategy for real-time inference latency optimization using vLLM and TensorRT-LLM on sovereign hardware.",
        "input": "Candidate explains: 'For serving local models with low latency, batch size should always be set to maximum capacity (e.g. 256) even if only one user is querying.'",
        "output": "Critique: The candidate conflates throughput with latency. While large batch sizes maximize overall token throughput (tokens per second across the entire cluster), they dramatically increase time-to-first-token (TTFT) and per-token generation latency for individual interactive sessions due to queued scheduling and attention compute saturation. For interactive developer co-pilots and real-time agents, serving engines like vLLM should utilize continuous batching (iteration-level scheduling) with dynamic KV-cache management (PagedAttention), tensor parallelism across dual-node GPUs, and speculative decoding using a small draft model (e.g. Qwen 2.5 0.5B drafting for Qwen 32B) to achieve sub-15ms per-token latency. Probe the candidate on KV-cache memory budgeting during concurrent swarm execution."
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
