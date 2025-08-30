import pandas as pd
import json


df = pd.read_json("dataset/original_calsa_testset.json")
results = []
with (
    open("dataset/all_agg_ptns.jsonl", "r") as f1,
):
    for line in f1:
        instance = json.loads(line)
        target_original_instance = df[df.lo_id == instance["ca_id"]]
        instance["ca_essay"] = "\n".join(target_original_instance.lo_speech.values[0])
        instance["ia_id"] = target_original_instance.pm_id.values[0]
        results.append(instance)

pd.DataFrame.from_records(results).to_json(
    "dataset/calsaplus_dataset.jsonl",
    orient="records",
    lines=True,
)
