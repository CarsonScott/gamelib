from gamelib import *

class Particle(Mover):
	def __init__(self, mass, radius, position=P2Vector()):
		super().__init__(image=generate_agent_image(body_radius=radius, head_radius=1), position=position)
		self.radius=radius
		self.mass=mass

	def compute(self, particles, gravity, dt):
		Pi=self.position
		mi=self.mass
		ri=self.radius
		Vi=self.velocity
		Mi=Vi*mi
		for j in range(len(particles)):
			Pj=particles[j].position
			mj=particles[j].mass
			rj=particles[j].radius
			Vj=particles[j].velocity
			Mj=Vj*mj
			d=compute_distance(Pi,Pj)
			a=compute_angle(Pi,Pj)
			f=gravity*mj/d
			self.apply_force(f, a, dt)
			# if d <= ri+rj:
			# 	# dx,dy=(Mi-Mj)/mi
			# 	# f=compute_norm([dx,dy])
			# 	# a=math.atan2(dy,dx)
			# 	# f=math.sqrt(pow(dy,2)+pow(dx,2))
			# 	# self.apply_force(f, a, dt)

				# ai=self.movement_angle()
				# di=self.movement_distance()
				# aj=particles[j].movement_angle()
				# dj=particles[j].movement_distance()
		self.angle=math.atan2(self.acceleration.y, self.acceleration.x)

class ParticleGame(Game):
	def initialize(self, particle_count, gravity=1):
		self.dt=0.1
		self.particles=[]
		self.gravity=gravity
		for i in range(particle_count):
			particle=Particle(mass=10, radius=10, position=random_position(self.screen_size))
			self.particles.append(particle)

	def update(self):
		for i in range(len(self.particles)):
			for j in range(i, len(self.particles)):
				if i!=j:
					p1=self.particles[i].position
					p2=self.particles[j].position
					m1=self.particles[i].mass
					m2=self.particles[j].mass
					r1=self.particles[i].radius
					r2=self.particles[j].radius
					v1=P2Vector(self.particles[i].velocity)
					v2=P2Vector(self.particles[j].velocity)
					d=compute_distance(p1,p2)
					if d <= r1+r2:
						nv1=v1*((m1-m2)/(m1+m2)) + v2*((2*m2)/(m1+m2))
						nv2=v1*((2*m1)/(m1+m2)) + v2*((m2-m1)/(m1+m2))
						self.particles[i].velocity=nv1
						self.particles[j].velocity=nv2
						self.particles[i].position=p1+nv1*self.dt
						self.particles[j].position=p2+nv2*self.dt
		for i in range(len(self.particles)):
			particles=list(self.particles)
			del particles[i]
			self.particles[i].compute(particles, self.gravity, self.dt)
		for i in range(len(self.particles)):
			self.particles[i].update(self.dt)


	def draw(self):
		for i in range(len(self.particles)):
			self.particles[i].draw(self.camera)

SCREENSIZE = P2Vector(640, 480)

game = ParticleGame(SCREENSIZE)
game.initialize(10, 1)
game.run()