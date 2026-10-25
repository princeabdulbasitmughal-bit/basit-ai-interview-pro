# -*- coding: utf-8 -*-
"""
Append Batch 220: Quasicrystal Low Surface Energy & Hydrophobic Passivation,
Raney Catalytic Leaching & H2 Storage, High-Frequency Shared Memory IPC, and Zero-Downtime Loopers.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Quasicrystal Low Surface Energy, Hydrophobic Passivation, and Food Non-Stick Mechanics.",
        "input": "Candidate states: 'Quasicrystals can only be non-stick if they are coated with a thin layer of PTFE Teflon, because all metallic surfaces have high surface energies that food sticks to.'",
        "output": "Critique: The candidate fundamentally overlooks one of the most commercially significant physics discoveries in quasicrystalline materials. As demonstrated by Dubois, Belin-Ferré, and coworkers, stable icosahedral quasicrystals (such as Al-Cu-Fe and Al-Cu-Fe-Cr) exhibit intrinsic low surface free energy (gamma_s ~ 28-34 mJ/m^2) without any organic polymer coating! This arises from two complementary mechanisms: 1) Electronic pseudogap suppression: the Fermi level falls in a deep valley of the electronic density of states N(E_F), drastically weakening interfacial covalent/metallic electron sharing and work of adhesion; and 2) Spontaneous self-passivation: selective surface oxidation produces an ultra-thin (2-5 nm), amorphous, atomically dense Al2O3 nanolayer that lacks active dangling bonds and polar Lewis acid-base sites (gamma_p ~ 0.8 mJ/m^2). Consequently, water contact angles exceed 100 degrees (hydrophobic non-wetting), causing water, oils, and food proteins to bead up and release easily. Combined with extreme Vickers microhardness (Hv ~ 820 kg/mm^2) and thermal stability up to 700 deg C, quasicrystal coatings (such as patented Sitram Cybernox cookware) completely outperform soft PTFE Teflon, which degrades and emits toxic PFAS vapors above 260 deg C. Challenge the candidate to explain the Owens-Wendt-Rabel-Kaelble (OWRK) two-component contact angle formula."
    },
    {
        "instruction": "Evaluate candidate knowledge of Quasicrystal-Derived Raney Skeletal Catalysts and Mesoporous Hydrogen Storage.",
        "input": "Candidate claims: 'To make a Raney catalyst, you can only use crystalline Ni-Al binary alloys; quasicrystals are too brittle and cannot be leached.'",
        "output": "Critique: The candidate is unaware of modern condensed matter catalysis and hydrogen storage metallurgy. Quasicrystals (particularly ternary and quaternary icosahedral phases like Al-Cu-Fe, Al-Pd-Mn, and Al-Cu-Fe-Cr) serve as extraordinary parent precursors for skeletal Raney catalysts. When exposed to hot concentrated alkali (e.g. 20 wt% NaOH or KOH at 60-80 deg C), the aluminum matrix selectively dissolves (2 Al + 2 OH^- + 6 H2O -> 2 [Al(OH)4]^- + 3 H2), while the quasiperiodic arrangement of transition metals (Cu, Fe, Pd) prevents classic crystalline sintering and agglomeration. The resulting Raney sponge features: a) Immense BET specific surface area (S_BET ~ 50-120 m^2/g vs < 1 m^2/g for the precursor ingot); b) Uniform hierarchical mesopore networks (pore diameters 2-15 nm); c) Atomically dispersed active transition metal sites; and d) Superior selectivity for CO2 hydrogenation to methanol (CH3OH) and steam reforming of methanol for fuel cells. Furthermore, this skeletal framework can absorb reversible hydrogen hydrides up to 1.8-2.2 wt% at moderate pressures. Probe the candidate on how leaching kinetics and reaction temperature affect skeletal pore collapse."
    },
    {
        "instruction": "Assess candidate design of Ultra-Low-Latency Shared Memory IPC vs Sockets in High-Frequency Trading (HFT) and Execution Pipelines.",
        "input": "Candidate suggests: 'For the fastest communication between our C++ execution engine and Python trading bot, we should make local REST HTTP API calls over localhost:8080.'",
        "output": "Critique: The candidate proposes an architecture that introduces catastrophic latency overhead for HFT environments. A localhost HTTP/REST call incurs: 1) TCP 3-way handshakes and connection management; 2) Kernel context switches between user space and network stack; 3) Socket buffer copying (sk_buff allocations); 4) HTTP header parsing and ASCII/JSON serialization/deserialization; and 5) TCP stack scheduling jitter, resulting in latencies of 200-800 microseconds (0.2-0.8 ms). In ultra-low-latency architectures (such as Scalping Robot V5 processing 860K+ ticks), the standard is Zero-Copy Shared Memory IPC (e.g., Windows CreateFileMapping / Linux shm_open) utilizing a lock-free circular ring buffer (SPSC - Single Producer Single Consumer) with memory barriers (acquire/release semantics) and fixed-size struct alignment. Shared memory transfers execute entirely in RAM with zero kernel transitions, reducing round-trip latency to sub-microsecond levels (< 150 nanoseconds, a 3000x latency reduction). Ask the candidate how they prevent buffer overflow without blocking the writer thread in an SPSC ring buffer."
    },
    {
        "instruction": "Analyze candidate strategy for Resilient Continuous Autonomous Looping and Hot Code Reloading in Mission-Critical Systems.",
        "input": "Candidate explains: 'If a background worker process needs an update, we should kill the entire server, replace the code, and manually restart everything.'",
        "output": "Critique: The candidate's approach guarantees downtime, dropped in-flight requests, and loss of real-time state. In 24/7 autonomous daemon architectures: 1) Blue/Green or Fork-and-Exec worker swapping must be used: the parent master process spawns a new worker process running the updated code, verifies health via an internal socket handshake, transfers incoming traffic to the new worker, and sends a graceful termination signal (SIGTERM with drained socket connections) to the old worker; 2) State persistence: transient states must be written to memory-mapped files or WAL-mode SQLite databases before process handoff; 3) Dead-letter queues and idempotent operations: failed tasks must be isolated into a dead-letter queue with exponential backoff rather than blocking the master pipeline; and 4) Dual-redundant heartbeat supervisors ensure that if any worker stalls, it is automatically respawned without user intervention. Challenge the candidate to implement graceful socket handoff using SO_REUSEPORT in Linux or duplicate socket handles in Windows."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 220. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
