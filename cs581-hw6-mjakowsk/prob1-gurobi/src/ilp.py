import gurobipy

m = gurobipy.Model("cities-ilp")

#flow variables
f_sv1 = m.addVar(lb=0, ub=18, name="f_sv1")
f_sv2 = m.addVar(lb=0, ub=15, name="f_sv2")
f_v1v3 = m.addVar(lb=0, ub=14, name="f_v1v3")
f_v2v1 = m.addVar(lb=0, ub=5, name="f_v2v1")
f_v2v4  = m.addVar(lb=0, ub=16, name="f_v2v4")
f_v3t = m.addVar(lb=0, ub=22, name="f_v3t")
f_v3v2 = m.addVar(lb=0, ub=7, name="f_v3v2")
f_v4v3 = m.addVar(lb=0, ub=9, name="f_v4v3")
f_v4t = m.addVar(lb=0, ub=6, name="f_v4t")

#constraints
m.addConstr(f_sv1 + f_v2v1 == f_v1v3, "v1")
m.addConstr(f_sv2 + f_v3v2 == f_v2v1 + f_v2v4, "v2")
m.addConstr(f_v1v3 + f_v4v3 == f_v3v2 + f_v3t, "v3")
m.addConstr(f_v2v4 == f_v4v3 + f_v4t, "v4")

#maximize flow out of s
m.setObjective(f_sv1 + f_sv2, gurobipy.GRB.MAXIMIZE)

m.optimize()

with open("output.txt", "w") as file:
    file.write(f"Maximum Flow = {m.objVal}\n")
    for v in m.getVars():
        file.write(f"{int(v.ub)}/{int(v.x)}\n")