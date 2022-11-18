import seaborn as sns
import pandas as pd
from matplotlib import rc
import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt

ep_5_rbgs = [1.3,1.2,1.3,1.8,1.45,0.70,1.0,0.9]
ep_2_rbgs = [1.0,0.9,1.20,1.40,1.2,1.4,0.65,1.2,1.25,1.45,1.1,0.8]
ep_10_rbgs = [0.55,1.4,1.15,1.10,0.2,0.55,1.40,0.65,1.10,1.05,0.65,1.25,0.80]
ep_3_rbgs = [1.05,1.25,1.15,1.25,1.1,1.25,0.75]
ep_4_rbgs = [1.1,1.7,0.45,1.05]
ep_8_rbgs = [1.15,1.05,1.0,0.95,0.7,1.0,0.7]
rbgs = ep_5_rbgs+ep_2_rbgs+ep_10_rbgs+ep_3_rbgs+ep_4_rbgs+ep_8_rbgs

ep_5_jacobi = [1.45,1.35,1.80,0.55,0.95]
ep_2_jacobi = [1.0]
ep_10_jacobi = [1.50, 0.25]
ep_3_jacobi = [1.25]
ep_4_jacobi = [0.95,1.05,0.3,1.7,1.05,0.30,1.25]
ep_8_jacobi = [1.55]
jacobi = ep_5_jacobi+ep_2_jacobi+ep_10_jacobi+ep_3_jacobi+ep_4_jacobi+ep_8_jacobi
ep_5_cgc = [1.0,1.0,0.8,1.6,0.85,0.85,1.05,1.1,1.05,1.80]
ep_2_cgc = [1.0,1.6,0.85,0.3,0.85,0.3,0.85,0.3,0.85,1.35]
ep_10_cgc = [1.0,0.7,1.1,0.85,1.0,1.40,1.70,1.65,1.40,0.80]
ep_3_cgc = [1.0,1.25,1.05,0.9,0.9,1.4]
ep_4_cgc = [1.0,0.8,1.0,0.55,1.7,1.8,1.1,0.95,1.1,0.55,0.95,0.95,1.1,0.9]
ep_8_cgc = [1.0,0.95,1.45,1.3,1.1,1.65,1.1,1.2]
cgc = ep_5_cgc+ep_2_cgc+ep_10_cgc+ep_3_cgc+ep_4_cgc+ep_8_cgc
rc('text', usetex=True)
sns.set_context("paper")
sns.set_style('ticks', {'font.family': 'serif', 'font.serif': 'Times New Roman'})
cgc = pd.DataFrame(cgc)
ax = sns.histplot(cgc, binwidth=0.1, binrange=[0.0,2.0], legend=False)
ax.set_xlabel("Relaxation Factor")
ax.set_xlim(0.0,2.0)
plt.tight_layout()
plt.savefig("histogram_cgc.pdf", dpi=300)