import traceback
import sys
import numpy as np

class Simulation:

    def __init__(self):
        pass

    # Confidence interval

    def bootstrap_ci(self,input_array,sim_size,sample_size,alpha):

        try:

            self.bounce_bootstrap_means = np.empty(sim_size)

            for i in range(sim_size):
                self.bs_sample = np.random.choice(input_array.astype('float'),size = sample_size)
                self.bounce_bootstrap_means[i] = self.bs_sample.mean()

            return np.percentile(self.bounce_bootstrap_means,[(alpha/2)*100,100-(alpha/2)*100])

        except:

            traceback.print_exception(*sys.exc_info())

    def mc_ci(self,input_array,sim_size,sample_size,alpha):

        try:

            self.mc_bootstrap_means =  np.empty(sim_size)

            for i in range(sim_size):
                self.mc_bs_sample = np.random.normal(loc = input_array.astype('float').mean(),scale=input_array.astype('float').std(),size = sample_size)
                self.mc_bootstrap_means[i] = self.mc_bs_sample.mean()

            return np.percentile(self.mc_bootstrap_means,[(alpha/2)*100,100-(alpha/2)*100])

        except:

            traceback.print_exception(*sys.exc_info())

    # Sample generation

    def bootstrap_sm(self,input_array,sim_size,sample_size,alpha):

        try:

            self.bs_samples =  []

            for i in range(sim_size):
                self.bs_sample = np.random.choice(input_array.astype('float'),size = sample_size)
                self.bs_samples.append(self.bs_sample)

            return np.array(self.bs_samples)

        except:

            traceback.print_exception(*sys.exc_info())

    def mc_sm(self,input_array,sim_size,sample_size,alpha):

        try:

            self.mc_samples =  []

            for i in range(sim_size):
                self.mc_bs_sample = np.random.normal(loc = input_array.astype('float').mean(),scale=input_array.astype('float').std(),size = sample_size)
                self.mc_samples.append(self.mc_bs_sample)

            return np.array(self.mc_samples)

        except:

            traceback.print_exception(*sys.exc_info())
