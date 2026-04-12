# Object Transforms

The most basic way to use geometry nodes (GN) is to transform objects.

"Transform" means: translate, rotate and scale.

<br>
<br>

# Create GN modifier 

Launch Blender and select the Geometry Nodes workspace. 

<center>
    <img src="ss/gn_workspace.jpg" alt="image" width="1000"/>
    <br>
		<br>
		<br>
</center>



Select "New" to create a new Geometry Nodes modifier:

<center>
    <img src="ss/gn_workspace_init.jpg" alt="image" width="1000"/>
    <br>
		<br>
		<br>
</center>


After creating the geometry nodes modifier you will two nodes: an input node (`Group Input`) and an output node (`Group Output`).

Initially the input geometry is sent directly to the output geometry.

<center>
    <img src="ss/gn_workspace_new.jpg" alt="image" width="1000"/>
    <br>
		<br>
		<br>
</center>



# Change view and move nodes

Use a two-finger swipe to pan your view of the Geomtery Nodes editor.

Zoom in:  <kbd>CTRL</kbd> + two-finger swipe UP


<center>
    <img src="ss/gn_zoom_in.jpg" alt="image" width="600"/>
    <br>
		<br>
		<br>
</center>

Zoom out:   <kbd>CTRL</kbd> + two-finger swipe DOWN

<center>
    <img src="ss/gn_zoom_out.jpg" alt="image" width="600"/>
    <br>
		<br>
		<br>
</center>

Just like in the 3D Viewport, the <kbd>G</kbd> key can be used to translate nodes.

Select one of the nodes, press <kbd>G</kbd> and drag the mouse around. You will see that the nodes stay connected. 

Moving nodes does not affect the output geometry. 

Moving nodes allows you to keep the nodes visually organized.

<center>
    <img src="ss/gn_move.jpg" alt="image" width="300"/>
    <br>
    <br>
		<br>
</center>





# Add a transform node

The "Add" menu in the Geometry Nodes Editor can be used to add a variety of geometry nodes.

Add a `Transform Geometry` node by selecting:

```
Add.. Geometry.. Operations.. Transform Geometry
```
<br>

<center>
    <img src="ss/transform0.jpg" alt="image" width="600"/>
    <br>
    <br>
		<br>
</center>



Drop the `Transform Geometry` node between the input and output nodes.

If you drop the node close to the existing connection between the input and output nodes, Blender will automatically create connections to and from the new node.

<center>
    <img src="ss/transform1.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</em>
</center>



# Adjust node values



Adjust the X value in the `Transform Geometry` node to a new value like 5.

Note that the selected object transforms when you change `Transform Geometry` parameters.

Changing node parameters generally changes the output geometry

<center>
    <img src="ss/transform2.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>
