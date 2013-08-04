import math

from direct.showbase.ShowBase import ShowBase
from direct.task import Task 
from direct.interval.IntervalGlobal import *
from panda3d.core import *

class Hello(ShowBase):
	def __init__(self):
		ShowBase.__init__(self)
		
		base.setBackgroundColor(0.0, 0.0, 0.0)
		base.disableMouse()
		
		# Load a model and parent it to the renderer
		sphere = loader.loadModel("models/sphere")
		sphere.setPos(0.0, 0.0, 0.0)
		sphere.reparentTo(render)
		
		# Position and aim the camera
		base.camLens.setNearFar(1.0, 50.0)
		base.camLens.setFov(45.0)
		self.camera.setPos(0.0, 5.0, 15.0)
		self.camera.lookAt(0.0, 0.0, 0.0)
		
		# Set up an ambient light
		ambientLight = AmbientLight("ambientLight")
		ambientLight.setColor(Vec4(0.3, 0.3, 0.3, 1))
		ambientLightNP = render.attachNewNode(ambientLight)
		render.setLight(ambientLightNP)
		
		# Add a point light
		pointLight = PointLight("pointLight")
		pointLight.setColor(VBase4(1.0, 1.0, 1.0, 1))
		pointLightNodePath = render.attachNewNode(pointLight)
		pointLightNodePath.setPos(5.0, 0.0, 5.0)
		render.setLight(pointLightNodePath)
		
		# Apply a texture to the sphere
		textureStage = TextureStage("ts")
		texture = loader.loadTexture("textures/grid.png")
		sphere.setTexture(textureStage, texture)
		sphere.setTexScale(textureStage, 2.0, 2.0)
		
		# Spin the object
		def SpinTask(task): 
			x, y, z = sphere.getHpr()
			sphere.setHpr(x + 1.0, y + 1.0, z + 1.0)
			return Task.cont 
		self.taskMgr.add(SpinTask, "SpinTask")
	
hello = Hello()
hello.run()