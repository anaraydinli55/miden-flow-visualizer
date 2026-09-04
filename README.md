# Miden Note & State Flow Visualizer

A lightweight developer CLI and HTML dashboard visualizer for Polygon Miden, mapping out transaction execution, consumed input notes (nullifiers), created output notes (commitments), and account state transitions.

## Why Visualizing Miden Flow Matters
Polygon Miden uses an Actor-based and Note-based hybrid state model (UTXO + Account hybrid). Understanding how transactions consume and emit notes is critical for developers:
- Consumed Notes: Input notes consumed by the transaction and nullified on-chain.
- Client-Side Proving: The Miden VM produces a STARK proof locally.
- Created Notes: New output notes emitted to recipients as commitments.

## Quickstart

### Run the Visualizer
Generate terminal ASCII flow and the interactive HTML dashboard:
./run_visualizer.sh

## Output
- Terminal ASCII architecture diagram
- Standalone dark-mode dashboard.html report

## License
MIT
