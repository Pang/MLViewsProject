# MLViewsProject

To report what impact a video title, tags and category have on the views of a video when trending. (A thanks to Kaggle.com for the dataset)
Rows: 40949

### Test 1
For my first test, I have only used the video title as the feature to predict the views. This was with a test_size of 0.2 and a multinomial classifier.
I was let down to see a 0.0007326007326007326% accuracy when predicting but feel this may be improved with a regressional approach.

### Test 2
Used a Support Vector Regression (SVR) algo this time and got -0.058562924377011605% accuracy :(

### Test 3
Linear regression: -17.792931238184103%

### Test 4
Changed the features, tested predictions of how many views a video has from likes/dislikes and the score was 0.7290173774892932%. Not amazing but an improvement.
When looking at these predictions side by side (heres the first 3) it doesnt look too far!
| Prediction  | Actual   |
| :---------: | :------: | 
| 1424143     | 1675844  |
| 21919310    | 21344664 | 
| 1922427     | 1138884  |

### Test 5
Implementing an ANN gave confusing results as sometimes it did better and sometimes worse, I think overall better but since Keras doesn't have a metrics API I will have to dive into this a bit more
| Prediction  | Actual   |
| :---------: | :------: | 
| 1083568     | 1675844  |
| 21749090    | 21344664 |
| 1587554     | 1138884  |
