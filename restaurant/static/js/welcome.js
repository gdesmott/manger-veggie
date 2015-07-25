var userPrefs = JSON.parse(localStorage.getItem("userPrefs"));

if(userPrefs == null) {
    userPrefs = {}
    userPrefs.gluten_free = false;
    userPrefs.vegan = false;
}

$(document).ready(function() {
    var modal_options = {backdrop: 'static', keyboard: false}
    $("#next-page-button").click(function() {
        $("#welcomeModal").removeAttr("fade");
        $("#welcomeModal").collapse();

        //it's ugly and I'm sorry
        //TODO: use more suited components and their databinding
        if(userPrefs.vegan)
            $("#vegan").addClass("active");
        else
            $("#not-vegan").addClass("active");

        if(userPrefs.gluten_free)
            $("#gluten-free").addClass("active");
        else
            $("#not-gluten-free").addClass("active");

        $("#vegan").click(function(){
            userPrefs.vegan = true;
            $("#vegan").addClass("active");
            $("#not-vegan").removeClass("active");
        });
        $("#not-vegan").click(function(){
            userPrefs.vegan = false;
            $("#not-vegan").addClass("active");
            $("#vegan").removeClass("active");
        });
        $("#not-gluten-free").click(function(){
            console.log("notgf");
            userPrefs.gluten_free = false;
            $("#not-gluten-free").addClass("active");
            $("#gluten-free").removeClass("active");
        });
        $("#gluten-free").click(function(){
            console.log("gf");
            userPrefs.gluten_free = true;
            $("#gluten-free").addClass("active");
            $("#not-gluten-free").removeClass("active");
        });


        $("#preferenceModal").modal(modal_options);
    });
    $("#finish-button").click(function() {
        localStorage.setItem("userPrefs", JSON.stringify(userPrefs));
        $("#preferenceModal").attr("fade", "true");
        $("#preferenceModal").collapse();
        console.log(JSON.stringify(userPrefs));
        map_init(global_map, null);
        localStorage.setItem("welcome-message-seen", "true");
    });

    if(!localStorage.getItem("welcome-message-seen"))
        $("#welcomeModal").modal(modal_options);
});