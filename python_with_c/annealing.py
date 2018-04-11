def T_anneal(T, ii, num_steps, num_burnin):

    #implement annealing code here
	if ii < num_burnin:
		#T_a = T*float(num_burnin - ii)/(num_burnin) + T
		mult = 0.99 #0.8#1.- 1./num_burnin
		T_a = T*mult**num_burnin + T 
	else:
		T_a = T
	return float(T_a)

def B_anneal(B, ii, num_steps, num_burnin):

    #implement annealing code here
	if ii < num_burnin:
		B_a = 2*(1 - float(ii)/num_burnin) 
	else:
		B_a = B
	
	return float(B_a)