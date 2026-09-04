import json
import os
import subprocess
import time

def generate_ascii_flow(tx_data):
    print("\n" + "=" * 75)
    print("      📊 POLYGON MIDEN TRANSACTION & NOTE FLOW VISUALIZER")
    print("=" * 75)
    print(f"Transaction ID : {tx_data['tx_id']}")
    print(f"Account Target : {tx_data['account_id']}")
    print(f"STARK Proof    : {tx_data['proof_status']}")
    print("-" * 75)
    
    flow = f"""
    ┌──────────────────────────┐          ┌──────────────────────────┐
    │     CONSUMED NOTES       │          │      CREATED NOTES       │
    │  (Nullifiers Published)  │          │    (New Commitments)     │
    └─────────────┬────────────┘          └────────────┬─────────────┘
                  │                                    ▲
                  ▼                                    │
    ┌──────────────────────────────────────────────────┴─────────────┐
    │                    MIDEN VM / CLIENT PROVER                    │
    │  • State Nonce: {tx_data['nonce_before']} ➔ {tx_data['nonce_after']}                                      │
    │  • Asset Delta: {tx_data['asset_transferred']} SKS                                │
    │  • Execution  : Client-Side STARK Proved                       │
    └────────────────────────────────────────────────────────────────┘
    """
    print(flow)
    print("=" * 75)

def generate_html_dashboard(tx_data):
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Polygon Miden Flow Visualizer</title>
    <style>
        body {{ background: #0b0e14; color: #e6edf3; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; padding: 30px; }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #30363d; padding-bottom: 20px; }}
        .title {{ color: #7c3aed; font-size: 24px; font-weight: bold; }}
        .badge {{ background: #238636; color: #fff; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; }}
        .card {{ background: #161b22; border: 1px solid #30363d; border-radius: 12px; padding: 20px; margin-top: 20px; }}
        .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px; }}
        .flow-box {{ background: #0d1117; border: 1px dashed #8957e5; border-radius: 8px; padding: 15px; }}
        .highlight {{ color: #a371f7; font-family: monospace; font-size: 13px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="title">⚡ Polygon Miden State Flow Report</div>
            <div class="badge">STARK VERIFIED</div>
        </div>
        <div class="card">
            <h3>Transaction Details</h3>
            <p><strong>Tx ID:</strong> <span class="highlight">{tx_data['tx_id']}</span></p>
            <p><strong>Account:</strong> <span class="highlight">{tx_data['account_id']}</span></p>
            <p><strong>Asset Transfer:</strong> <span style="color:#3fb950; font-weight:bold;">{tx_data['asset_transferred']} SKS</span></p>
        </div>
        <div class="grid">
            <div class="flow-box">
                <h4>📥 Input Notes (Consumed)</h4>
                <p>Status: <span style="color:#f85149;">Nullified on-chain</span></p>
                <p class="highlight">Note: 0x9f8e...4b12 (P2ID)</p>
            </div>
            <div class="flow-box">
                <h4>📤 Output Notes (Created)</h4>
                <p>Status: <span style="color:#2ea043;">Committed on-chain</span></p>
                <p class="highlight">Note: 0x3d2a...8c90 (Private)</p>
            </div>
        </div>
    </div>
</body>
</html>"""

    with open("dashboard.html", "w") as f:
        f.write(html_content)
    print("🌐 Modern HTML Dashboard 'dashboard.html' olarak kaydedildi!")

def main():
    sample_tx = {
        "tx_id": "0x7a8b9c0d1e2f3a4b5c6d7e8f90123456789abcdef0123456789abcdef0123456",
        "account_id": "mtst1aqqd4l85vlzk75txw36lplrxkqws2tkt",
        "proof_status": "Client-Side STARK Generated (Verified)",
        "nonce_before": 12,
        "nonce_after": 13,
        "asset_transferred": "1.00000000"
    }
    
    generate_ascii_flow(sample_tx)
    generate_html_dashboard(sample_tx)

if __name__ == "__main__":
    main()
