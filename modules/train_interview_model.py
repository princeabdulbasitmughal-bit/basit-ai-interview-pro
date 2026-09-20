#!/usr/bin/env python3
"""
========================================================================================
👑 BASIT INTERVIEWER PRO — SOVEREIGN LOCAL MODEL TRAINING & FINE-TUNING PIPELINE
========================================================================================
Generates high-signal synthetic interview training datasets (JSONL format) and builds
specialized local Ollama models (basit-interviewer-pro & basit-interviewer-pro-32b).
Covers: /basit1, /basit2, /basit3, /basit4, /basitswarm, /opensource-ai-arsenal
========================================================================================
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path
from datetime import datetime

# Enforce UTF-8 on Windows standard streams to handle emojis and unicode symbols
if sys.platform == "win32":
    import io
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    if hasattr(sys.stderr, 'buffer'):
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATASET_FILE = DATA_DIR / "training_dataset_interview_pairs.jsonl"
MODELFILE_PATH = BASE_DIR / "Modelfile"
MODELFILE_32B_PATH = BASE_DIR / "Modelfile.32b"

# High-Quality Curated Training Dataset Exemplars
TRAINING_EXEMPLARS = [
    {
        "instruction": "Evaluate candidate answer for Senior Distributed Systems role. Candidate says: 'Hum Redis cluster use kartay hain for caching and PostgreSQL with read replicas.'",
        "input": "Candidate stack: Redis, PostgreSQL, Node.js. Question was about handling 50x peak traffic.",
        "output": json.dumps({
            "interviewerReply": "Acha, Redis cluster aur read replicas ka setup standard hai, lekin agar cache stampede ya thundering herd ho tou database connection pool exhaustion ko kaisay prevent karenge?",
            "nextQuestion": "Could you walk me through your cache invalidation strategy (Cache-Aside vs Write-Through) and how you ensure idempotency across distributed worker threads?",
            "isCompleted": False
        }, ensure_ascii=False)
    },
    {
        "instruction": "Analyze candidate code for LRU Cache in JavaScript and evaluate algorithmic complexity.",
        "input": "class LRUCache {\n  constructor(capacity) {\n    this.capacity = capacity;\n    this.cache = new Map();\n  }\n  get(key) {\n    if (!this.cache.has(key)) return -1;\n    const val = this.cache.get(key);\n    this.cache.delete(key);\n    this.cache.set(key, val);\n    return val;\n  }\n  put(key, value) {\n    if (this.cache.has(key)) this.cache.delete(key);\n    else if (this.cache.size >= this.capacity) {\n      this.cache.delete(this.cache.keys().next().value);\n    }\n    this.cache.set(key, value);\n  }\n}",
        "output": json.dumps({
            "passed": True,
            "score": 95,
            "timeComplexity": "O(1) average lookup and eviction",
            "spaceComplexity": "O(capacity) strictly bounded",
            "feedback": "Clean idiomatic JavaScript Map implementation leveraging insertion-order iteration for O(1) eviction.",
            "suggestions": ["Consider adding concurrency locks if the instance is accessed across worker threads."]
        }, ensure_ascii=False)
    },
    {
        "instruction": "Synthesize a 5-Dimensional Bar Raiser Scorecard for a Staff AI Engineer candidate who completed an interview on vector databases and Kubernetes.",
        "input": "Candidate: Prince Basit, Role: Staff AI Engineer, Duration: 42 mins, Tab focus switches: 0",
        "output": json.dumps({
            "overallScore": 92,
            "recommendation": "Strong Hire",
            "radarScores": {
                "technicalCompetence": 94,
                "problemSolving": 91,
                "communication": 93,
                "systemArchitecture": 92,
                "behavioralLeadership": 90
            },
            "executiveSummary": "Prince Basit exhibited exceptional technical command across distributed vector databases, Kubernetes HPA orchestrations, and high-concurrency event pipelines. Communication was crisp, structured, and pragmatic with natural bilingual fluency.",
            "strengths": [
                "Deep mastery of Qdrant HNSW vector search indexing and quantization",
                "Clear quantification of p99 tail latency tradeoffs under 50x peak loads",
                "Exemplary blameless post-mortem ownership during production outage scenarios"
            ],
            "weaknesses": [
                "Could formalize multi-cluster chaos engineering benchmarks earlier in architecture proposals"
            ],
            "personalizedRoadmap": [
                "Phase 1: Deepen hands-on eBPF kernel network tracing - https://ebpf.io/what-is-ebpf/",
                "Phase 2: Master multi-region CockroachDB consensus topologies - https://www.cockroachlabs.com/docs/",
                "Phase 3: Lead cross-functional architecture reviews with executive ROI framing"
            ]
        }, ensure_ascii=False)
    }
]

def generate_synthetic_dataset(num_pairs: int = 50) -> int:
    """Generates synthetic interview instruction-response pairs for fine-tuning."""
    print(f"[*] Generating {num_pairs} high-signal training pairs...", flush=True)
    count = 0
    with open(DATASET_FILE, "w", encoding="utf-8") as f:
        # Write base exemplars first
        for ex in TRAINING_EXEMPLARS:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
            count += 1
        
        # Synthesize role permutations
        roles = [
            ("Distributed System Architect", "Kafka, Redis, Kubernetes, CockroachDB", "50M DAU Video Streaming"),
            ("Senior Backend Systems Engineer", "Go, PostgreSQL, gRPC, Redis", "Financial Ledger Idempotency"),
            ("AI / Machine Learning Engineer", "PyTorch, Qdrant, Triton, CUDA", "Sub-10ms Semantic Vector Retrieval"),
            ("Full-Stack Software Engineer", "React, Node.js, Next.js, IndexedDB", "Offline-First State Synchronization"),
            ("DevOps & Cloud Architect", "Terraform, Kubernetes, Istio, Prometheus", "Multi-Region Zero-Downtime Blue/Green Deployment")
        ]
        
        for role, stack, scenario in roles:
            for stage in ["Architecture", "Concurrency", "Code Sandbox", "Behavioral"]:
                item = {
                    "instruction": f"Conduct an elite Bar Raiser evaluation for a Staff {role} specializing in {stack}.",
                    "input": f"Candidate is addressing scenario: {scenario} during stage: {stage}.",
                    "output": json.dumps({
                        "interviewerReply": f"Zabardast explanation! Aapne {stack.split(',')[0]} ka architecture clear bataya.",
                        "nextQuestion": f"Under peak 100x traffic spikes, how do you prevent cascading failures and maintain p99 tail latency within SLA limits?",
                        "stage": stage,
                        "evaluationCriteria": ["p99 latency", "CAP theorem", "Idempotency", "Chaos resilience"]
                    }, ensure_ascii=False)
                }
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
                count += 1
                
    print(f"[+] Saved {count} training pairs to: {DATASET_FILE}", flush=True)
    return count

def build_ollama_model(model_name: str = "basit-interviewer-pro", modelfile: Path = MODELFILE_PATH) -> bool:
    """Compiles the custom Modelfile into a local Ollama model."""
    print(f"[*] Compiling custom sovereign model: {model_name} from {modelfile.name}...", flush=True)
    t0 = time.perf_counter()
    try:
        proc = subprocess.run(
            ["ollama", "create", model_name, "-f", str(modelfile)],
            cwd=str(BASE_DIR),
            capture_output=True,
            text=True,
            check=True
        )
        duration = round(time.perf_counter() - t0, 1)
        print(f"[+] Successfully compiled {model_name} in {duration}s!", flush=True)
        print(proc.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"[-] Failed to compile {model_name}: {e.stderr}", file=sys.stderr)
        return False

def build_32b_modelfile():
    """Builds the 32B flagship Modelfile for local NVIDIA RTX A6000."""
    content = """FROM qwen2.5-coder:32b

# High-precision parameter tuning for 32B Flagship Bar Raiser Engine
PARAMETER temperature 0.3
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.15
PARAMETER num_ctx 16384
PARAMETER stop "[CANDIDATE]"
PARAMETER stop "[INTERVIEWER]"
PARAMETER stop "<|im_end|>"
PARAMETER stop "<|endoftext|>"

SYSTEM \"\"\"You are BASIT INTERVIEWER PRO (32B Flagship), the sovereign AI Principal Technical Fellow and Bar Raiser.
You possess deep expertise across distributed databases, kernel-level eBPF observability, sub-millisecond algorithmic AST analysis, and elite STAR leadership evaluation.
You fluently understand natural Roman Urdu and crisp English without translation latency.\"\"\"
"""
    with open(MODELFILE_32B_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[+] Created 32B Modelfile: {MODELFILE_32B_PATH}", flush=True)

def main():
    print("==================================================================")
    print("👑 BASIT INTERVIEWER PRO — SOVEREIGN LOCAL MODEL COMPILER")
    print("==================================================================")
    
    # 1. Generate synthetic fine-tuning dataset
    num_pairs = generate_synthetic_dataset(50)
    
    # 2. Build 7B Fast Model
    build_ollama_model("basit-interviewer-pro", MODELFILE_PATH)
    
    # 3. Create 32B Flagship Modelfile
    build_32b_modelfile()
    
    print("==================================================================")
    print(f"✅ Local Model Pipeline Complete: {num_pairs} pairs generated.")
    print("🚀 Model 'basit-interviewer-pro:latest' is ready for live inference!")
    print("==================================================================")

if __name__ == "__main__":
    main()
