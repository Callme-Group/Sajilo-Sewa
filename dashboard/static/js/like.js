

    var fa_heart = document.querySelectorAll('.like-btn')
    var like_count = document.querySelectorAll('.like-count')
    //  unique id is set for all the like
    for (var i = 0; i < like_count.length; i++) {
           like_count[i].id = `like-count${i}`


    }
    // for each like button a ajax call is made
    fa_heart.forEach((item, index, arr) => {
        
        arr[index].addEventListener('click', (e) => {
            let target = e.target
            item.classList.toggle('text-primary')
            e.preventDefault();

            

            var postId = arr[index].getAttribute('data-new')
            $.ajax({
                type: "POST",
                url: "/" + postId + "/like",
                enctype: 'multipart/form-data',
                data: {
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                // headers: {
                // 'X-CSRFToken': token
                // },
                success: function (data) {
                    if (data.is_like) {
                        var liked = document.getElementById(`like-count${index}`)
                        
                        liked.innerHTML = data.like_count
                    } else {
                        var liked = document.getElementById(`like-count${index}`)
                        liked.innerHTML = data.like_count
                    }
                }
            })
        })
    })