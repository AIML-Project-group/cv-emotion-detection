(function () {
    window.addEventListener('DOMContentLoaded', function () {
        const form = this.document.forms[0]
        const imageInput = form.querySelector('input')
        const output = document.querySelector('#output')

        // https://medium.com/@codefoxx/how-to-upload-and-preview-an-image-with-javascript-749b92711b91
        imageInput.addEventListener('change', function () {
            const reader = new FileReader()
            reader.addEventListener('load', () => {
                const uploaded_image = reader.result;
                document.querySelector("#input").style.backgroundImage = `url(${uploaded_image})`;
            })
            reader.readAsDataURL(this.files[0])
        })
        imageInput.dispatchEvent(new Event('change'))


        form.onsubmit = function sendImageToServer(event) {
            event.preventDefault()
            output.classList.add('loading')

            fetch(form.action, {
                body: new FormData(form),
                method: 'POST',
                credentials: 'include'
            })
                .then(response => response.blob())
                .then(blob => URL.createObjectURL(blob))
                .then(generated_image => {
                    output.style.backgroundImage = `url(${generated_image})`;
                })
                .finally(() => {
                    output.classList.remove('loading')
                })
        }
    })
}) ()
