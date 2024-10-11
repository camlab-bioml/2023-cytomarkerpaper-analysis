# 2023-cytomarkerpaper-analysis

Code to reproduce the figures and results from the cytomarker paper.

## Data directory configuration

Prior to running, the following data files need to be placed in the `data` directory:

- `singlecells.csv`
- The nygc multimodal pbmc data set from: `https://datasets.cellxgene.cziscience.com/de42a173-458a-429c-b129-c26bcd3adb3b.h5ad`, 
named as `nygc-pbmc.h5ad`
- The transcriptome and proteome data from Nicolet et al. 2022 from `https://doi.org/10.1371/journal.pone.0276294.s006`

## Running

To run all:

```
cd 2023-cytomarkerpaper-analysis
snakemake --cores all # user can specify number of cores
```


Code run in order:

1. `scripts/parse-screen-to-sce.R` Takes Simon's singlecells.csv and subsamples, clusters, then projects to full dataset. Saves `data/sce_screen_full.rds` and `data/sce_screen_subsample.rds`
2. `notebooks/interpret_screen_clusters.qmd`. Outputs `../figs/screen_cluster_heatmap_unscaled.png` and `../figs/screen_cluster_heatmap_scaled.png` to be used in cluster interpretation. User should then create `data/cluster-interpretation-nov23.xlsx` (what clusters are what cell types) 
3. `notebooks/compare-screen-scrna-marker-rank-nygc.qmd` - takes the NYGC PMBC data for a single donor, subsamples, collapses to major cluster, and saves to `results/nygc_pbmc_subsampled.rds` 
4. `notebooks/compare-screen-scrna-marker-rank-nygc.qmd`. Outputs `figs/screen-vs-scrna.pdf`
5. `notebooks/rna-protein-correlation.qmd` - outputs `figs/rna-protein-scatter.pdf` and `figs/cytomarker_sens_spec_no_ms.pdf`
6. `notebooks/mammary-single-cell-heatmap.qmd` - outputs `figs/heatmap_mammary_single_cell.pdf`