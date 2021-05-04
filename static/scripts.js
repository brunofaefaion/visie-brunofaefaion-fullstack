async function deleteItem(id){
  try {
    await fetch('/', {
      method: 'DELETE',
      body: JSON.stringify({id: `${id}`}),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    location.reload()
  } catch (e) {
    console.error('Error on call...', e)
  }
}
