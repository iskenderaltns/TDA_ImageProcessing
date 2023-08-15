# trace generated using paraview version 5.11.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PNG Series Reader'
a1542633552ericomarcelino235177unsplashpng = PNGSeriesReader(registrationName='1542633552-erico-marcelino-235177-unsplash.png', FileNames=['C:/Users/isken/Downloads/1542633552-erico-marcelino-235177-unsplash.png'])

# set active source
SetActiveSource(a1542633552ericomarcelino235177unsplashpng)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
a1542633552ericomarcelino235177unsplashpngDisplay = Show(a1542633552ericomarcelino235177unsplashpng, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'PNGImage'
pNGImageLUT = GetColorTransferFunction('PNGImage')

# get opacity transfer function/opacity map for 'PNGImage'
pNGImagePWF = GetOpacityTransferFunction('PNGImage')

# trace defaults for the display properties.
a1542633552ericomarcelino235177unsplashpngDisplay.Representation = 'Slice'
a1542633552ericomarcelino235177unsplashpngDisplay.ColorArrayName = ['POINTS', 'PNGImage']
a1542633552ericomarcelino235177unsplashpngDisplay.LookupTable = pNGImageLUT
a1542633552ericomarcelino235177unsplashpngDisplay.SelectTCoordArray = 'None'
a1542633552ericomarcelino235177unsplashpngDisplay.SelectNormalArray = 'None'
a1542633552ericomarcelino235177unsplashpngDisplay.SelectTangentArray = 'None'
a1542633552ericomarcelino235177unsplashpngDisplay.OSPRayScaleArray = 'PNGImage'
a1542633552ericomarcelino235177unsplashpngDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a1542633552ericomarcelino235177unsplashpngDisplay.SelectOrientationVectors = 'None'
a1542633552ericomarcelino235177unsplashpngDisplay.ScaleFactor = 49.900000000000006
a1542633552ericomarcelino235177unsplashpngDisplay.SelectScaleArray = 'PNGImage'
a1542633552ericomarcelino235177unsplashpngDisplay.GlyphType = 'Arrow'
a1542633552ericomarcelino235177unsplashpngDisplay.GlyphTableIndexArray = 'PNGImage'
a1542633552ericomarcelino235177unsplashpngDisplay.GaussianRadius = 2.495
a1542633552ericomarcelino235177unsplashpngDisplay.SetScaleArray = ['POINTS', 'PNGImage']
a1542633552ericomarcelino235177unsplashpngDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a1542633552ericomarcelino235177unsplashpngDisplay.OpacityArray = ['POINTS', 'PNGImage']
a1542633552ericomarcelino235177unsplashpngDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a1542633552ericomarcelino235177unsplashpngDisplay.DataAxesGrid = 'GridAxesRepresentation'
a1542633552ericomarcelino235177unsplashpngDisplay.PolarAxes = 'PolarAxesRepresentation'
a1542633552ericomarcelino235177unsplashpngDisplay.ScalarOpacityUnitDistance = 10.91282188705295
a1542633552ericomarcelino235177unsplashpngDisplay.ScalarOpacityFunction = pNGImagePWF
a1542633552ericomarcelino235177unsplashpngDisplay.OpacityArrayName = ['POINTS', 'PNGImage']
a1542633552ericomarcelino235177unsplashpngDisplay.ColorArray2Name = ['POINTS', 'PNGImage']
a1542633552ericomarcelino235177unsplashpngDisplay.IsosurfaceValues = [127.5]
a1542633552ericomarcelino235177unsplashpngDisplay.SliceFunction = 'Plane'
a1542633552ericomarcelino235177unsplashpngDisplay.SelectInputVectors = [None, '']
a1542633552ericomarcelino235177unsplashpngDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
a1542633552ericomarcelino235177unsplashpngDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
a1542633552ericomarcelino235177unsplashpngDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
a1542633552ericomarcelino235177unsplashpngDisplay.SliceFunction.Origin = [249.5, 166.0, 0.0]

# show color bar/color legend
a1542633552ericomarcelino235177unsplashpngDisplay.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [249.5, 166.0, 1671.65]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False)

# get 2D transfer function for 'PNGImage'
pNGImageTF2D = GetTransferFunction2D('PNGImage')

# set active source
SetActiveSource(a1542633552ericomarcelino235177unsplashpng)

# show data in view
a1542633552ericomarcelino235177unsplashpngDisplay = Show(a1542633552ericomarcelino235177unsplashpng, renderView1, 'UniformGridRepresentation')

# reset view to fit data
renderView1.ResetCamera(False)

#changing interaction mode based on data extents
renderView1.CameraPosition = [249.5, 166.0, 1671.65]

# show color bar/color legend
a1542633552ericomarcelino235177unsplashpngDisplay.SetScalarBarVisibility(renderView1, True)

# create a new 'Compute Derivatives'
computeDerivatives1 = ComputeDerivatives(registrationName='ComputeDerivatives1', Input=a1542633552ericomarcelino235177unsplashpng)
computeDerivatives1.Scalars = ['POINTS', 'PNGImage']
computeDerivatives1.Vectors = [None, '1']

# Properties modified on computeDerivatives1
computeDerivatives1.Vectors = ['POINTS', '1']

# show data in view
computeDerivatives1Display = Show(computeDerivatives1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
computeDerivatives1Display.Representation = 'Slice'
computeDerivatives1Display.ColorArrayName = ['POINTS', 'PNGImage']
computeDerivatives1Display.LookupTable = pNGImageLUT
computeDerivatives1Display.SelectTCoordArray = 'None'
computeDerivatives1Display.SelectNormalArray = 'None'
computeDerivatives1Display.SelectTangentArray = 'None'
computeDerivatives1Display.OSPRayScaleArray = 'PNGImage'
computeDerivatives1Display.OSPRayScaleFunction = 'PiecewiseFunction'
computeDerivatives1Display.SelectOrientationVectors = 'ScalarGradient'
computeDerivatives1Display.ScaleFactor = 49.900000000000006
computeDerivatives1Display.SelectScaleArray = 'PNGImage'
computeDerivatives1Display.GlyphType = 'Arrow'
computeDerivatives1Display.GlyphTableIndexArray = 'PNGImage'
computeDerivatives1Display.GaussianRadius = 2.495
computeDerivatives1Display.SetScaleArray = ['POINTS', 'PNGImage']
computeDerivatives1Display.ScaleTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display.OpacityArray = ['POINTS', 'PNGImage']
computeDerivatives1Display.OpacityTransferFunction = 'PiecewiseFunction'
computeDerivatives1Display.DataAxesGrid = 'GridAxesRepresentation'
computeDerivatives1Display.PolarAxes = 'PolarAxesRepresentation'
computeDerivatives1Display.ScalarOpacityUnitDistance = 10.91282188705295
computeDerivatives1Display.ScalarOpacityFunction = pNGImagePWF
computeDerivatives1Display.OpacityArrayName = ['POINTS', 'PNGImage']
computeDerivatives1Display.ColorArray2Name = ['POINTS', 'PNGImage']
computeDerivatives1Display.IsosurfaceValues = [127.5]
computeDerivatives1Display.SliceFunction = 'Plane'
computeDerivatives1Display.SelectInputVectors = [None, '']
computeDerivatives1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
computeDerivatives1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
computeDerivatives1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
computeDerivatives1Display.SliceFunction.Origin = [249.5, 166.0, 0.0]

# hide data in view
Hide(a1542633552ericomarcelino235177unsplashpng, renderView1)

# show color bar/color legend
computeDerivatives1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=computeDerivatives1)
cellDatatoPointData1.CellDataArraytoprocess = ['ScalarGradient']

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Slice'
cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'PNGImage']
cellDatatoPointData1Display.LookupTable = pNGImageLUT
cellDatatoPointData1Display.SelectTCoordArray = 'None'
cellDatatoPointData1Display.SelectNormalArray = 'None'
cellDatatoPointData1Display.SelectTangentArray = 'None'
cellDatatoPointData1Display.OSPRayScaleArray = 'PNGImage'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'ScalarGradient'
cellDatatoPointData1Display.ScaleFactor = 49.900000000000006
cellDatatoPointData1Display.SelectScaleArray = 'PNGImage'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'PNGImage'
cellDatatoPointData1Display.GaussianRadius = 2.495
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'PNGImage']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'PNGImage']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'
cellDatatoPointData1Display.ScalarOpacityUnitDistance = 10.91282188705295
cellDatatoPointData1Display.ScalarOpacityFunction = pNGImagePWF
cellDatatoPointData1Display.OpacityArrayName = ['POINTS', 'PNGImage']
cellDatatoPointData1Display.ColorArray2Name = ['POINTS', 'PNGImage']
cellDatatoPointData1Display.IsosurfaceValues = [127.5]
cellDatatoPointData1Display.SliceFunction = 'Plane'
cellDatatoPointData1Display.SelectInputVectors = ['POINTS', 'ScalarGradient']
cellDatatoPointData1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
cellDatatoPointData1Display.SliceFunction.Origin = [249.5, 166.0, 0.0]

# hide data in view
Hide(computeDerivatives1, renderView1)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=cellDatatoPointData1)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.Function = 'mag(ScalarGradient)'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'Result'
resultLUT = GetColorTransferFunction('Result')

# get opacity transfer function/opacity map for 'Result'
resultPWF = GetOpacityTransferFunction('Result')

# trace defaults for the display properties.
calculator1Display.Representation = 'Slice'
calculator1Display.ColorArrayName = ['POINTS', 'Result']
calculator1Display.LookupTable = resultLUT
calculator1Display.SelectTCoordArray = 'None'
calculator1Display.SelectNormalArray = 'None'
calculator1Display.SelectTangentArray = 'None'
calculator1Display.OSPRayScaleArray = 'Result'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'ScalarGradient'
calculator1Display.ScaleFactor = 49.900000000000006
calculator1Display.SelectScaleArray = 'Result'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.GlyphTableIndexArray = 'Result'
calculator1Display.GaussianRadius = 2.495
calculator1Display.SetScaleArray = ['POINTS', 'Result']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Result']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 10.91282188705295
calculator1Display.ScalarOpacityFunction = resultPWF
calculator1Display.OpacityArrayName = ['POINTS', 'Result']
calculator1Display.ColorArray2Name = ['POINTS', 'Result']
calculator1Display.IsosurfaceValues = [64.96639756443327]
calculator1Display.SliceFunction = 'Plane'
calculator1Display.SelectInputVectors = ['POINTS', 'ScalarGradient']
calculator1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
calculator1Display.SliceFunction.Origin = [249.5, 166.0, 0.0]

# hide data in view
Hide(cellDatatoPointData1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get 2D transfer function for 'Result'
resultTF2D = GetTransferFunction2D('Result')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
resultLUT.ApplyPreset('X Ray', True)

# invert the transfer function
resultLUT.InvertTransferFunction()

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 90.23110961914062, 0.7119565606117249, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 90.83264923095703, 0.635869562625885, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 91.43419647216797, 0.5978261232376099, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 92.33650207519531, 0.5597826242446899, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 93.53958892822266, 0.52173912525177, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 94.14112854003906, 0.5054348111152649, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 95.94574737548828, 0.46195653080940247, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 97.1488265991211, 0.4184782803058624, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 97.1488265991211, 0.4130434989929199, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 97.75037384033203, 0.4021739065647125, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 98.65267944335938, 0.375, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 98.65267944335938, 0.3586956560611725, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 98.95345306396484, 0.3478260934352875, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 99.25421905517578, 0.31521740555763245, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=calculator1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'Result']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'Result']

# show data in view
tTKPersistenceDiagram1Display = Show(tTKPersistenceDiagram1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKPersistenceDiagram1Display.Representation = 'Surface'
tTKPersistenceDiagram1Display.ColorArrayName = [None, '']
tTKPersistenceDiagram1Display.SelectTCoordArray = 'None'
tTKPersistenceDiagram1Display.SelectNormalArray = 'None'
tTKPersistenceDiagram1Display.SelectTangentArray = 'None'
tTKPersistenceDiagram1Display.OSPRayScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.SelectOrientationVectors = 'Coordinates'
tTKPersistenceDiagram1Display.ScaleFactor = 12.993280029296876
tTKPersistenceDiagram1Display.SelectScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.GlyphType = 'Arrow'
tTKPersistenceDiagram1Display.GlyphTableIndexArray = 'Coordinates'
tTKPersistenceDiagram1Display.GaussianRadius = 0.6496640014648437
tTKPersistenceDiagram1Display.SetScaleArray = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.OpacityArray = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPersistenceDiagram1Display.PolarAxes = 'PolarAxesRepresentation'
tTKPersistenceDiagram1Display.ScalarOpacityUnitDistance = 6.046198333683019
tTKPersistenceDiagram1Display.OpacityArrayName = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.SelectInputVectors = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPersistenceDiagram1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 499.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPersistenceDiagram1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 499.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(calculator1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tTKPersistenceDiagram1Display, ('CELLS', 'Persistence'))

# rescale color and/or opacity maps used to include current data range
tTKPersistenceDiagram1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tTKPersistenceDiagram1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Persistence'
persistenceLUT = GetColorTransferFunction('Persistence')

# get opacity transfer function/opacity map for 'Persistence'
persistencePWF = GetOpacityTransferFunction('Persistence')

# get 2D transfer function for 'Persistence'
persistenceTF2D = GetTransferFunction2D('Persistence')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
persistenceLUT.ApplyPreset('Rainbow Uniform', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
persistenceLUT.ApplyPreset('Turbo', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
persistenceLUT.ApplyPreset('Cold and Hot', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
persistenceLUT.ApplyPreset('Rainbow Uniform', True)

# set active source
SetActiveSource(calculator1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=calculator1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=calculator1Display)

# set active source
SetActiveSource(tTKPersistenceDiagram1)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKPersistenceDiagram1)
threshold1.Scalars = ['POINTS', 'CriticalType']
threshold1.UpperThreshold = 3.0

# Properties modified on threshold1
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.UpperThreshold = 99999999999.0

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['CELLS', 'Persistence']
threshold1Display.LookupTable = persistenceLUT
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleArray = 'Coordinates'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'Coordinates'
threshold1Display.ScaleFactor = 12.993280029296876
threshold1Display.SelectScaleArray = 'Coordinates'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'Coordinates'
threshold1Display.GaussianRadius = 0.6496640014648437
threshold1Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'Coordinates']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = persistencePWF
threshold1Display.ScalarOpacityUnitDistance = 6.046284178161872
threshold1Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold1Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 499.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 499.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(tTKPersistenceDiagram1, renderView1)

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=threshold1)
threshold2.Scalars = ['POINTS', 'CriticalType']
threshold2.UpperThreshold = 3.0

# Properties modified on threshold2
threshold2.Scalars = ['CELLS', 'Persistence']
threshold2.LowerThreshold = 6.0
threshold2.UpperThreshold = 999999999.0

# show data in view
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['CELLS', 'Persistence']
threshold2Display.LookupTable = persistenceLUT
threshold2Display.SelectTCoordArray = 'None'
threshold2Display.SelectNormalArray = 'None'
threshold2Display.SelectTangentArray = 'None'
threshold2Display.OSPRayScaleArray = 'Coordinates'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'Coordinates'
threshold2Display.ScaleFactor = 12.993280029296876
threshold2Display.SelectScaleArray = 'Coordinates'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'Coordinates'
threshold2Display.GaussianRadius = 0.6496640014648437
threshold2Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'Coordinates']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = persistencePWF
threshold2Display.ScalarOpacityUnitDistance = 12.789655604896776
threshold2Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold2Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 499.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 499.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(threshold1, renderView1)

# show color bar/color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(registrationName='TTKTopologicalSimplification1', Domain=calculator1,
    Constraints=threshold2)
tTKTopologicalSimplification1.ScalarField = ['POINTS', 'Result']
tTKTopologicalSimplification1.InputOffsetField = ['POINTS', 'Result']
tTKTopologicalSimplification1.VertexIdentifierField = ['POINTS', 'CriticalType']

# show data in view
tTKTopologicalSimplification1Display = Show(tTKTopologicalSimplification1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKTopologicalSimplification1Display.Representation = 'Slice'
tTKTopologicalSimplification1Display.ColorArrayName = ['POINTS', 'Result']
tTKTopologicalSimplification1Display.LookupTable = resultLUT
tTKTopologicalSimplification1Display.SelectTCoordArray = 'None'
tTKTopologicalSimplification1Display.SelectNormalArray = 'None'
tTKTopologicalSimplification1Display.SelectTangentArray = 'None'
tTKTopologicalSimplification1Display.OSPRayScaleArray = 'Result'
tTKTopologicalSimplification1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.SelectOrientationVectors = 'ScalarGradient'
tTKTopologicalSimplification1Display.ScaleFactor = 49.900000000000006
tTKTopologicalSimplification1Display.SelectScaleArray = 'Result'
tTKTopologicalSimplification1Display.GlyphType = 'Arrow'
tTKTopologicalSimplification1Display.GlyphTableIndexArray = 'Result'
tTKTopologicalSimplification1Display.GaussianRadius = 2.495
tTKTopologicalSimplification1Display.SetScaleArray = ['POINTS', 'Result']
tTKTopologicalSimplification1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.OpacityArray = ['POINTS', 'Result']
tTKTopologicalSimplification1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKTopologicalSimplification1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKTopologicalSimplification1Display.PolarAxes = 'PolarAxesRepresentation'
tTKTopologicalSimplification1Display.ScalarOpacityUnitDistance = 10.91282188705295
tTKTopologicalSimplification1Display.ScalarOpacityFunction = resultPWF
tTKTopologicalSimplification1Display.OpacityArrayName = ['POINTS', 'Result']
tTKTopologicalSimplification1Display.ColorArray2Name = ['POINTS', 'Result']
tTKTopologicalSimplification1Display.IsosurfaceValues = [64.96639756443327]
tTKTopologicalSimplification1Display.SliceFunction = 'Plane'
tTKTopologicalSimplification1Display.SelectInputVectors = ['POINTS', 'ScalarGradient']
tTKTopologicalSimplification1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKTopologicalSimplification1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKTopologicalSimplification1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
tTKTopologicalSimplification1Display.SliceFunction.Origin = [249.5, 166.0, 0.0]

# hide data in view
Hide(threshold2, renderView1)

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
tTKTopologicalSimplification1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplification1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'Result']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'Result']

# show data in view
tTKMorseSmaleComplex1Display = Show(tTKMorseSmaleComplex1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display.Representation = 'Surface'
tTKMorseSmaleComplex1Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.LookupTable = cellDimensionLUT
tTKMorseSmaleComplex1Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display.ScaleFactor = 49.900000000000006
tTKMorseSmaleComplex1Display.SelectScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GaussianRadius = 2.495
tTKMorseSmaleComplex1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1Display.SelectInputVectors = [None, '']
tTKMorseSmaleComplex1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(tTKTopologicalSimplification1, renderView1)

# show color bar/color legend
tTKMorseSmaleComplex1Display.SetScalarBarVisibility(renderView1, True)

# show data in view
tTKMorseSmaleComplex1Display_1 = Show(OutputPort(tTKMorseSmaleComplex1, 1), renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'SeparatrixType'
separatrixTypeLUT = GetColorTransferFunction('SeparatrixType')

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display_1.Representation = 'Surface'
tTKMorseSmaleComplex1Display_1.ColorArrayName = ['CELLS', 'SeparatrixType']
tTKMorseSmaleComplex1Display_1.LookupTable = separatrixTypeLUT
tTKMorseSmaleComplex1Display_1.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display_1.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display_1.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display_1.OSPRayScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_1.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display_1.ScaleFactor = 49.900000000000006
tTKMorseSmaleComplex1Display_1.SelectScaleArray = 'SeparatrixType'
tTKMorseSmaleComplex1Display_1.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display_1.GlyphTableIndexArray = 'SeparatrixType'
tTKMorseSmaleComplex1Display_1.GaussianRadius = 2.495
tTKMorseSmaleComplex1Display_1.SetScaleArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_1.OpacityArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display_1.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1Display_1.SelectInputVectors = [None, '']
tTKMorseSmaleComplex1Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(tTKTopologicalSimplification1, renderView1)

# show color bar/color legend
tTKMorseSmaleComplex1Display_1.SetScalarBarVisibility(renderView1, True)

# show data in view
tTKMorseSmaleComplex1Display_2 = Show(OutputPort(tTKMorseSmaleComplex1, 2), renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display_2.Representation = 'Surface'
tTKMorseSmaleComplex1Display_2.ColorArrayName = [None, '']
tTKMorseSmaleComplex1Display_2.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display_2.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display_2.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_2.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display_2.ScaleFactor = -0.2
tTKMorseSmaleComplex1Display_2.SelectScaleArray = 'None'
tTKMorseSmaleComplex1Display_2.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display_2.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex1Display_2.GaussianRadius = -0.01
tTKMorseSmaleComplex1Display_2.SetScaleArray = [None, '']
tTKMorseSmaleComplex1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_2.OpacityArray = [None, '']
tTKMorseSmaleComplex1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_2.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display_2.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1Display_2.SelectInputVectors = [None, '']
tTKMorseSmaleComplex1Display_2.WriteLog = ''

# hide data in view
Hide(tTKTopologicalSimplification1, renderView1)

# show data in view
tTKMorseSmaleComplex1Display_3 = Show(OutputPort(tTKMorseSmaleComplex1, 3), renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display_3.Representation = 'Slice'
tTKMorseSmaleComplex1Display_3.ColorArrayName = ['POINTS', 'Result']
tTKMorseSmaleComplex1Display_3.LookupTable = resultLUT
tTKMorseSmaleComplex1Display_3.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display_3.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display_3.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display_3.OSPRayScaleArray = 'Result'
tTKMorseSmaleComplex1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_3.SelectOrientationVectors = 'ScalarGradient'
tTKMorseSmaleComplex1Display_3.ScaleFactor = 49.900000000000006
tTKMorseSmaleComplex1Display_3.SelectScaleArray = 'Result'
tTKMorseSmaleComplex1Display_3.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display_3.GlyphTableIndexArray = 'Result'
tTKMorseSmaleComplex1Display_3.GaussianRadius = 2.495
tTKMorseSmaleComplex1Display_3.SetScaleArray = ['POINTS', 'Result']
tTKMorseSmaleComplex1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_3.OpacityArray = ['POINTS', 'Result']
tTKMorseSmaleComplex1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display_3.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display_3.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1Display_3.ScalarOpacityUnitDistance = 10.91282188705295
tTKMorseSmaleComplex1Display_3.ScalarOpacityFunction = resultPWF
tTKMorseSmaleComplex1Display_3.OpacityArrayName = ['POINTS', 'Result']
tTKMorseSmaleComplex1Display_3.ColorArray2Name = ['POINTS', 'Result']
tTKMorseSmaleComplex1Display_3.IsosurfaceValues = [64.96639756443327]
tTKMorseSmaleComplex1Display_3.SliceFunction = 'Plane'
tTKMorseSmaleComplex1Display_3.SelectInputVectors = ['POINTS', 'ScalarGradient']
tTKMorseSmaleComplex1Display_3.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display_3.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display_3.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
tTKMorseSmaleComplex1Display_3.SliceFunction.Origin = [249.5, 166.0, 0.0]

# hide data in view
Hide(tTKTopologicalSimplification1, renderView1)

# show color bar/color legend
tTKMorseSmaleComplex1Display_3.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')

# get 2D transfer function for 'CellDimension'
cellDimensionTF2D = GetTransferFunction2D('CellDimension')

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# get opacity transfer function/opacity map for 'SeparatrixType'
separatrixTypePWF = GetOpacityTransferFunction('SeparatrixType')

# get 2D transfer function for 'SeparatrixType'
separatrixTypeTF2D = GetTransferFunction2D('SeparatrixType')

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=OutputPort(tTKMorseSmaleComplex1_1,1))
threshold3.Scalars = ['CELLS', 'SeparatrixType']
threshold3.UpperThreshold = 1.0

# Properties modified on threshold3
threshold3.LowerThreshold = 1.0

# show data in view
threshold3Display = Show(threshold3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = ['CELLS', 'SeparatrixType']
threshold3Display.LookupTable = separatrixTypeLUT
threshold3Display.SelectTCoordArray = 'None'
threshold3Display.SelectNormalArray = 'None'
threshold3Display.SelectTangentArray = 'None'
threshold3Display.OSPRayScaleArray = 'CellDimension'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'None'
threshold3Display.ScaleFactor = 49.900000000000006
threshold3Display.SelectScaleArray = 'SeparatrixType'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GlyphTableIndexArray = 'SeparatrixType'
threshold3Display.GaussianRadius = 2.495
threshold3Display.SetScaleArray = ['POINTS', 'CellDimension']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = ['POINTS', 'CellDimension']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityFunction = separatrixTypePWF
threshold3Display.ScalarOpacityUnitDistance = 13.197192691328018
threshold3Display.OpacityArrayName = ['CELLS', 'SeparatrixType']
threshold3Display.SelectInputVectors = [None, '']
threshold3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 1), renderView1)

# show color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=tTKMorseSmaleComplex1Display_3.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=tTKMorseSmaleComplex1Display_3)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=tTKMorseSmaleComplex1Display_3.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=tTKMorseSmaleComplex1Display_3)

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK IdentifierRandomizer'
tTKIdentifierRandomizer1 = TTKIdentifierRandomizer(registrationName='TTKIdentifierRandomizer1', Input=OutputPort(tTKMorseSmaleComplex1_2,3))
tTKIdentifierRandomizer1.ScalarField = ['POINTS', 'Result']

# Properties modified on tTKIdentifierRandomizer1
tTKIdentifierRandomizer1.RandomSeed = 3

# show data in view
tTKIdentifierRandomizer1Display = Show(tTKIdentifierRandomizer1, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKIdentifierRandomizer1Display.Representation = 'Slice'
tTKIdentifierRandomizer1Display.ColorArrayName = ['POINTS', 'Result']
tTKIdentifierRandomizer1Display.LookupTable = resultLUT
tTKIdentifierRandomizer1Display.SelectTCoordArray = 'None'
tTKIdentifierRandomizer1Display.SelectNormalArray = 'None'
tTKIdentifierRandomizer1Display.SelectTangentArray = 'None'
tTKIdentifierRandomizer1Display.OSPRayScaleArray = 'Result'
tTKIdentifierRandomizer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIdentifierRandomizer1Display.SelectOrientationVectors = 'ScalarGradient'
tTKIdentifierRandomizer1Display.ScaleFactor = 49.900000000000006
tTKIdentifierRandomizer1Display.SelectScaleArray = 'Result'
tTKIdentifierRandomizer1Display.GlyphType = 'Arrow'
tTKIdentifierRandomizer1Display.GlyphTableIndexArray = 'Result'
tTKIdentifierRandomizer1Display.GaussianRadius = 2.495
tTKIdentifierRandomizer1Display.SetScaleArray = ['POINTS', 'Result']
tTKIdentifierRandomizer1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKIdentifierRandomizer1Display.OpacityArray = ['POINTS', 'Result']
tTKIdentifierRandomizer1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKIdentifierRandomizer1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKIdentifierRandomizer1Display.PolarAxes = 'PolarAxesRepresentation'
tTKIdentifierRandomizer1Display.ScalarOpacityUnitDistance = 10.91282188705295
tTKIdentifierRandomizer1Display.ScalarOpacityFunction = resultPWF
tTKIdentifierRandomizer1Display.OpacityArrayName = ['POINTS', 'Result']
tTKIdentifierRandomizer1Display.ColorArray2Name = ['POINTS', 'Result']
tTKIdentifierRandomizer1Display.IsosurfaceValues = [64.96639756443327]
tTKIdentifierRandomizer1Display.SliceFunction = 'Plane'
tTKIdentifierRandomizer1Display.SelectInputVectors = ['POINTS', 'ScalarGradient']
tTKIdentifierRandomizer1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIdentifierRandomizer1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIdentifierRandomizer1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
tTKIdentifierRandomizer1Display.SliceFunction.Origin = [249.5, 166.0, 0.0]

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 3), renderView1)

# show color bar/color legend
tTKIdentifierRandomizer1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 2), renderView1)

# hide data in view
Hide(threshold3, renderView1)

# hide data in view
Hide(tTKMorseSmaleComplex1, renderView1)

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# show data in view
tTKMorseSmaleComplex1Display_1 = Show(OutputPort(tTKMorseSmaleComplex1, 1), renderView1, 'GeometryRepresentation')

# show color bar/color legend
tTKMorseSmaleComplex1Display_1.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 1), renderView1)

# show data in view
tTKMorseSmaleComplex1Display_1 = Show(OutputPort(tTKMorseSmaleComplex1, 1), renderView1, 'GeometryRepresentation')

# show color bar/color legend
tTKMorseSmaleComplex1Display_1.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# show data in view
tTKMorseSmaleComplex1Display = Show(tTKMorseSmaleComplex1, renderView1, 'GeometryRepresentation')

# show color bar/color legend
tTKMorseSmaleComplex1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 1), renderView1)

# set active source
SetActiveSource(threshold3)

# show data in view
threshold3Display = Show(threshold3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(threshold3, renderView1)

# show data in view
threshold3Display = Show(threshold3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(threshold3, renderView1)

# show data in view
threshold3Display = Show(threshold3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView1, True)

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
cellDimensionLUT.ApplyPreset('Linear Green (Gr4L)', True)

# invert the transfer function
cellDimensionLUT.InvertTransferFunction()

# invert the transfer function
cellDimensionLUT.InvertTransferFunction()

# invert the transfer function
cellDimensionLUT.InvertTransferFunction()

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# show data in view
tTKMorseSmaleComplex1Display_2 = Show(OutputPort(tTKMorseSmaleComplex1, 2), renderView1, 'GeometryRepresentation')

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=tTKMorseSmaleComplex1Display_3.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=tTKMorseSmaleComplex1Display_3)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=tTKMorseSmaleComplex1Display_3.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=tTKMorseSmaleComplex1Display_3)

# show data in view
tTKMorseSmaleComplex1Display_3 = Show(OutputPort(tTKMorseSmaleComplex1, 3), renderView1, 'UniformGridRepresentation')

# show color bar/color legend
tTKMorseSmaleComplex1Display_3.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 3), renderView1)

# show data in view
tTKMorseSmaleComplex1Display_3 = Show(OutputPort(tTKMorseSmaleComplex1, 3), renderView1, 'UniformGridRepresentation')

# show color bar/color legend
tTKMorseSmaleComplex1Display_3.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 3), renderView1)

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# show data in view
tTKMorseSmaleComplex1Display_1 = Show(OutputPort(tTKMorseSmaleComplex1, 1), renderView1, 'GeometryRepresentation')

# show color bar/color legend
tTKMorseSmaleComplex1Display_1.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 1), renderView1)

# show data in view
tTKMorseSmaleComplex1Display_1 = Show(OutputPort(tTKMorseSmaleComplex1, 1), renderView1, 'GeometryRepresentation')

# show color bar/color legend
tTKMorseSmaleComplex1Display_1.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 1), renderView1)

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 2), renderView1)

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# show data in view
tTKMorseSmaleComplex1Display_2 = Show(OutputPort(tTKMorseSmaleComplex1, 2), renderView1, 'GeometryRepresentation')

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 2), renderView1)

# show data in view
tTKMorseSmaleComplex1Display_2 = Show(OutputPort(tTKMorseSmaleComplex1, 2), renderView1, 'GeometryRepresentation')

# hide data in view
Hide(OutputPort(tTKMorseSmaleComplex1, 2), renderView1)

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# set active source
SetActiveSource(threshold3)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
separatrixTypeLUT.ApplyPreset('X Ray', True)

# invert the transfer function
separatrixTypeLUT.InvertTransferFunction()

# invert the transfer function
separatrixTypeLUT.InvertTransferFunction()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
separatrixTypeLUT.ApplyPreset('Cool to Warm (Extended)', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
separatrixTypeLUT.ApplyPreset('Cold and Hot', True)

# invert the transfer function
separatrixTypeLUT.InvertTransferFunction()

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
cellDimensionLUT.ApplyPreset('Turbo', True)

# invert the transfer function
cellDimensionLUT.InvertTransferFunction()

# invert the transfer function
cellDimensionLUT.InvertTransferFunction()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
cellDimensionLUT.ApplyPreset('Rainbow Uniform', True)

# invert the transfer function
cellDimensionLUT.InvertTransferFunction()

# invert the transfer function
cellDimensionLUT.InvertTransferFunction()

# set active source
SetActiveSource(tTKMorseSmaleComplex1)

# set active source
SetActiveSource(tTKIdentifierRandomizer1)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=tTKIdentifierRandomizer1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
ShowInteractiveWidgets(proxy=tTKIdentifierRandomizer1Display)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=tTKIdentifierRandomizer1Display.SliceFunction)

# toggle interactive widget visibility (only when running from the GUI)
HideInteractiveWidgets(proxy=tTKIdentifierRandomizer1Display)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
resultLUT.ApplyPreset('Black-Body Radiation', True)

# invert the transfer function
resultLUT.InvertTransferFunction()

# invert the transfer function
resultLUT.InvertTransferFunction()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
resultLUT.ApplyPreset('Rainbow Desaturated', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
resultLUT.ApplyPreset('Yellow - Gray - Blue', True)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
resultLUT.ApplyPreset('Cool to Warm (Extended)', True)

# invert the transfer function
resultLUT.InvertTransferFunction()

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
resultLUT.ApplyPreset('X Ray', True)

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 100.75807189941406, 0.32065218687057495, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 101.9611587524414, 0.3478260934352875, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 107.9765625, 0.42391306161880493, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 109.17964172363281, 0.43478262424468994, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 111.88658142089844, 0.44565218687057495, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 112.78888702392578, 0.45108696818351746, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 113.08966064453125, 0.45652174949645996, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 113.69120025634766, 0.45652174949645996, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 114.89427947998047, 0.4728260934352875, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 118.50352478027344, 0.5, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 118.50352478027344, 0.5054348111152649, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 119.10506439208984, 0.52173912525177, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 120.9096908569336, 0.5380434989929199, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 121.21045684814453, 0.554347813129425, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 121.21045684814453, 0.5652173757553101, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 122.1127700805664, 0.58152174949646, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 122.1127700805664, 0.5869565606117249, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 122.41354370117188, 0.6195652484893799, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 122.71430969238281, 0.6521739363670349, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 122.71430969238281, 0.657608687877655, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 122.71430969238281, 0.66847825050354, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 122.1127700805664, 0.7119565606117249, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 121.81200408935547, 0.717391312122345, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 121.51123046875, 0.72826087474823, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 121.51123046875, 0.7336956858634949, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 121.81200408935547, 0.739130437374115, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 123.61662292480469, 0.75, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 126.02278900146484, 0.717391312122345, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 126.02278900146484, 0.70652174949646, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 126.32355499267578, 0.695652186870575, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 126.62432861328125, 0.592391312122345, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 126.62432861328125, 0.5869565606117249, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 126.62432861328125, 0.5597826242446899, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 126.02278900146484, 0.510869562625885, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.47826087474823, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.44021740555763245, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.39673912525177, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.3586956560611725, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.32608696818351746, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.2663043439388275, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.21195653080940247, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.20108695328235626, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.15760870277881622, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.135869562625885, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.1304347813129425, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.72201538085938, 0.125, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.12047576904297, 0.125, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.12047576904297, 0.1195652186870575, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.12047576904297, 0.10326087474822998, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# Properties modified on resultPWF
resultPWF.Points = [0.0, 0.0, 0.5, 0.0, 125.12047576904297, 0.09782608598470688, 0.5, 0.0, 129.93279512886653, 1.0, 0.5, 0.0]

# invert the transfer function
resultLUT.InvertTransferFunction()

# invert the transfer function
resultLUT.InvertTransferFunction()

# invert the transfer function
resultLUT.InvertTransferFunction()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(867, 782)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [258.0888452284744, 112.88798268811094, 1671.65]
renderView1.CameraFocalPoint = [258.0888452284744, 112.88798268811094, 0.0]
renderView1.CameraParallelScale = 362.6090603184093

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).