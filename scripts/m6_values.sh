#!/bin/sh
# Milestone 6: V(k, inf, rho) for the larger games, one solve at a time, 10 minutes each.
# Usage: ./scripts/m6_values.sh [priv|pub ...]   (default: priv pub)
cd "$(dirname "$0")/.."
export FAI_THREADS=2 FAI_GUROBI_MEM_GB=2
for rho in ${@:-priv pub}; do
  for job in "attack4x4 0" "attack4x4 1" "attack4x4 2" "blocker16 0" "blocker16 1" "blocker16 2" \
             "suit4x4 0" "suit4x4 1" "suit4x4 2" "blocker16 4" "suit4x4 4"; do
    set -- $job
    echo "== $1 k=$2 $rho $(date +%T)"
    timeout 600 nice -n 19 .venv/bin/python scripts/run_values.py --config configs/m6_values.yaml \
        --games "$1" --k "$2" --rho "$rho" 2>&1 | grep -E "V=|Error|error" \
        || echo "$1 k=$2 $rho: not finished in 10 minutes"
  done
done
echo "== done $(date +%T)"
