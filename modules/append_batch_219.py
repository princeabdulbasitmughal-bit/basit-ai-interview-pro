# -*- coding: utf-8 -*-
"""
Append Batch 219: Quasicrystal Glass-Like Thermal Transport, Cahill-Pohl Diffuson Limits,
Aerospace Thermal Barrier Coatings (TBC), and High-Availability Daemon Supervision.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Glass-Like Thermal Transport and Cahill-Pohl Diffuson Limits in icosahedral quasicrystals.",
        "input": "Candidate argues: 'Since quasicrystals are metallic alloys composed of 60-70% aluminum, their thermal conductivity must follow standard metals with high electronic conduction governed by the Wiedemann-Franz law.'",
        "output": "Critique: The candidate demonstrates a critical misconception of electron and phonon transport in quasiperiodic systems. In conventional metals, thermal conductivity is dominated by free electrons (kappa_e ~ 100-200 W/(m*K)) governed by the Wiedemann-Franz law (kappa_e = L_0 * sigma * T). However, in stable icosahedral quasicrystals (e.g. Al63Cu25Fe12), the Fermi level is pinned inside a deep Mott-Friedel pseudogap, suppressing electronic conductivity so drastically (sigma ~ 100-500 S/cm) that electronic thermal transport collapses to kappa_e < 0.25 W/(m*K). More remarkably, lattice thermal transport kappa_ph does not follow standard crystalline Umklapp scattering (which yields kappa ~ 1/T); instead, the absence of translational symmetry causes severe acoustic phonon localization. According to the Allen-Feldman theory and the Cahill-Pohl minimum thermal conductivity model, propagating phonons collapse into non-propagating diffusons with mean free paths on the order of the interatomic spacing (~2.5 Angstroms). Consequently, total thermal conductivity is exceptionally low (kappa ~ 1.2-1.5 W/(m*K) at 300 K) and exhibits a positive temperature coefficient (d_kappa/dT > 0), exactly resembling amorphous silica glass rather than crystalline aluminum. Ask the candidate how thermal conductivity scales at cryogenic temperatures (e.g., Plateau between 5 K and 30 K)."
    },
    {
        "instruction": "Evaluate candidate knowledge on aerospace Thermal Barrier Coatings (TBC) comparing Quasicrystals to standard Yttria-Stabilized Zirconia (7YSZ).",
        "input": "Candidate states: 'Ceramic 7YSZ is the only viable thermal barrier coating for jet turbine blades because metallic coatings will immediately melt and conduct all heat directly into the nickel superalloy substrate.'",
        "output": "Critique: The candidate is unaware of cutting-edge aerospace thermal barrier metallurgy. While 7YSZ (7 wt% Y2O3-ZrO2) is widespread, it suffers from severe operational vulnerabilities: 1) High brittleness and low fracture toughness; 2) Significant thermal expansion mismatch (CTE of 7YSZ is ~10.5 ppm/K vs Inconel 718 substrate at ~14.5 ppm/K), creating immense cyclic shear stresses that trigger interfacial delamination and ceramic spallation; and 3) Molten silicate sand (CMAS) chemical attack at temperatures > 1200 deg C. In contrast, quaternary icosahedral quasicrystal coatings (such as Al-Cu-Fe-Cr) exhibit: a) Glass-like thermal conductivity (kappa ~ 1.3-1.5 W/(m*K)), which is actually lower than 7YSZ (kappa ~ 2.2 W/(m*K)), providing a 125-130 deg C thermal temperature drop across a 150-micron plasma-sprayed coating; b) Coefficient of thermal expansion (CTE ~ 15.2 ppm/K) that matches the Inconel 718 superalloy substrate within 5%, virtually eliminating thermal mismatch interfacial spallation; c) Much higher metallic fracture toughness than brittle ceramics; and d) Dense protective alumina (Al2O3) passivating scale formation up to 1000 deg C. Probe the candidate on how quasicrystalline TBCs handle thermal shock cycling."
    },
    {
        "instruction": "Assess candidate design of Multi-Tenant Token-Bucket Rate Limiting and Distributed Throttling in high-throughput enterprise REST API microservices.",
        "input": "Candidate proposes: 'We can enforce API rate limiting by keeping a global in-memory Python dictionary counting requests per user ID and resetting the dictionary every 60 seconds.'",
        "output": "Critique: The candidate's approach fails completely in production for multiple reasons: 1) Severe edge-of-window burst vulnerability: a user can send 100% of their quota at second 59 and another 100% at second 61, effectively doubling the allowable concurrency spike on upstream services; 2) Multi-worker and multi-instance inconsistency: in-memory dictionaries are isolated per process/worker, meaning a 4-worker Gunicorn/Uvicorn cluster will multiply allowable requests by 4x; 3) Memory leaks: an unevicted dictionary tracking millions of ephemeral IP addresses will cause unbounded RAM growth; and 4) Lack of concurrency safety: standard Python dictionaries lack atomic read-modify-write synchronization across asynchronous event loops. The production architecture requires: a Redis-backed sliding window counter or token-bucket algorithm executed via an atomic Lua script (to eliminate race conditions in a single network round-trip); strict HTTP response headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`); and return of HTTP 429 Too Many Requests with a precise `Retry-After` timestamp. Challenge the candidate to write the Lua script for atomic token consumption."
    },
    {
        "instruction": "Analyze candidate strategy for 24/7 Autonomous Process Guards, Zombie Sweeping, and Zero-Hang Process Supervision across multi-daemon architectures.",
        "input": "Candidate suggests: 'To keep background microservices alive, a simple infinite bash loop `while true; do python server.py; done` is sufficient.'",
        "output": "Critique: The candidate suggests an uncontrolled restart loop that can destabilize the host operating system. In production multi-daemon environments (e.g., managing 8-10 heterogeneous daemons across ports 8077, 8088, 8090, 8095, 8888, 8890, 8899, 3000): 1) Rapid crash looping without backoff consumes 100% CPU, locks socket ports in `TIME_WAIT` states, and exhausts file descriptors; 2) Orphaned child threads remain alive, creating invisible zombie processes that hold GPU VRAM or socket locks; 3) Lack of health telemetry leaves stalled event loops undetected when the process is technically running but unresponsive. A professional supervisor implementation requires: a) Exponential backoff with jitter on consecutive rapid crashes; b) Bi-directional active health probes (e.g. GET /health with 5-second socket timeout) rather than mere PID existence checks; c) Strict process tree termination (sending SIGTERM, waiting for graceful shutdown grace period, then issuing SIGKILL/taskkill /F /T to prune all child processes); d) PID file locking to prevent duplicate instances; and e) Structured telemetry event logging. Ask the candidate how they detect socket port exhaustion in Windows/Linux environments."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 219. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
