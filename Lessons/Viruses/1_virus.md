Lesson Overview

# Create viruses geometry

This mini-tutorial demonstrates how to use Particle Systems to create a simple virus model. 



# Initialize scene

Launch Blender.

Select the cube and press <kbd>X</kbd> to delete the cube.

Verify that the cube does not appear in the Scene Collection.

<center>
    <img src="ss/vr00.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>



# Create membrane

A vrius membrane can be modeled as a sphere.

To add a UV sphere object:

```
Add.. Mesh.. UV Sphere
```



<center>
    <img src="ss/vr01.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>



WITHOUT deselecting the sphere, click the arrow on the "Add UV Sphere" dialog

<center>
    <img src="ss/vr02.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>





Set the number of Rings to 32

<center>
    <img src="ss/vr04.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Right-click on the sphere and select "Shade Smooth"

<center>
    <img src="ss/vr05.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>


Verify that the sphere is shaded smoothly in the 3D Viewport.


<center>
    <img src="ss/vr06.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>

# Create spike

A virus spike protein can be modeled as a modified cylinder.

First add a cylinder:

```
Add.. Mesh.. Cylinder
```



<center>
    <img src="ss/vr07.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>


Press the "X" on the navigation axes to change the view to the YZ plane.

Move the cylinder away from the sphere.

> [!IMPORTANT]
> Press the X-ray button.




<center>
    <img src="ss/vr09.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>
Change to Edit Mode

Select the top nodes, then press <kbd>S</kbd> and then <kbd>Y</kbd> to scale in the Y direction.

Drag the mouse to narrow the top part of the cylinder.

<center>
    <img src="ss/vr10.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>

Press <kbd>E</kbd> to extrude the top surface, then drag your mouse to produce a new layer of nodes.

Press <kbd>ENTER</kbd> to apply the extrusion.

<center>
    <img src="ss/vr11.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Repeat extrusion several times.

<center>
    <img src="ss/vr12.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Select one layer of vertices.

<center>
    <img src="ss/vr13.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Press <kbd>S</kbd> and then <kbd>Y</kbd> to scale the layer of vertices in the Y direction.

Repeat for each layer of vertices to create a spike-like shape.

<center>
    <img src="ss/vr14.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Enable proportional editing.

<center>
    <img src="ss/vr14a.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
Select to the top vertices, then press <kbd>G</kbd> and drag the mouse downward.

If proportional editing is enabled you will see a large grey circle around the selected nodes.

<center>
    <img src="ss/vr15.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>
Proportional editing will displace not only the selected vertices, but also surrounding vertices.

Drag the vertices downward until the spike looks like this:

<center>
    <img src="ss/vr15a.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Press the "Z" button on the navigation axes to change the view to the XY plane.

Verify that the top vertices are still selected.


<center>
    <img src="ss/vr16.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
Press <kbd>S</kbd> then <kbd>X</kbd> to and drag the mouse to scale in the X direction.

Press <kbd>ENTER</kbd> to apply.

<center>
    <img src="ss/vr17.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Exit Edit Mode and return to Object Mode.

<center>
    <img src="ss/vr18.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>


Right-click on the spike and select "Shade Smooth"

<center>
    <img src="ss/vr19.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>


Verify that the spike has been shaded smoothly in the 3D Viewport.

<center>
    <img src="ss/vr20.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Return to the YZ view.

<center>
    <img src="ss/vr21.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>


Enter Edit Mode.

Press <kbd>A</kbd> to select all vertices.

Verify that the spike geometry does NOT start at the Y axis (i.e., Y=0).

<center>
    <img src="ss/vr22.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Press <kbd>G</kbd> then drag the mouse up to move the spike up until it starts at Y=0

<center>
    <img src="ss/vr23.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Return to Object Mode.

Press <kbd>N</kbd> to show the side panel.

Set the X rotation to -90 so that the spike points in the +Y direction.

<center>
    <img src="ss/vr24.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>


Apply the transforms by selecting:

```
Object.. Apply.. All Transforms
```



<center>
    <img src="ss/vr25.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>


Verify that the locations and rotations are now 0, and that the scale is 1.

<center>
    <img src="ss/vr26.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>


# Create spike particle system

Select the membrane object (i.e., the sphere).

Select the Particle System panel.

Press the "+" button to create a new particle system.


<center>
    <img src="ss/vr27.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>


Change the particle system type to "Hair"


<center>
    <img src="ss/vr28.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
Adjust the particle system options:

- `Advanced` = True
- `Emission.Number` = 50
- `Rotation` = True
- `Render.RenderAs` = Object
- `Render.Object.InstanceObject` = Cylinder

<center>
    <img src="ss/vr29.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


These settings will add 50 spikes at random locations around the membrane.

However, notice that the spikes are offset from the membrane surface.

<center>
    <img src="ss/vr30.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Select the spike and enter Edit mode.

Select <kbd>A</kbd> to select all vertices.

Press <kbd>G</kbd> then <kbd>Y</kbd> and drag the spike until that it is close to the global origin (0,0,0).

<center>
    <img src="ss/vr31.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>


Verify that the spikes now start on the membrane surface.

<center>
    <img src="ss/vr32.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>


Return to Object Mode.

Select the sphere.

In the Particle Sytem panel adjust the scale until the spikes are an appropriate size.

<center>
    <img src="ss/vr33.jpg" alt="image" width="1000"/>
    <br>
    <br>
    <br>
</center>


From the main menu select `Render.. Render Image` 

<center>
    <img src="ss/vr34.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>


