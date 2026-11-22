#!/usr/bin/env bash
# Regenerate every table and figure of the report.
#
#   scripts/reproduce_report.sh          # from the cached results in results/ (about a minute, no Gurobi)
#   scripts/reproduce_report.sh --full   # first rerun every learning experiment (hours, no Gurobi),
#                                        # then regenerate from the fresh results
#
# The exact values (Tables 1 and 2) need a Gurobi licence to recompute; they are cached in results/.
# See README.md for the solver commands.
set -euo pipefail
cd "$(dirname "$0")/.."
PY="${PYTHON:-.venv/bin/python}"
[ -x "$PY" ] || PY=python

if [ "${1:-}" = "--full" ]; then
  echo "== rerunning learning experiments (deterministic: same configs and seeds give the same numbers)"
  for cfg in m4_seeds m4_selfplay m4_psro m4_kuhn m4_tune_selfplay; do
    nice -n 19 "$PY" scripts/run_m4.py --config "configs/$cfg.yaml"
  done
  for cfg in m5_dose m5_model m5_model_t1 m5_suit m5_curriculum m6_timescale m6_exactgrad m8_resp; do
    nice -n 19 "$PY" scripts/run_m5.py --config "configs/$cfg.yaml"
  done
  "$PY" scripts/m6_adv_diag.py
  for cfg in m6_neural_tune m6_neural m7_tabinit_tune m7_tabinit m7_tabinit_long m7_neural_diag \
             m7_neural_combo m7_neural_gate; do
    nice -n 19 "$PY" scripts/run_m6.py --config "configs/$cfg.yaml"
  done
  "$PY" scripts/m8_analyze.py "$(ls -d results/m8_resp/*/seeds | head -1)"
  "$PY" scripts/describe_learned_bit.py "$(ls -d results/m4_kuhn/*/seeds | head -1)" \
      > "$(ls -d results/m4_kuhn/*/seeds | head -1)/learned_bits.txt"
  "$PY" scripts/export_runs_csv.py
fi

echo "== tables (Tables 1 to 5, Figure 1 data, inline counts)"
"$PY" scripts/report_tables.py
echo "== Milestone 6 targets"
"$PY" scripts/m6_targets.py > /dev/null && echo "wrote results/m6_targets/targets.md"
echo "== figures"
"$PY" scripts/make_report_figures.py
"$PY" scripts/render_screenshots.py
