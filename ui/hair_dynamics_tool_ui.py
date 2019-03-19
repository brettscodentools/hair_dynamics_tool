#the window UI for the Hair Dynamics Toll

import maya.cmds as cmds

#close window if it already exists
if cmds.window(window, exists=True):
    cmds.deleteUI(window)
else:
    pass

#------------------------------- UI Elements ---------------------------------

window = cmds.window(title = "Dynamic hair maker", widthHeight = (370,535))
#swapped to a column layout because its mostly going down in one column, and saves a lot of useless text noted that would just be blank and a waste
boss = cmds.columnLayout( columnAttach=('both', 5), rowSpacing = 10 , columnWidth= 365, cal = 'center')
cmds.text(label="STEPS:")
cmds.text(label="1. First select your parent joint or ctl for the hair")
cmds.text(label="2. Then add intended joint's for dynamic hair to selection")
cmds.text(label="3.a. Finally, adjust settings for hair dynamic, or select a preset layout")
cmds.text(label="3.b. OR you could chose to make a balloon")
#this is a usefull little son of a bitch
cmds.separator(h=10)
cmds.text(label="DYNAMIC HAIR SETTINGS:")
#here im swapping up the layout to put the preset buttons side by side and sort of smaller, well see how this goes
cmds.rowColumnLayout(numberOfRows = 1, p=boss, )
cmds.button(label='short hair preset', width = 182)
cmds.button(label='long hair preset', width = 182)
#this escapes the above layout for the next column layout
cmds.setParent('..')

#starting the slider layout to scroll through the settings comprised of frame layouts to be collapsed or expanded
scrollSection = cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=16, height = 250)
cmds.frameLayout( label='Settings', cll =True, po =True, width = 325 )
cmds.columnLayout( columnAttach=('both', 5), rowSpacing = 1 , columnWidth= 325)
cmds.frameLayout( label='collisions', cll =True, po =True, width = 325 )
frictionVar = cmds.floatSliderGrp( label='Friction', cw3=(50,50,50), field=True, minValue=-10.0, maxValue=10.0, fieldMinValue=-10.00, fieldMaxValue=10.0, value=0 )
cmds.setParent('..')

#the resistance and dynamic frame layout with its settings
cmds.frameLayout( label='Resistances and Dynamic Properties', cll =True, po =True, width = 350 )
stretchResistVar = cmds.floatSliderGrp( label='Stretch Resist', cw3=(100,50,50), field=True, minValue=-600.00, maxValue=600.00, fieldMinValue=-600.00, fieldMaxValue=600.00, value=0 )
compressionResistVar = cmds.floatSliderGrp( label='Compression Resist', cw3=(100,50,50), field=True, minValue=-600.00, maxValue=600, fieldMinValue=-600.00, fieldMaxValue=600.00, value=0 )
bendResistVar = cmds.floatSliderGrp( label='Bend Resist', cw3=(100,50,50), field=True, minValue=-600.00, maxValue=600.00, fieldMinValue=-600.00, fieldMaxValue=600.00, value=0 )
twistResistVar = cmds.floatSliderGrp( label='Twist Resist', cw3=(100,50,50), field=True, minValue=-600.00, maxValue=600.00, fieldMinValue=-600.00, fieldMaxValue=600.00, value=0 )
extraBendLinksVar = cmds.floatSliderGrp( label='Extra Bend Links', cw3=(100,50,50), field=True, minValue=-10.00, maxValue=10.00, fieldMinValue=-10, fieldMaxValue=10.00, value=0 )
cmds.setParent('..')

#the stiffness scale frame layout with its settings and graph
cmds.frameLayout( label='Stiffness Scale', cll =True, po =True, width = 350)
#going to need layouts on these graphed frame layouts
stiffnessForm = cmds.formLayout(numberOfDivisions=50)
stiffColumn= cmds.columnLayout( columnAttach=('both', 5), rowSpacing = 1 , columnWidth= 175, cal = 'left')
#adding the float fields and drop down blend mode
stiffnessPosVar = cmds.floatFieldGrp( numberOfFields = 1, label='Selected Position', value1 = 0.0, columnWidth = ([1, 100], [2, 50]))
sitffnessValVar = cmds.floatFieldGrp( numberOfFields = 1, label='Selected value', value1 = 0.0, columnWidth = ([1, 100], [2, 50]))
stiffInterp = cmds.optionMenu( label='Interpolation', w = 75)
cmds.menuItem( label='None' )
cmds.menuItem( label='Linear')
cmds.menuItem( label='Smooth' )
cmds.menuItem( label='Spline' )
cmds.setParent('..')
#this line makes the graphed gradient ui peice
stiffnessGradient = cmds.gradientControl( at=('hairSystemShape1' + '.stiffnessScale'), )
cmds.formLayout(stiffnessForm, edit=True, attachForm = [(stiffColumn, 'left', 5)], attachControl = [stiffnessGradient, 'left', 5, stiffColumn ])
cmds.setParent('..')
cmds.setParent('..')


#the start curve atrract frame layout with its settings and graph
cmds.frameLayout( label='Start Curve Attract', cll =True, po =True, width = 350 )
startCurveAttractVar = cmds.floatSliderGrp( label='Start Curve Attract', cw3=(100,50,50), field=True, minValue=-0, maxValue=1.00, fieldMinValue=-0, fieldMaxValue=1.00, value=0 )
attractDampVar = cmds.floatSliderGrp( label='Attraction Damp', cw3=(100,50,50), field=True, minValue=-0, maxValue=1.00, fieldMinValue=-0, fieldMaxValue=1.00, value=0 )
cmds.setParent('..')


#the attraction scale frame layout with its settings and graph
cmds.frameLayout( label='Attraction Scale', cll =True, po =True, width = 350)
attractForm = cmds.formLayout(numberOfDivisions=50)
attractColumn = cmds.columnLayout( columnAttach=('both', 5), rowSpacing = 1 , columnWidth= 175, cal = 'left')
#adding the float fields and drop down blend mode
attractPosVar = cmds.floatFieldGrp( numberOfFields = 1, label='Selected Position', value1 = 0.0, columnWidth = ([1, 100], [2, 50]))
attractValVar = cmds.floatFieldGrp( numberOfFields = 1, label='Selected value', value1 = 0.0, columnWidth = ([1, 100], [2, 50]))
attractInterp = cmds.optionMenu( label='Interpolation', w = 75)
cmds.menuItem( label='None' )
cmds.menuItem( label='Linear' )
cmds.menuItem( label='Smooth' )
cmds.menuItem( label='Spline' )
cmds.setParent('..')
#this line makes the graphed gradient ui peice
attractGradient = cmds.gradientControl( at=('hairSystemShape1' + '.attractionScale') )
cmds.formLayout(attractForm, edit=True, attachForm = [(attractColumn, 'left', 5)], attachControl = [attractGradient, 'left', 5, attractColumn])
cmds.setParent('..')
cmds.setParent('..')


#the forces frame layout with its settings and graph
cmds.frameLayout( label='Forces', cll =True, po =True, width = 350 )
cmds.columnLayout( columnAttach=('both', 5), rowSpacing = 1 , columnWidth= 325)
massVar = cmds.floatSliderGrp( label='Mass', cw3=(100,50,50), field=True, minValue=-0, maxValue=10.00, fieldMinValue=-0, fieldMaxValue=10.00, value=0 )
dragVar = cmds.floatSliderGrp( label='Drag', cw3=(100,50,50), field=True, minValue=-0, maxValue=1.00, fieldMinValue=-0, fieldMaxValue=1.00, value=0 )
tangDragVar = cmds.floatSliderGrp( label='Tangential Drag', cw3=(100,50,50), field=True, minValue=-0, maxValue=1.00, fieldMinValue=-0, fieldMaxValue=1.00, value=0 )
motionDragVar = cmds.floatSliderGrp( label='Motion Drag', cw3=(100,50,50), field=True, minValue=-0, maxValue=1.00, fieldMinValue=-0, fieldMaxValue=1.00, value=0 )
dampVar = cmds.floatSliderGrp( label='Damp', cw3=(100,50,50), field=True, minValue=-0, maxValue=10.00, fieldMinValue=-0, fieldMaxValue=10.00, value=0 )
stretchDampVar = cmds.floatSliderGrp( label='Stretch Damp', cw3=(100,50,50), field=True, minValue=-0, maxValue=10.00, fieldMinValue=-0, fieldMaxValue=10.00, value=0 )
dynamWeightVar = cmds.floatSliderGrp( label='Dynamics Weight', cw3=(100,50,50), field=True, minValue=-0, maxValue=1.00, fieldMinValue=-0, fieldMaxValue=1.00, value=0 )
cmds.setParent('..')





cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')
cmds.setParent('..')
cmds.separator(h=10)
cmds.button(label = 'makeBalloon')
cmds.button(label = 'makeHair')



cmds.showWindow(window)

#---------------------- Commented out work for later progress ----------------------

#def updateFloats( dragControl, x, y, modifiers ):
    


#Settings for the dynamic hair that need to change to what
# so do all the resistances as fields for sure with extra bend links



#under hair system shape
#FOR SHORT

#FRICTION SET TO .800
#setAttr "L_hair_hairSystemShape1.friction" 0.8;

#bend and twitst resistance borth set to 15
#setAttr "L_hair_hairSystemShape1.bendResistance" 15;
#setAttr "L_hair_hairSystemShape1.twistResistance" 15;

# stiffness to .750
#setAttr "L_hair_hairSystemShape1.stiffnessScale[0].stiffnessScale_FloatValue" 0.75;

#damp and stretch damp to .500
#setAttr "L_hair_hairSystemShape1.damp" 0.5;
#setAttr "L_hair_hairSystemShape1.stretchDamp" 0.5;


#FOR LONG HAIR

#1
#FRICTION TO .5 (the DEFAULT)
#
#stretch and compression resistance to 300
#setAttr "L_hair_hairSystemShape1.stretchResistance" 300;
#setAttr "L_hair_hairSystemShape1.compressionResistance" 300;

# bend resistance to 200
#twist resistance to 500
# extra bend links to 2



#stiffness and attration graphed values:
#setAttr "L_hair_hairSystemShape1.stiffnessScale[0].stiffnessScale_FloatValue" 0.52;
#setAttr |L_hair_dynamic_group|L_hair_hairSystem1|L_hair_hairSystemShape1.stiffnessScale[1].stiffnessScale_FloatValue 0.1;
#setAttr |L_hair_dynamic_group|L_hair_hairSystem1|L_hair_hairSystemShape1.stiffnessScale[1].stiffnessScale_Position 0.226;
#setAttr |L_hair_dynamic_group|L_hair_hairSystem1|L_hair_hairSystemShape1.stiffnessScale[1].stiffnessScale_Interp 0;
#setAttr "L_hair_hairSystemShape1.stiffnessScale[2].stiffnessScale_Position" 1;
#setAttr "L_hair_hairSystemShape1.stiffnessScale[2].stiffnessScale_FloatValue" 0;    
#also set both to smooth interpolation

#drag, mass, and tang drag to 0
#setAttr "L_hair_hairSystemShape1.drag" 0;
#setAttr "L_hair_hairSystemShape1.mass" 0;
#setAttr "L_hair_hairSystemShape1.tangentialDrag" 0;

#motion drag to 1
#setAttr "L_hair_hairSystemShape1.motionDrag" 1;
#DAMP to 5.330
#setAttr "L_hair_hairSystemShape1.damp" 5.33;

#stretch damp to .5
#setAttr "L_hair_hairSystemShape1.stretchDamp" 0.5;