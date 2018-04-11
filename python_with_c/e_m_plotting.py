

Msamp, Esamp = run_ising(lattice, temp,num_steps,num_burnin,j,b)

M_mean, E_mean, M_std, E_std = get_plot_values(temp,Msamp,Esamp,num_analysis)
temp_arr.append(temp)
M_mean_arr.append(M_mean)
E_mean_arr.append(E_mean)
M_std_arr.append(M_std)
E_std_arr.append(E_std)

def get_plot_values(temp,Msamp,Esamp,num_analysis): #only for plotting at end
    try:
        M_mean = np.average(Msamp[-num_analysis:])
        E_mean = np.average(Esamp[-num_analysis:])
        M_std = np.std(Msamp[-num_analysis:])
        E_std = np.std(Esamp[-num_analysis:])
        return M_mean, E_mean, M_std, E_std
    except:
        logging.error("Temp={0}: Error getting plot values".format(temp))
        return False

def plot_graphs(temp_arr,M_mean_arr,M_std_arr,E_mean_arr,E_std_arr): #plot graphs at end
    plt.figure(1)
    plt.ylim(0,1)
    plt.errorbar(temp_arr, np.absolute(M_mean_arr), yerr=M_std_arr, uplims=True, lolims=True,fmt='o')
    plt.xlabel('Temperature')
    plt.ylabel('Magnetization')
    plt.figure(2)
    plt.errorbar(temp_arr, E_mean_arr, yerr=E_std_arr, fmt='o')
    plt.xlabel('Temperature')
    plt.ylabel('Energy')
    plt.show()