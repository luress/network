document.addEventListener('DOMContentLoaded', function( ) {
    
    document.querySelector("#all-post").onclick = function(){
        document.querySelector('#post-button').onclick = function(){
            create_post()
        }
        document.querySelector('#post-button-hide').onclick = function() {
            hide_create_post()
        }
    }
    
    edit()
    
})


function hide_create_post() {
    document.querySelector('#post-button').style.display = 'block';
    document.querySelector('#post-create').style.display = 'none';
    document.querySelector('#post-button-hide').style.display = 'none';
}

function create_post() {
    document.querySelector('#post-button').style.display = 'none';
    document.querySelector('#post-create').style.display = 'block';
    document.querySelector('#post-button-hide').style.display = 'block';
    
    
    document.querySelector('#new-post-text').value = '';
    document.querySelector('#post-form').onsubmit = function(){
        add_post();
        document.querySelector('#post-create').style.display = 'none'
        
    }
}

function add_post(){
    
    const text = document.querySelector('#new-post-text').value;
    fetch('/posts', {
        method: 'POST',
        body: JSON.stringify({
            text: `${text}`
        })
    })
    .then(response => response.json())
    .then(result => {
    });
}

function edit() {
    document.addEventListener('click', event => {

        const element = event.target
        //edit our post 
        if(element.className === "post-edit"){
                fetch(`/posts/${element.parentElement.id}`)
                .then(response => response.json())
                .then(post => {
                    const temp = post.text
                    const el = element.parentElement.querySelector('.post-text');
            el.innerHTML = ''

            

            const created = document.createElement('textarea');
            created.className = 'edit-textarea';
            created.style.animationPlayState = 'running';


            const but = document.createElement('button');
            but.className = "button-submit";
            but.setAttribute("value", "Edit")
            but.innerHTML = "Edit"

            
            
            
            created.innerHTML = temp
            el.append(created)
            el.append(but)
                })
            const temp = element.parentElement.querySelector('.post-text').textContent;
                      
            
            
            
        }
    })

    document.addEventListener("click", event => {
        
        const element = event.target;

        if(element.className === "button-submit"){

            new_text = element.parentElement.querySelector('.edit-textarea').value;
            fetch(`/posts/${element.parentElement.parentElement.id}`, {
            method: 'PUT',
            body: JSON.stringify({
                text: new_text
            })
          })
          element.parentElement.parentElement.querySelector('.post-text').innerHTML = new_text
          
          
          
        }
    })
    document.addEventListener("click", event => {
         
        const element = event.target;

        if(element.className === "like-img") {
            const likes = parseInt(element.parentElement.parentElement.querySelector('.post-likes').textContent) + 1
            
            fetch(`/posts/${element.parentElement.parentElement.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    number_of_likes: likes
                })
              })
              fetch(`/posts/${element.parentElement.parentElement.id}`)
              .then(response => response.json())
              .then(post => {
                element.parentElement.parentElement.querySelector('.post-likes').innerHTML = `<img class="like-img" src="/static/network/like2.png">${post.number_of_likes}`
              })
              
              
        }
    })

}

