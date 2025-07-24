function deleteNote(noteId) {
  fetch('/delete-note', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ noteId })
  }).then(response => {
    if (response.ok) {
      window.location.href = '/'
    } else {
      alert('Failed to delete note.')
    }
  })
}