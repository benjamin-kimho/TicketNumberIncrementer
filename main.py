import os

import cv2

sample_path = "./sample.png"
save_to_dir = "./results"

font = cv2.FONT_HERSHEY_SIMPLEX

sample = cv2.imread(sample_path)
img_height = sample.shape[0]
img_width = sample.shape[1]

counter = 1

while counter <= 100:
    img = sample.copy()
    print(f'printing ticket number {counter}')
    cv2.putText(img, str(counter).rjust(3, '0'), (10, 60), font, 1.75, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(img, str(counter).rjust(3, '0'), (img_width - 450, 60), font, 1.75, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.imwrite(os.path.join(save_to_dir, f"ticket_{counter}.png"), img)
    counter += 1
