import stl
import matplotlib.pyplot as plt


cube = stl.read_ascii_file(open("cube.stl",'r'))
chess = stl.read_ascii_file(open("./dataset/chess_pawn/chess_pawn_ascii.stl",'r'))
print(cube.facets[0].vertices)

def intersection_plan_solide(plan,solide,p=False):
	inter = []
	for facet in solide.facets:
		new_inter = intersection_plan_facette(plan,facet,p)
		inter.append(new_inter)
	return inter
	
def intersection_plan_facette(plan,facette,p=False):
	inter = []
	i=0
	lst = [[facette.vertices[0],facette.vertices[1]],[facette.vertices[1],facette.vertices[2]],[facette.vertices[0],facette.vertices[2]]]
	for duo in lst:
		vertice1 = duo[0]
		vertice2 = duo[1]
		i+=1
		if (plan[0]*(vertice2[0]-vertice1[0])+plan[1]*(vertice2[1]-vertice1[1])+plan[2]*(vertice2[2]-vertice1[2])) :
			#print('a')
			k = (plan[3] - plan[0] * vertice1[0] - plan[1] * vertice1[1] - plan[2] * vertice1[2]) / (plan[0] * (vertice2[0] - vertice1[0]) + plan[1] * (vertice2[1] - vertice1[1]) + plan[2] * (vertice2[2] - vertice1[2]))

			if k <=1 and k>=0:
				#print('b')
				np = [k*(vertice2[0]-vertice1[0])+vertice1[0],k*(vertice2[1]-vertice1[1])+vertice1[1],k*(vertice2[2]-vertice1[2])+vertice1[2]]
				inter.append(np)
	if p:
		#print(len(inter))
		if len(inter)==2:
			plot3(inter,ax,'r')
		elif len(inter)==1:
			ax.scatter3D(inter[0][0],inter[0][1],inter[0][2],'r')
		for duo in lst:
			vertice1 = duo[0]
			vertice2 = duo[1]
			lgn = [vertice1,vertice2]
			plot3(lgn,ax)
	
	return inter



def plot3(ligne,ax=plt.axes(projection='3d'),c='b'):
	xs=ligne[0][0],ligne[1][0]
	ys=ligne[0][1],ligne[1][1]
	zs=ligne[0][2],ligne[1][2]
	ax.plot3D(xs,ys,zs,c)
	return



ax=plt.axes(projection='3d')
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)
#lgn=intersection_plan_facette([0,0,1,0.5],cube.facets[0],True)
#lgn=intersection_plan_solide([0,0,1,0.5],cube,True)
lgn=intersection_plan_solide([1.4,3,0.3,3],chess,True)
print(lgn[0])
plt.show()
