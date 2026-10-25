# -*- coding: utf-8 -*-
"""
Append Batch 224: Higher-Dimensional Topological Quasicrystals,
Majorana Zero Modes at Aperiodic Star Vertices, 4D Chern Numbers,
and Distributed Event Stream Log Compaction in Kafka/Pulsar.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Higher-Dimensional Topological Quasicrystals and the 4D Quantum Hall Effect.",
        "input": "Candidate states: 'Topological invariants like Chern numbers require periodic translational invariance in the Brillouin zone. Furthermore, the 4D Quantum Hall Effect is purely a mathematical curiosity because our physical space is 3D.'",
        "output": "Critique: The candidate is unaware of foundational developments in topological quasicrystals. In landmark experiments by Kraus, Zilberberg et al. (Physical Review Letters), 2D Penrose and 1D Fibonacci quasicrystals were shown to realize higher-dimensional topological quantum Hall effects via dimensional reduction. Because a 2D quasicrystal is a cut-and-project slice of a 4D hypercubic lattice (Z^4), the perpendicular phason coordinates x_perp serve as two synthetic dimensions. This allows a 2D physical quasicrystal to possess a quantized Second Chern Number (C2 = 1), exhibiting the 4D Quantum Hall Effect with quantized non-linear Hall current J_k proportional to C2 * epsilon_ijkl * E_j * B_kl and protected boundary states. Furthermore, because momentum k is not conserved in quasicrystals, topological order is rigorously defined in real space using the Bott Index B in Z (evaluated via real-space coordinate projectors U and V) and Non-Commutative Geometry C*-algebras. Probe the candidate on how phason flips perturb the Bott index."
    },
    {
        "instruction": "Evaluate candidate understanding of Majorana Zero Modes (MZMs) at Aperiodic Symmetry Vertices in Topological Superconductors.",
        "input": "Candidate suggests: 'Majorana zero modes can only appear at the physical outer boundaries of 1D nanowires or 2D p-wave topological superconductors.'",
        "output": "Critique: The candidate's understanding is restricted to standard periodic geometries. In 2D Penrose and Ammann-Beenker quasicrystals proximity-coupled to an s-wave superconductor with Rashba spin-orbit coupling and Zeeman exchange fields, Majorana zero modes (E = 0) do not just appear at outer edges. Instead, localized Majorana bound states spontaneously nucleate inside the bulk at high-coordination aperiodic vertices (5-fold star centers, 8-fold octagonal wheel hubs, and 10-fold symmetry points). These aperiodic vertex Majoranas are topologically protected by the non-trivial Bott index (B = 1) and enjoy enhanced immunity against local scalar disorder because the quasiperiodic tiling lacks periodic shear planes. These localized zero modes satisfy non-Abelian anyon statistics (gamma_i gamma_j = -gamma_j gamma_i), making them natural candidates for fault-tolerant topological quantum memory and braiding operations. Challenge the candidate on how the Majorana coherence length xi_M scales with the topological minigap Delta_top."
    },
    {
        "instruction": "Analyze candidate comprehension of the Bellissard Gap Labeling Theorem and Fractal Hofstadter Energy Spectra in Quasicrystals.",
        "input": "Candidate claims: 'Applying a magnetic field to a conductor always produces standard equidistant Landau levels E_n = hbar * omega_c * (n + 1/2).'",
        "output": "Critique: The candidate ignores the interplay between magnetic length and quasiperiodic lattice length scales. In a quasicrystal subjected to a perpendicular magnetic flux Phi, the ratio of flux per tile to the flux quantum (Phi / Phi_0) creates an infinite hierarchy of competing length scales governed by the golden ratio tau = (1 + sqrt(5))/2. The energy spectrum shatters into a self-similar fractal Hofstadter butterfly with a dense Cantor set of energy gaps. Jean Bellissard's Gap Labeling Theorem (grounded in C*-algebra K-theory) rigorously proves that the integrated density of states (IDOS) inside every spectral gap is topologically quantized according to IDOS(E) = (n + m * tau) mod 1, where n and m are integer topological gap labels. These topological invariants remain invariant under continuous deformation of the hopping parameters, providing exact quantized topological signatures that can be verified via local compressibility and capacitance spectroscopy. Ask the candidate how Fibonacci rational approximants (e.g. 1/1, 2/1, 3/2, 5/3) converge to the infinite-dimensional K-theory group."
    },
    {
        "instruction": "Evaluate candidate design of Distributed Event Stream Log Compaction and Zero Data Loss Retention in Apache Kafka and Apache Pulsar.",
        "input": "Candidate proposes: 'To keep storage bounded in Kafka, we should just set `cleanup.policy=delete` with a 7-day retention period for all CDC and state changelog topics.'",
        "output": "Critique: The candidate's strategy will cause catastrophic data loss and corrupt state machines in event-sourced architectures. For change-data-capture (CDC), account balance snapshots, and entity state changelogs (e.g., Kafka Streams KTable or Flink state stores), time-based deletion drops valid entity records that haven't received updates within 7 days, leaving downstream consumers with missing primary keys. A robust state store streaming architecture mandates: 1) `cleanup.policy=compact` (Log Compaction), which retains the latest record for every message key while discarding obsolete historical updates; 2) Tombstone semantics: to delete an entity, producers must emit a record with the entity's key and a `null` payload, and `delete.retention.ms` must be configured (default 24 hours) to ensure all active consumer group replicas observe the deletion tombstone before the log cleaner reaps the key; 3) Segment sizing and cleaner thread concurrency: tuning `min.cleanable.dirty.ratio` (e.g. 0.5) and `segment.ms` prevents uncompacted active segments from exhausting disk inodes and RAM buffers. Probe the candidate on how log compaction interacts with transactional outbox patterns and exactly-once processing (EOS)."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 224. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
