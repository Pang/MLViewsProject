# MLViewsProject

To report what impact a video title, tags and category have on the views of a video when trending. (A thanks to Kaggle.com for the dataset)

Columns I have removed from the original file that I thought may not have an affect on views are:
- video_id
- comments_disabled
- ratings_disabled
- video_error_or_removed
- likes
- dislikes
- comment_count
- publish_time
- trending_date
- channel_title (since channels could bias the data, also confusing the model when making a prediction on unknown channels)
- thumbnail_link (This could probably be a seperate ML algorithm in itself)
