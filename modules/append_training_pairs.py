import json
import os

new_pairs = [
    {
        "instruction": "Evaluate candidate explanation of Hume-Rothery stabilization mechanism in Tsai-type icosahedral quasicrystals.",
        "input": "Candidate says: 'Quasicrystals are stable because the Fermi surface touches the quasi-Brillouin zone boundary (2k_F ≈ K_p), creating a deep pseudogap at the Fermi energy that lowers the electronic kinetic energy.'",
        "output": json.dumps({
            "interviewerReply": "Beshak, Fermi surface-Brillouin zone interaction (Hume-Rothery mechanism) electronic structure ko stabilize karta hai. Lekin Al-Cu-Fe system mein d-state hybridization ka kya role hai?",
            "nextQuestion": "How does transition metal d-band hybridization with Al sp-conduction states deepen the pseudogap in Raynor valence theory, and why does substituting Fe with Mn or Cr alter the thermal conductivity?",
            "score": 92,
            "isCompleted": False
        })
    },
    {
        "instruction": "Analyze candidate architectural response on handling split-brain in Raft consensus clusters across 3 data centers.",
        "input": "Candidate proposes 5 nodes: 2 in DC-A, 2 in DC-B, 1 in DC-C (witness node).",
        "output": json.dumps({
            "passed": True,
            "score": 94,
            "feedback": "Excellent quorum partitioning design. Having odd number of nodes with an independent witness in DC-C guarantees strict majority (3/5) even if either primary DC experiences catastrophic network partition.",
            "nextProbingQuestion": "If network partition separates DC-A from DC-B and DC-C, what happens to ongoing in-flight client proposals that received a local append entry in DC-A?"
        })
    },
    {
        "instruction": "Evaluate candidate Python code for a lock-free ring buffer for streaming real-time audio frames at 16kHz.",
        "input": "Candidate provides atomic pointer swap with multiprocessing.shared_memory and threading.Condition.",
        "output": json.dumps({
            "passed": True,
            "score": 90,
            "latencyProfile": "Sub-millisecond frame delivery for WebRTC PCM16 chunks",
            "feedback": "Good use of shared memory buffers to prevent inter-process serialization overhead.",
            "suggestions": ["Add memory barrier fences to guarantee sequential consistency across NUMA nodes."]
        })
    },
    {
        "instruction": "Probe candidate on difference between 3D icosahedral (i-QC) and 2D decagonal (d-QC) quasicrystals in materials engineering.",
        "input": "Candidate states that decagonal quasicrystals are periodic along the c-axis but quasiperiodic in the plane.",
        "output": json.dumps({
            "interviewerReply": "Sahi farmaya, decagonal phases 1D periodic aur 2D quasiperiodic hoti hain. Yeh anisotropy mechanical properties ko kaisay affect karti hai?",
            "nextQuestion": "In applications like low-friction thermal barrier coatings, how does the periodic c-axis orientation influence epitaxial bonding to titanium or superalloy substrates?",
            "score": 95,
            "isCompleted": False
        })
    },
    {
        "instruction": "Evaluate candidate approach to mitigating toxic liquidation cascades in perpetual futures decentralized exchanges (DEX).",
        "input": "Candidate proposes using dynamic funding rates linked to skew and TWAP-based oracle aggregation to prevent front-running flash loans.",
        "output": json.dumps({
            "passed": True,
            "score": 96,
            "feedback": "Robust DeFi risk model. TWAP mitigation coupled with insurance fund buffer prevents sandwich attacks.",
            "nextQuestion": "How do you prevent oracle stale-price attacks during extreme L1 gas congestion periods?"
        })
    },
    {
        "instruction": "Analyze candidate design for an automated leaching reactor for Raney-type hydrogen catalysts from Al-Cu-Fe quasicrystal precursors.",
        "input": "Candidate explains chemical leaching in 10M NaOH at 80°C to selectively dissolve Al and leave high-surface-area nanoporous Fe-Cu framework.",
        "output": json.dumps({
            "passed": True,
            "score": 97,
            "feedback": "Accurate leaching protocol based on Raney alloy catalysis principles. Nanoporous skeleton exhibits enhanced electrocatalytic HER activity.",
            "nextProbingQuestion": "How do you control passivation oxide formation on residual Fe sites during water washing and drying under inert argon?"
        })
    }
]

dataset_path = r"E:\basit-ai-interview\data\training_dataset_interview_pairs.jsonl"
with open(dataset_path, "a", encoding="utf-8") as f:
    for item in new_pairs:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(new_pairs)} verified pairs. Dataset updated at: {dataset_path}")
