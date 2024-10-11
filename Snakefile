import pandas as pd

cell_types = pd.read_excel("data/screen-scrna-celltype-match.xlsx")
cell_types = cell_types['cell_type']


outputs = {
    'rank-figs': 'figs/screen-vs-scrna.pdf',
    'fig-heatmap-scaled': 'figs/screen_cluster_heatmap_scaled.png',
    'fig-heatmap-unscaled': 'figs/screen_cluster_heatmap_unscaled.png',
    'fig-umap-celltype': 'figs/UMAP_celltype.png',
    'fig-umap-expression': 'figs/UMAP_expression.png',
    'fig-correlation': "figs/rna-protein-scatter.pdf",
    'fig-sens-spec': 'figs/cytomarker_sens_spec.pdf',
    'fig-mammary-heatmap-single-cell': 'figs/heatmap_mammary_single_cell.pdf'
}


rule all:
    input:
        outputs.values()

rule parse_screen:
    input:
        'data/singlecells.csv',
        'data/antigen-metal-map-simon.xlsx',
    output:
        'data/sce_screen_full.rds',
        "data/sce_screen_subsample.rds",
    script:
        'scripts/parse-screen-to-sce.R'

rule interpret_clusters:
    input:
        'data/sce_screen_subsample.rds',
        'data/cluster-interpretation-nov23.xlsx',
    output:
        outputs['fig-heatmap-scaled'],
        outputs['fig-heatmap-unscaled'],
        outputs['fig-umap-celltype'],
        outputs['fig-umap-expression'],
    shell:
        'quarto render notebooks/interpret-screen-clusters.qmd'
    
## Prepare the NYGC scRNA data
rule parse_nygc_pbmc_data:
    input:
        'data/nygc-pbmc.h5ad',
        'data/screen-scrna-celltype-match-lee.xlsx',
        'data/sce_screen_full.rds'
    output:
        'results/nygc_pbmc_subsampled.rds'
    shell:
        'quarto render notebooks/parse-nygc-pbmc-data.qmd'

rule make_rank_figs:
    input:
        "data/sce_screen_subsample.rds",
        "data/screen-scrna-celltype-match-lee.xlsx",
        "data/cluster-interpretation-nov23.xlsx",
        'data/sce_screen_full.rds',
        "data/sce_screen_subsample.rds",
        "data/aliasmatch_kieranreview-annots.xlsx",
        "results/nygc_pbmc_subsampled.rds"
    output:
        outputs['rank-figs'],
    shell:
        'quarto render notebooks/compare-screen-scrna-marker-rank-nygc.qmd'

rule rna_protein_correlation:
    input:
        "results/nygc_pbmc_subsampled.rds",
        'data/cluster-interpretation-nov23.xlsx',
        'data/aliasmatch_kieranreview-annots.xlsx',
        'data/screen-scrna-celltype-match.xlsx'
    output:
        outputs['fig-correlation'],
        outputs['fig-sens-spec'],
    shell:
        'quarto render notebooks/rna-protein-correlation-nygc.qmd'

rule mammary_single_cell_heatmap:
    input:
        'data/mammary_expression_heatmap.csv'
    output:
        outputs['fig-mammary-heatmap-single-cell']
    shell:
        'quarto render notebooks/mammary-single-cell-heatmap.qmd'

