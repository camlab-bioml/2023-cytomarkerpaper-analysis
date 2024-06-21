# 2023-cytomarkerpaper-analysis

Code run in order:

1. `scripts/parse-screen-to-sce.R` Takes Simon's singlecells.csv and subsamples, clusters, then projects to full dataset. Saves `data/sce_screen_full.rds` and `data/sce_screen_subsample.rds`
2. `notebooks/0_interpret_screen_clusters.qmd`. Outputs `../figs/screen_cluster_heatmap_unscaled.png` and `../figs/screen_cluster_heatmap_scaled.png` to be used in cluster interpretation. User should then create `data/cluster-interpretation-nov23.xlsx` (what clusters are what cell types) 
3. `notebooks/compare-screen-scrna-marker-rank-nygc.qmd` - takes the NYGC PMBC data for a single donor, subsamples, collapses to major cluster, and saves to `results/nygc_pbmc_subsampled.rds` 
4. `notebooks/compare-screen-scrna-marker-rank-nygc.qmd`. Outputs `figs/screen-vs-scrna.pdf`
5. `notebooks/rna-protein-correlation.qmd` - outputs `figs/rna-protein-scatter.pdf` and `igs/cytomarker_sens_spec_no_ms.pdf`
