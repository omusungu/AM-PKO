# AM-PKO Embedding Experiment

## Experiment ID

EXP-4B4-001

## Purpose

Evaluate three candidate embedding model families for semantic retrieval in the AM-PKO Personal Knowledge Operating System.

The experiment uses:

- 5 canonical knowledge records
- 5 canonical retrieval queries
- predefined relevance judgments
- 3 candidate embedding models

No model is selected as the winner before evaluation.

## Experiment Files

- corpus.json - canonical evaluation corpus
- queries.json - canonical retrieval queries
- judgments.json - ground-truth relevance judgments
- models.json - candidate embedding models
- results.json - experiment results
- README.md - experiment documentation

## Corpus

Number of records: 5

IDs:

- K-000001
- K-000002
- K-000003
- K-000004
- K-000005

The corpus must remain unchanged during this experiment.

## Queries

Number of queries: 5

IDs:

- Q-000001
- Q-000002
- Q-000003
- Q-000004
- Q-000005

The query set must remain unchanged during this experiment.

## Relevance Scale

- 2 = highly relevant
- 1 = partially relevant
- 0 = not relevant

Judgments are established before model evaluation and must not be changed because of model results.

## Candidate Models

1. BAAI BGE-M3
2. intfloat multilingual-e5-large
3. Qwen3-Embedding

All remain CANDIDATE models until evaluation is complete.

## Retrieval Procedure

For each model:

1. Generate embeddings for the 5 corpus records.
2. Generate embeddings for the 5 queries.
3. Calculate cosine similarity.
4. Rank corpus records for each query.
5. Compare rankings with the predefined relevance judgments.
6. Record latency and retrieval results.

## Reproducibility

Keep the following fixed:

- corpus
- queries
- judgments
- model configuration
- text preprocessing
- similarity metric
- ranking procedure

Any change to these should create a new experiment.

## Status

SETUP COMPLETE

Next phase: actual embedding smoke test.

## Results

Results will be recorded in results.json.

No model winner is declared until the experiment has been executed and evaluated.
