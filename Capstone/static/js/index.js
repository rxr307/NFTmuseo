
let likeButtons = document.querySelectorAll('.like') // this method returns a list of the documents elements that match the selector (the like buttons on our template)

    csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0]; // this method returns list of elements with a given -name- attribute, returning 1st index [0] from that list


const axios_config = {
  // axios.headers.post['Content-Type'] = 'application/json',
  // axios.headers.post['X-CSRFToken'] = csrfToken.value ,
  headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken.value 
  }, 
  xsrfHeaderName: 'X-CSRFToken' 
}

function galleryLike(event){          // creating event or 'signal' in browser that will run the following code when prompted
  let galleryID = event.target.id  // referencing the object onto which the event will occur (the like icons)
  galleryID = galleryID.split('-')[1]
  let url = 'http://localhost:8000/likegallery/' + galleryID 
  axios.post(url, {}, axios_config)  // {} is representing the HTTP reuqest body
    .then(response=>{ // once post request is made, Axios returns promise that is either fulfilled or rejected (response)
      console.log(response);
      const userliked = response.data.userliked //JsonResponse if user has liked yet or not 
      const likebutton = document.querySelector(`#like-${galleryID}`) // this identifies the like icon
      const numberlikes = document.querySelector(`#like-count-${galleryID}`) // this identifies the element holding our number of likes

      numberlikes.innerHTML = response.data.numberlikes // const numberlikes is the element holding number of likes, response data is response from axios post request telling us number of likes

      if(userliked){
        likebutton.classList.remove('expressionless')
        likebutton.classList.add('grin-hearts')
      } else {
        likebutton.classList.remove('grin-hearts')
        likebutton.classList.add('expressionless')
      }

    })

    .catch(error=>console.log(error))
}

likeButtons.forEach(likeButton =>
  likeButton.addEventListener('click', galleryLike)
)