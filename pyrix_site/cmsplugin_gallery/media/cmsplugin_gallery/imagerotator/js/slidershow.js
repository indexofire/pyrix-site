$(document).ready(function() {
	//Show Banner
	$(".main_image .desc").show(); //Show Banner
	$(".main_image .imgblock").animate({ opacity: 0.85 }, 1 ); //Set Opacity

	//Click and Hover events for thumbnail list
	$(".image_thumb ul li:first").addClass('active');
	$(".image_thumb ul li").click(function(){
		//Set Variables
		var imgAlt = $(this).find('img').attr("alt"); //Get Alt Tag of Image
		var imgTitle = $(this).find('a').attr("href"); //Get Main Image URL
		var imgDesc = $(this).find('.imgblock').html(); 	//Get HTML of block
		var imgDescHeight = $(".main_image").find('.imgblock').height();	//Calculate height of block

		if ($(this).is(".active")) {  //If it's already active, then...
			return false; // Don't click through
		} else {
			//Animate the Teaser
			$(".main_image img").animate({ opacity: 0}, 250 );
			$(".main_image .imgblock").animate({ opacity: 0, marginBottom: -imgDescHeight }, 250 , function() {
				$(".main_image .imgblock").html(imgDesc).animate({ opacity: 0.85,	marginBottom: "0" }, 250 );
				$(".main_image img").attr({ src: imgTitle , alt: imgAlt}).animate({ opacity: 1}, 250 );
			});
		}

		$(".image_thumb ul li").removeClass('active'); //Remove class of 'active' on all lists
		$(this).addClass('active');  //add class of 'active' on this list only
		return false;

	}) .hover(function(){
		$(this).addClass('hover');
		}, function() {
		$(this).removeClass('hover');
	});

	//Toggle Teaser
	$("a.collapse").click(function(){
		$(".main_image .imgblock").slideToggle();
		$("a.collapse").toggleClass("show");
	});

});//Close Function
