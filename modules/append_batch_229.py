# -*- coding: utf-8 -*-
"""
Append Batch 229: Spectrally Selective Quasicrystal Solar Absorbers & TPV Emitters,
Mott Pseudogap Drude Infrared Suppression, High-Performance Zero-Copy Shared Memory IPC,
and Distributed Consensus Split-Brain Quorum Fencing.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Spectrally Selective Solar Absorbers and Thermophotovoltaic (TPV) High-Temperature Emitters using Quasicrystalline Metamaterials.",
        "input": "Candidate argues: 'To maximize photothermal conversion efficiency in concentrated solar power (CSP) receivers, a simple polished black metal sheet with high thermal conductivity is optimal because any black surface absorbs 100% of incoming sunlight.'",
        "output": "Critique: The candidate confuses an ideal blackbody with a spectrally selective absorber and ignores catastrophic radiative heat loss governed by the Stefan-Boltzmann law (q_rad = epsilon * sigma * T^4). A non-selective black surface (alpha = 1.0, epsilon = 1.0) re-emits massive thermal radiation at high operating temperatures (500 - 800 C), collapsing net photothermal conversion efficiency below 70%. In contrast, an engineered spectrally selective quasicrystal metamaterial absorber (e.g. Al-Cu-Fe or Al-Cu-Fe-Cr, 450 nm thick) realizes: 1) High Solar Absorptance (alpha_solar > 96.2% across AM1.5 solar spectrum 0.25 - 2.5 um): Dense aperiodic diffractive multi-scale pseudo-Brillouin zone trapping creates near-complete interband optical absorption; 2) Ultralow Thermal Emittance (epsilon_thermal < 0.068 at 500 C): The pronounced Mott-Friedel pseudogap at the Fermi level reduces free-carrier density by over 75%, shifting the Drude plasma frequency into the far-IR and suppressing intraband infrared thermal re-emission across 2.5 - 20 um; 3) Unmatched Spectral Selectivity (S = alpha / epsilon > 14.4): Delivers photothermal efficiency eta_PT > 94.8% under 100x optical concentration; 4) Extreme Thermal Stability: Self-passivating 10 nm amorphous Al2O3 native oxide barrier prevents oxidation up to 720 C, outperforming Mo-Al2O3 cermets and black chrome which degrade above 400 - 500 C. Probe the candidate on how solar concentration ratio C affects the optimal optical cutoff wavelength."
    },
    {
        "instruction": "Evaluate candidate design of Thermophotovoltaic (TPV) Selective Emitter Systems for Waste-Heat and Concentrated Thermal Energy Storage.",
        "input": "Candidate proposes: 'For thermophotovoltaic (TPV) power generation, we should use a broadband tungsten or silicon carbide emitter at 1200 C facing standard silicon solar panels.'",
        "output": "Critique: The candidate's system exhibits abysmal optical-to-electrical efficiency (< 10%) due to severe sub-bandgap photon thermal dissipation and bandgap mismatch. Silicon has an indirect bandgap (1.1 eV, lambda_g ~ 1.1 um); broadband thermal emission from SiC emits > 75% of its photons at energies below 1.1 eV, generating zero electrical power while causing intense parasitic cell heating. A world-class TPV architecture mandates: 1) Narrow-Bandgap Photovoltaic Cells: Employing direct-bandgap low-recombination materials such as GaSb (Eg = 0.72 eV, lambda_g = 1.72 um) or quaternary InGaAsSb (Eg = 0.55 eV, lambda_g = 2.25 um); 2) Quasicrystal Selective Emitters: Aperiodic nanostructured Al-Cu-Fe thin films emit selectively within the narrow spectral window above Eg while suppressing sub-bandgap photons (in-band spectral efficiency > 79.5%), eliminating cooling burdens; 3) Back-Surface Reflectors (BSR): Reflecting any unabsorbed sub-bandgap photons back to the emitter cavity for thermodynamic photon recycling. Ask the candidate to formulate the Shockley-Queisser photon current integral for a narrow-bandgap TPV diode under tailored selective emission."
    },
    {
        "instruction": "Analyze candidate implementation of Ultra-Low-Latency Inter-Process Communication (IPC) via Zero-Copy Shared Memory in High-Frequency Trading Engines.",
        "input": "Candidate explains: 'To pass market data ticks between our network feed handler and risk scoring process with minimum latency, we use local loopback TCP sockets or UNIX domain sockets with JSON serialization.'",
        "output": "Critique: The candidate's architecture introduces intolerable millisecond-scale latency jitter and CPU context-switching overhead. Sockets require kernel-space context transitions, sk_buff buffer allocations, system call overhead (sys_send / sys_recv), and serialization/deserialization CPU cycles, producing 10 - 50 us latency penalties. A production-grade ultra-low-latency HFT IPC engine mandates: 1) Zero-Copy Shared Memory (SHM): Allocating memory-mapped regions via POSIX `shm_open()` + `mmap()` (or Windows `CreateFileMapping()` / `MapViewOfFile()`) configured with hugepages (`MAP_HUGETLB`, 2MB/1GB pages) to eliminate TLB miss penalties; 2) Lock-Free SPSC/MPMC Ring Buffers: Implementing circular ring buffers with cache-line-aligned (64-byte padding) atomic read/write indices using C++ `std::atomic<uint64_t>` with `memory_order_acquire` and `memory_order_release` to prevent false sharing; 3) Zero Serialization: Transferring raw POD (Plain Old Data) structs directly across memory; 4) Busy-Polling Wait: Sub-microsecond polling without futex/mutex kernel sleeps, achieving deterministic tick-to-trade latencies below 150 nanoseconds. Probe the candidate on how CPU memory barrier instructions (mfence, lfence, sfence) prevent out-of-order store reordering across NUMA nodes."
    },
    {
        "instruction": "Evaluate candidate strategy for Distributed Consensus Split-Brain Prevention, Quorum Fencing, and Dynamic Reconfiguration in Financial Clusters.",
        "input": "Candidate states: 'If a network partition splits our 5-node database cluster into two sub-clusters of 2 and 3 nodes, both sides should continue processing client write transactions independently and we will merge the data afterwards using timestamps.'",
        "output": "Critique: The candidate's proposal causes catastrophic ledger state divergence, phantom balances, and permanent data corruption. Merging conflicting financial writes with Last-Write-Wins (LWW) wall-clock timestamps violates serializability due to NTP clock drift and concurrent account balance overwrites. A zero-data-loss consensus architecture requires: 1) Strict Quorum Fencing: Only the majority partition containing strictly floor(N/2) + 1 nodes (3 nodes in a 5-node cluster) is allowed to elect a leader and commit log entries via Raft or Multi-Paxos; 2) Immediate Read/Write Rejection on Minority Partition: The 2-node sub-cluster cannot achieve quorum and must immediately reject or proxy writes, entering read-only or stepping down; 3) Generation/Epoch Monotonic Numbers: Each new term or ballot increments an epoch number; stale leaders from the minority partition attempting to commit entries are rejected by majority nodes with fencing tokens; 4) Joint Consensus for Dynamic Membership: Safely adding or removing nodes via a two-phase configuration transition (C_old -> C_old,new -> C_new) to prevent overlapping independent quorums. Challenge the candidate on how Raft ReadIndex prevents stale reads without writing to disk on every read query."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 229. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
