print("Hello World")

import cobra.test
model = cobra.test.create_test_model("salmonella")

print(len(model.reactions))

print(len(model.metabolites))

print(len(model.genes))


print(model.reactions[29])


atp_c = model.metabolites.get_by_id("atp_c")
print(atp_c.formula)

print(cobra.solvers.solver_dict)

print(model.optimize(solver='optlang-cplex'))