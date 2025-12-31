import dolfinx
import meshio
import numpy as np
from mpi4py import MPI
from petsc4py import PETSc
from dolfinx import mesh
from dolfinx import fem



def create_mesh(geometry_type="sharp"):
    # Simplified 2D rectangular pouch cell: Anode | Separator | Cathode
    length = 1.0  # arbitrary units
    height = 0.1  # pouch cell thickness
    
    # Sharp / Fillet / Setback adjustments
    if geometry_type == "sharp":
        pass  # baseline
    elif geometry_type == "fillet":
        pass  # placeholder 
    elif geometry_type == "setback":
        pass  # placeholder 
    elif geometry_type == "setback + fillet":
        pass  # placeholder 
    # what follows is just base code
    nx, ny = 100, 20
    domain = mesh.create_rectangle(MPI.COMM_WORLD, [np.array([0, 0]), np.array([length, height])], [nx, ny], mesh.CellType.quadrilateral)
    
    # Export mesh
    filename = f"../meshes/{geometry_type}_mesh.xdmf"
    with dolfinx.io.XDMFFile(MPI.COMM_WORLD, filename, "w") as file:
        file.write_mesh(domain)
    print(f"{geometry_type} mesh saved to {filename}")

if __name__ == "__main__":
    for geom in ["sharp", "fillet", "setback"]:
        create_mesh(geom)