"""Illustration only: plots are not the evidence for nonexistence."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
a,r,t,u,v = 12/25,1/2,3/4,1641/3200,103/200
f = lambda x:x*(1+.5*(x*x-.25)*(1-x*x))
plt.rcParams.update({"font.size":9,"axes.spines.top":False,"axes.spines.right":False})
fig,axes = plt.subplots(1,2,figsize=(7.2,2.65),layout="constrained")
x = np.linspace(0,1,500)
ax = axes[0]
ax.axvspan(0,a,color="#8cceaf",alpha=.4,label="Initial set (positive half)")
ax.axhspan(u,v,color="#d87c7c",alpha=.75,label="Unsafe successor band")
ax.plot(x,f(x),color="#224e7a",lw=2,label="True map")
ax.plot(x,x,color="#68727d",ls=":",lw=1,label="Identity")
ax.plot([r,r],[0,r],color="#333333",ls="--",lw=.9)
ax.plot([0,r],[r,r],color="#333333",ls="--",lw=.9)
ax.set(xlabel="$x$",ylabel="$f(x)$",title="Quadratic invariant: $|x|\\leq 1/2$",xlim=(0,1),ylim=(0,1))
ax.legend(fontsize=6.7,loc="upper left",frameon=False)
ax = axes[1]
z = np.linspace(0,1,500)
ax.plot(z,f(np.sqrt(z))**2,color="#224e7a",lw=2,label="True lifted graph")
ax.plot([0,t*t],[0,f(t)**2],color="#af5a23",ls="--",lw=1.5,label="Convexified transition")
ax.scatter([a*a],[u*u],color="#af5a23",s=30,zorder=4)
ax.scatter([0,t*t],[0,f(t)**2],color="#224e7a",s=17,zorder=3)
ax.axvline(a*a,color="#359267",ls=":",lw=1)
ax.axhline(u*u,color="#b45454",ls=":",lw=1)
ax.annotate("$(a^2,u^2)$",(a*a,u*u),xytext=(.30,.14),
            arrowprops={"arrowstyle":"-","lw":.6},fontsize=9)
ax.set(xlabel="$z=x^2$",ylabel="$f(x)^2$",title="A moment transition crosses the safety gap",xlim=(0,1),ylim=(0,1))
ax.legend(fontsize=7,loc="upper left",frameon=False)
for extension in ["pdf","png"]:
    fig.savefig(root/"paper"/f"geometry.{extension}",dpi=200)
print("Created paper/geometry.pdf and paper/geometry.png")
