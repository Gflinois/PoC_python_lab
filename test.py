import stl
import matplotlib.pyplot as plt


cube = stl.read_ascii_file(open("cube.stl",'r'))

print(cube.facets[0].vertices)

def intersection_plan_solide(plan,solide,p=False):
	inter = []
	for facet in solide.facets:
		new_inter = intersection_plan_facette(plan,facet,p)
		inter.append(nex_inter)
	return inter
	
def intersection_plan_facette(plan,facette,p=False):
	inter = []
	i=0
	for vertice1 in facette.vertices:
		for vertice2 in facette.vertices:
			if vertice1!=vertice2:
				if (plan[0]*(vertice2[0]-vertice1[0])+plan[1]*(vertice2[1]-vertice1[1])+plan[2]*(vertice2[2]-vertice1[2])) :
					k=plan[3]-plan[0]*vertice1[0]-plan[1]*vertice1[1]-plan[2]*vertice1[2]/(plan[0]*(vertice2[0]-vertice1[0])+plan[1]*(vertice2[1]-vertice1[1])+plan[2]*(vertice2[2]-vertice1[2]))
					if k <=1 and k>=0:
						inter.append( [k*(vertice2[0]-vertice1[0])+vertice1[0],k*(vertice2[1]-vertice1[1])+vertice1[1],k*(vertice2[2]-vertice1[2])+vertice1[2]])
						i+=1
	
	if p:
		plot3(inter,ax,'r')
		for vertice1 in cube.facets[0].vertices:
			for vertice2 in cube.facets[0].vertices: 
				lgn = [vertice1,vertice2]
				plot3(lgn,ax)
	
	return inter



def plot3(ligne,ax=plt.axes(projection='3d'),c='k'):
	xs=ligne[0][0],ligne[1][0]
	ys=ligne[0][1],ligne[1][1]
	zs=ligne[0][2],ligne[1][2]
	ax.plot3D(xs,ys,zs,c)
	return



ax=plt.axes(projection='3d')
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)
#lgn=intersection_plan_facette([0,1,0,0.5],cube.facets[0],True)
lgn=intersection_plan_facette([0,1,0,0.5],cube.facets[0],True)

print(lgn[0])
plt.show()
