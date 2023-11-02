
suppressPackageStartupMessages({
  library(tidyverse)
  library(SingleCellExperiment)
  library(readxl)
  library(Nebulosa)
  library(ComplexHeatmap)
  library(here)
  library(nnet)
})

set.seed(123L)

#' This script reads in the raw data matrix,
#' converts it to a SingleCellExperiment object,
#' PCA, UMAP, cluster etc, imputes it for full dataset, then saves
#' 

message("Reading in data...")

raw_dat <- read_csv(here("data/singlecells.csv"))

metal_target_map <- read_excel(here("data/antigen-metal-map-simon.xlsx"))

colnames(raw_dat) <- plyr::mapvalues(colnames(raw_dat), from = metal_target_map$metal, to = metal_target_map$target)

lc <- select(raw_dat, CD66b:CD4) |> 
  as.matrix() |> 
  t()
cd <- select(raw_dat, Nd148Di:target)

sce <- SingleCellExperiment(
  assays = list(
    counts = lc,
    logcounts = log1p(lc)
  ),
  colData = cd
)

message("Converting to SCE complete!")

colnames(sce) <- paste0("cell_", seq_len(ncol(sce)))

assay(sce, 'seuratNormData') <- assay(sce, 'logcounts')

message("Scale & PCA...")
sce <- singleCellTK::runSeuratScaleData(sce)


set.seed(123L)
sce_subsample <- sce[, sample(ncol(sce), 1e4)]
sce_subsample@metadata <- list()

sce_subsample <- singleCellTK::runSeuratPCA(sce_subsample)

message("UMAP...")
sce_subsample <- singleCellTK::runSeuratUMAP(sce_subsample)

message("Clustering...")
sce_subsample <- singleCellTK::runSeuratFindClusters(sce_subsample, resolution = 0.5)

message("Transferring annotations to full dataset")
df <- data.frame(t(logcounts(sce_subsample)))
df$class <- sce_subsample$Seurat_louvain_Resolution0.5

model <- multinom(class ~ ., data = df)

labels_full <- predict(model, newdata = data.frame(t(logcounts(sce))))

sce$predicted_label <- labels_full

message("Done! Saving...")
saveRDS(sce, here("data/sce_screen_full.rds"))
saveRDS(sce_subsample, here("data/sce_screen_subsample.rds"))


