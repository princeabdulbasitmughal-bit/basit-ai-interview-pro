# -*- coding: utf-8 -*-
"""
Append Batch 226: Quasicrystal PGEC Thermoelectrics, Mott Thermopower Asymmetry,
eBPF XDP Sub-Microsecond Packet Filtering, and Raft Joint Consensus Reconfiguration.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Quasicrystal Thermoelectrics and the Phonon-Glass Electron-Crystal (PGEC) Slack Paradigm.",
        "input": "Candidate states: 'Metals are fundamentally unsuitable for thermoelectric generation because the Wiedemann-Franz law forces thermal conductivity to scale directly with electrical conductivity, capping ZT below 0.01.'",
        "output": "Critique: The candidate's understanding applies only to standard periodic metals, ignoring the breakthrough physics of aperiodic complex metallic alloys (CMAs). As demonstrated by Maciá, Poon, and Takeuchi, quasicrystals (such as icosahedral Al-Cu-Fe) uniquely circumvent the Wiedemann-Franz trade-off by realizing the Slack 'Phonon-Glass Electron-Crystal' (PGEC) paradigm: 1) Diffuson Thermal Transport: Because quasicrystals lack periodic translational symmetry, Umklapp phonon-phonon scattering is replaced by cluster boundary scattering, pinning lattice thermal conductivity near the Cahill-Pohl minimum diffuson limit (kappa_ph approx 1.25 W/(m*K)), comparable to silica glass; 2) Mott Thermopower Asymmetry: The sharp Mott-Friedel pseudogap at the Fermi level E_F generates an immense slope [d ln sigma(E) / dE], producing unusually large Seebeck thermopower (|S| approx 60 to 150 uV/K) with p-type (hole) or n-type (electron) sign determined by the Raynor e/a ratio; 3) Negative TCR: Unlike crystalline metals whose resistivity increases with temperature, quasicrystal conductivity increases with temperature (d sigma / dT > 0), driving power factors P = S^2 * sigma to peak at elevated temperatures (600 - 1000 K) with ZT exceeding 0.50. Probe the candidate on how Si or Ru doping tunes the Fermi level across the pseudogap."
    },
    {
        "instruction": "Evaluate candidate design of Solid-State Thermoelectric Waste-Heat Recovery (TEG) Systems versus Organic Rankine Cycles (ORC).",
        "input": "Candidate argues: 'For industrial kiln and automotive exhaust heat recovery at 700 K, Organic Rankine Cycles with turbines are always superior because their thermodynamic efficiency is higher than TEGs.'",
        "output": "Critique: The candidate evaluates thermal efficiency in isolation from system complexity, capital expenditure (CapEx), and operational maintenance (OpEx). While Organic Rankine Cycles (ORC) achieve 10-15% thermodynamic efficiency, they require mechanical turbines, high-pressure fluid pumps, volatile organic working fluids, condensers, and dynamic seals that fail under thermal cycling, vibration, and automotive shock. In contrast, solid-state Thermoelectric Generators (TEG) based on Al-Cu-Fe quasicrystals offer: 1) Zero moving parts and zero fluid leakage, providing MTBF > 100,000 hours in harsh industrial exhaust environments; 2) Direct solid-state DC power conversion via Seebeck thermocouples operating across Delta T = 450 K with power densities exceeding 1.2 - 2.8 W/cm^2; 3) Low cost and toxicity: Unlike commercial Bi2Te3 (which oxidizes and sublimates above 250 C and relies on toxic, scarce Tellurium) or SiGe (which requires expensive vacuum sputtering), Al-Cu-Fe quasicrystals utilize non-toxic, Earth-abundant elements with thermal stability up to 800 C. Ask the candidate how thermal expansion coefficient (CTE) mismatch is accommodated at the ceramic cold-plate interface."
    },
    {
        "instruction": "Analyze candidate comprehension of Linux Kernel eBPF XDP (eXpress Data Path) for High-Throughput Packet Processing and Sub-Microsecond Firewalls.",
        "input": "Candidate proposes: 'To handle 10 million packets per second with low latency, we can write an iptables or nftables firewall rule set, or inspect packets in user-space via libpcap socket sniffing.'",
        "output": "Critique: The candidate's approach will collapse under network interrupt storms and OS memory allocation bottlenecks. Standard Linux networking allocates an `sk_buff` data structure for every incoming packet, traversing the TCP/IP stack with multiple context switches and CPU cache invalidations, capping single-core throughput well below 1.5 Mpps. A high-performance telemetry and security architecture mandates: 1) eXpress Data Path (XDP): Executing an in-kernel eBPF bytecode program directly inside the network driver's RX ring buffer before the OS allocates an `sk_buff`; 2) XDP Actions: Executing zero-copy decisions—`XDP_DROP` for DDoS mitigation, `XDP_TX` for microsecond packet reflection, or `XDP_REDIRECT` via AF_XDP (XSK) sockets to pass raw packets directly into user-space memory buffers with zero kernel copies; 3) Lockless State: Using eBPF BPF_MAP_TYPE_PERCPU_HASH and BPF_MAP_TYPE_LRU_HASH to track connection rate limits and IP reputation without spinlock contention across NUMA nodes. Challenge the candidate on the differences between XDP Generic, Native (Driver), and Offloaded (NIC SmartNIC) modes."
    },
    {
        "instruction": "Evaluate candidate understanding of Distributed Consensus Reconfiguration: Raft Joint Consensus versus Single-Server Membership Changes.",
        "input": "Candidate suggests: 'To add three new nodes to a running Raft consensus cluster, we can simply update the configuration files on all servers and restart the cluster nodes one by one.'",
        "output": "Critique: The candidate's procedure guarantees split-brain states and conflicting leader elections during cluster reconfiguration. When transitioning between configuration C_old and C_new, arbitrary sequential node restarts allow disjoint majorities: nodes still running C_old can elect one leader while updated nodes running C_new can elect a second independent leader, resulting in dual uncoordinated log commits. In Diego Ongaro's Raft specification, safe cluster membership transition requires: 1) Joint Consensus (C_old,new): The leader commits a transitional configuration entry C_old,new that requires separate majorities from BOTH C_old and C_new to agree on any log entry or election; 2) Once C_old,new is committed across both majorities, the leader commits the final C_new entry; 3) Alternatively, single-server stepping (adding or removing strictly one server at a time) prevents overlapping majorities without joint consensus, provided each change is fully committed before the next begins. Ask the candidate how Raft non-voting learners (Catch-Up phase) prevent cluster availability drops when onboarding empty new nodes."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 226. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
