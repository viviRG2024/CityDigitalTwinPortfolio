# Global City Digital Twin–SDG Case Library

## Overview

This repository provides the **Global City Digital Twin–Sustainable Development Goal (CDT–SDG) Case Library**, together with analysis notebooks supporting the associated study *A Global Perspective on City Digital Twins*.

The repository is intended to support transparent and reproducible research on the global development of City Digital Twins (CDTs). It documents where CDT implementations have been reported, what urban systems and data sources they represent, which stakeholders are involved, and how their documented applications relate to the United Nations Sustainable Development Goals (SDGs).

The study draws on two complementary sources of evidence:

1. **published literature and other publicly accessible source material**, used to construct the literature-derived CDT case library; and
2. **semi-structured expert interviews**, used to complement the literature-based evidence with practice-based information.

The **literature-derived case library is publicly released through this repository**. Source evidence for individual literature-derived cases can be traced through the `Reference` field in the dataset.

The **case-level dataset derived from semi-structured expert interviews is not publicly released**. It was maintained as a separate sheet in the internal research workbook and is described below only to clarify the evidence base and methodology of the associated study.

The public case library is intended to function as a **living research resource** and may be expanded as new CDT implementations, publications, technical reports, project documentation, and other relevant evidence become available. The dataset version associated with the published study should, however, be treated as a fixed research snapshot for replication of the reported results.

---

## Repository contents

```text
CityDigitalTwinPortfolio/
├── README.md
├── LICENSE
├── Global_CDT-SDG_Case_Library.xlsx
└── code/
    ├── CDT-fig2.py
    └── CDT-fig3.py
```

### Public data workbook

The public workbook contains two literature-derived data sheets:

| Sheet | Description |
|---|---|
| `CDTs_from_literature` | The principal literature-derived CDT case dataset, containing **1,111 case records**. |
| `Appendix-CDT_labelling` | Additional descriptive characterisation of the same literature-derived cases using CDT archetype, technical, and application-domain dimensions. |

The **1,111 records represent cases rather than unique publications or source documents**. A single source may support more than one case record where distinct implementations or locations can be identified.

The internal research workbook used during the study also contained a third sheet, `CDTs_from_expert_interview`, comprising case-level records derived from semi-structured expert interviews. **This sheet is not included in the public data release.**

### Analysis notebooks

The `code/` directory contains Python scripts supporting analyses and figures reported in the associated manuscript:

- `CDT-fig2.py` – generates panels for Fig. 2 (bar chart and bubble plots).
- `CDT-fig3.py` – generates panels for Fig. 3 (stacked bar, co-occurrence network, phi heatmaps, and SDG-related charts).

The scripts are provided for research transparency and replication. Before running, please edit the `DATA_DIR` and `OUTPUT_DIR` variables at the top of each script to point to your local data and output directories.
---

## Scope and research questions

The case library was developed to support three related research questions:

1. **Where have CDT implementations been documented?**  
   The library records the geographical distribution and temporal development of documented CDT cases.

2. **What do documented CDTs represent?**  
   Cases are coded according to the urban systems they represent and the geometric and non-geometric data sources documented in each implementation.

3. **How do documented CDT applications relate to sustainable urban development?**  
   CDT application scenarios are harmonised into city-service categories and subsequently mapped to relevant SDGs to enable comparison across the broader sustainability agenda.

The library records **documented CDT characteristics and stated or inferred application scope**. It does **not** measure the effectiveness, maturity, operational success, or verified sustainability impact of individual CDT implementations.

The geographical and thematic distributions represented in the library should therefore be interpreted as distributions of **documented cases**, rather than as a complete census of all CDTs developed worldwide.

---

## Data sources and collection process

### 1. Systematic literature review

The majority of cases were identified through a systematic literature review following a PRISMA-based screening process.

The initial literature database contained **25,873 publications** retrieved from four major academic databases:

- Web of Science
- Scopus
- IEEE Xplore
- ACM Digital Library

The search covered the period **2000–2025**.

Search terms included explicit city digital twin and digital-twin terminology and, particularly for earlier cases, terminology associated with urban digital systems and data environments considered relevant to the developmental trajectory of contemporary CDTs.

Broad, non-SDG-specific search terms were used to reduce the risk of identifying cases only because they had already been explicitly framed around sustainability.

Following screening and case-level review, **1,111 literature-derived CDT case records** were retained in the public dataset.

#### Source traceability

Each literature-derived case contains a `Reference` field identifying the underlying source evidence used for case identification and coding.

Depending on the source, the `Reference` field may contain:

- a DOI;
- a URL to a publication, report, project, or other publicly accessible source; or
- another source locator where appropriate.

This field enables users to trace individual case records back to their underlying source material.

The case library should therefore be understood as a **structured synthesis and coding of source evidence**, rather than as a replacement for the original publications or project documentation.

When reusing or discussing information relating to an individual CDT case, users should consult and cite the corresponding original source identified in the `Reference` field.

### 2. Semi-structured expert interviews

The literature review was complemented by semi-structured interviews with experts from academic and professional practice.

The interviews were used to:

- validate and contextualise patterns identified from published and publicly accessible sources;
- document practice-based and industry-led CDT cases that may be underrepresented in the academic literature;
- capture technical, organisational, governance, and data-integration issues that are often incompletely documented in publications; and
- provide additional information on stakeholder requirements and common data environments where available.

Case-level information derived from these interviews was organised in a separate sheet, `CDTs_from_expert_interview`, within the **internal research workbook**.

**The interview-derived case-level dataset is not included in the public repository or public workbook release.**

Interview information was anonymised or generalised where necessary to protect participants and commercially sensitive information. The associated manuscript and Supplementary Information describe the methodological role of the interview evidence, but the underlying interview material and case-level interview records are not publicly distributed.

### 3. Case review and standardisation

Following data collection, cases were reviewed and standardised by a research team with expertise in digital twins, urban systems, asset management, and data-related research.

The standardisation process included:

1. review of available publications, project documentation, and, where applicable, interview material;
2. identification of the urban-management and development scenario or scenarios represented by each case;
3. harmonisation of scenario descriptions;
4. mapping of scenarios to harmonised city-service categories informed by ISO 37120;
5. mapping of documented scenarios to relevant SDGs; and
6. documentation of urban systems, data sources, stakeholders, spatial context, and other relevant case characteristics.

---

## Unit of analysis and case selection

### Unit of analysis

The primary unit of the public dataset is the **documented CDT case** rather than the publication.

A publication or other source may describe:

- a single CDT case;
- multiple geographically distinct implementations;
- multiple implementations serving different urban systems or locations; or
- an implementation that is also documented in other sources.

Consequently, the number of case records should not be interpreted as the number of unique publications.

Where multiple source records referred to the same implementation without substantively new case-level information, duplicate descriptions were reviewed during the screening and standardisation process.

### Case selection criteria

The library is intended to capture **implemented or practically demonstrated urban digital-twin cases**, rather than purely conceptual discussions of digital twins.

A case was considered for inclusion where the available evidence described an actual platform, system, model, digital environment, or implemented digital representation applied in an urban or urban-related context and provided sufficient information to identify its represented systems, data foundation, or application purpose.

The conceptual framing used in the study considers three broad dimensions of a CDT:

1. **physical assets and city form**;
2. **processes, services, and systems**; and
3. **human and organisational activities**.

Because the library is also intended to document the historical development of the field, earlier and domain-specific implementations were not excluded solely because they did not yet incorporate all three dimensions.

Such cases were retained where they represented a meaningful combination of these dimensions and were considered relevant to the developmental trajectory of city-scale digital twins.

Their inclusion represents an **analytical classification used in this study** and does not necessarily imply that the original project or source explicitly described the implementation as a "City Digital Twin".

### Geographical scope

The geographical unit is treated pragmatically.

Documented CDT implementations may operate at the scale of a:

- city;
- district;
- campus;
- infrastructure network;
- settlement;
- region; or
- cross-jurisdictional urban system.

Host-city or settlement population values are therefore used as **contextual descriptors and sensitivity variables**, rather than as estimates of the number of CDT users or as a universal definition of what constitutes a CDT.

### General exclusions

Records were excluded where they were, for example:

- purely conceptual or theoretical and did not describe an implemented or demonstrated digital environment;
- unrelated to urban, city, settlement, infrastructure, or urban-management contexts;
- duplicate descriptions of the same case that did not provide substantively new implementation information; or
- too incomplete to establish a meaningful CDT application, system representation, or data foundation.

Full screening details and the PRISMA process are reported in the Supplementary Information of the associated manuscript.

---

## Public workbook structure and data dictionary

## Sheet 1: `CDTs_from_literature`

This is the principal case-level dataset and contains **1,111 literature-derived CDT records**.

### Case, source, and location information

| Field | Description |
|---|---|
| `Paper_title` | Title or name of the publication, report, project documentation, webpage, or other source record used to identify the case. The field name is retained for consistency with the research dataset even where the source is not a conventional journal paper. |
| `Published_Year` | Broad temporal descriptor associated with the source or implementation. Depending on the case, this may represent a publication year, project year, implementation period, or operational period (e.g., `2015-present`). It should therefore not be interpreted universally as the formal publication year of an academic paper. |
| `City` | Reported host city or primary urban location associated with the case. |
| `Area` | More specific study or implementation area where available, such as a district, campus, infrastructure corridor, facility, or other sub-city area. |
| `Country/Region` | Country or territorial context associated with the case. |
| `Full_address` | Standardised geographical description used to support geocoding. |
| `Population` | Population associated with the host city or settlement where available. This is a contextual variable and is not an estimate of CDT users. |
| `Latitude` | Latitude used for spatial analysis. |
| `Longitude` | Longitude used for spatial analysis. |
| `Region` | Broad geographical or structural grouping used in the global analysis. |
| `Cluster` | Spatial cluster assignment used in the global distribution analysis. See the associated analysis notebook and Supplementary Information for analytical details. |
| `Reference` | Source locator for the evidence underlying the case, most commonly a DOI or URL. Users should consult the corresponding original source when interpreting or citing an individual case. |

### Sustainability context

| Field | Description |
|---|---|
| `2025 SDG Index Score` | Country-level SDG Index score from the Sustainable Development Report 2025, assigned as contextual information according to the country associated with the case. |
| `2025 SDG layer` | Analytical grouping derived from the country-level 2025 SDG Index score. |
| `2025 SDG Index Rank` | Country-level rank in the 2025 SDG Index. |
| `Covered_SDGs` | SDGs associated with the documented CDT application scenario or scenarios according to the mapping procedure described below. |

Country-level SDG indicators are included as **contextual benchmarks only**.

They should not be interpreted as:

- measures of city-level sustainability performance;
- indicators of the sustainability need of a particular city;
- evidence of CDT effectiveness; or
- verified contributions of an individual CDT to SDG progress.

### Urban-system representation

The dataset contains descriptive coding across six broad urban-system dimensions:

| Field | Interpretation |
|---|---|
| `IoT_technology` | IoT, sensing, sensor, connected-device, or related technology documented in the case. |
| `Transportation` | Transportation-related systems or data, including roads, rail, traffic, bridges, ports, mobility, or other transport infrastructure. |
| `Workplace` | Non-residential buildings and activity environments, including offices, hospitals, universities, industrial facilities, public buildings, and related assets. |
| `Land_and_agriculture` | Land, terrain, environmental surfaces, agricultural areas, landscape, or related spatial systems. |
| `Household` | Residential buildings, housing, or household-related systems. |
| `People` | Explicit representation or involvement of residents, occupants, users, citizens, behavioural information, or other human/social information. |

For these six dimensions, the workbook contains **two sets of columns with the same field names**:

1. the first occurrence contains descriptive text documenting how the system is represented in the source; and
2. the later occurrence contains binary `0/1` presence–absence coding used for quantitative analysis.

For the binary columns:

- `1` indicates that the corresponding dimension was coded as present; and
- `0` indicates that it was coded as absent according to the study's coding procedure.

Users importing the workbook into software that automatically renames duplicate column headers should verify how these later binary columns have been represented before reproducing analyses.

### Application and city-service coding

| Field | Description |
|---|---|
| `City services` | Application or service scenario documented for the CDT case. |
| `ISO_37120 Standardised City Services` | Harmonised city-service category informed by ISO 37120 and used as an intermediate classification layer in the CDT–SDG mapping. |
| `Covered_SDGs` | One or more SDGs associated with the documented scenario according to the mapping procedure used in the study. |

The ISO 37120-based classification is used as an **analytical reference layer**. It should not be interpreted as a claim that the categories constitute a complete CDT ontology or that every category is reproduced directly from the standard.

### Stakeholders and data foundation

| Field | Description |
|---|---|
| `Involved_stakeholders` | Stakeholder groups, organisations, roles, users, or intended decision-makers documented in the source. |
| `Geometric` | Geometric or spatial data sources and representations documented for the case, such as GIS, BIM/IFC, 3D models, LiDAR, point clouds, remote sensing, terrain models, maps, or related spatial information. |
| `Non-geometric` | Non-geometric information documented for the case, such as IoT observations, environmental measurements, operational records, administrative information, mobility data, documents, or behavioural/social data. |

---

## Sheet 2: `Appendix-CDT_labelling`

This sheet provides an additional **descriptive characterisation** of the 1,111 literature-derived cases.

The labels support comparative analysis of CDT implementation characteristics and future reuse of the case library. They are **not combined into a composite maturity score** and should not be interpreted as a definitive CDT ontology or certification framework.

The sheet retains the following case-identification fields:

- `Paper_title`
- `Published_Year`
- `City`
- `Area`
- `Country`
- `Full_address`

The descriptive labelling fields are:

| Field | Description |
|---|---|
| `CDT Archetype` | Descriptive implementation archetype, including categories such as city-scale CDT, domain-specific CDT, asset/infrastructure DT, GIS/BIM/CIM base model, IoT/sensor/information-system platform, or research prototype/micro-scale implementation. |
| `Temporal Frequency` | Approximate temporal update or refresh characteristic, including static/archival, periodic, near-real-time, real-time, or claimed real-time where exact frequency is not specified. |
| `Spatial Fidelity` | Approximate spatial scope or fidelity of the documented implementation. |
| `Modeling/Simulation` | Whether modelling or simulation capability is documented. |
| `Integration Density` | Descriptive degree of integration across systems, domains, or information sources. |
| `Tech Stack` | Reported deployment arrangement, such as cloud-only or hybrid edge-cloud, where sufficient information is available. |
| `Interface` | Documented user-facing interaction mode, such as a 2D/3D dashboard, web-based visualisation, or immersive/VR-style interface. |
| `Application Domain` | Broad application domain, including built environment, natural environment, social and organisational systems, or combinations of these. |

Because source publications and project documentation vary substantially in reporting detail, `N/A` generally indicates that the relevant information was unavailable, unreported, not applicable, or could not be coded reliably from the available evidence.

The absence of reported information should not automatically be interpreted as evidence that a particular capability was absent from the actual implementation.

---

## Restricted interview-derived data

### Internal Sheet 3: `CDTs_from_expert_interview`

The internal research workbook used in the associated study contained a third sheet, `CDTs_from_expert_interview`, documenting case-level information derived from the semi-structured expert interviews.

The sheet included information corresponding broadly to the literature-based coding framework, including:

- case and location descriptors;
- urban-system representation;
- city-service and SDG coding;
- stakeholder involvement;
- geometric and non-geometric data sources; and
- contextual information derived from practitioner accounts.

It also contained interview-specific information relating to topics such as:

- stakeholder requirements; and
- the development or use of common data environments (CDEs), where discussed.

**This sheet is not part of the public data release.**

The underlying interview-derived case records and interview material are not distributed through this repository. Descriptions of the interview component are provided to document the methodological basis of the study and should not be interpreted as indicating public access to the underlying records.

---

## CDT–SDG mapping

The CDT–SDG mapping was designed to examine documented CDT relevance across the broader sustainability agenda rather than restricting the analysis to a small set of infrastructure-oriented goals.

For each case, the general procedure was to:

1. identify the urban-management and development scenario or scenarios documented for the CDT;
2. harmonise these scenarios into a reference scenario structure;
3. map the scenarios to harmonised city-service categories informed by **ISO 37120** as an intermediate external reference layer; and
4. map each scenario to one or more of the **17 United Nations Sustainable Development Goals**.

An **inclusive mapping strategy** was used:

- where a source explicitly identified one or more SDGs associated with a CDT application, those **source-stated SDGs** were retained; and
- where no SDG was explicitly stated, relevant SDGs were inferred from the documented application scenario and corresponding SDG targets using the study's coding procedure.

A random subsample was independently re-coded to assess inter-coder reliability.

Full mapping rules, scenario definitions, coding procedures, and reliability statistics are reported in the Supplementary Information of the associated manuscript.

The mapping represents **documented relevance or coverage**.

It does **not** demonstrate:

- causal contribution to an SDG;
- verified improvement in an SDG indicator;
- effectiveness of the CDT intervention; or
- achievement of a sustainability outcome.

---

## Data availability

### Publicly available data

The public release contains:

- `CDTs_from_literature`; and
- `Appendix-CDT_labelling`.

These sheets contain the literature-derived case library and its associated descriptive classifications.

The source evidence underlying individual literature-derived cases can be traced through the `Reference` field.

### Restricted data

The case-level dataset derived from semi-structured expert interviews, maintained internally as `CDTs_from_expert_interview`, is **not publicly released**.

The underlying interview materials are also not distributed through this repository.

Accordingly, the public repository enables inspection, reuse, and reanalysis of the **literature-derived CDT case library**, while interview-derived evidence used in the associated study cannot be independently reconstructed at the case level from the public repository alone.

Users should refer to the associated manuscript and Supplementary Information for the methodological description and reported analysis of the interview component.

---

## Missing and unavailable information

Reporting practices vary considerably across publications, projects, regions, and implementation types.

Users should therefore distinguish between:

- an explicitly coded absence;
- information that was not reported in the available source;
- information that was not applicable; and
- information that could not be coded reliably.

In particular:

- `N/A` generally denotes unavailable, unreported, non-applicable, or insufficiently documented information;
- blank cells should **not** automatically be interpreted as confirmed absence unless the corresponding coding rule explicitly defines them that way; and
- for the later binary urban-system columns in `CDTs_from_literature`, `0` and `1` represent explicit presence–absence coding according to the study's analytical procedure.

---

## Reproducibility

### Suggested environment

The analysis scripts are written for **Python 3**.

To download and run the repository:

```bash
git clone https://github.com/viviRG2024/CityDigitalTwinPortfolio.git
cd CityDigitalTwinPortfolio
```

Open the Python scripts in `code/` and, where necessary, update the workbook path to point to the downloaded public workbook.

The scripts use commonly available scientific-Python libraries. Users should inspect the import statements in each script and install the required packages in their local environment.

### Reproducing the published analyses

For replication of results reported in the associated manuscript, users should use the **dataset version released or archived with that study**, rather than automatically substituting a later version of the living case library.

Subsequent versions of the case library may include:

- newly documented cases;
- corrections;
- revised classifications; or
- additional contextual information.

As a result, later versions may not reproduce the exact case counts or descriptive statistics reported in the original publication.

### Replication notes

When reproducing or extending the analysis:

- use the dataset version appropriate to the analysis being reproduced;
- do not reinterpret blank cells as confirmed absence unless explicitly specified by the coding rule;
- treat `N/A` as unavailable, unreported, non-applicable, or insufficiently documented information rather than automatically as absence;
- remember that `Published_Year` is a broad temporal field and may represent a publication year, project year, implementation period, or operational period;
- treat country-level SDG metrics as contextual variables rather than city-level outcomes;
- treat `Population` as a host-city or settlement context variable rather than the number of CDT users;
- distinguish descriptive urban-system columns from the later binary columns with the same field names;
- treat the labels in `Appendix-CDT_labelling` as analytical characterisations rather than validated maturity scores; and
- consult the `Reference` field and underlying source evidence before making detailed claims about an individual CDT implementation.

---

## Updates and community contributions

The Global CDT–SDG Case Library is intended to evolve as the CDT field develops.

Future updates may include:

- newly published or publicly documented CDT cases;
- documented updates to existing cases;
- additional technical or governance information;
- corrections or improved source information;
- newly documented practitioner- or government-led implementations; and
- more structured information on intended or explicitly stated SDG relevance.

Researchers, practitioners, governments, CDT developers, and other organisations are encouraged to propose new cases or corrections through GitHub issues or pull requests.

When proposing a new literature- or publicly documented case, please provide, where possible:

- project or case name;
- city, region, and country;
- publication, report, project URL, or DOI;
- relevant year or implementation period;
- a short description of the CDT and its application;
- represented urban systems;
- geometric and non-geometric data sources;
- stakeholder groups;
- relevant technical characteristics;
- intended or explicitly stated SDG relevance; and
- source evidence supporting the submitted information.

Community-submitted records should be treated as **candidate cases** until they have been reviewed against the same inclusion, standardisation, and coding principles applied to the existing case library.

Community contribution mechanisms apply to information that can be supported through publicly shareable evidence. They do not provide a mechanism for releasing or reconstructing restricted interview-derived records.

---

## Recommended use

The public case library may be useful for:

- comparative CDT research;
- systematic reviews and meta-research;
- urban digitalisation and smart-city studies;
- CDT–SDG research;
- analysis of urban-system representation;
- data architecture and interoperability research;
- analysis of the geographical and temporal distribution of documented CDT activity;
- identification of underrepresented regions, systems, or sustainability goals; and
- development of future CDT reporting, classification, and benchmarking frameworks.

When reusing the dataset, users should:

- preserve attribution to the case library;
- consult and cite the original evidence identified in the `Reference` field when discussing individual cases;
- clearly document any filtering, cleaning, recoding, aggregation, or derived variables;
- report the dataset version used; and
- avoid interpreting documented coverage as verified CDT performance or sustainability impact.

---

## Important interpretation notes

Several limitations should be considered when interpreting the dataset.

### Documented cases are not a global census

The geographical distribution of cases is influenced by the availability of publications, reports, project documentation, database coverage, language, research activity, and disclosure practices.

An area with fewer documented cases should therefore not automatically be interpreted as having less CDT activity in practice.

### Source reporting is heterogeneous

Different sources provide substantially different levels of technical, organisational, spatial, and operational detail.

A missing feature in the dataset may reflect incomplete reporting rather than true absence from an implementation.

### Historical cases use an analytical definition

Some earlier urban digital systems were included because they meet the study's analytical inclusion criteria and contribute to understanding the developmental trajectory of CDTs.

Their inclusion does not imply that the original developers or authors necessarily used the term "City Digital Twin".

### SDG mappings represent relevance, not impact

The CDT–SDG mapping identifies documented or inferred relationships between application scenarios and SDGs. It does not establish that a CDT produced a measurable sustainability benefit.

---

## Associated manuscript

This repository supports the manuscript:

> **A Global Perspective on City Digital Twins**

The manuscript is currently under review.

Full methodological details, screening procedures, sensitivity analyses, coding rules, interview methods, and CDT–SDG mapping procedures are documented in the manuscript and its Supplementary Information.

This section will be updated with the full bibliographic citation and DOI following publication.

---

## Citation

If you use the Global CDT–SDG Case Library before publication of the associated manuscript, please cite or acknowledge the repository and report the **dataset version or release used**.

When referring to an individual CDT case, users should also consult and cite the original source identified in that record's `Reference` field.

A formal citation for the associated article will be added here following publication.

---

## License

This repository is released under the **MIT License**. See [`LICENSE`](LICENSE) for details.

The repository license does not replace or override copyright, licensing, or other rights associated with the original publications, project documentation, websites, or third-party data sources referenced by individual CDT cases.

The restricted interview-derived dataset and underlying interview materials are **not distributed as part of this repository**.

---

## Contact

For questions, corrections, or proposed contributions, please use the repository's **Issues** function so that discussions and updates relating to the public case library can remain transparent to the research community.