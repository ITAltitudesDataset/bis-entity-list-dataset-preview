# BIS Entity List Dataset — Data Quality Report

**Prepared by IT Altitudes Inc.**

**Dataset:** BIS Entity List Reference Dataset  
**Original Source:** U.S. Department of Commerce — Bureau of Industry and Security (BIS)  
**Report Type:** Dataset Quality & Transparency Summary

---

## 1. Executive Summary

This report describes the BIS Entity List Dataset's documented structure, quality-review framework, source provenance, and known limitations.

The dataset is intended for regulatory research, export-control analysis, educational studies, and non-production data engineering.

This is a publisher-issued transparency report, not an independent audit or BIS certification.

## 2. Dataset Overview

| Metric | Documented Value |
|---|---|
| Free preview records | 50 |
| Preview fields | 4 |
| Original source | Bureau of Industry and Security |
| Geographic coverage | International entities listed by BIS |
| Dataset type | Static regulatory reference |
| Preview formats | Excel, CSV, JSON |

### Preview Data Fields

| Column | Description |
|---|---|
| Entity Name | Name of the listed entity |
| Country | Country or jurisdiction associated with the entry |
| Federal Register Citation | Reference to a related Federal Register publication |
| License Requirement | Export licensing requirements reported for the entry |

The counts and field names above reflect existing publisher documentation and have not been independently rechecked against the preview files for this report.

## 3. Data Quality Review Framework

| Quality Dimension | Review Objective | Evidence Status |
|---|---|---|
| Record completeness | Identify missing or blank fields | Quantitative results pending |
| Duplicate detection | Review repeated entity entries | Quantitative results pending |
| Entity-name consistency | Review formatting and naming variations | Detailed results pending |
| Country consistency | Review country and jurisdiction labels | Detailed results pending |
| Citation availability | Check Federal Register references | Detailed results pending |
| License requirement consistency | Review requirement field structure | Detailed results pending |
| Source provenance | Identify original BIS source | Source documented |
| Cross-format consistency | Compare Excel, CSV, and JSON previews | Detailed results pending |

These checks describe the intended validation framework and should not be interpreted as completed or passed without supporting measurements.

## 4. Missing-Value Assessment

BIS Entity List entries may differ in the information available for individual entities.

Some fields may contain complex regulatory text or may not be applicable in the same way to every entry.

**Measurement status:**

- Total missing values: Pending validation
- Field-level completeness: Pending validation
- Required-field completeness: Pending validation
- Missing-value percentage: Pending validation

## 5. Duplicate-Record Assessment

Duplicate review should distinguish between:

- Exact duplicate rows
- Repeated entity names
- Multiple locations associated with one entity
- Different regulatory references for related entities
- Legitimate source-level variations

Repeated names should not automatically be treated as erroneous duplicate records.

**Measured duplicate count:** Pending validation.

## 6. Regulatory Field Review

Recommended checks include:

- Reviewing entity-name formatting
- Checking country and jurisdiction consistency
- Identifying missing Federal Register citations
- Reviewing the structure of license requirement values
- Preserving regulatory wording where applicable
- Checking source-reference consistency

**Measured results:** Pending validation.

## 7. Source Attribution & Provenance

**Original Source:** U.S. Department of Commerce — Bureau of Industry and Security (BIS).

The BIS Entity List is published in Supplement No. 4 to Part 744 of the Export Administration Regulations.

IT Altitudes Inc. independently prepares structured reference information and is not affiliated with or endorsed by BIS.

Users should consult official BIS publications for current regulatory requirements.

## 8. Known Limitations

- This is a static historical reference snapshot.
- Entity List entries may be added, amended, or removed.
- Names and country references may change.
- License requirements depend on applicable regulations and transaction circumstances.
- Absence from this dataset does not establish that a transaction is permitted.
- The dataset does not cover every applicable export-control restriction.
- No independently measured overall quality score is claimed in this report.

## 9. Intended Buyer Applications

The dataset may support:

- Export-control research
- Historical regulatory analysis
- Entity-name matching experiments
- Data cleaning and normalization testing
- ETL and database workflows
- Academic and educational research

These are potential research applications, not guarantees of suitability for operational compliance screening.

## 10. Validation Status

**Current status:** Publisher-issued quality and transparency documentation prepared.

**Pending:** Quantitative validation of completeness, duplicates, field consistency, and cross-format alignment.

No independently measured accuracy percentage or overall quality score is claimed.

## 11. License & Disclaimer

- [License & Usage Terms](LICENSE.md)
- [Source & Liability Disclaimer](DISCLAIMER.md)

The dataset is intended for research and analytical use.

It is not a live export-control screening or compliance determination service.

## 12. Free Preview & Complete Dataset

**[Explore the Free GitHub Preview](https://github.com/ITAltitudesDataset/bis-entity-list-dataset-preview)**

**[Purchase the Complete BIS Entity List Dataset](https://italtitudes.gumroad.com/l/cuwozq)**

## 13. Support

**IT Altitudes Inc.**

support@italtitudesdataset.zohodesk.in

---

*Publisher-Issued Data Quality & Transparency Report — 2026*
