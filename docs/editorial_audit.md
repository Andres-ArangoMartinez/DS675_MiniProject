# Editorial audit

Inspected commit: `ac6ba439f0739e1562c310fbe50bcc8c2fb1e445`, branch `main`. The remote matched this commit before editing. These local revisions await student review of the content and commit message. The subsequent [account-export supplement](../evidence/ai_interactions/chatgpt_export/README.md) adds source evidence; the counts below cover the existing edited Markdown files, excluding new transcripts and export navigation.

## Scope and word counts

Edited 13 primary Markdown files and four secondary files. Secondary edits clarify the paper-index license basis, two PDF link labels and SAM-kNN preprint/publication identity; study methods, metrics, IDs and citations are retained. Screening notes and the other detailed reviews remain unchanged.

Counts are whitespace-separated tokens in Markdown source, including tables, links and commands, using the same rule before/after. The table excludes this new audit.

| File | Before | After | Reduction |
|---|---:|---:|---:|
| [README.md](../README.md) | 591 | 455 | 23.01% |
| [docs/professor_feedback.md](../docs/professor_feedback.md) | 428 | 316 | 26.17% |
| [docs/student_contributions.md](../docs/student_contributions.md) | 604 | 542 | 10.26% |
| [docs/research_scope.md](../docs/research_scope.md) | 545 | 433 | 20.55% |
| [docs/exploratory_analysis.md](../docs/exploratory_analysis.md) | 579 | 463 | 20.03% |
| [docs/anticipated_contributions.md](../docs/anticipated_contributions.md) | 518 | 454 | 12.36% |
| [docs/reproducibility.md](../docs/reproducibility.md) | 764 | 567 | 25.79% |
| [docs/reproducibility_repair.md](../docs/reproducibility_repair.md) | 562 | 338 | 39.86% |
| [literature/README.md](../literature/README.md) | 602 | 450 | 25.25% |
| [literature/ahmed_feedback.md](../literature/ahmed_feedback.md) | 366 | 313 | 14.48% |
| [evidence/ai_interactions/README.md](../evidence/ai_interactions/README.md) | 4,593 | 2,452 | 46.61% |
| [evidence/ai_interactions/publication_procedure.md](../evidence/ai_interactions/publication_procedure.md) | 611 | 487 | 20.29% |
| [NOTICE.md](../NOTICE.md) | 158 | 133 | 15.82% |
| [literature/detailed_review/chebnet.md](../literature/detailed_review/chebnet.md) | 299 | 298 | 0.33% |
| [literature/detailed_review/gatres.md](../literature/detailed_review/gatres.md) | 312 | 311 | 0.32% |
| [literature/detailed_review/sam_knn.md](../literature/detailed_review/sam_knn.md) | 345 | 341 | 1.16% |
| [literature/papers/README.md](../literature/papers/README.md) | 1,024 | 1,027 | -0.29% |
| **Total existing edited files** | **12,901** | **9,380** | **27.29%** |

Most reduction comes from repeated activity summaries and repeated link collections in the AI guide. The 20–30% target was advisory; retention of unique evidence and qualifications governed editing. The revised guide preserves all **94 original unique destinations**, including **48 original unique transcript anchors**, while reducing repeated occurrences. A01–A10 and R01–R05 remain identifiable; A11/A12 add source-linked prompt-drafting activities.

This audit is counted separately from the existing-file comparison; newly recovered conversation text is evidence added under the later recovery request.

## Specific corrections

| Item | Editorial correction and source |
|---|---|
| E01 | [README](../README.md) describes recorded interests, choices and technical actions; later professional explanations remain student accounts in the [attribution guide](../evidence/ai_interactions/README.md). |
| E02 | [C1–C3](anticipated_contributions.md) state proposed preparation, comparisons, criteria and expected outputs, with completed descriptive analysis identified separately. |
| E03 | [Student contributions](student_contributions.md), [analysis explanation](exploratory_analysis.md) and A06 distinguish retrospective reading, contemporary questions and recorded AI inspections. |
| E04 | [Literature inventory](../literature/README.md) retains 47 records, 35 groups, six selections and partial historical query coverage, without asserting a complete search sequence. |
| E05 | [Source notice](../NOTICE.md) and paper index identify declared licenses, supporting records and retained fingerprints rather than legal certification. |
| E06 | [Repair history](reproducibility_repair.md) cites the corrected commit and its [successful workflow](https://github.com/Andres-ArangoMartinez/DS675_MiniProject/actions/runs/41067513928), replacing approval chronology. |
| E07 | [Reproduction instructions](reproducibility.md) distinguish retained-copy hash agreement from external course-platform authentication. |
| E08 | A09 and A11/A12 distinguish student requests from ChatGPT drafting. Five supplied prompts match exported assistant JSON; a separate later attachment retains its unresolved drafting-authorship limit. |

## Preservation and validation

Comparisons use pre-edit file fingerprints, retained source passages, report text, professor feedback, syllabus, manifests and code. The dataset, n1(+15), six signals, proposed C1–C3 experiments and chronological periods remain unchanged. Submitted-report copies, figures, legacy transcript parts, redaction/index records, source data, scientific code, tests, notebook and numerical outputs retain their bytes. New evidence importer/validator scripts handle the export, and existing evidence validators invoke those additional checks.

The student authorized refreshing explanatory-document fingerprints and validator-generated records. The [run manifest](../results/run_manifest.json) records the old/new student-contribution document hashes and editorial basis, retaining its scientific execution date, code/input/output hashes and values. The [guide record](../evidence/ai_interactions/guide_validation.json) identifies checks of the revised guide; historical transcript manifests remain unchanged. The [export comparison](../evidence/ai_interactions/chatgpt_export/validation.json) reconstructs twelve selected native-source transcripts and validates five supplied-prompt matches.

| Command | Actual outcome |
|---|---|
| `python scripts/validate_repository_hygiene.py` | PASS; exit code 0. |
| `python scripts/validate_ai_interactions.py` | PASS; exit code 0. |
| `python scripts/validate_ai_interactions.py --originals <authorized-local-archives>` | PASS; exit code 0; 16 original views compared. |
| `python scripts/validate_repository.py` | PASS; exit code 0. |

Scientific computations and model training were not rerun for this editorial change. The prior seven-test and notebook execution records remain unchanged. Published author scores retain their source context. [Current repository validation](../results/repository_validation.json) records the executed consistency checks.

## Remaining evidence limits

The export resolves the fifteen pending assistant bodies and five truncated messages, matching all 82 prior entries. Private binaries, non-text model records and export boundaries still limit historical completeness. Codex retains its stated capture cutoffs. Search-query coverage and the separate later attachment's drafting authorship remain limited. Source hashes establish retained-copy integrity; academic assessment remains with the instructor.
