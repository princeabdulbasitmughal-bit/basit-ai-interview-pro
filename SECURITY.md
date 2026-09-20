# Security Policy — Basit AI Interview Pro

## Security Architecture & Guarantees

Basit AI Interview Pro is architected with enterprise-grade Zero-Trust defenses:

1. **Zero-NPM Native Node.js Core**: Eliminates supply-chain vulnerabilities, compromised node_modules packages, and dependency drift.
2. **OWASP Top 10 Hardened**:
   - **CWE-22 (Path Traversal)**: Strict canonical path resolution with forbidden parent directory traversal traps (`..`, `%2e%2e`).
   - **DoS / Slowloris Defense**: 30-second server socket timeouts with 512KB payload ceiling limits.
   - **XSS & Injection Defense**: Content Security Policy (CSP), `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, and AST VM execution isolation.
3. **Sovereign Local Inference**: All sensitive candidate interview answers and code solutions can be evaluated 100% locally on NVIDIA RTX GPUs via Ollama with zero external telemetry leakage.

## Reporting a Vulnerability

Please report any security findings or vulnerability disclosures directly to:
- **Lead Maintainer**: Prince Abdul Basit (`absh5506@gmail.com`)
- Response Window: Within 24 hours.
