# -*- coding: utf-8 -*-
"""
Append Batch 214: Meteoritic Quasicrystal Mineralogy, Hugoniot EOS, and Distributed Multi-GPU Parallelism
"""
import json
import os

new_pairs = [
    {
        "instruction": "Evaluate candidate knowledge regarding the discovery and classification of natural quasicrystals in carbonaceous chondrites.",
        "input": "Candidate claims: 'Natural quasicrystals are identical to synthetic lab-grown quasicrystals and were synthesized in ancient hydrothermal vents on Earth.'",
        "output": "Critique: The candidate is factually incorrect on multiple accounts. Natural quasicrystals were not formed on Earth or in hydrothermal vents; they were discovered in fragments of the Khatyrka meteorite—a 4.5-billion-year-old CV3 carbonaceous chondrite that fell in the Koryak Mountains of Chukotka, Russia. The International Mineralogical Association (IMA) has formally recognized three natural quasicrystalline and approximant minerals from Khatyrka: Icosahedrite (IMA 2010-042, Al63Cu24Fe13, with icosahedral symmetry), Decagonite (IMA 2015-017, Al71Ni24Fe5, with 10-fold decagonal symmetry), and Steinhardtite (IMA 2014-036, a cubic approximant). Their formation required unearthly redox conditions where metallic aluminum and copper coexisted at zero oxygen fugacity prior to hypervelocity planetesimal shock. Follow up by asking how oxygen fugacity is determined in chondritic inclusions."
    },
    {
        "instruction": "Assess candidate understanding of Rankine-Hugoniot jump relations in impact petrology and shock-wave metallurgy.",
        "input": "Candidate states: 'The shock pressure generated during a meteoritic impact is calculated solely by Newton's second law F = m*a without considering particle velocity or material bulk sound speed.'",
        "output": "Critique: The candidate lacks basic comprehension of shock physics and equation of state (EOS) principles. Dynamic impact pressures in condensed matter are governed by the conservation of mass, momentum, and energy across the shock discontinuity (the Rankine-Hugoniot equations). For planar symmetric impact, particle velocity is up = v_impact / 2. The shock velocity follows the empirical linear Hugoniot relation Us = c0 + s * up, where c0 is the bulk acoustic sound speed and s is the Hugoniot slope parameter. The peak Hugoniot pressure is P_H = rho0 * Us * up. In the Khatyrka shock event, an impact velocity of ~2.2 km/s produced a peak pressure of ~28 GPa, corresponding to shock stage S6 (planetary impact melting). Probe the candidate on how Hugoniot curves differ between porous chondrites and solid metallic iron meteorites."
    },
    {
        "instruction": "Evaluate candidate architectural insight into Pipeline Parallelism vs Tensor Parallelism for distributed LLM inference on sovereign clusters.",
        "input": "Candidate suggests: 'For low-latency interactive code completion, we should always split model layers sequentially across multiple nodes using Pipeline Parallelism (PP) rather than Tensor Parallelism (TP).'",
        "output": "Critique: The candidate recommends the opposite of optimal practice for low-latency generation. Pipeline Parallelism splits layers sequentially (e.g. Layers 1-16 on GPU 0, 17-32 on GPU 1). During autoregressive token-by-token generation (batch size = 1), Pipeline Parallelism suffers from severe 'pipeline bubble' idling, where downstream GPUs sit completely idle waiting for upstream layers to produce activations, multiplying latency by the pipeline depth. For low-latency single-stream interactive coding, Tensor Parallelism (TP) is far superior: it splits individual matrix multiplications (QKV projections and MLP gates) across GPUs in parallel via fast NVLink/PCIe All-Reduce, keeping all GPUs active concurrently and reducing per-token latency. Pipeline Parallelism is only beneficial for high-throughput batched training or when inter-node interconnect bandwidth (Ethernet) is too slow for Tensor Parallelism All-Reduce communication."
    },
    {
        "instruction": "Assess candidate expertise in managing GPU KV-cache fragmentation during concurrent multi-agent swarm bursts.",
        "input": "Candidate explains: 'To handle 88 concurrent sub-agents in Ollama or vLLM, we simply pre-allocate static contiguous memory buffers for the maximum 128K context for every single agent.'",
        "output": "Critique: The candidate's approach leads directly to Out-Of-Memory (OOM) crashes and catastrophic memory waste. Pre-allocating contiguous 128K context buffers for 88 agents would require terabytes of VRAM due to internal memory fragmentation, even though most agents only generate a few hundred tokens. Enterprise serving engines prevent this using PagedAttention (as implemented in vLLM): KV-cache is partitioned into small virtual memory blocks (e.g. 16 or 32 tokens per block) allocated dynamically on demand via a page table, eliminating internal fragmentation and reducing external memory waste to under 4%. This enables 88+ concurrent agent conversations to be multiplexed seamlessly within a single 48GB GPU. Ask the candidate how prefix caching further optimizes agent prompts sharing identical system instructions."
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
