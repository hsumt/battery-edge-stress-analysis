# Separator Edge Stress Analysis in FEniCSx

**Goal:**  
Assess how different separator edge geometries (sharp vs fillet vs setback) affect stress concentrations under stack pressure (~5 MPa) and simple charging strain in a 2D pouch cell model.

**Geometries:**  
- Sharp re-entrant corner (baseline)  
- Fillet at separator edge (~0.5–1× separator thickness radius)  
- Separator setback (~10–20% inward)

**Folder Structure:**
- `meshes/`: FEniCSx-ready meshes  
- `scripts/`: Python scripts for mesh creation, simulation, and post-processing  
- `results/`: Simulation output (plots, tables)  

**Docker Usage:**
```bash
filler
