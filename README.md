# TDA_ImageProcessing
 Image processing with ParaView
**Pipeline description**:
This example processes a grayscale image  to generate a segmentation. We will construct the segmentation from the image gradient.

First, the image is loaded from disk. 
The gradient is computed with ParaView's ComputeDerivatives or Gradient filters. 
Since TTK only works on scalar field, a Calculator is used to compute the gradient magnitude.
From the gradient magnitude, a simplification step involving PersistenceDiagram and TopologicalSimplification helps removing the noise in the gradient.
To segment the image, we use the MorseSmaleComplex filter. 
Since in the input image the objects correspond to low values in the gradient and their edges to high values, we are interested in the DescendingManifold scalar field of the Segmentation output, whose cells represent regions of low scalar field values.
The IdentifierRandomizer filter is eventually used in order to color neighbor cells with a distinct color.

### **Input**
<div>
  <img src="https://github.com/iskenderaltns/Ty_WebScraping/assets/86206193/4e43390a-228a-433d-95a5-dbd732f320eb.png" alt="Resim 1" width="40%" height="60%" />
</div>

### **Outputs**
<div>
  <img src="https://github.com/iskenderaltns/Ty_WebScraping/assets/86206193/a8292a37-3616-4fd0-8929-8a4ee0330ccc.png" alt="Resim 2" width="40%" height="60%" />
</div>
<div>
  <img src="https://github.com/iskenderaltns/Ty_WebScraping/assets/86206193/adf84aa9-dc80-459f-9c50-2748029f26c3.png" alt="Resim 3" width="40%" height="60%" />
</div>
