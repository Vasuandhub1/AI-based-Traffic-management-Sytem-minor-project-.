import multiprocessing as mu
from ultralytics import YOLO
import detection0 as d


if __name__=="__main__":
    p1=mu.Process(target=d.pretrainde)
    p2=mu.Process(target=d.emergency)
    p3=mu.Process(target=d.accident)

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()