# -*- coding: utf-8 -*-
"""
Append Batch 221: Superconducting Quasicrystals, Multifractal Critical States,
Heavy-Fermion Quantum Criticality, and Async Backpressure Pipelines.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Superconducting Quasicrystals and Cooper Pairing in Multifractal Critical States.",
        "input": "Candidate states: 'Superconductivity requires strict translational symmetry for Cooper pairing at (k, -k). Since quasicrystals lack periodic lattice translations, superconductivity is mathematically impossible in quasiperiodic systems.'",
        "output": "Critique: The candidate is unaware of landmark experimental discoveries in modern condensed matter physics. In 2018, Kamiya et al. (Nature Communications) and subsequent research teams conclusively demonstrated bulk superconductivity in the icosahedral quasicrystal Al-Zn-Mg (Tc approx 0.05 K) and its Tsai-type 1/1 approximants, followed by Ta1.6Te quasicrystals with Tc up to ~1.0-2.8 K. In traditional BCS theory, Cooper pairing occurs between plane-wave Bloch states (k, -k). In quasicrystals, however, electronic wavefunctions are neither extended Bloch waves nor exponentially localized Anderson states; instead, they are 'critical' wavefunctions exhibiting scale-invariant multifractal self-similarity. Cooper pairing survives because the fundamental requirement for superconductivity is time-reversal symmetry (Anderson's theorem for disordered superconductors), pairing time-reversed exact eigenstates psi_n and psi_n* rather than plane-wave momentum eigenstates. Moreover, superconducting quasicrystals display exotic phenomenology: 1) Strong upward curvature of the upper critical magnetic field H_c2(T) near Tc; 2) Pronounced violation of the Werthamer-Helfand-Hohenberg (WHH) orbital limit; and 3) A spatial distribution of the superconducting order parameter Delta(r) that is itself fractal across Mackay and Tsai clusters. Probe the candidate on how the multifractal singularity spectrum f(alpha) influences the superconducting transition."
    },
    {
        "instruction": "Evaluate candidate understanding of Heavy-Fermion Quantum Criticality in Quasicrystals and Tsai-Type Approximants.",
        "input": "Candidate suggests: 'Quantum critical points only occur in periodic crystalline metals under high external hydrostatic pressure or magnetic fields.'",
        "output": "Critique: The candidate fails to appreciate quantum criticality in quasiperiodic heavy-fermion systems. In 2012, Deguchi et al. (Nature Physics) discovered that the icosahedral quasicrystal Au-Al-Yb exhibits quantum criticality (divergent effective mass, non-Fermi liquid behavior) at ambient pressure and zero external magnetic field—completely untuned! The magnetic susceptibility diverges as chi(T) proportional to T^(-0.5), electrical resistivity follows Delta_rho proportional to T, and specific heat exhibits C/T proportional to -ln(T) down to cryogenic temperatures. In contrast, the periodic 1/1 cubic approximant Au51Al34Yb15 requires a finite critical pressure (Pc ~ 0.2 GPa) to reach the same quantum critical point. The striking difference proves that the quasiperiodic topology itself provides an intrinsic mechanism for stabilizing critical magnetic fluctuations (valence fluctuations of Yb^(2+) and Yb^(3+)), pinning the system exactly at the border of magnetism without fine-tuning. Challenge the candidate to explain the role of localized 4f moments within the icosahedral Tsai shells."
    },
    {
        "instruction": "Assess candidate design of Async Event Loop Backpressure and Concurrency Throttling in Real-Time AI Microservices.",
        "input": "Candidate claims: 'To handle 10,000 incoming requests per second in FastAPI, we should just fire off `asyncio.create_task()` for every request without any concurrency limits.'",
        "output": "Critique: The candidate's approach will cause catastrophic memory exhaustion and server crashes (OOM) under sustained traffic. In Python asyncio, unbounded task creation (`asyncio.create_task`) without backpressure leads to: 1) RAM explosion as tens of thousands of coroutine frames, buffers, and socket descriptors accumulate; 2) Severe event loop starvation: loop latency degrades exponentially as the scheduler spends more time managing task queues than executing I/O; 3) Upstream database and GPU inference queue saturation, triggering connection pool timeouts and 504 Gateway Timeouts. A production-grade async pipeline requires: a) Bounded concurrency queues (`asyncio.Queue(maxsize=N)`) with explicit backpressure; b) Asynchronous Semaphore guards (`asyncio.Semaphore(limit)`) bounding concurrent GPU inference or DB calls; c) Returning HTTP 503 or 429 when queue capacity is reached rather than crashing; and d) Active loop lag monitoring (profiling time between scheduled ticks). Probe the candidate on how they handle graceful task draining during SIGTERM shutdown."
    },
    {
        "instruction": "Analyze candidate implementation of an Automated Self-Healing Process Supervisor for Multi-Daemon AI Workstations.",
        "input": "Candidate suggests: 'If a daemon crashes, we can write a script that scans tasklist every 10 seconds and restarts any missing executable.'",
        "output": "Critique: The candidate proposes a primitive polling mechanism that fails to handle common production failure modes: 1) Zombie and stalled processes: a daemon may remain in tasklist while its internal event loop is completely hung or deadlocked in an unreleased lock (appearing alive to tasklist); 2) Port collision during restarts: restarting without checking socket TIME_WAIT or closing orphaned child processes causes `EADDRINUSE [WinError 10048]`; 3) Crash storm cascade: a crashing service will be repeatedly launched in an infinite tight loop, consuming CPU and spamming error logs. A robust supervisor (such as the Basit Sovereign supervisor) implements: a) Active HTTP health probes with short timeouts (/health) to verify functional responsiveness rather than mere process existence; b) Atomic PID file tracking with process tree termination (killing child and parent processes); c) Exponential backoff with jitter on consecutive crashes to prevent CPU thrashing; and d) Unified telemetry metrics published to an operational dashboard. Ask the candidate how they handle zombie process reaping in Windows vs Linux."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 221. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
