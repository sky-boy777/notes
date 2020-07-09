// JavaScript Document
$(function(){
	"use strict";
			var oWinTop;
			var oBoxH = $(".box").height();
			var vLen = 0;
			var vIndex = [];
			$(".slidecount li").each(function(){
				vLen = vLen + 1;
				vIndex.push($(this).index());
			});
			$(window).scroll(function(){
				oWinTop = $(window).scrollTop();
				if(oWinTop >= 0 && oWinTop < oBoxH){
					$(".slidecount li:eq("+vIndex[0]+")").addClass("focus").siblings("li").removeClass("focus");
				}else if(oWinTop >= oBoxH && oWinTop < (oBoxH * vIndex[2])){
					$(".slidecount li:eq("+vIndex[1]+")").addClass("focus").siblings("li").removeClass("focus");
				}else{
					$(".slidecount li:eq("+vIndex[2]+")").addClass("focus").siblings("li").removeClass("focus");
				}
			});
			$(".slidecount li").click(function(){
				if($(this).index() == 0){
					$("body").animate({
						scrollTop:0
					},2000);
					return false;
				}else if($(this).index() == 1){
					$("body").animate({
						scrollTop:$("#n2").offset().top
					},2000);
					return false;
				}else if($(this).index() == 2){
					$("body").animate({
						scrollTop:$("#n3").offset().top
					},2000);
					return false;
				}
			});
		});