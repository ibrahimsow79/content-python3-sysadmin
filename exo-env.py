#!/usr/bin/env python3.8
import os

stage = os.getenv("STAGE", "DEV").upper

output = f"We are running in {stage}"

if stage.startswith("PROD"):
  output = "DANGER!!!! - " + output

print(output)
