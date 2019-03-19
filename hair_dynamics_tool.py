#hair Dynamics tool
import maya.cmds as cmds
import maya.mel as mel

#-------------USER INSTRUCTIONS--------------------------

# HOW THIS IS GOING TO WORK FOR FUTURE REFERENCE

# The User will select the joints for the intended dynamic starting from the..
# .. !JOINT TO BE THE HAIR PARENT CONSTRAINT! secondly the BASE and selecting..
# .. all the way down to the END

#-------------USER INSTRUCTIONS--------------------------

#How the scripts works
#Then Take the array of joints and run them through a loop to get their x form coordinates
#Create the Starting Curve (NOT TO KEEP) curve from the list of coordinates from the joints
#	most likely rebuild the curve to some degree to get the proper build and insert extra Curve points as needed
#
#Create Dynamic hair from the curve created (TO KEEP), Delete the Starting Curve (PS: might have to use a mel eval to run make curve dynamic.. seems theres no python equivelent])
#Maybe have a pop up window consisting of the more important Attributes for setting up the hair
#	have the values start at a point I prefer to have as a default
#Set the Dynamic Hair Curve's point lock attribute from BOTH ENDS to BASE
#
#Create an IK Spline Handle, Select first the Base joint and then to the Dynamic Curve during Creation. Or insert them into a function w/e is called for
# LASTLY clean up the created assets from the dynamic and put them into a group
#
#make a joint array from selection
joints = cmds.ls(sl=True)
#real quickly lets get this out of the way and store the parent of the joint chain we selected so that i can be our parent constrain for the hair later
pConstrainor = cmds.listRelatives( joints[0], p = True )
print(pConstrainor)
#make the edit point array for creating the curve later
eP = []
#store a name for the starting curve based on the base selection for the hair dynamic
cName = str(joints[0])
cName = cName.replace('_1', '_sCurve')

#append the xform cordinates to an array  
for j in joints:
	jPos = cmds.xform( j, q = 1, ws = 1, t = 1)
	eP.append(jPos)
	
#Create the Curve
sC = cmds.curve( ep = eP, d=3,)
#rename the starter curve
cmds.rename(sC, cName)



#were going to use some of that funky mel magic for the making the curve dynamic, and use the eval node
#well do a classic clear select, and then select the dynamic and call the most basic version of the mel command
cmds.select(cl=1)
cmds.select(cName)
mel.eval('makeCurvesDynamic 2 { "1", "0", "1", "1", "0"};')
cmds.select(cl=1)
cmds.setAttr("follicle1.pointLock", 1)


#set the point lock for the follicle
#setAttr "follicleShape1.pointLock" 1;


#Group up the outputs from making the curve dynamic
#but quickly lets store the future names real quick
gName = str(cName.replace('_sCurve', '_dynamic_group'))
dName = str(cName.replace('_sCurve', '_dynamic_curve'))
ikName = str(joints[0])
ikName = (ikName + '_ik_handle')
pFix = str(cName.replace('_sCurve','_ad'))
print(gName)
cmds.select(cl=1)
#store array to rename in a second

folGrp = []
rGNames = ['hairSystem1', 'nucleus1', 'hairSystem1Follicles', 'hairSystem1OutputCurves']
rName = ['hairSystem1', 'nucleus1','follicle1', 'hairSystem1Follicles', 'curve1', 'hairSystem1OutputCurves']
cmds.select('hairSystem1', 'nucleus1', 'hairSystem1Follicles', 'hairSystem1OutputCurves')
cmds.Group()
cmds.select(cl=1)
#rename group and new Dynamic Curve
cmds.rename('group1', gName)
cmds.rename('curve1', dName)

#add prefix to names... AS well as check if its the hair follicle group so we can store that new name away for parenting to the head
for n in rName:
    if n == 'hairSystem1Follicles':
        newName = pFix.replace('_ad', ('_' + n))
        cmds.rename(n, newName)
        print('Changed hair follicle system name')
        folGrp.append(newName)
    if n == dName:
        cmds.rename(n, dName)
    else:   
        newName = pFix.replace('_ad', ('_' + n))
        print('trying to change ' + n)
        print(newName)
        if cmds.objExists(n):
            cmds.rename(n, newName)
        else:
            pass
    
    
#delete the group with the old hair curve
cmds.select (cl=1)

#Create the IK Spline with the array
print(ikName)
ikJ = str(joints[0])
ikL= len(joints)
ikE = str(joints[ikL - 1])
print(ikJ)


#CREATING THE IK SPLINE
#putting the selections for a manual create loop
ikA= [ikJ, ikE, dName]
#make selections from array, replace selection if its the first item in the array going through so it should be the first thing it does THEN adds items from the array
for i in ikA:
    if ikA[0] == i:
        cmds.select(i, r=True)
    else:
        cmds.select(i, add=True)

#these are the flags when you make it only snap curve to root        
cmds.ikHandle( n = ikName, ccv = False, roc = False, pcv = False, snc = True, sol = 'ikSplineSolver')
cmds.select(cl=1)

cmds.select(cl=1)
cmds.select(ikName)
cmds.parent(ikName, gName)

#lastly add the follicle group to the parent joint so that it follows
cmds.parent(folGrp, pConstrainor)



#Finished