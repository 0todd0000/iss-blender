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
</center>
<br>
<br>
<br>

After creating the geometry nodes modifier you will two nodes: an input node and an output node.

Initially the input geometry (`Group Input`) is sent directly to the output geometry (`Group Output`).



<center>
    <img src="ss/gn_workspace_new.jpg" alt="image" width="1000"/>
    <br>
    <em>A new geometry nodes modfier simply sends input geometry to output geometry.</em>
</center>
<br>
<br>
<br>



# Change view and move nodes

Use a two-finger swipe to pan your view of the Geomtery Nodes editor.

Use <kbd>CTRL</kbd> + two-finger swipe UP to zoom in.


<center>
    <img src="ss/gn_zoom_in.jpg" alt="image" width="600"/>
</center>
<br>
<br>
<br>

Use <kbd>CTRL</kbd> + two-finger swipe DOWN to zoom out.

<center>
    <img src="ss/gn_zoom_out.jpg" alt="image" width="600"/>
</center>
<br>
<br>
<br>

Just like in the 3D View, you can use the <kbd>G</kbd> key to translate nodes.

Select one of the nodes, press <kbd>G</kbd> and drag the mouse around. You will see that the nodes stay connected. Moving nodes does not affect the output geometry. Moving nodes simply allows you to keep all nodes visually organized.

<center>
    <img src="ss/gn_move.jpg" alt="image" width="600"/>
    <br>
    <em>Zoom out.</em>
</center>

<br>
<br>
<br>







# Add a transform node

From the menu in the Geometry Nodes Editor select:

```
Add.. Geometry.. Operations.. Transform Geometry
```
<br>

<center>
    <img src="ss/transform0.jpg" alt="image" width="600"/>
    <br>
    <em>The "Add" menu can be used to add a variety of nodes.</em>
</center>

<br>
<br>
<br>


Drop the Transform Geometry node between the input and output nodes.

If you drop the node close to the existing connection between the input and output nodes, Blender will automatically create connections to and from the new node.

<center>
    <img src="ss/transform1.jpg" alt="image" width="600"/>
    <br>
    <em>Connections between the input, transform and output nodes.</em>
</center>

<br>
<br>
<br>

# Adjust node values



Adjust the X value in the Transform Geometry node to a new value like 5.

Note that the selected object will transform when you change values in the Transform Geometry node.



<center>
    <img src="ss/transform2.jpg" alt="image" width="600"/>
    <br>
    <em>Changing node parameters will change the output geometry</em>
</center>

<br>
<br>
<br>
