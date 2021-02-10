const one = document.getElementById('rate-1')
const two = document.getElementById('rate-2')
const three = document.getElementById('rate-3')
const four = document.getElementById('rate-4')
const five = document.getElementById('rate-5')
const six = document.getElementById('rate-6')
const seven = document.getElementById('rate-7')
const eight = document.getElementById('rate-8')
const nine = document.getElementById('rate-9')
const ten = document.getElementById('rate-10')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const handleStartSelect = (size) => {
    const children = form.children
    for (let i=0; i < children.length; i++) {
        if (i<size) {
            children[i].classList.add('checked')
        }
        else {
            children[i].remove('checked')
        }
    }
}

const argument =  [one, two, three, four, five, six, seven, eight, nine, ten]

function handleSelect(event) {
    switch (event) {
        case 'rate-1': {
            handleStartSelect(1)
            return
        }
        case 'rate-2': {
            handleStartSelect(2)
            return
        }
        case 'rate-3': {
            handleStartSelect(3)
            return
        }
        case 'rate-4': {
            handleStartSelect(4)
            return
        }
        case 'rate-5': {
            handleStartSelect(5)
            return
        }
        case 'rate-6': {
            handleStartSelect(6)
            return
        }
        case 'rate-7': {
            handleStartSelect(7)
            return
        }
        case 'rate-8': {
            handleStartSelect(8)
            return
        }
        case 'rate-9': {
            handleStartSelect(9)
            return
        }
        case 'rate-10': {
            handleStartSelect(10)
            return
        }
    }
}

const getNumericValue = (stringValue) => {
    let numericValue;
    if (stringValue === 'rate-1') {
        numericValue = 1
    }
    else if (stringValue === 'rate-2') {
        numericValue = 2
    }
    else if (stringValue === 'rate-3') {
        numericValue = 3
    }
    else if (stringValue === 'rate-4') {
        numericValue = 4
    }
    else if (stringValue === 'rate-5') {
        numericValue = 5
    }
    else if (stringValue === 'rate-6') {
        numericValue = 6
    }
    else if (stringValue === 'rate-7') {
        numericValue = 7
    }
    else if (stringValue === 'rate-8') {
        numericValue = 8
    }
    else if (stringValue === 'rate-9') {
        numericValue = 9
    }
    else if (stringValue === 'rate-10') {
        numericValue = 10
    }
    else {
        numericValue = 0
    }
    return numericValue
}

if (one) {
    argument.forEach(item=> item.addEventListener('mouseover', (event)=>{
        handleSelect(event.target)
    }))

    argument.forEach(item=> item.addEventListener('click', (event)=>{
        const val = event.target.id
        let isSubmit = false

        form.addEventListener('submit', e=>{
            e.preventDefault()
            if (isSubmit) {
                return
            }
            isSubmit = true
            const id = e.target.id
            const val_num = getNumericValue(val)

            $.ajax({
                type: 'POST',
                url: '/add-rating/',
                data: {
                    'csrfmiddlewaretoken': csrf[0].value,
                    'el_id': id,
                    'val': val_num
                },
                success: function (response) {
                    confirmBox.innerHTML = `<h1>Успешно поставил свой рейтинг</h1>`
                },
                error: function (error) {
                    confirmBox.innerHTML = `<h1>Ошибка</h1>`
                }
            })
        })
    }))
}