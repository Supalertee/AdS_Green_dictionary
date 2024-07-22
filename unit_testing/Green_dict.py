import numpy as np
import matplotlib.pyplot as plt

__version__ = '0.01'


class Noninteracting:
    def __init__(self):
        print("Check Mathematica file at {}")

    @staticmethod
    def G(kx, ky, kz, w):
        w = w + 0.001*1j
        matrix = np.array([[kx+w, -ky+kz*1j, 0, 0], 
                           [-ky-kz*1j, -kx+w, 0, 0],
                           [0, 0, kx+w, -ky-kz*1j],
                           [0, 0, -ky+kz*1j, -kx+w]]) * (1/(kx**2 + ky**2 + kz**2 - w**2)**(1/2))
        return matrix
    
class Scalarss:
    def __init__(self):
        print("Check Mathematica file at{}")

    @staticmethod
    def G(kx, ky, kz, w, b = 2):
        w = w + 0.001*1j
        factor1 = np.sqrt(kx**2 + ky**2+kz**2 + b**2 - w**2)
        denorminator = kx**2 + ky**2 + kz**2 - w**2
        matrix = np.array([[(kx+w) * factor1, (-ky+kz*1j)*factor1, b*(kx+w), -b*(ky-kz*1j)], 
                           [(-ky-kz*1j)*factor1, (-kx+w)*factor1, -b*(ky+kz*1j) , b*(-kx+w)],
                           [b*(kx+w), -b*(ky-kz*1j), (kx+w) * factor1, (-ky+kz*1j)*factor1],
                           [-b*(ky+kz*1j), b*(-kx+w), (-ky-kz*1j)* factor1, (-kx+w)* factor1]])
        return matrix/denorminator
    
class Scalarsa:
    def __init__(self):
          print("Check Mathematica file ar {}")

    @staticmethod
    def G(kx,ky,kz,w, b =2):
        w = w +0.001*1j
        factor1 = np.sqrt(kx**2 + ky**2+kz**2 + b**2 - w**2)
        matrix = np.array([[kx+w,-ky+kz*1j, 0 , b*1j]
                            ,[-ky-kz*1j, -kx + w,  -b*1j , 0]
                            ,[0 , b*1j , kx+w , -ky-kz*1j]
                            ,[-b*1j , 0 , -ky+kz*1j , -kx + w]])
        return matrix/factor1

class Bxss:
    def __init__(self):
          print("Check Mathematica file ar {}")
    
    @staticmethod
    def G(kx,ky,kz,w, b =2):
        w = w +0.001*1j
        Omega_p = np.sqrt((b+kx)**2 +ky**2 + kz**2 - w**2)
        Omega_m = np.sqrt((b-kx)**2 +ky**2 + kz**2 - w**2)
        matrix = np.array([[-b*(Omega_p-Omega_m)+((kx+w)*(Omega_p+Omega_m)) , -(ky-kz*1j)*(Omega_p+Omega_m), -((kx+w)*(Omega_m-Omega_p))-b*(Omega_m+Omega_p) , (ky-kz*1j)*(Omega_m-Omega_p)],
                           [-(ky+kz*1j)*(Omega_p+Omega_m),-b*(-Omega_p+Omega_m)-(kx-w)*(Omega_p+Omega_m) , (ky+kz*1j)*(-Omega_p+Omega_m) , ((kx-w)*(Omega_m-Omega_p))+(b*(Omega_m+Omega_p))],
                           [ (-((kx+w)*(Omega_m-Omega_p))-(b*(Omega_m+Omega_p))),(ky-kz*1j)*(Omega_m-Omega_p), -b*(Omega_p-Omega_m)+((kx+w)*(Omega_p+Omega_m)) ,  -(ky-kz*1j)*(Omega_p+Omega_m)  ],
                           [(ky+kz*1j)*(Omega_m-Omega_p)  , (kx-w)*(Omega_m-Omega_p)+b*(Omega_m+Omega_p) , -(ky+kz*1j)*(Omega_p+Omega_m) , -b*(-Omega_p+Omega_m)-((kx-w)*(Omega_p+Omega_m)) ]])
        return matrix/(2*Omega_m*Omega_p)


def spectra(Interaction, section = "all" , kx = 0,ky = 0 , kz = 0, omega = 0):
    if str(section) in ["xw", "wx"]:
    
        x = np.arange(-5,5,0.05)
        w = np.arange(-5,5,0.05)
        Kx, W = np.meshgrid(x, w, indexing='ij')
        Gf = np.zeros(np.meshgrid(x, w, indexing='ij')[0].shape)

        for i in range(Kx.shape[0]):
            for j in range(W.shape[1]):
                Gf[i,j] = np.trace(Interaction.G(Kx[i,j],ky,kz,W[i,j])).imag
        
        plt.imshow(Gf.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
        plt.xticks(np.arange(-5, 5, step=1))
        plt.yticks(np.arange(-5, 5, step=1))
        plt.xlabel("kx")
        plt.ylabel("w")
        plt.show()

    elif str(section) in ["yw", "wy"]:
    
        y = np.arange(-5,5,0.05)
        w = np.arange(-5,5,0.05)
        Ky, W = np.meshgrid(y, w, indexing='ij')

        Gf = np.zeros(np.meshgrid(y, w, indexing='ij')[0].shape)

        for i in range(Ky.shape[0]):
            for j in range(W.shape[1]):
                Gf[i,j] = np.trace(Interaction.G(kx,Ky[i,j],ky,W[i,j])).imag
        
        plt.imshow(Gf.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
        plt.xticks(np.arange(-5, 5, step=1))
        plt.yticks(np.arange(-5, 5, step=1))
        plt.xlabel("ky")
        plt.ylabel("w")
        plt.show()

    elif str(section) in ["zw", "wz"]:
        
            z = np.arange(-5,5,0.05)
            w = np.arange(-5,5,0.05)
            Kz, W = np.meshgrid(z, w, indexing='ij')

            Gf = np.zeros(np.meshgrid(z, w, indexing='ij')[0].shape)

            for i in range(Kz.shape[0]):
                for j in range(W.shape[1]):
                    Gf[i,j] = np.trace(Interaction.G(kx,ky,kz[i,j],W[i,j])).imag
            
            plt.imshow(Gf.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("kz")
            plt.ylabel("w")
            plt.show()

    elif str(section) in ["xy", "yx"]:
        
            x = np.arange(-5,5,0.05)
            y = np.arange(-5,5,0.05)
            Kx, Ky = np.meshgrid(x, y, indexing='ij')

            Gf = np.zeros(np.meshgrid(x, y, indexing='ij')[0].shape)

            for i in range(Kx.shape[0]):
                for j in range(Ky.shape[1]):
                    Gf[i,j] = np.trace(Interaction.G(Kx[i,j],Ky[i,j],kz,omega)).imag
            
            plt.imshow(Gf.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("kx")
            plt.ylabel("ky")
            plt.show()
    elif str(section) in ["xz", "zx"]:
        
            x = np.arange(-5,5,0.05)
            z = np.arange(-5,5,0.05)
            Kx, Kz = np.meshgrid(x, z, indexing='ij')

            Gf = np.zeros(np.meshgrid(x,z, indexing='ij')[0].shape)

            for i in range(Kx.shape[0]):
                for j in range(Kz.shape[1]):
                    Gf[i,j] = np.trace(Interaction.G(Kx[i,j],ky,Kz[i,j],omega)).imag
            
            plt.imshow(Gf.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("kx")
            plt.ylabel("kz")
            plt.show()

    elif str(section) in ["yz", "zy"]:
        
            y = np.arange(-5,5,0.05)
            z = np.arange(-5,5,0.05)
            Ky, Kz = np.meshgrid(y, z, indexing='ij')

            Gf = np.zeros(np.meshgrid(y,z, indexing='ij')[0].shape)

            for i in range(Ky.shape[0]):
                for j in range(Kz.shape[1]):
                    Gf[i,j] = np.trace(Interaction.G(kx,Ky[i,j],Kz[i,j],omega)).imag
            
            plt.imshow(Gf.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("ky")
            plt.ylabel("kz")
            plt.show()          
    elif str(section) in ["all","All"]: 
            y = np.arange(-5,5,0.05)
            z = np.arange(-5,5,0.05)
            q1, q2 = np.meshgrid(y, z, indexing='ij')
         
            Gfxw = np.zeros(np.meshgrid(y,z, indexing='ij')[0].shape)
            Gfyw = np.zeros(np.meshgrid(y,z, indexing='ij')[0].shape)
            Gfzw = np.zeros(np.meshgrid(y,z, indexing='ij')[0].shape)
            Gfxy = np.zeros(np.meshgrid(y,z, indexing='ij')[0].shape)
            Gfyz = np.zeros(np.meshgrid(y,z, indexing='ij')[0].shape)
            Gfxz = np.zeros(np.meshgrid(y,z, indexing='ij')[0].shape)
         
            for i in range(q1.shape[0]):
                for j in range(q2.shape[1]):
                    Gfxw[i,j] = np.trace(Interaction.G(q1[i,j],ky,kz,q2[i,j])).imag
                    Gfyw[i,j] = np.trace(Interaction.G(kx,q1[i,j],kz,q2[i,j])).imag
                    Gfzw[i,j] = np.trace(Interaction.G(kx,ky,q1[i,j],q2[i,j])).imag
                    Gfxy[i,j] = np.trace(Interaction.G(q1[i,j],q2[i,j],kz,omega)).imag
                    Gfyz[i,j] = np.trace(Interaction.G(kx,q1[i,j],q2[i,j],omega)).imag
                    Gfxz[i,j] = np.trace(Interaction.G(q1[i,j],ky,q2[i,j],omega)).imag

            plt.subplot(2,3,1)
            plt.imshow(Gfxw.T , cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("kx")
            plt.ylabel("w")
            plt.subplot(2,3,2)
            plt.imshow(Gfyw.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("ky")
            plt.ylabel("w")
            plt.subplot(2,3,3)
            plt.imshow(Gfzw.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("kz")
            plt.ylabel("w")
            plt.subplot(2,3,4)
            plt.imshow(Gfxy.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("kx")
            plt.ylabel("ky")
            plt.subplot(2,3,5)
            plt.imshow(Gfyz.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("ky")
            plt.ylabel("kz")
            plt.subplot(2,3,6)
            plt.imshow(Gfxz.T, cmap='inferno',vmax=20,vmin=0, extent=(-5, 5, -5, 5), origin='lower')
            plt.xticks(np.arange(-5, 5, step=1))
            plt.yticks(np.arange(-5, 5, step=1))
            plt.xlabel("kx")
            plt.ylabel("kz")

            plt.show()          

