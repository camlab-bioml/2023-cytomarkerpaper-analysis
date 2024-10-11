# 2023-cytomarkerpaper-analysis

Code to reproduce the figures and results from the cytomarker paper.

## Data directory configuration

Prior to running, the following data files need to be placed in the `data` directory:

- `singlecells.csv` from the cytomarker paper (# TODO: add the link here)
- The nygc multimodal pbmc data set from: `https://datasets.cellxgene.cziscience.com/de42a173-458a-429c-b129-c26bcd3adb3b.h5ad`, 
named as `nygc-pbmc.h5ad`
- The transcriptome and proteome data from Nicolet et al. 2022 from `https://doi.org/10.1371/journal.pone.0276294.s006`
- The protein-RNA correlation table from the Gygi Lab here: https://gygi.hms.harvard.edu/data/ccle/Table_S4_Protein_RNA_Correlation_and_Enrichments.xlsx, put
into the `depmap` sub-directory in `data`

## Running

To run all:

```
cd 2023-cytomarkerpaper-analysis
snakemake --cores all # user can specify number of cores
```

## Outputs: 

1. `data/sce_screen_full.rds` and `data/sce_screen_subsample.rds`
2. `/figs/screen_cluster_heatmap_unscaled.png` and `/figs/screen_cluster_heatmap_scaled.png` to be used in cluster interpretation. User should then create `data/cluster-interpretation-nov23.xlsx` (what clusters are what cell types) 
3. `results/nygc_pbmc_subsampled.rds` 
4. `figs/screen-vs-scrna.pdf`
5. `figs/rna-protein-scatter.pdf` and `figs/cytomarker_sens_spec_no_ms.pdf`
6. `figs/heatmap_mammary_single_cell.pdf`
