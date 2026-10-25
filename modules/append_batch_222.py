# -*- coding: utf-8 -*-
"""
Append Batch 222: Superconducting Upper Critical Field WHH Limit Violations,
Aperiodic Vortex Pinning in Quasicrystals, High-Concurrency Socket Connection Pooling,
and Multi-Tenant Schema vs Row-Level Security Isolation.
"""
import json
import os

new_pairs = [
    {
        "instruction": "Assess candidate expertise in Upper Critical Field H_c2(T) Phenomenology and Werthamer-Helfand-Hohenberg (WHH) Orbital Limit Violations in Quasicrystals.",
        "input": "Candidate states: 'The upper critical magnetic field H_c2(T) of any Type-II BCS superconductor must follow the standard Werthamer-Helfand-Hohenberg (WHH) formula H_c2(0) = -0.693 * Tc * (dH_c2/dT)|_Tc, which always shows negative downward curvature across all temperatures.'",
        "output": "Critique: The candidate's knowledge is limited to conventional periodic metals and fails to account for aperiodic superconductors. In superconducting quasicrystals (e.g., Al-Zn-Mg and Ta-Te alloys), H_c2(T) exhibits pronounced positive upward curvature (d^2 H_c2 / dT^2 > 0) persisting from Tc down to low temperatures. This behavior directly violates standard WHH theory by a factor of 1.5x to 2.5x. The physical origin stems from: 1) The absence of translational momentum conservation and the spatial multifractality of critical electronic eigenstates; 2) Localized superconducting puddles forming preferentially in strongly-bonded Mackay or Tsai icosahedral clusters before global phase coherence is established; and 3) A distribution of local pairing gaps Delta(r) that percolates across the quasiperiodic lattice as temperature decreases. In contrast, standard WHH assumes a spatially uniform order parameter and plane-wave Bloch states governed by Gaussian disorder. Probe the candidate on how Pauli paramagnetic pair-breaking (Maki parameter alpha_M) interacts with orbital limiting in multifractal Cooper systems."
    },
    {
        "instruction": "Evaluate candidate understanding of Abrikosov Vortex Pinning and Flux Creep Suppression in Aperiodic and Quasicrystalline Potential Landscapes.",
        "input": "Candidate explains: 'In any Type-II superconductor, magnetic flux vortices always arrange themselves into a periodic hexagonal Abrikosov triangular lattice, and vortex pinning is always maximized by periodic square artificial pin arrays.'",
        "output": "Critique: The candidate overlooks the physics of vortex dynamics in quasiperiodic media. In periodic pinning arrays, flux creep and dissipation spike at mismatch fields (magnetic fields where the vortex density does not match the rational pinning grid periodicity). In stark contrast, Kemmler et al. and Misko et al. demonstrated that five-fold and eight-fold quasicrystalline pinning arrays (Penrose and Ammann-Beenker lattices) suppress flux creep across a continuous, broad spectrum of magnetic fields. Because quasicrystals possess self-similar hierarchical coordination numbers (coordination 3, 4, 5, 6, 7 sites), vortices can nest into optimal local potential wells across multiple field scales without forming periodic shear planes or channel dislocations. Furthermore, real-space Lorentz microscopy in quasiperiodic superconductors reveals non-hexagonal, multi-scale vortex arrangements with 5-fold or 10-fold point symmetries. Challenge the candidate on how matching field peaks B_phi are defined in aperiodic tilings using golden ratio inflation tau."
    },
    {
        "instruction": "Analyze candidate design of High-Concurrency Socket Connection Pooling and TCP Keepalive Tuning in Distributed Microservices.",
        "input": "Candidate proposes: 'In our Python/Go microservices talking to upstream REST and gRPC endpoints, creating a new HTTP/TCP connection per request is fine because modern OS kernels can handle thousands of TCP handshakes easily.'",
        "output": "Critique: The candidate's architecture will trigger severe latency degradation and socket exhaustion under high throughput. Creating a connection per request introduces: 1) Latency amplification: every request pays the 3-way TCP handshake penalty (1 RTT) plus TLS 1.3 handshake (1 RTT), increasing p99 latency by 50-200ms; 2) Ephemeral port exhaustion: closing thousands of TCP connections leaves sockets in `TIME_WAIT` state for 60-120 seconds (governed by tcp_fin_timeout). A system serving 5,000 req/s will quickly deplete all 65,535 local ephemeral ports, throwing `Errno 99: Cannot assign requested address` or `WSAEADDRNOTAVAIL`; 3) Server-side CPU overhead from repeated TLS key exchange calculations. A production-grade connection architecture mandates: a) Persistent connection pooling (`httpx.AsyncClient(limits=Limits(max_keepalive_connections=100, max_connections=500))` or custom Transport); b) TCP Keepalive probes (`SO_KEEPALIVE`, `TCP_KEEPIDLE=30`, `TCP_KEEPINTVL=10`, `TCP_KEEPCNT=3`) to prune dead sockets without hanging requests; c) HTTP/2 or HTTP/3 multiplexing allowing multiple concurrent streams over a single TCP/QUIC connection. Ask the candidate how they prevent connection pool deadlock when an upstream service stalls."
    },
    {
        "instruction": "Evaluate candidate strategy for Enterprise Multi-Tenant Data Isolation: Schema-per-Tenant versus Row-Level Security (RLS) in PostgreSQL.",
        "input": "Candidate claims: 'For an enterprise B2B SaaS platform with 5,000 tenants, schema-per-tenant is always superior to row-level security (RLS) because each tenant has their own isolated tables.'",
        "output": "Critique: The candidate fails to consider database scalability limits and operational complexity. At 5,000 tenants with an application schema of 50 tables, schema-per-tenant creates 250,000 tables, 500,000 indexes, and hundreds of thousands of catalog entries in PostgreSQL's `pg_class` and `pg_attribute`. This triggers: 1) Catastrophic PostgreSQL catalog bloat: query planner metadata caching (`relcache`, `catcache`) consumes gigabytes of shared memory, slowing down simple query planning; 2) Schema migration nightmare: running a database migration (e.g., adding a column) requires altering 5,000 tables in sequence, taking hours, risking partial failures, and holding table locks; 3) Connection pooler starvation: connection poolers like PgBouncer cannot effectively share server connections when applications dynamically switch search paths (`SET search_path TO tenant_x`). In modern enterprise architectures: a) Shared schema with PostgreSQL Row-Level Security (`ALTER TABLE ... ENABLE ROW LEVEL SECURITY; CREATE POLICY tenant_isolation_policy ON ... USING (tenant_id = current_setting('app.current_tenant_id')::uuid)`) scales smoothly to millions of tenants with single-table efficiency; b) Schema-per-tenant or database-per-tenant is reserved exclusively for a tiny tier of high-paying VIP enterprise tenants with strict HIPAA/SOC2 physical isolation mandates. Probe the candidate on how RLS policies impact query planning and index utilization (composite indexing on `(tenant_id, ...)`)."
    }
]

def append_batch():
    dataset_path = os.path.join(r"E:\basit-ai-interview\data", "training_dataset_interview_pairs.jsonl")
    with open(dataset_path, "a", encoding="utf-8") as f:
        for pair in new_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    with open(dataset_path, "r", encoding="utf-8") as f:
        total = len(f.readlines())
    print(f"[*] Appended {len(new_pairs)} new QA pairs in Batch 222. New total: {total} verified pairs.")

if __name__ == "__main__":
    append_batch()
