import pandas as pd

cell_types = pd.read_excel("data/screen-scrna-celltype-match.xlsx")
cell_types = cell_types['cell_type']


outputs = {
    'rank-figs': expand('figs/{cell_type}-screen-vs-scrna.pdf', cell_type = cell_types)
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

rule make_rank_figs:
    input:
        'data/sce_screen_full.rds',
        "data/sce_screen_subsample.rds",
    output:
        'figs/{cell_type}-screen-vs-scrna.pdf',
    shell:
        'quarto render notebooks/compare-screen-scrna-marker-rank.qmd -P cell_type:{wildcards.cell_type}'