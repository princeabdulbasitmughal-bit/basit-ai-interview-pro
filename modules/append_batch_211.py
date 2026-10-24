# -*- coding: utf-8 -*-
import json
import os

new_pairs = [
    {
        "instruction": "Evaluate candidate understanding of Rietveld refinement and 6D Elser indexing in quasicrystalline powder diffraction.",
        "input": "Candidate states: 'In periodic crystals, diffraction peaks are indexed with 3 Miller indices (hkl). In icosahedral quasicrystals, 6 integers (n1, n2, n3, n4, n5, n6) are required to index reflections projected from 6D hypercubic reciprocal space onto 3D physical space, where peak positions scale by powers of tau (1.618).' ",
        "output": json.dumps({
            "interviewerReply": "Bilkul theek farmaya, 6D projection Elser indexing ka bunyadi usool hai. Lekin phason strain diffuse scattering ko kaisay broaden karta hai?",
            "nextQuestion": "How do linear and quadratic phason fluctuations manifest as anisotropic peak broadening in high-resolution synchrotron powder XRD compared to standard instrumental microstrain?",
            "score": 96,
            "isCompleted": False
        })
    },
    {
        "instruction": "Probe candidate on derivation of the Hume-Rothery pseudogap affine valley formula in ternary Al-Cu-Fe alloys.",
        "input": "Candidate derives: 'Starting from Raynor e/a = 3*f_Al + 1*f_Cu - 2*f_Fe with f_Al + f_Cu + f_Fe = 1, substituting f_Cu = 1 - f_Al - f_Fe directly produces e/a = 1 + 2*f_Al - 3*f_Fe.'",
        "output": json.dumps({
            "passed": True,
            "score": 98,
            "feedback": "Flawless mathematical reduction. The affine equation defines parallel iso-e/a contour lines in Gibbs barycentric coordinates, accurately enclosing the 1.75 <= e/a <= 1.86 stabilization corridor.",
            "nextProbingQuestion": "Why does negative Raynor valence for Fe (-2) arise from transition metal d-band electron absorption from the conduction sea?"
        })
    },
    {
        "instruction": "Analyze candidate design for an automated zero-hang watchdog supervisor in high-frequency trading (HFT) engines.",
        "input": "Candidate uses non-blocking Unix/Windows domain sockets with monotonic deadline timers and self-terminating heartbeat thread pools.",
        "output": json.dumps({
            "passed": True,
            "score": 93,
            "latencyProfile": "Sub-100 microsecond heartbeat tripwire",
            "feedback": "Robust architecture. Monotonic clocks eliminate NTP time-jump false positives.",
            "suggestions": ["Incorporate kernel-level process job objects on Windows to cleanly purge zombie child processes upon ungraceful shutdown."]
        })
    },
    {
        "instruction": "Evaluate candidate explanation of Robinson triangle deflation in Penrose P3 quasiperiodic tilings.",
        "input": "Candidate explains that deflating golden triangles (72-72-36) and golden gnomons (36-36-108) scales side lengths by 1/tau, where the asymptotic ratio of obtuse to acute triangles converges strictly to tau = (1+sqrt(5))/2.",
        "output": json.dumps({
            "interviewerReply": "Aala mathematical clarity. Robinson triangle deflation geometric scale invariance ko perfectly model karti hai.",
            "nextQuestion": "How does this deflation rule relate to the self-similar electronic wave functions that produce critical hierarchical energy spectra in quasicrystals?",
            "score": 95,
            "isCompleted": False
        })
    },
    {
        "instruction": "Probe candidate on VRAM fragmentation and buffer reuse in PyTorch / CuPy under continuous multi-agent burst workloads.",
        "input": "Candidate suggests pre-allocating contiguous tensor pools with custom CUDA memory arenas and disabling GC during latency-sensitive inference spikes.",
        "output": json.dumps({
            "passed": True,
            "score": 94,
            "feedback": "Demonstrates deep knowledge of CUDA runtime memory management. Eliminates OS-level malloc/free context switches.",
            "nextQuestion": "What is the trade-off between cudaStreamSynchronize vs CUDA event-based dependency recording in multi-stream pipelined models?"
        })
    },
    {
        "instruction": "Analyze candidate strategy for selective leaching of ternary Al-Cu-Fe precursors to create skeleton Raney catalysts.",
        "input": "Candidate specifies 20 wt% NaOH solution at 70°C for 4 hours, followed by deoxygenated water neutralization until pH 8.",
        "output": json.dumps({
            "passed": True,
            "score": 95,
            "feedback": "Accurate leaching parameters. Dissolving amphoteric aluminum exposes catalytically active interdispersed Fe-Cu clusters with high Brunauer-Emmett-Teller (BET) specific surface area.",
            "nextProbingQuestion": "How does residual unreacted Al in the core preserve structural integrity and prevent pyrophoric collapse upon exposure to ambient air?"
        })
    },
    {
        "instruction": "Probe candidate on Bayesian meta-ensemble calibration for financial regime switching models.",
        "input": "Candidate uses Dirichlet-multinomial conjugate priors to dynamically adjust weights between trend-following and mean-reverting sub-agents based on rolling Calmar ratio.",
        "output": json.dumps({
            "interviewerReply": "Shandar approach. Dirichlet update market regimes k mutabiq weights ko smooth rakhta hai bina over-react kiye.",
            "nextQuestion": "How do you calibrate the Dirichlet hyperparameter concentration vector alpha to prevent regime lock-in during low-volatility consolidation?",
            "score": 96,
            "isCompleted": False
        })
    },
    {
        "instruction": "Evaluate candidate proposal for Model Context Protocol (MCP) tool schema versioning and schema backwards compatibility.",
        "input": "Candidate recommends semantic versioning with JSON Schema validation, optional property defaults, and strict input schema sanitization before dispatch.",
        "output": json.dumps({
            "passed": True,
            "score": 95,
            "feedback": "Conforms to modern enterprise MCP specifications. Ensures seamless backward compatibility with older LLM agents and clients.",
            "nextQuestion": "How do you handle tool deprecation notices in MCP manifest metadata without breaking legacy client integrations?"
        })
    }
]

dataset_path = r"E:\basit-ai-interview\data\training_dataset_interview_pairs.jsonl"
with open(dataset_path, "a", encoding="utf-8") as f:
    for item in new_pairs:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Successfully appended {len(new_pairs)} verified QA pairs to {dataset_path}")
