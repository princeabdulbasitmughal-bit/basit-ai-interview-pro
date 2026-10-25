# -*- coding: utf-8 -*-
"""
Append Batch 230: Electrocatalytic Green Nitrogen Reduction (NRR) vs Haber-Bosch,
Aperiodic Multi-Metal Ensemble HER Suppression, High-Throughput Redis Lua Rate Limiting,
and Linux Kernel Page Cache Dirty Throttling & I/O Stall Prevention.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Electrocatalytic Green Nitrogen Reduction (NRR) and Ammonia (NH3) Synthesis over Aperiodic Quasicrystals vs Conventional Haber-Bosch.",
        "input": "Candidate states: 'The only reason we still use the 100-year-old Haber-Bosch process at 450 C and 200 bar is because ambient electrocatalytic nitrogen reduction (NRR) is thermodynamically impossible at room temperature.'",
        "output": "Critique: The candidate confuses thermochemical equilibrium constraints with electrochemical kinetics and Sabatier scaling relations. Electrocatalytic NRR (N2 + 6H+ + 6e- -> 2NH3) is thermodynamically downhill (E0 = +0.06 V vs RHE); the primary roadblock in conventional periodic metals (Fe, Ru, Ti) is the immense kinetic barrier for breaking the non-polar N#N triple bond (945 kJ/mol) and universal scaling relations that bind intermediate *N and *NHx species too tightly or weakly. In contrast, aperiodic quasicrystalline alloys (e.g. Al65Cu20Fe10Mo5 or dealloyed nanoporous quasicrystals) break periodic Sabatier limitations through: 1) Multi-Metal Ensemble Geometry: Dense Mackay icosahedral cluster vertices provide triangular Fe-Fe-Mo active hollows with atomic spacing (~2.72 A) perfectly matching bridge-mode N2 chemisorption; 2) Orbital Backdonation: Strong d-to-pi* backdonation from low-coordination transition metal sites elongates the N#N bond from 1.10 A to 1.26 A, slashing the potential-determining step (*N2 -> *NNH) activation barrier to Delta G_PDS <= 0.42 eV (vs 1.35 eV on Cu); 3) High Faradaic Efficiency: Delivers FE_NRR > 45.2% and NH3 yield rate > 94 ug/(h*mg_cat) at mild overpotential (-0.20 V vs RHE) in ambient water and air, eliminating fossil methane steam reforming and 1.8% of global CO2 emissions. Probe the candidate on how isotopic 15N2 labeling with 1H NMR confirms that synthesized ammonia originates from gas-phase nitrogen rather than nitrate/nitrite contaminants."
    },
    {
        "instruction": "Evaluate candidate understanding of Competitive Hydrogen Evolution Reaction (HER) Suppression during Aqueous Nitrogen Electroreduction.",
        "input": "Candidate claims: 'To boost electrochemical ammonia production in aqueous electrolytes, we should apply much more negative cathode potentials like -1.0 V vs RHE to drive faster electron transfer.'",
        "output": "Critique: The candidate's approach completely destroys NRR selectivity and results in near-100% parasitic hydrogen gas generation. In aqueous media, proton reduction to H2 (HER) has faster kinetics (fewer proton-coupled electron transfers) and higher reactant concentration (water/protons) than dissolved N2 (solubility ~ 0.6 mM). Applying high overpotentials drives the cathode into severe mass-transport limitation for N2, causing Faradaic efficiency to plunge from over 40% to below 1%. Advanced electrocatalytic design mandates: 1) Volcano Peak Potential Window: Operating strictly near the optimal thermodynamic window (-0.15 to -0.25 V vs RHE) where N2 chemisorption is maximized and overpotential for HER remains small; 2) Aperiodic Electronic Structure: Tuning d-band centers to make adsorption free energy for nitrogen more negative than hydrogen (Delta G_*N2 < Delta G_*H), selectively blocking proton poisoning; 3) Hydrophobic Gas-Diffusion Electrodes (GDE): Using PTFE-backed porous gas-diffusion layers with three-phase (gas-liquid-solid) boundaries to boost interfacial N2 concentration by orders of magnitude; 4) Non-Aqueous or Water-in-Salt Electrolytes: Employing concentrated salts or fluorinated ionic liquids to restrict free water activity. Ask the candidate how Faradaic efficiency is calculated from spectrophotometric indophenol blue UV-Vis absorbance."
    },
    {
        "instruction": "Analyze candidate implementation of Distributed Rate Limiting and Quota Enforcement across High-Throughput Microservice Clusters.",
        "input": "Candidate suggests: 'For rate limiting 100k requests/second across 50 API gateway pods, each pod should keep an in-memory counter and reset it every second using a local background timer.'",
        "output": "Critique: The candidate's local in-memory approach allows massive traffic bursts and quota violations (up to 50x over-limit if traffic distributes unevenly or spikes against specific gateway instances). A production-grade distributed rate-limiting architecture mandates: 1) Centralized Redis Cluster with Atomic Lua Scripts: Executing Token Bucket or Generic Cell Rate Algorithm (GCRA) via single atomic Lua scripts in Redis (`redis.call('EVAL', ...)`) to eliminate race conditions without distributed locks; 2) Sliding Window Counter: Storing timestamps in Redis Sorted Sets (`ZADD`, `ZREMRANGEBYSCORE`, `ZCARD`) or combining fixed-window counters with weighted lookback to eliminate window-boundary burst attacks; 3) Local Batching with Lease Consumption: For extreme throughput (millions of RPS), gateways pre-acquire token batches (e.g. 100 tokens per lease) from Redis asynchronously, trading minor precision for 100x lower Redis network latency; 4) RFC 6585 Standard Headers: Returning `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, and `Retry-After` on HTTP 429 Too Many Requests. Probe the candidate on how Redis Cluster slot hash hashing (`{user_id}:ratelimit`) ensures multi-key operations execute on the same shard."
    },
    {
        "instruction": "Evaluate candidate diagnosis and tuning of Linux Page Cache Dirty Throttling and Storage I/O Stalls under Write-Heavy Database Ingestion.",
        "input": "Candidate states: 'When our write-heavy database causes operating system freeze-ups and latency spikes, we should increase `vm.dirty_ratio` and `vm.dirty_background_ratio` to maximum values so the kernel can cache as much data in RAM as possible without touching the SSD.'",
        "output": "Critique: The candidate's action exacerbates the exact pathology causing system freezes. Setting high dirty ratios allows the Linux Page Cache to accumulate dozens of gigabytes of unwritten dirty pages. Once the `vm.dirty_ratio` ceiling is breached, the kernel abruptly triggers synchronous writeback throttling, blocking application worker threads in `D-state` (uninterruptible disk sleep) while the storage controller flushes a massive backlog of dirty blocks, freezing the entire OS and crushing database p99 latencies. Production-grade Linux kernel virtual memory tuning mandates: 1) Lower Dirty Thresholds: Reducing `vm.dirty_background_ratio = 5` and `vm.dirty_ratio = 10` (or specifying absolute bytes via `vm.dirty_background_bytes = 268435456` [256MB] and `vm.dirty_bytes = 1073741824` [1GB]) to initiate smooth, continuous asynchronous background writeback via pdflush/kworker threads; 2) More Frequent Flushing: Decreasing `vm.dirty_writeback_centisecs = 100` (1 second) and `vm.dirty_expire_centisecs = 500` (5 seconds); 3) Direct I/O and Asynchronous I/O (O_DIRECT / io_uring): Bypassing the Linux page cache entirely for database write-ahead logs (WAL) to avoid double-buffering and unpredictable kernel writeback stalls. Ask the candidate how `sync_file_range()` differs from `fsync()`."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 230. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
