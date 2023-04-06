import numpy as np

####################################################################

# parameters need to be changed for each experiment

# saving location


####################################################################



# parameters for network structure (same for each experiment)

# Parameter of the simulation
dt                      = 0.1
MSP_update_interval     = 100                       # update interval for MSP in ms
total_num_virtual_procs = 1                         # number = nodes * ppn in experiment.moab
growth_time             = 1000000.                   # simulation time in ms
cicles                  = 20
growth_step             = growth_time/cicles
mini_step             = growth_step/50.
min_delay               = 1.0
max_delay               = 1.5

n_rank                  = total_num_virtual_procs*1 #For MPI run

# Parameters for asynchronous irregular firing
g       = 8.0
eta     = 1.5
epsilon = 0.1                                       # connection probability

order     = 200
NE        = 4*order
NI        = 1*order
N_neurons = NE+NI


CE    = int(epsilon*NE)                             # number of excitatory synapses per neuron
CI    = int(epsilon*NI)                             # number of inhibitory synapses per neuron  
C_tot = int(CI+CE)                                  # total number of synapses per neuron


# Initialize the parameters of the integrate and fire neuron
neuron_model    = "iaf_psc_delta"
CMem            = 250.0
tauMem          = 20.0
theta           = 20.0
tau_Ca          = 1000.
beta_Ca         = 1./1000.
J               = 0.1                               # postsynaptic amplitude in mV

neuron_params   = {
                    "C_m"       : CMem,
                    "tau_m"     : tauMem,
                    "t_ref"     : 2.0,
                    "E_L"       : 0.0,
                    "V_reset"   : 0.0,
                    "V_m"       : 0.0,
                    "beta_Ca"   : beta_Ca,
                    "tau_Ca"    : tau_Ca,
                    "V_th"      : theta
                   }

weight          = J


# threshold rate, equivalent rate of events needed to
# have mean input current equal to threshold
nu_th  = theta/(J*CE*tauMem)
nu_ex  = eta*nu_th
rate = 10000.#1000.0*nu_ex*CE  

 
# Parameter for synpatic elements' growth curve
growth_curve_d    = "gaussian"
z0_mean           = 1.
growth_curve_a    = "gaussian"
z0_std            = .1
slope             = 0.5
target_rate       = 0.0097


# Parameter for structural plasticity synapse model
synapse_model   = "static_synapse"

# recording spikes

long_duration  = 5000.
short_duration = 1000. 


# scaling factor
scaling_factor = 0.1

