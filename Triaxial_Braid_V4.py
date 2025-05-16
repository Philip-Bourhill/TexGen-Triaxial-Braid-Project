# =============================================================================
# TexGen: Geometric textile modeller.
# Copyright (C) 2006 Martin Sherburn

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# =============================================================================

from TexGen.Core import * 
import math 

# Create a textile 
Textile = CTextile() 

# Create a list containing 3 yarns 
Yarns = [CYarn(), CYarn(), CYarn()] 

# Define cross section of axial yarns
# Axial Yarn Height
a=2;
# Axial Yarn Width
b=0.51;

# Define cross section of bias yarns
# Bias Yarn Height
c=4;
# Bias Yarn Width
d=1;

# Define general geometry of the yarns
# Distance between Axial Yarns
X=8;
# Braiding angle
theta=math.radians(45);
# Combined height of yarns
Z=(b+(d/2));

# Calculate the distance for a repeatable length of the axial yarns
Y=2*X/math.tan(theta);

# Define the resolution for the surface mesh
Resolution=20;

# Define nodes for the axial yarn
Yarns[0].AddNode(CNode(XYZ(0, 0, 0))) 
Yarns[0].AddNode(CNode(XYZ(0, Y, 0))) 

# Calculate the adjusted distance of a and X in the angle theta 
W=a/math.cos(theta);
V=X/math.cos(theta);

# Calculate the point at which the bias yarns no longer follow the edge of the axial yarn and moves in a straight line to the bottom of the next axial yarn
Xmax = (1) / (((2 * V) / (W**2 * (4 - (d / (b**2))))) - math.sqrt(-((((V**2) / d) - 1 + (W**2 / (b**2)) - (4 * V**2) / (4 * d - ((d**2) / (b**2))))) / (W**4 * ((4 / d) - (1 / (b**2))))))
Ymax = math.sqrt((1 - (Xmax**2 / W**2)) * b**2)
Xf = Xmax + math.sqrt(((d / 2)**2) / (1 - (W**2 / b**2) + (W**4 / (Xmax**2 * b**2))))
Zf = Ymax + (math.sqrt((1 - (Xmax**2 / W**2)) * b**2) * W**2) / (Xmax * b**2) * math.sqrt(((d / 2)**2) / (1 - (W**2 / b**2) + (W**4 / (Xmax**2 * b**2))))

# Adjust Xf and back to original coordinate system
Xfa=Xf*math.cos(theta);

# Calculate Yfa
Yfa=(Xf*math.cos(theta))/math.tan(theta);

# Caculate the height of each node
Zf2 = (math.sqrt((1 - ((0.2*Xmax)**2 / W**2)) * b**2)) + (math.sqrt((1 - ((0.2*Xmax)**2 / W**2)) * b**2) * W**2) / ((0.2*Xmax) * b**2) * math.sqrt(((d / 2)**2) / (1 - (W**2 / b**2) + (W**4 / ((0.2*Xmax)**2 * b**2))))
Zf4 = (math.sqrt((1 - ((0.4*Xmax)**2 / W**2)) * b**2)) + (math.sqrt((1 - ((0.4*Xmax)**2 / W**2)) * b**2) * W**2) / ((0.4*Xmax) * b**2) * math.sqrt(((d / 2)**2) / (1 - (W**2 / b**2) + (W**4 / ((0.4*Xmax)**2 * b**2))))
Zf6 = (math.sqrt((1 - ((0.6*Xmax)**2 / W**2)) * b**2)) + (math.sqrt((1 - ((0.6*Xmax)**2 / W**2)) * b**2) * W**2) / ((0.6*Xmax) * b**2) * math.sqrt(((d / 2)**2) / (1 - (W**2 / b**2) + (W**4 / ((0.6*Xmax)**2 * b**2))))
Zf8 = (math.sqrt((1 - ((0.8*Xmax)**2 / W**2)) * b**2)) + (math.sqrt((1 - ((0.8*Xmax)**2 / W**2)) * b**2) * W**2) / ((0.8*Xmax) * b**2) * math.sqrt(((d / 2)**2) / (1 - (W**2 / b**2) + (W**4 / ((0.8*Xmax)**2 * b**2))))

Zfa = ((-Zf - Zf) / (Xfb - Xfa)) * ((Xfa*1.2) - Xf * math.cos(theta)) + Zf;



# Assign Nodes to Positive Bias Yarn
Yarns[1].AddNode(CNode(XYZ(0, 0, Z+0.01))) 

Yarns[1].AddNode(CNode(XYZ((Xfa*0.2), (Yfa*0.2), Zf2+0.01)))
Yarns[1].AddNode(CNode(XYZ((Xfa*0.4), (Yfa*0.4), Zf4+0.01)))
Yarns[1].AddNode(CNode(XYZ((Xfa*0.6), (Yfa*0.6), Zf6+0.01)))
Yarns[1].AddNode(CNode(XYZ((Xfa*0.8), (Yfa*0.8), Zf8+0.01)))
 
Yarns[1].AddNode(CNode(XYZ(Xfa, Yfa, Zf+0.01))) 

Yarns[1].AddNode(CNode(XYZ(Xfa*1.2, Yfa*1.2, +Zfa+0.02)))

Yarns[1].AddNode(CNode(XYZ(X/2, Y/4, 0))) 

Yarns[1].AddNode(CNode(XYZ(X-(Xfa*1.2), (Y/2)-(Yfa*1.2), -Zfa-0.02)))

Yarns[1].AddNode(CNode(XYZ(X-Xfa, (Y/2)-Yfa, -Zf-0.01))) 

Yarns[1].AddNode(CNode(XYZ(X-(Xfa*0.8), (Y/2)-(Yfa*0.8), -Zf8-0.01)))
Yarns[1].AddNode(CNode(XYZ(X-(Xfa*0.6), (Y/2)-(Yfa*0.6), -Zf6-0.01)))
Yarns[1].AddNode(CNode(XYZ(X-(Xfa*0.4), (Y/2)-(Yfa*0.4), -Zf4-0.01)))
Yarns[1].AddNode(CNode(XYZ(X-(Xfa*0.2), (Y/2)-(Yfa*0.2), -Zf2-0.01)))

Yarns[1].AddNode(CNode(XYZ(X, Y/2, -Z-0.01))) 

Yarns[1].AddNode(CNode(XYZ(X+(Xfa*0.2), (Y/2)+(Yfa*0.2), -Zf2-0.01)))
Yarns[1].AddNode(CNode(XYZ(X+(Xfa*0.4), (Y/2)+(Yfa*0.4), -Zf4-0.01)))
Yarns[1].AddNode(CNode(XYZ(X+(Xfa*0.6), (Y/2)+(Yfa*0.6), -Zf6-0.01)))
Yarns[1].AddNode(CNode(XYZ(X+(Xfa*0.8), (Y/2)+(Yfa*0.8), -Zf8-0.01)))

Yarns[1].AddNode(CNode(XYZ(X+Xfa, (Y/2)+Yfa, -Zf-0.01))) 

Yarns[1].AddNode(CNode(XYZ(X+(Xfa*1.2), (Y/2)+(Yfa*1.2), -Zfa-0.02)))

Yarns[1].AddNode(CNode(XYZ(3*X/2, 3*Y/4, 0))) 

Yarns[1].AddNode(CNode(XYZ(2*X-(Xfa*1.2), Y-(Yfa*1.2), Zfa+0.02)))

Yarns[1].AddNode(CNode(XYZ(2*X-Xfa, Y-Yfa, Zf+0.01))) 

Yarns[1].AddNode(CNode(XYZ(2*X-(Xfa*0.8), Y-(Yfa*0.8), Zf8+0.01)))
Yarns[1].AddNode(CNode(XYZ(2*X-(Xfa*0.6), Y-(Yfa*0.6), Zf6+0.01)))
Yarns[1].AddNode(CNode(XYZ(2*X-(Xfa*0.4), Y-(Yfa*0.4), Zf4+0.01)))
Yarns[1].AddNode(CNode(XYZ(2*X-(Xfa*0.2), Y-(Yfa*0.2), Zf2+0.01)))

Yarns[1].AddNode(CNode(XYZ(2*X, Y, Z+0.01))) 


# Assign Nodes to Negative Bias Yarn
Yarns[2].AddNode(CNode(XYZ(0, Y/4, -Z-0.01))) 

Yarns[2].AddNode(CNode(XYZ((-Xfa*0.2), (Yfa*0.2)+(Y/4), -Zf2-0.01)))
Yarns[2].AddNode(CNode(XYZ((-Xfa*0.4), (Yfa*0.4)+(Y/4), -Zf4-0.01)))
Yarns[2].AddNode(CNode(XYZ((-Xfa*0.6), (Yfa*0.6)+(Y/4), -Zf6-0.01)))
Yarns[2].AddNode(CNode(XYZ((-Xfa*0.8), (Yfa*0.8)+(Y/4), -Zf8-0.01)))
 
Yarns[2].AddNode(CNode(XYZ(-Xfa, Yfa+(Y/4), -Zf-0.01))) 

Yarns[2].AddNode(CNode(XYZ(-Xfa*1.2, Yfa*1.2+(Y/4), -Zfa-0.02)))

Yarns[2].AddNode(CNode(XYZ(-X/2, Y/4+(Y/4), 0))) 

Yarns[2].AddNode(CNode(XYZ(-(X-(Xfa*1.2)), (Y/2)-(Yfa*1.2)+(Y/4), Zfa+0.02)))

Yarns[2].AddNode(CNode(XYZ(-(X-Xfa), (Y/2)-Yfa+(Y/4), Zf+0.01))) 

Yarns[2].AddNode(CNode(XYZ(-(X-(Xfa*0.8)), (Y/2)-(Yfa*0.8)+(Y/4), Zf8+0.01)))
Yarns[2].AddNode(CNode(XYZ(-(X-(Xfa*0.6)), (Y/2)-(Yfa*0.6)+(Y/4), Zf6+0.01)))
Yarns[2].AddNode(CNode(XYZ(-(X-(Xfa*0.4)), (Y/2)-(Yfa*0.4)+(Y/4), Zf4+0.01)))
Yarns[2].AddNode(CNode(XYZ(-(X-(Xfa*0.2)), (Y/2)-(Yfa*0.2)+(Y/4), Zf2+0.01)))

Yarns[2].AddNode(CNode(XYZ(-X, Y/2+(Y/4), Z+0.01))) 

Yarns[2].AddNode(CNode(XYZ(-(X+(Xfa*0.2)), (Y/2)+(Yfa*0.2)+(Y/4), Zf2+0.01)))
Yarns[2].AddNode(CNode(XYZ(-(X+(Xfa*0.4)), (Y/2)+(Yfa*0.4)+(Y/4), Zf4+0.01)))
Yarns[2].AddNode(CNode(XYZ(-(X+(Xfa*0.6)), (Y/2)+(Yfa*0.6)+(Y/4), Zf6+0.01)))
Yarns[2].AddNode(CNode(XYZ(-(X+(Xfa*0.8)), (Y/2)+(Yfa*0.8)+(Y/4), Zf8+0.01)))

Yarns[2].AddNode(CNode(XYZ(-(X+Xfa), (Y/2)+Yfa+(Y/4), Zf+0.01))) 

Yarns[2].AddNode(CNode(XYZ(-(X+(Xfa*1.2)), (Y/2)+(Yfa*1.2)+(Y/4), Zfa+0.02)))

Yarns[2].AddNode(CNode(XYZ(-3*X/2, 3*Y/4+(Y/4), 0))) 

Yarns[2].AddNode(CNode(XYZ(-(2*X-(Xfa*1.2)), Y-(Yfa*1.2)+(Y/4), -Zfa-0.02)))

Yarns[2].AddNode(CNode(XYZ(-(2*X-Xfa), Y-Yfa+(Y/4), -Zf-0.01))) 

Yarns[2].AddNode(CNode(XYZ(-(2*X-(Xfa*0.8)), Y-(Yfa*0.8)+(Y/4), -Zf8-0.01)))
Yarns[2].AddNode(CNode(XYZ(-(2*X-(Xfa*0.6)), Y-(Yfa*0.6)+(Y/4), -Zf6-0.01)))
Yarns[2].AddNode(CNode(XYZ(-(2*X-(Xfa*0.4)), Y-(Yfa*0.4)+(Y/4), -Zf4-0.01)))
Yarns[2].AddNode(CNode(XYZ(-(2*X-(Xfa*0.2)), Y-(Yfa*0.2)+(Y/4), -Zf2-0.01)))

Yarns[2].AddNode(CNode(XYZ(-2*X, Y+(Y/4), -Z-0.01))) 

# Create a lenticular cross section for the yarns

AxialCrossSection = CSectionEllipse(2*a, 2*b) 
BiasCrossSection = CSectionEllipse(c, d) 

#Assign the cross section to the axial yarn
Yarns[0].AssignSection(CYarnSectionConstant(AxialCrossSection)) 

# The section will be rotated at the appropriate points to avoid interference 
# So create an interpolated yarn section 
BiasYarnSection = CYarnSectionInterpPosition(True, True) 

# Calculate the angle of the bias yarns at Xf
beta = math.atan((Xmax * b**2) / (Ymax * W**2))

# Calculate the fraction at which Xf is along the bias yarns
fraction=Xf/(2*X)

# Add rotated sections along the yarn 
# at angles of +- beta

BiasYarnSection.AddSection(0, CSectionRotated(BiasCrossSection, 0)) 
BiasYarnSection.AddSection(fraction, CSectionRotated(BiasCrossSection, -beta)) 
BiasYarnSection.AddSection(0.25, CSectionRotated(BiasCrossSection, 0)) 
BiasYarnSection.AddSection(0.5-fraction, CSectionRotated(BiasCrossSection, -beta))
BiasYarnSection.AddSection(0.5, CSectionRotated(BiasCrossSection, 0)) 
BiasYarnSection.AddSection(0.5+fraction, CSectionRotated(BiasCrossSection, beta)) 
BiasYarnSection.AddSection(0.75, CSectionRotated(BiasCrossSection, 0)) 
BiasYarnSection.AddSection(1-fraction, CSectionRotated(BiasCrossSection, beta))
BiasYarnSection.AddSection(1, CSectionRotated(BiasCrossSection, 0)) 

#Assign the cross section to the positive and negative bias yarns
Yarns[1].AssignSection(BiasYarnSection) 
Yarns[2].AssignSection(BiasYarnSection) 

#Create repeates of the yarns in the x axis
Yarns[0].AddRepeat(XYZ(X, 0, 0)) 
Yarns[1].AddRepeat(XYZ(2*X, 0, 0)) 
Yarns[2].AddRepeat(XYZ(2*X, 0, 0)) 

# Create loop to run for each defined yarn
for Yarn in Yarns: 
    # Assign interpolation function 
    Yarn.AssignInterpolation(CInterpolationCubic()) 

    # Assign resolution of surface mesh
    Yarn.SetResolution(Resolution) 

    # Create repeat of the yarns in the y axis
    Yarn.AddRepeat(XYZ(0, Y/2, 0)) 

    # Add yarn to the textile
    Textile.AddYarn(Yarn) 

# Create and assign a domain
Textile.AssignDomain(CDomainPlanes(XYZ(0, 0, -2*Z), XYZ(1.5*X, 1*Y, 2*Z))) 

# Add the textile 
AddTextile("triaxialbraid_v4", Textile) 
