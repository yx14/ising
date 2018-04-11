def T_anneal(T, ii, num_steps, num_burnin):

    #implement annealing code here

    T_a = T*(num_burnin - num_steps)/(num_burnin) + T

    return float(T_a)

def B_anneal(B, ii, num_steps, num_burnin):

    #implement annealing code here

    B_a = B*(num_burning-num_steps)/(num_burnin) + B

    return float(B_a)
