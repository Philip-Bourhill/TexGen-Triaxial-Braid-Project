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

# Define initial parameters of the yarns
x=4;
theta=math.radians(45);
z=0.5;
Width=2

# Calculate the distance y
y=2*x/math.tan(theta);

# Define the resolution for the surface mesh
Resolution=20;

# Define nodes for the axial yarn
Yarns[0].AddNode(CNode(XYZ(0, 0, 0))) 
Yarns[0].AddNode(CNode(XYZ(0, y, 0))) 

# Define nodes for the positive bias yarn
Yarns[1].AddNode(CNode(XYZ(0, 0, z))) 
Yarns[1].AddNode(CNode(XYZ(x/2, y/4, 0))) 
Yarns[1].AddNode(CNode(XYZ(x, y/2, -z))) 
Yarns[1].AddNode(CNode(XYZ(3*x/2, 3*y/4, 0))) 
Yarns[1].AddNode(CNode(XYZ(2*x, y, z))) 

# Define nodes for the negative bias yarn
Yarns[2].AddNode(CNode(XYZ(0, 0-y/4, -z))) 
Yarns[2].AddNode(CNode(XYZ(-x/2, y/4-y/4, 0))) 
Yarns[2].AddNode(CNode(XYZ(-x, y/2-y/4, z))) 
Yarns[2].AddNode(CNode(XYZ(-3*x/2, 3*y/4-y/4, 0))) 
Yarns[2].AddNode(CNode(XYZ(-2*x, y-y/4, -z))) 

# Create a lenticular cross section for the yarns
CrossSection = CSectionEllipse(Width, z) 

#Assign the cross section to the axial yarn
Yarns[0].AssignSection(CYarnSectionConstant(CrossSection)) 

#Define the cross sections at each node of the positive and negative bias yarns
BiasYarnSection = CYarnSectionInterpPosition(True, True) 
BiasYarnSection.AddSection(0, CSectionRotated(CrossSection, 0)) 
BiasYarnSection.AddSection(1/4, CSectionRotated(CrossSection, 0)) 
BiasYarnSection.AddSection(1/2, CSectionRotated(CrossSection, 0)) 
BiasYarnSection.AddSection(3/4, CSectionRotated(CrossSection, 0)) 

#Create repeates of the yarns in the x axis
Yarns[0].AddRepeat(XYZ(x, 0, 0)) 
Yarns[1].AddRepeat(XYZ(2*x, 0, 0)) 
Yarns[2].AddRepeat(XYZ(2*x, 0, 0)) 

# Create loop to run for each defined yarn
for Yarn in Yarns: 
    # Assign interpolation function 
    Yarn.AssignInterpolation(CInterpolationCubic()) 

    # Assign resolution of surface mesh
    Yarn.SetResolution(Resolution) 

    # Create repeat of the yarns in the y axis
    Yarn.AddRepeat(XYZ(0, 0.5*y, 0)) 

    # Add yarn to the textile
    Textile.AddYarn(Yarn) 

# Create and assign a domain
Textile.AssignDomain(CDomainPlanes(XYZ(0, 0, -2*z), XYZ(1.5*x, 1*y, 2*z))) 

# Add the textile 
AddTextile("triaxialbraid_v2", Textile) 
