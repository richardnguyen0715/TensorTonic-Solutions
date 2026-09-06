import numpy as np

def adadelta_step(w: list, grad: list, E_grad_sq: list, E_update_sq: list, rho: float = 0.9, eps: float = 1e-6) -> dict:
    """
    Returns a dictionary with new_w, new_E_grad_sq, and new_E_update_sq.
    """
    # Write code here
    w = np.array(w)
    grad = np.array(grad)
    E_grad_sq = np.array(E_grad_sq)
    E_update_sq = np.array(E_update_sq)

    # First: Update running squared-gradient average
    new_E_grad_sq = rho * E_grad_sq + (1 - rho) * grad ** 2
    print("Done 1")

    # Second: Compute parameter change
    delta_W = -1 * np.sqrt(E_update_sq + eps) / np.sqrt(new_E_grad_sq + eps) * grad
    print("Done 2 with delta_W: ", delta_W)

    # Third: Update runniong squared-change average
    new_E_update_sq = rho * E_update_sq + (1 - rho) * delta_W ** 2
    print("Done 3")

    # Finally: update the parameter
    new_w = w + delta_W
    print("Done 4")

    return {"new_w": new_w, "new_E_grad_sq": new_E_grad_sq, "new_E_update_sq": new_E_update_sq}
    