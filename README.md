# TruAID Demo 🛡️🤖

**TruAID (Trusted AI Decentralized)** is a platform that enables trusted, auditable, privacy-preserving collaboration between autonomous agents. This demo showcases how agents can communicate securely using Google A2A protocols, log their behavior to a blockchain-based audit trail, and surface model behavior through Weights & Biases — all while preserving PII.

---

## 🔍 What this Demo Shows

- 🤝 Secure **Agent-to-Agent (A2A)** interactions using Google’s A2A protocol.
- 🔗 Blockchain-anchored audit trails with **PII-preserving hash commitments**.
- 📊 Integrated observability using **Weights & Biases** (W&B) for agent behavior and model traces.
- 🚨 Privacy-aware logging system that alerts when **sensitive flows** are detected.

---

## 🧱 Architecture Overview

      +------------+       A2A Protocol       +------------+
      |  Agent A   |  <-------------------->  |  Agent B   |
      +------------+                         +------------+
           |                                        |
     [Local Action Logs]                    [Local Action Logs]
           |                                        |
           v                                        v
 +------------------+                  +------------------+
 |  PII-Redaction & |                  |  PII-Redaction & |
 |  Hash Generation |                  |  Hash Generation |
 +------------------+                  +------------------+
           |                                        |
           +-------------------+--------------------+
                               |
                               v
                     +--------------------+
                     |   Merkle Log Root  |
                     |   (batch anchor)   |
                     +--------------------+
                               |
                               |
                               v
                    +------------------------+
                    |     TruAID Dashboard   |
                    |  (via W&B + blockchain)|
                    +------------------------+


