var list_snapshot = []

function buildList() {
    var wrapper = document.getElementById('list-wrapper')
    //wrapper.innerHTML = ''


    var url = 'http://127.0.0.1:8000/api/task-list/'

    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            console.log('Data:', data)

            var list = data
            for (var i in list) {


                try {
                    document.getElementById(`data-row-${i}`).remove()
                } catch (err) {

                }


                var title = `<span class="title">${list[i].title}</span>`
                if (list[i].completed == true) {
                    title = `<strike class="title">${list[i].title}</strike>`
                }

                var item = `
						<div id="data-row-${i}" class="task-wrapper flex-wrapper">
							<div style="flex:7">
								${title}
							</div>
							<div style="flex:1">
								<button class="btn btn-sm btn-outline-info edit">Edit </button>
							</div>
							<div style="flex:1">
								<button class="btn btn-sm btn-outline-dark delete">-</button>
							</div>
						</div>

					`
                wrapper.innerHTML += item

            }

            if (list_snapshot.length > list.length) {
                for (var i = list.length; i < list_snapshot.length; i++) {
                    document.getElementById(`data-row-${i}`).remove()
                }
            }

            list_snapshot = list


            for (var i in list) {
                var editBtn = document.getElementsByClassName('edit')[i]
                var deleteBtn = document.getElementsByClassName('delete')[i]
                var title = document.getElementsByClassName('title')[i]

                //Immediatly Invoked Function (IIF) + Closure for saving current loop item in memory
                editBtn.addEventListener('click', (() => {

                    let item = list[i]
                    return () => {
                        editItem(item)
                    }
                })())


                deleteBtn.addEventListener('click', (function (item) {
                    return function () {
                        deleteItem(item)
                    }
                })(list[i]))


                title.addEventListener('click', (function (item) {
                    return function () {
                        strikeUnstrike(item)
                    }
                })(list[i]))


            }


        })
}
