import pygame, sys
from pygame.locals import QUIT
import matplotlib.pyplot as plt
from doctor import Medic
from virus import Virus
import random

pygame.init()
size = (width, height) = (400, 300)
SCREEN = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 26)
roond = 0
#pygame.display.set_caption('Hello World!')
success = 0
tests = 0
case_samples = 10
test_data = []
display = False
done = False

b_score = 0
d_score = 0

split_time = 500

b_num = 5
d_num = 1

bacteria = pygame.sprite.Group()
doctors = pygame.sprite.Group()


def process_data():
  x = []
  y = []
  for row in test_data:
    if row[-1] >= 75:
      x.append(row[2])
      y.append(row[0])
  fig = plt.figure()
  plt.scatter(x, y)
  plt.title("Doctors needed to prevent an outbreak\n started by 5 bacteria")
  plt.xlabel('split time (refreshes)')
  plt.ylabel('Doctors Needed')
  fig.savefig('data.png')


def init():
  for b in range(b_num):
    bacteria.add(
        Virus((random.randint(0, width), random.randint(0, height)),
              split_time))

  for d in range(d_num):
    doctors.add(Medic((random.randint(0, width), random.randint(0, height))))


def newroond():
  global roond
  doctors.empty()
  bacteria.empty()
  #roond += 1
  init()


def checkWin():
  global success
  if len(bacteria) < 1:
    success += 1
    return True
  elif len(bacteria) > b_num * split_time:
    return True
  return False


def main():
  global display, b_num, d_num, tests, success, case_samples, test_data, done, split_time
  newroond()
  # stuff
  while not done:
    if display:
      clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
          display = not display

    if checkWin():
      #end of roond
      tests += 1
      if tests >= case_samples:
        test_data.append(
            [d_num, b_num, split_time, tests, success / tests * 100])
        print(test_data[-1])
        if test_data[-1][-1] == 0:
          d_num += 2
        elif test_data[-1][-1] <= 75:
          d_num += 1
        else:
          split_time = round(split_time * 0.9)
          if split_time < 10:
            done = True
        tests = 0
        success = 0
      newroond()

    #Update!
    bacteria.update(bacteria)
    doctors.update()
    pygame.sprite.groupcollide(bacteria, doctors, True, False)

    # DRAW
    if display:
      SCREEN.fill("#eca1a6")
      bacteria.draw(SCREEN)
      doctors.draw(SCREEN)

      #vtext = font.render(f"Viruses: {len(bacteria)}", True, "black")
      #dtext = font.render(f"Doctors: {len(doctors)}", True, "black")
      #rtext = font.render(f"roond: {roond}", True, "black")

      #SCREEN.blit(vtext, (10, 10))
      #SCREEN.blit(dtext, (160, 10))
      #SCREEN.blit(rtext, (310, 10))

      # THE LAST LINE
      pygame.display.update()
  process_data()


if __name__ == "__main__":
  main()
