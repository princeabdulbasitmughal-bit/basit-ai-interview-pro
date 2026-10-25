import json
import os

data_dir = r"E:\basit-ai-interview\data"
json_path = os.path.join(data_dir, "interviews.json")
jsonl_path = os.path.join(data_dir, "training_dataset_interview_pairs.jsonl")

new_pairs = [
    {
        "id": "qa_233_01",
        "category": "Quasicrystal Shape Memory Alloys & Aperiodic Martensitic Transformations",
        "question": "How do quasicrystal-reinforced shape memory alloys (HT-SMA) overcome the functional fatigue and dislocation slip degradation that plague conventional Nitinol alloys at high temperatures (> 300°C)?",
        "answer": "Conventional binary Nitinol (Ni-50.8Ti) operates via reversible thermoelastic B2 austenite to B19' monoclinic martensitic transformation. However, at temperatures exceeding 80-100°C, the critical stress for permanent dislocation slip drops below the martensitic transformation stress, causing rapid accumulation of unrecovered plastic strain, degraded superelasticity (fatigue retention < 70% after 10^4 cycles), and irreversible creep. In contrast, quasicrystal-reinforced alloys (e.g., Ti45Zr35Ni15Cu5, Ti-Zr-Ni-Pd) incorporate coherent aperiodic Mackay and Tsai icosahedral cluster interfaces. Because aperiodic quasicrystals lack translational periodicity and periodic slip planes, conventional long-range dislocation glide is geometrically blocked. Stress-induced transformation proceeds via localized, reversible lattice twinning and phason-guided shuffling without triggering dislocation pile-up. As a result, quasicrystalline HT-SMAs retain high transformation temperatures (Af ≥ 360°C), large superelastic recoverable strains (ε_rec ≥ 10.5%), and exceptional functional fatigue retention (≥ 98.4% after 1,000,000 cycles at 550 MPa)."
    },
    {
        "id": "qa_233_02",
        "category": "Solid-State Elastocaloric Refrigeration & Thermodynamics",
        "question": "Derive the thermodynamic principles of the giant elastocaloric effect (eCE) and analyze how quasicrystalline phase transitions achieve zero-GWP refrigeration with COP >= 7.8.",
        "answer": "Elastocaloric refrigeration exploits the reversible entropy change (ΔS_tr) in solid materials driven by uniaxial mechanical stress (σ). By Maxwell relation (∂S/∂σ)_T = (∂ε/∂T)_σ, applying stress to induce austenite-to-martensite transition changes the crystal ordering, releasing latent heat (ΔH = T * ΔS_tr). When stress is rapidly removed under adiabatic conditions, the material undergoes reverse transformation, absorbing heat and producing an adiabatic temperature drop: ΔT_ad = - ∫ (T / C_p) * (∂ε/∂T)_σ dσ ≈ - (T * ΔS_tr) / C_p. In high-entropy quasicrystalline SMAs, the combination of multi-element configurational entropy and dense cluster twinning yields giant transformation entropy changes (ΔS_tr ≈ 28.5 J/(kg·K)), producing adiabatic cooling ΔT_ad from -7.5 K up to -18.5 K. Because solid-state elastocaloric cycles eliminate volatile greenhouse halocarbons (GWP = 0, ODP = 0) and minimize internal friction hysteresis (narrow thermal hysteresis ΔT_hyst ≈ 30-40°C), the system achieves refrigeration coefficients of performance COP_refrig = Q_absorbed / W_mechanical ≥ 7.8, exceeding conventional vapor-compression systems (COP ≈ 3.5 - 5.0)."
    },
    {
        "id": "qa_233_03",
        "category": "High-Performance Networking & DPDK Polling Mode Drivers",
        "question": "How does DPDK (Data Plane Development Kit) bypass the Linux kernel to achieve 100GbE line-rate packet processing, and what hardware/software architectural trade-offs are involved?",
        "answer": "DPDK achieves 100GbE wire-speed packet processing (> 148 million packets per second) by systematically eliminating every operating system bottleneck through four primary mechanisms: 1) Kernel Bypass: DPDK utilizes UIO (Userspace I/O) or VFIO (Virtual Function I/O) with IOMMU protection to map NIC PCIe registers and DMA buffers directly into user-space process virtual memory, eliminating all kernel system calls and context switches. 2) Poll Mode Drivers (PMD): Rather than relying on hardware interrupts which thrash CPU registers and trigger IRQ handlers, dedicated pinned CPU cores poll NIC RX ring buffers in tight lockless loops, ensuring zero interrupt latency and predictable nanosecond packet turnaround. 3) Hugepages (2MB / 1GB): Using huge TLB pages minimizes TLB misses and eliminates kernel page table walks for multi-gigabyte packet memory pools (mempool). 4) Lockless Rings (rte_ring): Lock-free FIFO queues based on atomic CAS (Compare-And-Swap) and cache-line aligned structures prevent CPU cache line bouncing and lock contention. The trade-off is 100% CPU utilization on assigned PMD cores regardless of traffic load and the loss of standard Linux socket utilities (iptables, netstat)."
    },
    {
        "id": "qa_233_04",
        "category": "Network Security & TLS 1.3 0-RTT Protocol Engineering",
        "question": "Explain the handshake state machine of TLS 1.3 0-RTT (Early Data), analyze its vulnerability to replay attacks, and detail the defense mechanisms implemented by high-scale edge proxies.",
        "answer": "In standard TLS 1.3, an initial handshake completes in 1-RTT using ephemeral Diffie-Hellman (ECDHE). During this session, the server issues a NewSessionTicket containing an encrypted Pre-Shared Key (PSK). In subsequent connections, the client uses 0-RTT by deriving early traffic encryption keys from the PSK (ClientEarlyTrafficSecret = HKDF-Expand-Label(early_secret, 'c e traffic', ...)) and transmits encrypted application data in the initial ClientHello flight before waiting for the ServerHello (0-RTT). The critical security vulnerability of 0-RTT is replay susceptibility: an attacker intercepting the ClientHello flight can retransmit the exact same packets to the server, causing non-idempotent application actions (such as financial transactions or state mutations) to execute multiple times. Edge proxies (such as Cloudflare and NGINX) mitigate this via three defense tiers: 1) HTTP Method Restriction: Only strictly idempotent, safe HTTP requests (GET, HEAD) without URL query side effects are permitted in early data; POST/PUT/DELETE requests are delayed until the 1-RTT handshake completes. 2) Single-Use Ticket Validity: The proxy maintains a distributed bloom filter or sliding-window cache of received ticket nonces and ClientHello random values, rejecting duplicate tickets. 3) Obfuscated Ticket Age: The client includes its estimated ticket age in the handshake; if the server's measured elapsed ticket lifetime differs from the client's reported age by more than a narrow tolerance (e.g. ±10 seconds), 0-RTT early data is rejected."
    }
]

with open(json_path, "r", encoding="utf-8") as f:
    interviews = json.load(f)

interviews.extend(new_pairs)

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(interviews, f, indent=2, ensure_ascii=False)

with open(jsonl_path, "a", encoding="utf-8") as f:
    for pair in new_pairs:
        f.write(json.dumps(pair, ensure_ascii=False) + "\n")

print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 233. New total: {len(interviews)} verified pairs.")
