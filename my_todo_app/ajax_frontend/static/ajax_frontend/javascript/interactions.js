var activeItem = null

function editItem(item) {
    console.log('Item clicked:', item)
    activeItem = item
    document.getElementById('title').value = activeItem.title
}


function deleteItem(item) {
    console.log('Delete clicked')
    fetch(`/api/task-delete/${item.id}/`, {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        }
    }).then((response) => {
        buildList()
    })
}

function strikeUnstrike(item) {
    console.log('Strike clicked')

    item.completed = !item.completed
    fetch(`/api/task-update/${item.id}/`, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'title': item.title, 'completed': item.completed})
    }).then((response) => {
        buildList()
    })
}
