import pygame

from utils.config import images
from utils.sheet_reader import get_sheet_images


class ParticleGroup(pygame.sprite.Group):
    def draw(self, screen):
        for particle in self.sprites():
            particle.draw(screen)


class Particle(pygame.sprite.Sprite):
    images = {}

    def __init__(self, particle, position):
        self.image = pygame.Surface((10, 10), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=position)

        self.__particle = particle

        self.__animation_frame = 0
        self.__animation_interval = images["particles"][particle]["animation_interval"]
        self.__last_frame = 0

        super().__init__()

    def __getstate__(self):
        state = self.__dict__.copy()
        state["_Particle__g"] = {}
        state["image"] = None
        return state

    @staticmethod
    def load_assets():
        Particle.load_particle_assets("explosion")

    @staticmethod
    def load_particle_assets(particle):
        Particle.images[particle] = []

        particle_sheet = get_sheet_images(
            images["particles"][particle]["sheet"][0], images["particles"][particle]["sheet"][1])

        for tile in particle_sheet:
            particle_tile = pygame.transform.scale_by(
                tile, images["particles"][particle]["sheet"][2])
            Particle.images[particle].append(particle_tile)

    @staticmethod
    def render(particle, frame):
        return Particle.images[particle][frame].copy()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        time_now = pygame.time.get_ticks()

        if self.__animation_frame >= len(Particle.images[self.__particle]):
            self.kill()
            return

        if time_now-self.__last_frame < self.__animation_interval:
            return

        self.image = Particle.render(self.__particle, self.__animation_frame)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.__animation_frame += 1
        self.__last_frame = time_now
