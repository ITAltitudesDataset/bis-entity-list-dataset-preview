# BIS Entity List — ML Entity Name Matching Demonstration

**Prepared by IT Altitudes Inc.**

## Purpose

This reproducible educational example searches the 50-row BIS Entity List preview for textually similar entity names. It uses TF-IDF character n-grams (2–4) and a scikit-learn Nearest Neighbors model with cosine distance. It is an information-retrieval demonstration, **not a trained regulatory risk classifier**.

## Input and results

- Input: `bis_entity_preview_50.csv` — 50 sample entity records.
- Query: `Chinese Academy of Sciences Institute of Physics` (punctuation variation of a sample name).
- Closest result: `Chinese Academy of Sciences, Institute of Physics` — similarity score **0.9682**.
- Output: `bis_entity_name_matching_results.csv`, containing the six closest text matches and their original preview fields.
- Chart: `bis_entity_name_matching_chart.png`.

The query is based on an existing preview entry, so this result demonstrates retrieval under a small punctuation change; it is **not** an independent evaluation of accuracy on unseen entities.

## Run locally

```bash
pip install pandas scikit-learn matplotlib
python bis_entity_name_matching_demo.py
```

The script rebuilds the TF-IDF vectors and nearest-neighbor index from the included sample CSV and writes a fresh results CSV.

## Limitations

- A text similarity score is **not** the probability that two names represent the same legal entity.
- Similar names may refer to different entities; transliterations and aliases may be missed.
- This 50-row sample is not comprehensive and does not reflect current BIS Entity List status.
- Do not use this example to determine export licensing requirements, approve transactions, or perform live screening.
- Consult official BIS and applicable export-control sources for current regulatory decisions.

## Dataset

[Free BIS GitHub Preview](https://github.com/ITAltitudesDataset/bis-entity-list-dataset-preview)  
[Complete Dataset Information](https://italtitudes.gumroad.com/l/cuwozq)

*Publisher-created educational demonstration; not endorsed or certified by BIS.*
