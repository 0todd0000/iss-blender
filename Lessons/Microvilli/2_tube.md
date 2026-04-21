# Microvilli tube

This mini-tutorial explains how to create a tube from which microvilli will stem.

<br>

# Create base geometry

Create a basic cylinder mesh by selecting:

```
Add.. Mesh.. Cylinder
```




<center>
    <img src="ss/tb00.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>


WITHOUT deselecting the cylinder, click on the "Add Cylinder" dialog to expand it.

<center>
    <img src="ss/tb01.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>

Change the "Vertices" property to 64

<center>
    <img src="ss/tb02.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>

Enter Edit Mode

Type <kbd>CTRL</kbd> <kbd>R</kbd> then <kbd>20</kbd> to generate 20 loop cuts.

Press <kbd>ENTER</kbd> then <kbd>ENTER</kbd> again to apply the loop cuts.

<center>
    <img src="ss/tb03.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Verify that there are now vertices for the new loop cuts.

<center>
    <img src="ss/tb04.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>

Delete the top and bottom cylinder faces:

- Go into Edit Mode
- Ensure that face-select is enabled
- Select the top face and type <kbd>X</kbd>

<center>
    <img src="ss/tb05.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>

Select "Faces"

<center>
    <img src="ss/tb06.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

Also delete the bottom face.

Verify that the cylinder is now tube-like, with no top or bottom face.

<center>
    <img src="ss/tb07.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

# Prepare simple tube

Go into Object Mode.

Rotate the cylinder 90 deg around the X axis.

<center>
    <img src="ss/tb08.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>

Apply the rotation by selecting:

```
Object.. Apply.. Rotation
```

Verify that the XYZ rotations are now zero.


<center>
    <img src="ss/tb09.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
Go to the Modifers panel.

Select "Add Modifier"

<center>
    <img src="ss/tb10.jpg" alt="image" width="250"/>
    <br>
    <br>
    <br>
</center>

Select the array modifier:

```
Add Modifier.. Generate.. Array
```



<center>
    <img src="ss/tb11.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

Set the followinng Array modifier parameters:

- Count = 3
- Offset (X, Y, Z) = (0, 1, 0)
- Merge = True  (i.e., checked)

Verify that there is now a tube-like structure.

<center>
    <img src="ss/tb12.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>

# Create a modifier curve

Press the "Z" button on the navigation axes to enter the XY plane view.

Change the viewport shading to Wireframe.



<center>
    <img src="ss/tb13.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

Add a Bezier curve:

```
Add.. Curve.. Bezier
```



<center>
    <img src="ss/tb14.jpg" alt="image" width="600"/>
    <br>
    <br>
    <br>
</center>


Verify that the Bezier curve is selected.

<center>
    <img src="ss/tb15.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Rotate the Bezier curve -90 deg around the Z axis.

<center>
    <img src="ss/tb16.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

Go into Edit Mode.

Select the top center point.

<center>
    <img src="ss/tb17.jpg" alt="image" width="250"/>
    <br>
    <br>
    <br>
</center>


Ensure that proportional editing is disabled.

<center>
    <img src="ss/tb18.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Type <kbd>G</kbd> and drag the mouse until the select curve point is approximately in the location shown.

<center>
    <img src="ss/tb19.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>


Select the right point.

<center>
    <img src="ss/tb20.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>


Type <kbd>G</kbd> and drag the mouse until the select point is approximately in the location shown.

<center>
    <img src="ss/tb21.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

Go into Object Mode.

Ensure that the Bezier curve is selected.

Go to the Curve properties panel.

Set "Resolution Preview U" to 36.


<center>
    <img src="ss/tb22.jpg" alt="image" width="800"/>
    <br>
    <br>
    <br>
</center>
# Apply modifier curve

Set viewport shading to Solid.

Select the tube.

<center>
    <img src="ss/tb23.jpg" alt="image" width="500"/>
    <br>
    <br>
    <br>
</center>

Go back to the Modifers property panel and add a new curve modifier:

```
Add Modifier.. Deform.. Curve
```



<center>
    <img src="ss/tb24.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Set the "Curve Object" to the Bezier Curve.

<center>
    <img src="ss/tb25.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Type <kbd>G</kbd> <kbd>Y</kbd> then drag your mouse downward to drag (and deform) the tube along the curve.

<center>
    <img src="ss/tb26.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>



# Add tube imperfection

Create a new displacement modifier:

```
Add Modifier.. Deform.. Displace
```



<center>
    <img src="ss/tb27.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Press "New"

<center>
    <img src="ss/tb28.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>

Go to the texture properties panel.

Click on "Image or Movie".

<center>
    <img src="ss/tb29.jpg" alt="image" width="300"/>
    <br>
    <br>
    <br>
</center>


Select "Clouds"

<center>
    <img src="ss/tb30.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>

Set the "Size" parameter to 1.5

<center>
    <img src="ss/tb31.jpg" alt="image" width="700"/>
    <br>
    <br>
    <br>
</center>

Return to the Modifers panel.

Set the "Strength" parameter to 0.8

<center>
    <img src="ss/tb32.jpg" alt="image" width="700"/>
    <br>
    <br>
    <br>
</center>


Right-click on the tube and select "Shade Smooth"

<center>
    <img src="ss/tb33.jpg" alt="image" width="400"/>
    <br>
    <br>
    <br>
</center>