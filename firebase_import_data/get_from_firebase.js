// hot el configuration mtaa el firebase houni (ps: matansech t3ayet el firebase fel fichier html)


var ref = firebase.database().ref("messages");
ref.once("value")
  .then(function(snapshot) {
  	var tableau = snapshot.val()
      
    for (var element in tableau)
    {
    	element_a_ajouter=tableau[element]["name"]// tekhou element mel tableau 
    	$("#names").append("<h3>"+element_a_ajouter+"</h3>") //tafichi el element 
    }
  });

