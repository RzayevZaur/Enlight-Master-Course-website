document.addEventListener('DOMContentLoaded', function() {
    {% for i in course_video_views %}
      var video{{ forloop.counter }} = document.getElementById("video{{ forloop.counter }}");
      var desiredTime{{ forloop.counter }} = {{ i.desired_time }};
  
      video{{ forloop.counter }}.addEventListener('loadedmetadata', function() {
        video{{ forloop.counter }}.currentTime = desiredTime{{ forloop.counter }};
      });
    {% endfor %}
  });
  
  function setVideoStartTime(videoId, startTime) {
    var video = document.getElementById(videoId);
    video.addEventListener('loadedmetadata', function() {
      video.currentTime = startTime;
    });
  }
  