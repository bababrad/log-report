#!/bin/bash
# Verifier entrypoint. Test dependencies (pytest, pytest-json-ctrf) are baked
# into environment/Dockerfile, so this runs plain pytest with no installs.

mkdir -p /logs/verifier

# pytest-json-ctrf writes a standard CTRF JSON report that Harbor consumes.
pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py -rA
status=$?

if [ "$status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
