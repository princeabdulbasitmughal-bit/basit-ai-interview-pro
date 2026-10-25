# -*- coding: utf-8 -*-
"""
Append Batch 225: Atomic Phason Flip Dynamics across Double-Well Potentials,
High-Temperature Superplasticity in CMAs, eBPF Event Loop Jitter Profiling,
and Conflict-Free Replicated Data Types (CRDTs) Convergence.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Quasicrystal Atomic Phason Jump Kinetics across Double-Well Potentials versus Vacancy Diffusion in Crystalline Metals.",
        "input": "Candidate claims: 'Atomic diffusion in quasicrystals follows the exact same vacancy migration mechanism as fcc metals, requiring the creation of missing lattice vacancies.'",
        "output": "Critique: The candidate fails to distinguish between crystalline defect diffusion and aperiodic phason dynamics. In icosahedral quasicrystals (such as i-Al-Cu-Fe and i-Al-Pd-Mn), atomic transport is uniquely governed by phason flips—localized atomic hops between two quasi-equivalent potential wells separated by a jump barrier (E_act approx 0.88 eV, jump distance d_jump approx 1.48 A). In Penrose P3 and Mackay cluster geometries, three rhombi sharing a common vertex rearrange by flipping the central vertex across a hexagon boundary without destroying long-range quasiperiodic order and without creating true lattice vacancies. Furthermore, under applied shear stress sigma, transition state theory dictates that forward and backward jump rates follow Arrhenius kinetics biased by the activation volume Omega_act approx 0.15 nm^3: Gamma_+/- = nu_0 * exp(-(E_act -/+ sigma * Omega / 2) / (k_B * T)). At room temperature, phason flips are pinned (D_phason < 10^-22 m^2/s), yielding extreme microhardness (>800 Hv). At high temperatures, stress bias creates a net atomic drift velocity producing mechanical internal friction Debye dissipation peaks (tan delta). Ask the candidate how internal friction experiments verify the 0.88 eV barrier."
    },
    {
        "instruction": "Evaluate candidate understanding of High-Temperature Superplasticity and Phason-Assisted Creep Mechanics in Complex Metallic Alloys (CMAs).",
        "input": "Candidate asserts: 'Because quasicrystals are brittle intermetallics, heating them to 700 C simply accelerates brittle cleavage failure without any plastic deformation.'",
        "output": "Critique: The candidate is unaware of high-temperature superplasticity in quasicrystals (demonstrated by Feuerbacher, Inoue, and Urban). At room temperature (T < 450 C), quasicrystals are brittle (K_IC approx 1.0-1.5 MPa*m^1/2) because dislocation motion is severely impeded: as a dislocation glides through an aperiodic lattice, it disrupts matching rules and trails an energetically costly phason fault ribbon (phason wall), locking the dislocation. However, at elevated temperatures (T > 600 C to 800 C, approx 0.7-0.85 T_m), thermal energy unfreezes phason hopping (D_phason approx 10^-13 m^2/s). Rapid phason flips dynamically heal the phason fault directly behind the moving dislocation core. Consequently, quasicrystals undergo a dramatic brittle-to-ductile transition, exhibiting superplastic flow with tensile elongations exceeding 100% to 250%, a high strain-rate sensitivity exponent m approx 0.4-0.5, and a stress exponent n approx 2-3 characteristic of grain boundary sliding accommodated by phason diffusion. Probe the candidate on how dynamic phason relaxation prevents dislocation locking."
    },
    {
        "instruction": "Analyze candidate strategy for Asynchronous Event Loop Latency Profiling and eBPF Tail Jitter Detection in High-Throughput Microservices.",
        "input": "Candidate states: 'To debug p99 latency spikes in our Python FastAPI/uvloop service, we just add timing logs inside each HTTP route handler with `time.perf_counter()`.'",
        "output": "Critique: The candidate's approach fails because user-space application timers cannot measure off-CPU time or event loop starvation. When an asynchronous worker thread is delayed by a synchronous CPU-bound task, garbage collection pause, or OS scheduler contention, the event loop cannot service the epoll/kqueue file descriptor, meaning incoming HTTP requests wait in OS kernel socket queues before user-space code even begins execution. A production-grade observability architecture mandates: 1) eBPF (extended Berkeley Packet Filter) kernel tracing using `sys_enter_epoll_wait` and `sched:sched_switch` to measure the precise time elapsed between network packet arrival on the socket and event loop retrieval; 2) Kernel run-queue latency tracking via `runqlat` to measure how long runnable threads spend waiting for an available CPU core; 3) Asyncio task loop watchdog timers that sample the loop lag (difference between requested sleep duration and actual callback invocation) to detect cooperative multitasking starvation; 4) Offloading CPU-bound tasks (cryptography, JSON parsing, ML inference) to process pools or Rust FFI extensions to prevent single-threaded event loop blocking. Ask the candidate how eBPF USDT probes can be injected into Python runtimes without recompilation."
    },
    {
        "instruction": "Evaluate candidate architecture for Conflict-Free Replicated Data Types (CRDTs): State-based (CvRDT) versus Operation-based (CmRDT) Convergence and Garbage Collection.",
        "input": "Candidate proposes: 'We can achieve multi-region active-active database synchronization by simply broadcasting SQL UPDATE statements across regions and overwriting conflicting rows with Last-Write-Wins (LWW) based on NTP timestamps.'",
        "output": "Critique: The candidate relies on wall-clock NTP timestamps, which suffer from clock skew, leap seconds, and network drift, guaranteeing silent data loss and causality violations (earlier updates overwriting later business operations). A mathematically sound active-active multi-region architecture requires Conflict-Free Replicated Data Types (CRDTs): 1) Convergent Replicated Data Types (CvRDTs / state-based): replicas synchronize by transmitting their full state (or delta-state) and merging via a join-semilattice operator (merge) that is commutative (A merge B = B merge A), associative ((A merge B) merge C = A merge (B merge C)), and idempotent (A merge A = A). Monotonic growth guarantees strong eventual consistency regardless of delivery order; 2) Commutative Replicated Data Types (CmRDTs / op-based): replicas broadcast operations that commute with all concurrent operations, requiring a causal broadcast layer with exactly-once or at-least-once idempotency; 3) Tombstone garbage collection: In Observed-Remove Sets (OR-Set), deletions leave tombstones with unique addition tags to prevent resurrected elements. Stable causal state pruning (tracking the minimum vector clock across all participating nodes) is required to purge tombstones without memory bloat. Challenge the candidate on Delta-State CRDTs (Delta-CvRDT) for reducing network bandwidth."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 225. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
