import pages 

size = (700, 750)
page = pages.Pages(size, "Chess Game", 60, (255, 255, 255))

def main():
    page.localMultyplayer()

if __name__ == '__main__':
    main()