function deleteOffer (offerID) {
    fetch('http://localhost:8000/api/offers/'+offerID, {
      method: "DELETE",
      headers: new Headers({'Content-Type': 'application/json'})
    })
    return
}

function deleteRequest (requestID) {
    fetch('http://localhost:8000/api/requests/'+requestID, {
      method: "DELETE",
      headers: new Headers({'Content-Type': 'application/json'})
    })
    return
}

function initiateContact (offusername,requsername){
	fetch('http://localhost:8000/api/initiateContact/'+offusername+'/'+requsername, {
	method: "POST",
	headers: new Headers({'Content-Type': 'application/json'})
	})
	return
}

export default {
  deleteOffer,
  deleteRequest,
  initiateContact
}