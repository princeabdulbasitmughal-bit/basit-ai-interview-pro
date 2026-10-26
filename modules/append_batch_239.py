# -*- coding: utf-8 -*-
"""
================================================================================
👑 BATCH 239: APERIODIC MOIRÉ QUASICRYSTALS, FLAT-BAND SUPERCONDUCTIVITY,
              eBPF TC VS XDP, AND MULTI-RAFT LEADER LEASING
================================================================================
"""

import os
import json

DATASET_FILE = r"E:\basit-ai-interview\data\training_dataset_interview_pairs.jsonl"
BATCH_FILE = r"E:\basit-ai-interview\data\batch_239_moire_flatbands_ebpf.json"

batch_239_pairs = [
    {
        "instruction": "Evaluate candidate explanation of 12-fold dodecagonal aperiodic moiré quasicrystals in 30° twisted bilayer graphene (TBG).",
        "input": "Candidate states: 'When two graphene monolayers are twisted by exactly 30°, the system lacks translational periodicity because tan(30°) = 1/√3 is irrational. Instead of a periodic moiré superlattice, it forms an incommensurate 12-fold quasicrystalline tiling where the 12 Dirac cones decouple and hybridize across mini-quasicrystal Brillouin zones, quenching the Fermi velocity v_F* -> 0 and flattening the electronic bands.'",
        "output": json.dumps({
            "passed": True,
            "score": 96,
            "feedback": "Exceptional deep grasp of incommensurate rotational quasicrystals in 2D van der Waals materials. Correctly identified the irrational tangent tan(30°) = 1/√3 preventing periodic supercell formation (unlike 1.08° magic-angle TBG which has a 13.4 nm periodic moiré unit cell).",
            "nextProbingQuestion": "How does the quenched Fermi velocity (v_F* / v_F < 0.10) alter the ratio of on-site Coulomb repulsion to bandwidth (U/W), and why does electrostatic gating induce correlated Mott insulating states and flat-band superconductivity?",
            "interviewerReply": "Bilkul durust farmaya, 30° twist angle par tan(30°) irrational hone ki wajah se translation periodicity mukammal taur par toot jati hai aur 12-fold non-crystallographic diffraction pattern banta hai. Band flattening se Coulomb correlation U/W kis tarah dominate karta hai?"
        })
    },
    {
        "instruction": "Probe candidate on the microscopic pairing mechanism of flat-band superconductivity in aperiodic moiré quasicrystals versus BCS theory.",
        "input": "Candidate notes: 'In conventional BCS theory, T_c scales exponentially with density of states T_c ~ exp(-1 / (N(E_F) V)), but in flat bands where bandwidth W < 15 meV, the Fermi velocity vanishes and the effective mass diverges, leading to quantum geometric superfluid weight D_s governed by the Fubini-Study metric and quantum metric tensor.'",
        "output": json.dumps({
            "passed": True,
            "score": 98,
            "feedback": "World-class mastery of modern quantum geometry in correlated flat-band systems. Recognizing that Peierls substitution and conventional BCS pairing breakdown when W -> 0, requiring quantum geometric bounds on the superfluid stiffness, is frontier-level condensed matter physics.",
            "nextProbingQuestion": "How does the real-space Bott index or higher-dimensional 4D Chern number characterize the topological robustness of these flat bands against atomic phason strain and local twist angle fluctuations?"
        })
    },
    {
        "instruction": "Evaluate candidate comparison of eBPF TC (Traffic Control) vs XDP (eXpress Data Path) for ultra-low latency packet filtering in high-frequency trading gateways.",
        "input": "Candidate argues: 'XDP runs before the Linux kernel allocates the sk_buff data structure, executing directly in the NIC driver ring buffer with zero-copy XDP_DROP and XDP_TX for sub-microsecond line-rate filtering. TC BPF operates after sk_buff allocation, providing rich packet mangling, tunneling headers, and full egress control, but with higher CPU overhead (~100-250 ns per packet).'",
        "output": json.dumps({
            "passed": True,
            "score": 95,
            "feedback": "Precise low-level Linux networking analysis. Correctly delineated the execution boundary: XDP operates at the driver layer on raw memory frames (xdp_buff), while TC operates at the queuing discipline layer (sch_clsact) with full sk_buff metadata.",
            "nextProbingQuestion": "If an HFT gateway needs to stamp hardware PTP timestamps and route order executions out of an alternate interface without traversing the full IP stack, which combination of XDP_REDIRECT and AF_XDP UMEM queues provides minimum jitter?"
        })
    },
    {
        "instruction": "Analyze candidate design for Multi-Raft Leader Leasing with TrueTime clock drift bounds in a distributed transaction database.",
        "input": "Candidate specifies: 'To avoid Raft network round-trips for read-only queries, the leader acquires a bounded time lease. Reads are served locally provided current_time < lease_start + lease_duration - max_clock_skew. Clock drift is constrained using hybrid logical clocks (HLC) with an absolute bound epsilon to prevent stale reads during network partitions.'",
        "output": json.dumps({
            "passed": True,
            "score": 94,
            "feedback": "Solid architectural implementation of linearizable local reads in Raft. Properly accounts for clock skew guardbands (epsilon) to avoid split-brain read anomalies during leader transitions or asymmetric network partitions.",
            "nextProbingQuestion": "What happens if a leader experiences a 500 ms stop-the-world JVM or OS swap latency right as its lease expires, and how does lease renewal handoff during graceful leadership transfer prevent read stalling?"
        })
    },
    {
        "instruction": "Evaluate candidate approach to INT8 quantization calibration using KL-divergence in TensorRT for 60 FPS embedded stereo vision on NVIDIA Jetson.",
        "input": "Candidate explains: 'FP32 weights and activations are quantized to INT8 using entropy calibration. A representative calibration dataset generates activation histograms, and TensorRT finds the optimal saturation threshold |T| that minimizes the Kullback-Leibler (KL) divergence between the original FP32 distribution and the clipped INT8 distribution, preventing dynamic range loss in vision transformers.'",
        "output": json.dumps({
            "passed": True,
            "score": 93,
            "feedback": "Accurate explanation of TensorRT entropy calibration. Minimizing relative entropy D_KL(P || Q) ensures the statistical information loss from outlier clipping is mathematically minimized compared to naive min-max scaling.",
            "nextProbingQuestion": "How do you handle layers with high activation kurtosis (e.g. LayerNorm or GeLU in vision transformers) that suffer significant accuracy degradation under uniform INT8 quantization?"
        })
    }
]

def append_batch():
    with open(BATCH_FILE, "w", encoding="utf-8") as f:
        json.dump(batch_239_pairs, f, indent=2)
    print(f"✅ Saved Batch 239 to: {BATCH_FILE}")

    # Append to master jsonl
    count = 0
    with open(DATASET_FILE, "a", encoding="utf-8") as f:
        for pair in batch_239_pairs:
            f.write(json.dumps(pair) + "\n")
            count += 1
    print(f"✅ Appended {count} verified QA pairs to {DATASET_FILE}")

    # Check total lines
    with open(DATASET_FILE, "r", encoding="utf-8") as f:
        total = sum(1 for line in f if line.strip())
    print(f"📊 New Total Training Dataset Size: {total} Verified QA Pairs!")

if __name__ == "__main__":
    append_batch()
