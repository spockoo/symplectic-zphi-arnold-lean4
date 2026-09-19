import sympy as sp
from mpmath import mp, mpf, cos, sin

# # 1. PREUVE SYMBOLIQUE FORMELLE (SymPy) - ISO-KAM
p1, p2 = sp.symbols('p_1 p_2', real=True)
q1, q2 = sp.symbols('q_1 q_2', real=True)
phi_sym = (1 + sp.sqrt(5)) / 2

H0 = sp.Rational(1, 2) * (p1**2 + p2**2)
dH0_dp1 = sp.diff(H0, p1)
dH0_dp2 = sp.diff(H0, p2)

Hess_Arnold = sp.Matrix([
    [sp.diff(H0, p1, p1), sp.diff(H0, p1, p2), dH0_dp1],
    [sp.diff(H0, p2, p1), sp.diff(H0, p2, p2), dH0_dp2],
    [dH0_dp1,             dH0_dp2,             0]
])

det_arnold = Hess_Arnold.det()  # Renvoie -p1**2 - p2**2

# # 2. SIMULATION DYNAMIQUE HAUTE DENSITE (mpmath - 100 dps)
mp.dps = 100
phi_mp = (mpf('1') + mp.sqrt(mpf('5'))) / mpf('2')
epsilon = mpf('0.001')
dt = mpf('0.001')
num_steps = 10000

q1_val, q2_val = mpf('0.1'), mpf('0.2')
p1_val, p2_val = mpf('1.0'), mpf('0.5')

def hamiltonian(q1, q2, p1, p2, eps, phi):
    return mpf('0.5') * (p1**2 + p2**2) + eps * (cos(q1) + cos(q2) + cos(q1 + phi * q2))

E_initial = hamiltonian(q1_val, q2_val, p1_val, p2_val, epsilon, phi_mp)

# Integrateur Symplectique Symes-Verlet (100 dps)
for _ in range(num_steps):
    f_q1 = epsilon * (-sin(q1_val) - sin(q1_val + phi_mp * q2_val))
    f_q2 = epsilon * (-sin(q2_val) - phi_mp * sin(q1_val + phi_mp * q2_val))
    
    p1_half = p1_val + mpf('0.5') * dt * f_q1
    p2_half = p2_val + mpf('0.5') * dt * f_q2
    
    q1_val = q1_val + dt * p1_half
    q2_val = q2_val + dt * p2_half
    
    f_q1_new = epsilon * (-sin(q1_val) - sin(q1_val + phi_mp * q2_val))
    f_q2_new = epsilon * (-sin(q2_val) - phi_mp * sin(q1_val + phi_mp * q2_val))
    
    p1_val = p1_half + mpf('0.5') * dt * f_q1_new
    p2_val = p2_half + mpf('0.5') * dt * f_q2_new

E_final = hamiltonian(q1_val, q2_val, p1_val, p2_val, epsilon, phi_mp)
delta_E = abs(E_final - E_initial)
ratio_eps = delta_E / mp.eps
print(f"det(U) symbolique : {det_arnold}")
print(f"Énergie initiale  : {E_initial}")
print(f"Énergie finale    : {E_final}")
print(f"Dérive Delta E    : {delta_E}")
print(f"Ratio / mp.eps    : {ratio_eps}")