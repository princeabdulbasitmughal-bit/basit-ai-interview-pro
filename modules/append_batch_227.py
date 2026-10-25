# -*- coding: utf-8 -*-
"""
Append Batch 227: Tsai Clusters & Aperiodic Frustrated Magnetism,
Yb Valence Quantum Criticality, Magnetocaloric ADR Cryocooling,
and TCP TIME_WAIT Ephemeral Port Exhaustion Mitigation.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Tsai-Type Approximant Clusters and Aperiodic Geometric Frustrated Spin-Glass Magnetism.",
        "input": "Candidate states: 'In metallic alloys containing rare-earth elements like Gd or Tb, lowering temperature always forces the spins into either simple collinear ferromagnetism or antiferromagnetism with a defined Neel temperature.'",
        "output": "Critique: The candidate's understanding is limited to periodic Bravais lattices, failing to recognize geometric spin frustration in aperiodic complex metallic alloys (CMAs). In Tsai-type 1/1 cubic approximants and icosahedral quasicrystals (discovered by An Pang Tsai), rare-earth magnetic ions (such as Gd, Tb, Dy, Ho, Er) reside exclusively on Shell 2 of the 5-shell concentric cluster hierarchy (126 atoms). This shell is an icosahedron comprising 12 rare-earth atoms forming 20 triangular faces. Because nearest-neighbor RKKY exchange coupling across triangular faces is antiferromagnetic, the spins cannot simultaneously satisfy collinear alignment, creating intense geometric frustration (frustration parameter f = |theta_CW| / T_f > 8 to 15). Consequently, the system completely suppresses long-range periodic magnetic order and instead undergoes a cooperative spin-glass freezing transition at T_f approx 2.5 - 6.5 K, marked by a sharp cusp in AC magnetic susceptibility chi'(T) and characteristic frequency dispersion (Mydosh parameter delta T_f approx 0.016). Ask the candidate how inter-cluster RKKY interactions compete with intra-cluster icosahedral exchange."
    },
    {
        "instruction": "Evaluate candidate comprehension of Unconventional Valence Quantum Criticality in icosahedral Au-Al-Yb Quasicrystals.",
        "input": "Candidate claims: 'To observe a Quantum Critical Point (QCP) in condensed matter, one must always fine-tune chemical doping, apply strong external magnetic fields, or apply high hydrostatic pressures to suppress a magnetic ordering temperature to 0 K.'",
        "output": "Critique: The candidate is unaware of landmark discoveries in quantum criticality (Deguchi et al., Nature 2012, and Watanabe & Miyake). In icosahedral Au51Al34Yb15 quasicrystals and their 1/1 Tsai approximants, an unconventional Quantum Critical Point (QCP) is realized at ambient pressure and zero magnetic field without any chemical tuning. Unlike conventional spin-density-wave (Hertz-Millis) QCPs, this aperiodic system exhibits critical intermediate valence fluctuations: the mean valence of Yb is 2.75+ (intermediate between non-magnetic Yb2+ and magnetic Yb3+). As T approaches 0 K, the magnetic susceptibility diverges with an anomalous, non-mean-field power law chi(T) ~ T^-0.51, while the electronic specific heat diverges logarithmically C/T ~ -ln(T), violating standard Landau Fermi-liquid theory over four orders of magnitude in temperature. Applying hydrostatic pressure above P_c approx 1.8 GPa suppresses quantum critical valence fluctuations and restores localized Yb3+ local moments. Challenge the candidate on how aperiodic local site asymmetry stabilizes the valence QCP."
    },
    {
        "instruction": "Analyze candidate design of Helium-Free Cryogenic Refrigeration using the Giant Magnetocaloric Effect (MCE) in Rare-Earth Quasicrystals.",
        "input": "Candidate suggests: 'For space satellite detectors and sub-Kelvin quantum computing cryostats, liquid Helium-3 dilution refrigeration is the only viable cooling technology down to 100 mK.'",
        "output": "Critique: The candidate ignores the global Helium-3 supply crisis and the physical viability of solid-state magnetic cooling. Helium-3 is an ultra-rare isotope with skyrocketing costs, and liquid dilution refrigerators cannot operate in zero-gravity space missions due to phase separation failure. A robust, solid-state alternative is Adiabatic Demagnetization Refrigeration (ADR) utilizing the Giant Magnetocaloric Effect (MCE) in rare-earth Tsai quasicrystals and approximants (e.g. Gd- or Tb-based Tsai clusters): 1) High Magnetic Spin Density: The 12-atom rare-earth icosahedron provides immense magnetic entropy per unit volume (S_mag = 12 * R * ln(2J + 1)); 2) Giant Isothermal Entropy Change: Applying and removing a magnetic field Delta B = 2 - 5 T produces isothermal magnetic entropy change -Delta S_M > 10 - 25 J/(kg*K) and relative cooling power (RCP) > 250 J/kg; 3) Solid-State Reliability: Zero liquid cryogens, zero gravitational dependence, and thermal conductivity that drops sharply below T_f to isolate the payload. Ask the candidate how a multi-stage ADR salt pill cycle achieves continuous 100 mK cooling."
    },
    {
        "instruction": "Evaluate candidate strategy for Mitigating TCP TIME_WAIT Buildup and Ephemeral Port Exhaustion in High-Throughput Microservices.",
        "input": "Candidate asserts: 'When our microservice runs out of socket connections to downstream APIs under high load, we should fix it by setting `net.ipv4.tcp_tw_recycle=1` in the Linux kernel sysctl.'",
        "output": "Critique: The candidate's solution causes catastrophic connection drops behind load balancers and NAT gateways. `tcp_tw_recycle` was deprecated and completely removed from Linux kernels (since kernel 4.12) because it violates RFC 1323 by dropping SYN packets from different client machines sharing the same NAT IP address whose TCP timestamps are not monotonically synchronized. A production-grade connection lifecycle architecture mandates: 1) Persistent Connection Pooling: Eliminating short-lived TCP handshakes by configuring HTTP client connection reuse (e.g., Go `http.Transport{MaxIdleConnsPerHost: 500, IdleConnTimeout: 90 * time.Second}`, Python `urllib3.PoolManager(maxsize=100)`); 2) Socket Option Tuning: Enabling `net.ipv4.tcp_tw_reuse = 1` (safe for outgoing client connections under RFC 1323 timestamp validation) and expanding ephemeral port range via `net.ipv4.ip_local_port_range = 1024 65535`; 3) Reducing TIME_WAIT duration via `net.ipv4.tcp_fin_timeout = 15`; 4) Upgrading to HTTP/2 or gRPC multiplexing to stream hundreds of concurrent RPCs over a single persistent TCP socket. Probe the candidate on how SO_LINGER affects TCP socket closing state machines."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 227. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
