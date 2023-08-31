import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib as mpl
colors=["#003049","#d62828","#f77f00","#fcbf49","#eae2b7"]

def plotsettings(col=False):
    rc('text.latex', preamble='\\usepackage{txfonts}')
    rc('text', usetex=True)
    rc('font', family='serif')
    rc('font', serif='times')
    rc('font', size=12)
    rc('mathtext', default='sf')
    rc("lines", markeredgewidth=1)
    rc("lines", linewidth=2)
    rc('axes', labelsize=12)  # 24
    rc('axes', titlesize=12)
    rc("axes", linewidth=0.5)  # 2)
    rc('xtick', labelsize=13)
    rc('ytick', labelsize=13)
    rc('legend', fontsize=13)  # 16
    rc('xtick.major', pad=6)  # 8)
    rc('ytick.major', pad=6)  # 8)
    rc('xtick.minor', size=8)  # 8)
    rc('ytick.minor', size=8)  # 8)
    if col:
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=colors) 
plotsettings(col=True)

def hd(x):
	fac = (1-np.cos(x))/2
	return 0.5 - fac/4 + 3*fac/2*np.log(fac)

zeta = np.linspace(1e-6,np.pi, 100)

# Compute the Hellings and Downs curve
C_HD = hd(zeta)

# Plotting the Hellings and Downs curve
plt.figure(figsize=(6,3))
plt.plot(180 * zeta/np.pi, C_HD)
plt.xlabel(r'Angle $\zeta$ between Earth-pulsar baselines (degrees)')
plt.ylabel(r'Expected Correlation $\chi(\zeta)$')
plt.title('Hellings and Downs Correlation Function')
plt.grid(False)
plt.xlim(0, 180)
plt.savefig("hd.png", transparent=True, bbox_inches='tight',dpi=200)
plt.show()

