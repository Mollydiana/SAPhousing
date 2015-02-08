//      var orgData = new sap.ui.model.json.JSONModel('{ "first_name": "SAP","last_name": "SAP", "social": 2531208, }');
//      var repoData = new sap.ui.model.json.JSONModel('{ "first_name": "SAP","last_name": "SAP", "social": 2531208, }');
//      sap.ui.getCore().setModel(repoData, "repos");
//      sap.ui.getCore().setModel(orgData, "org");
//new sap.ui.commons.TextField({
      var list = new sap.m.List();
      list.bindItems({
	      path: "repos>/", template : new sap.m.StandardListItem({ title: "{repos>name}" })
	    });

    	var page2 = new sap.m.Page("page2", {
    	  content: list,
    	  title: "Fill out the following:",
    	  showNavButton: true,
    	  navButtonTap: function(){
    	    app.back();
    	   }
    	 });
      var page1 = new sap.m.Page("page1", { title: "Rental Application",
    		content: [
    	      		new sap.m.Button({
    	      			text: "Click to fill out application",
    	      			press: function() {
    	      				app.to("page2");
    	      			}
    	      		})
    	   ]
     	});
     	var app = new sap.m.App().addPage(page1).addPage(page2).placeAt("content-ui");