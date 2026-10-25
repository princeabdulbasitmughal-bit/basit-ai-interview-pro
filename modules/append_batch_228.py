# -*- coding: utf-8 -*-
"""
Append Batch 228: Hydrogen Permeation Barriers & HELP Embrittlement Mitigation,
Ti-Zr-Ni Hydride Storage Thermodynamics, Linux Epoll Starvation & NIC RSS Tuning,
and Distributed Database Lock Escalation & Concurrency Control.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Hydrogen Permeation Barriers (HPB) and Hydrogen-Enhanced Localized Plasticity (HELP) Mitigation in High-Strength Alloys.",
        "input": "Candidate claims: 'To protect 700-bar hydrogen transmission pipelines and fuel storage tanks against hydrogen embrittlement, applying an ordinary electroplated nickel or zinc coating is sufficient because any metal layer blocks hydrogen diffusion equally.'",
        "output": "Critique: The candidate's understanding is fundamentally flawed from both transport physics and metallurgy perspectives. Conventional FCC or BCC electroplated metals (Ni, Zn, Cd) contain columnar grain boundaries and dislocation networks with low activation energy for hydrogen migration (E_p ~ 0.35 - 0.40 eV in Fe/Ni), permitting rapid interstitial hydrogen diffusion and catastrophic Hydrogen-Induced Cracking (HIC). Under high pressure (700 bar H2), dissolved atomic hydrogen concentrates at triaxial stress fields ahead of crack tips, triggering Hydrogen-Enhanced Localized Plasticity (HELP) via localized dislocation mobility acceleration and Hydrogen-Enhanced Decohesion (HEDE) along grain boundaries, dropping Notch Tensile Strength (NTS) by over 70%. In contrast, aperiodic icosahedral Quasicrystal coatings (such as Al-Cu-Fe or Ti-Zr-Ni, 2.5 um thick) provide: 1) Aperiodic Labyrinth Effect: Absence of periodic slip planes and high-angle grain boundary channels elevates migration barrier to E_p = 0.679 eV (65.5 kJ/mol); 2) Immense Permeation Reduction: Achieves Permeation Reduction Factors (PRF) exceeding 2,000x at ambient temperature; 3) Full Embrittlement Immunity: Preserves > 94.8% of Notch Tensile Strength (1,560+ MPa) and retains ductile microvoid coalescence fracture without subcritical crack propagation. Probe the candidate on how Devanathan-Stachurski electrochemical double-cell permeation testing validates PRF."
    },
    {
        "instruction": "Evaluate candidate design of Solid-State Hydrogen Storage Systems using Aperiodic Intermetallic Hydrides (Ti-Zr-Ni Quasicrystals).",
        "input": "Candidate asserts: 'Solid-state metal hydrides are obsolete for hydrogen vehicles because high-pressure 700 bar composite carbon fiber tanks store far more hydrogen per unit volume and don't require thermal management.'",
        "output": "Critique: The candidate confuses gravimetric metrics with volumetric packing limits and ignores the extreme mechanical hazards of 700-bar gas compression. Compressed H2 gas at 700 bar achieves a volumetric density of only ~39 kg H2/m^3 while requiring expensive multi-stage compressors and parasitic parasitic power losses (> 15% of fuel energy). In contrast, icosahedral Ti-Zr-Ni quasicrystals and their 1/1 rational approximants (Kelton et al., PRL 1999) realize superior solid-state volumetric density: 1) High Volumetric Capacity: Absorbs hydrogen into tetrahedral interstitial sites coordinated by Ti and Zr, reaching [H]/[M] ~ 1.85, corresponding to 2.24 wt% gravimetric capacity and 112 kg H2/m^3 volumetric density—nearly 3x denser than 700 bar gas cylinders and 1.6x denser than liquid cryogenic hydrogen (70.8 kg/m^3); 2) Van 't Hoff Thermodynamics: Moderate absorption enthalpy (Delta H_abs ~ -38.4 kJ/mol H2) yields convenient equilibrium desorption plateau pressures (P_eq ~ 1.25 bar at 250 C), matching PEM fuel cell operating delivery pressures; 3) Pulverization Resistance: The aperiodic cluster elasticity accommodates isotropic lattice expansion (~7.4%) without decrepitation or pulverization, eliminating pyrophoric dust hazards during multi-cycle refueling. Ask the candidate to calculate the thermal cooling load required during rapid 5-minute hydride refueling."
    },
    {
        "instruction": "Analyze candidate troubleshooting of Linux Epoll Starvation, Thread Thundering Herd, and Multi-Queue NIC RSS Load Balancing in Low-Latency Network Engines.",
        "input": "Candidate states: 'If our high-throughput TCP server encounters tail latency spikes under 100k concurrent connections, we should increase the number of worker threads all listening on the same epoll file descriptor with EPOLLET (Edge Triggered) mode.'",
        "output": "Critique: The candidate's recommendation induces the catastrophic epoll thundering herd problem and exacerbates thread lock contention. Multiple worker threads polling a shared epoll instance cause all threads to wake on new socket activity, leading to cache bouncing, context-switching overhead, and epoll lock contention in the kernel. A world-class low-latency architecture requires: 1) SO_REUSEPORT with Epoll-Per-Core: Assigning an independent epoll instance and dedicated worker thread pinned via CPU affinity (sched_setaffinity) to each CPU core, allowing kernel-level socket sharding; 2) EPOLLEXCLUSIVE or EPOLLONESHOT: If epoll sharing is unavoidable, using EPOLLEXCLUSIVE flag (Linux 4.5+) to ensure only one thread is awakened per event; 3) Multi-Queue NIC Receive Side Scaling (RSS): Aligning NIC hardware receive queues (RX rings) with CPU core affinity via `smp_affinity` and interrupt handling (`irqbalance` pinning) to avoid cross-NUMA memory bus traversal; 4) Busy-Polling (SO_BUSY_POLL): Enabling low-latency kernel polling (e.g. 50 us socket busy-poll) to bypass hardware interrupt context switches entirely for latency-critical paths (< 10 us). Ask the candidate how eBPF XDP redirect bypasses the entire Linux socket sk_buff stack."
    },
    {
        "instruction": "Evaluate candidate design of Distributed Database Concurrency Control, Lock Escalation Elimination, and Deadlock Resolution in Financial Ledgers.",
        "input": "Candidate suggests: 'To guarantee strict ACID consistency during multi-account balance transfers across thousands of concurrent transactions, we should wrap each transaction in `SELECT * FROM accounts FOR UPDATE` without sorting account IDs, and let the database auto-escalate row locks to table locks if the batch is large.'",
        "output": "Critique: The candidate's approach guarantees catastrophic distributed deadlocks and crushes system throughput. 1) Unordered Lock Acquisition Deadlocks: If Tx1 locks Account A then B, while Tx2 concurrently locks Account B then A, a circular wait (AB-BA) deadlock occurs immediately, forcing transaction rollbacks; 2) Lock Escalation Bottlenecks: In systems like SQL Server, lock escalation from thousands of row locks to an exclusive table lock freezes all concurrent reads and writes across the entire ledger, collapsing throughput from tens of thousands of TPS to single digits; 3) Modern Financial Ledger Architecture: Mandates strict global resource ordering (always acquire row locks in deterministic ascending primary key order `ORDER BY account_id ASC` to eliminate cycles in the Waits-For Graph by construction); 4) Row-Level Granularity & Optimistic Concurrency Control (OCC): Using versioned rows with CAS (`UPDATE accounts SET balance = balance - :amount, version = version + 1 WHERE id = :id AND version = :v`) or Postgres advisory transaction locks (`pg_advisory_xact_lock(hashtext(account_id))`) to isolate accounts without blocking unrelated ledger rows; 5) Micro-Partitioning & Raft Consensus: Partitioning hot merchant accounts across distinct state machine shards. Probe the candidate on how 2-Phase Locking (2PL) differs from Snapshot Isolation (SI) under write-skew anomalies."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 228. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
