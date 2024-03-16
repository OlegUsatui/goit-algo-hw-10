import pulp

model = pulp.LpProblem("MaximizeProduction", pulp.LpMaximize)

L = pulp.LpVariable('L', lowBound=0, cat='Integer')
F = pulp.LpVariable('F', lowBound=0, cat='Integer')

model += L + F, "TotalProduction"

model += 2*L + F <= 100, "WaterConstraint"
model += L <= 50, "SugarConstraint"
model += L <= 30, "LemonJuiceConstraint"
model += 2*F <= 40, "FruitPureeConstraint"

model.solve()

print("Optimal Production Plan:")
print("Number of Lemonades (L):", pulp.value(L))
print("Number of Fruit Juices (F):", pulp.value(F))