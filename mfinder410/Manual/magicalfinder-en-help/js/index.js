//﻿$(function () {
$(window).load(function () {
//index.js  2018-11-16

	console.log('============================== INIT ==============================');

	// クッキー名
	var cookieName = 'searchHistory_clipbag';

	// ハイライト用クエリ
	var searchQuery = '';

	// 検索履歴
	var searchHistoryNum = 5;
	var searchHistory = [];
	searchHistoryCreate();

	// LazyLoad
	$("img.lazy").lazyload({
		skip_invisible: true,
		threshold: 99999999
	});




	// チャプターもくじ生成
	for (var i = 0; i < $('nav>ul>li').length; i++) {
		var li = $('nav>ul>li').eq(i);
		var cHtml = '';
		cHtml += '<div id="chapter_' + i + '" class="chapterIndex">';
		cHtml += '<h1>' + li.children('span').children('a').html() + '</h1>';
		cHtml += '<div><ul>';

		for (var ii = 0; ii < li.children('ul').children(li).length; ii++) {
			cHtml += '<li>' + li.children('ul').children(li).eq(ii).html() + '</li>';
		}

		cHtml += '</ul></div>';
		$('#contentInner').append(cHtml);
	}
	$('.chapterIndex').hide();

	// NAV RESET
	$('nav>ul>li>ul').hide();
	var nowIn = 'index';


	// NAV固定
	var mainH;
	var sideH;




	// 用語リンク生成
	var termsOnesFlg = false;
	for (var i = 0; i < $('#terms>div').length; i++) {
		var q = $('#terms>div').eq(i).children('h1').html();
		$('#terms>div').eq(i).attr('id', '_terms_' + q.replace(/ /g, '---'));
		console.log('TERMS LINK: ' + q);
		//for (var ii = 0; ii < $('#contentInner>article').length; ii++) {
		//var a = $('#contentInner>article').eq(ii);
		for (var ii = 0; ii < $('.page').length; ii++) {
			termsOnesFlg = false;
			var a = $('.page').eq(ii);
			linkTerms(a, q);
			var text = a.html().replace(/___open___/g, "<");
			text = text.replace(/___close___/g, ">");
			a.html(text);
		}
	}

	// 用語リンク再帰処理
	var aFlg = false;
	function linkTerms(elm, q) {
		for (var i = 0; i < elm.length; i++) {
			if (elm[i].nodeName === "#text" && !termsOnesFlg) {
				var re = new RegExp("(" + q + ")", "im");
				var ss = elm[i].nodeValue;
				elm[i].nodeValue = ss.replace(re, '___open___a href="#_terms_' + q.replace(/ /g, '---') + '" data-lity class="termsLink"___close___$1___open___/a___close___');
				if (elm[i].nodeValue.match(/___open___a/)) {
					termsOnesFlg = true;
				}
			} else {
				if (elm[i].hasChildNodes() && elm[i].nodeName !== "A") {
					linkTerms(elm[i].childNodes, q);
				}
			}
		}
	}



	hashCheck();






	// クエリハイライト再帰処理
	function highlightSearch(elm, q) {
		for (var i = 0; i < elm.length; i++) {
			if (elm[i].nodeName === "#text") {

				var qarr = moji(q).convert("ZEtoHE").convert("HKtoZK").toString().split(/\s/); // qを半角スペースで区切ったもの
				var qor = "";
				for (var ii = 0; ii < qarr.length; ii++){
					qor += qarr[ii] + "|";
				}
				while (qor.slice(-1) === "|") {
					qor = qor.slice(0, -1);
				}
				while (qor.slice(0, 1) === "|") {
					qor = qor.slice(1);
				}
				while (qor.match(/\|\|/)) {
					qor = qor.replace(/\|\|/, "|");
				}
				var reor = new RegExp("(" + qor + ")", 'igm');

				var ss = elm[i].nodeValue;
				elm[i].nodeValue = ss.replace(reor, "___open___em___close___$1___open___/em___close___");
			} else {
				if (elm[i].hasChildNodes()) {
					highlightSearch(elm[i].childNodes, q);
				}
			}
		}
	}

	// ページ移動
	function move(n) {
		console.log('MOVE: ' + n);

		var a = '';
		if (n.match('__')) {
			a = n.split('__')[1];
			n = n.split('__')[0];
		}


		// 指定したidが存在しない場合、ハッシュを上書きする  by AK ***** ここから *****
		if (document.getElementById('c_' + n) === null && n!="") {
			console.log('ID: c_' + n + 'is null');
			var refUrl = document.referrer;
			if (refUrl=="") {refUrl = "Direct";}
			ga('send', 'event', 'err', 'NotExistPage', location.href + '__<referrer>__' + refUrl);
			document.location.hash = "index";//上書きするハッシュ（articleのid）
			return;
		}
		// 指定したidが存在しない場合、ハッシュを上書きする  by AK ***** ここまで *****


		$('#searchResults').hide();
		$('.chapterIndex').hide();
		$('article').hide();
		$('article#c_' + n).show();


		// GA send
		var gaPage = "";
		if (a === '') {
			gaPage = location.pathname + "?id=" + n;
		} else {
			gaPage = location.pathname + "?id=" + n + "__" + a;
		}
		var gaTitle = $('article#c_' + n + ' > h1').text() + "_" + $('div#title').text();
		ga('send', 'pageview', {'page': gaPage, 'title': gaTitle});
		console.log('GA-page:' + gaPage);
		console.log('GA-title:' + gaTitle);

		// NAV全閉
		$('nav>ul>li>span>a>em').text('▶');
		$('nav>ul>li>ul').hide();

		// NAV OPEN
		if (n === 'index' && a !== '') {
			//console.log('INDEX NAV OPEN');
			$('nav>ul>li').eq(a).children('span').children('a').children('em').text('▼');
			$('nav>ul>li').eq(a).children('ul').show();


			// NAVサイド色戻す
			$('nav>ul>li>ul>li>span>a').css('border-left', '11px solid #8fa2cc');
			// NAVサイドTRI戻す
			$('nav>ul>li>ul>li').removeClass('now');
		} else {
			$('#l_' + n).closest('ul').closest('li').children('span').children('a').children('em').text('▼');
			$('#l_' + n).closest('ul').show();

			// NAVサイド色
			$('nav>ul>li>ul>li>span>a').css('border-left', '11px solid #8fa2cc');
			$('#l_' + n).css('border-left', '11px solid #152144');

			// NAVサイドTRI
			$('nav>ul>li>ul>li').removeClass('now');
			$('#l_' + n).closest('li').addClass('now');
		}

		// SEARCH HIDE
		/*if ($('.spHeader').css('display') === 'block') {	// IF SP
			$('#search').hide();
		}*/
		$("input").val('');


		// ホームボタンにNAV INDEXを仕込む
		if (n !== 'index') {
			$('#homeButton>a').attr('href', '#index');
			for (var i = 0; i < $('nav>ul>li').length; i++) {
				if ($('nav>ul>li').eq(i).children('span').html().match(/▼/)) {
					$('#homeButton>a,.spHeader>a,#logo>a,#title>a').attr('href', '#index__' + i);
					break;
				}
			}
		}

		// NAVスイッチ
		navDispSwitch(n);

		nowIn = n;

		// クエリハイライト削除
		var text = $('article#c_' + n).html().replace(/<[/]*?em>/g, '');
		$('article#c_' + n).html(text);

		if (searchQuery !== '') {
			// クエリハイライト処理
			console.log('SEARCH Query: ' + searchQuery);
			highlightSearch($('article#c_' + n), searchQuery);
			var text = $('article#c_' + n).html().replace(/___open___/g, "<");
			text = text.replace(/___close___/g, ">");
			$('article#c_' + n).html(text);
			//検索した語句の一番上にスクロールする　はじめ
			for (var stnum = 0; stnum < $('article#c_' + n + ' em').length; stnum++) {
				var srchtarget = $('article#c_' + n + ' em').eq(stnum);
				if (srchtarget.parent().parent().attr('class') === "spHeader" || srchtarget.parent().prop('tagName') === "H1") {

				} else {
					break;
				}
			}
			setTimeout(function () {
				$('html, body').animate({scrollTop: $('article#c_' + n + ' em').eq(stnum).offset().top}, 300, 'easeOutCubic');
			}, 100);
			//検索した語句の一番上にスクロールする　おわり
			searchQuery = '';
		} else {

		}

		$("img.lazy").lazyload({
			threshold: 99999999
		});
		if (a !== '' && n !== 'index') {
			$('div.box:not(:has(div.elem2))').css('color', 'red');
			if (a !== 'srchword') {
				$('#' + a).wrapInner('<em />');
			}
			var allImage = $('article#c_' + n + ' img');
			var allImageCount = allImage.length;
			var completeImageCount = 0;
			if (allImageCount === 0) {
				setTimeout(function () {
					$('html, body').animate({scrollTop: $('#' + a).offset().top}, 300, 'easeOutCubic');
				}, 100);
			} else {
				for (var i = 0; i < allImageCount; i++) {
					$(allImage[i]).bind("load", function () {
						completeImageCount++;
						if (allImageCount === completeImageCount) {
							setTimeout(function () {
								$('html, body').animate({scrollTop: $('#' + a).offset().top}, 300, 'easeOutCubic');
							}, 100);
						}
					});
				}
			}
		} else if (n === 'index' && a !== '') {
			//console.log('INDEX NAV OPEN SCROLL');
			if (navOpenFlg) {
				//console.log('INDEX NAV OPENED');
				navOpenFlg = false;
			} else {
				$('html, body').scrollTop($('nav>ul>li').eq(a).offset().top);
			}
			$('#homeButton>a').attr('href', '#index');
		} else {
			// NAV閉じる際は無視
			if (location.hash !== '#index__') {
				console.log('SCROLL RESET');
				$('html, body').scrollTop(0);
			}
		}

		navFix();

		return false;
	}



	// NAVスイッチ
	function navDispSwitch(n) {
		if ($('.spHeader').css('display') === 'block') {
			// IF SP
			if (n !== 'index') {
				$('nav').hide();
				$('#spTopImage').hide();
			} else {
				$('nav').show();
				$('#spTopImage').show();
			}
		} else {
			// IF PC
			$('nav').show();
			$('#search').show();
			$('#spTopImage').hide();
			navFix();
		}
	}



	// リンク処理
	var searchMatch = false;
	$(document).on('click', 'a[href^="#"]', function (e) {
		if ($(this).attr("href") === "#") {
			e.preventDefault();
			return false;
		} else if ($(this).attr("href") === "#top") {
			$('html, body').animate({scrollTop: 0}, 500, 'easeOutCubic');
			e.preventDefault();
			return false;
		} else if ($(this).attr("href").substr(1).match(/^_terms_/)) {
			var glosquery = $(this).html() + "_" + location.hash + "_" + $('div#title').text();
			console.log("用語クリック：" + glosquery);
			ga('send', 'event', 'glos', 'click', glosquery, true);
			e.preventDefault();
			return false;
		} else {
			// 検索離脱時GAキック
			if ($(this).hasClass('searchResults')) {
				var gaquery;
				gaquery = searchQuery + '_' + $(this).attr("href").substr(1) + '_' + $('div#title').text();
				console.log('GA_SEND-> ' + gaquery);
				ga('send', 'event', 'search', 'result', gaquery, true);
				searchMatch = true;
			}

			if ($(this).hasClass('regWordResult')) {
				var gaquery;
				gaquery = $('div#searchResultsArea em').eq(0).text() + ' -> ' + $(this).text() + '_' + $('div#title').text();
				console.log('GA_SEND-> ' + gaquery);
				ga('send', 'event', 'regWord', 'click', gaquery, true);
				searchMatch = true;
			}

			if (location.hash !== $(this).attr('href')) {
				location.hash = $(this).attr('href').substr(1);
			} else {
				if ($(this).attr('href').substr(1).match(/^_search_/)) {
				} else {
					move($(this).attr('href').substr(1));
				}
			}
			e.preventDefault();
			return false;
		}
	});



	// 全ページプリント
	$(document).on('click', '#printAll', function (e) {
		$('article').show();
		$("img.lazy").lazyload({
			threshold: 99999999
		});
		$('article:not(:last-child)').css('page-break-after', 'always');

		var printquery = "print_" + $('div#title').text();
		console.log("印刷クリック：" + printquery);
		ga('send', 'event', 'print', 'click', printquery, true);

		$('#printCopy').show();

		window.print();

		$('#printCopy').hide();
		$('article').css('page-break-after', 'auto');
		$('article').hide();
		$('#c_index').show();

		e.preventDefault();
		return false;
	});

	window.onafterprint = function () {
		$('#printCopy').hide();
		$('article').css('page-break-after', 'auto');
		$('article').hide();
		move(nowIn);
	};


	// ナビ開閉
	var navOpenFlg = false;
	$(document).on('click', 'nav>ul>li>span>a', function (e) {
		var index = $('nav>ul>li').index($(this).closest('li'));
		if (nowIn.match(/^index/)) {
			// INDEXかどうか
			if (location.hash === '#index__' + index) {
				// 閉じる
				location.hash = 'index__';
			} else {
				// INDEX NAVモード
				location.hash = 'index__' + index;
				navOpenFlg = true;
			}
		} else {
			navOpen(index);
		}
	});

	function navOpen(n) {
		//console.log('NAV OPEN');
		var me = $('nav>ul>li').eq(n);

		// NAV全閉
		$('nav>ul>li>span>a>em').text('▶');
		$('nav>ul>li>ul').animate({height: 'hide'}, 100);
		if (me.children('ul').is(':visible')) {
			me.children('span').children('a').children('em').text('▶');
			me.children('ul').animate({height: 'hide'}, 100, "easeOutExpo", function () {
				navFix();
			});
			return false;
		} else {
			me.children('span').children('a').children('em').text('▼');
			me.children('ul').animate({height: 'show'}, 100, "easeOutExpo", function () {
				navFix();
			});
			return false;
		}
	}


	//文字サイズ変更
	$("#text-size-change ul li").click(function () {
		$("#text-size-change ul li").removeClass("select");
		var textsize = $(this).attr("class");
		$(this).addClass("select");
		if (textsize === "small-text") {
			$("article,#searchResultsArea").css("font-size", "0.875em");
		} else if (textsize === "middle-text") {
			$("article,#searchResultsArea").css("font-size", "1em");
		} else if (textsize === "big-text") {
			$("article,#searchResultsArea").css("font-size", "1.15em");
		}

	});


	// SEARCH ON/OFF
	$('#search_button>a').click(function (e) {
		$('#search').animate({height: 'toggle'}, 100);
		$("#input-text").focus();
	});


	// 履歴窓生成
	function searchHistoryCreate() {
		if ($.cookie(cookieName)) {
			searchHistory = decodeURI($.cookie(cookieName)).split('|||||');
			$('#searchHistory').html('');
			for (var i = 0; i < searchHistory.length; i++) {
				$('#searchHistory').append('<li><a href="#_search_' + encodeURI(searchHistory[i]) + '">' + searchHistory[i] + '</a></li>');
			}
		} else {
			$('#searchHistory').html('');
		}
	}


	// 履歴窓表示
	$("#input-text").focus(function (e) {
		if (searchHistory.length > 0) {
			setTimeout(function () {
				$("#searchHistory").fadeIn(100);
			}, 100);
		}
	});
	$("#input-text").blur(function (e) {
		setTimeout(function () {
			$("#searchHistory").fadeOut(100);
		}, 100);
	});


	// 検索
	$("form").submit(function () {
		if ($("input").val()) {
			location.hash = '_search_' + encodeURI($("input").val());
			// 検索窓クリア
			$("input").val('');
			$("input").blur();
		}
		return false;
	});


	// 検索処理
	function search(q) {
		var q = q;
		searchQuery = q;
		//GA Search Event
		/*
		 var gaSearch = searchQuery + "_" + $('div#title').text();
		 ga('send', 'event', 'search', 'input', gaSearch);
		 console.log('GA-Search:' + gaSearch);
		 */

		var qarr = moji(q).convert("ZEtoHE").convert("HKtoZK").toString().split(/\s/);
		// and検索用
		var qand = "^";
		for (var ii = 0; ii < qarr.length; ii++){
			qand += "(?=.*" + qarr[ii] + ")";
		}
		while (qand.match(/\(\?=\.\*\)/)) {
			qand = qand.replace(/\(\?=\.\*\)/, "");
		}
		var reand = new RegExp(qand, 'igm');

		// or検索：emタグ用
		var qor = "";
		for (var ii = 0; ii < qarr.length; ii++){
			qor += qarr[ii] + "|";
		}
		while (qor.slice(-1) === "|") {
			qor = qor.slice(0, -1);
		}
		while (qor.slice(0, 1) === "|") {
			qor = qor.slice(1);
		}
		while (qor.match(/\|\|/)) {
			qor = qor.replace(/\|\|/, "|");
		}
		var reor = new RegExp("(" + qor + ")", 'igm');


		// NAV全閉
		$('nav>ul>li>span>a>em').text('▶');
		$('nav>ul>li>ul').hide();
		// SP SEARCH HIDE
		/*if ($('.spHeader').css('display') === 'block') {	// IF SP
			$('#search').hide();
		}*/

		// 検索結果初期化
		$('#searchResultsArea>div.page').html('');
		$('#searchResultsArea>div.page').append('<section><em>' + $('<span/>').text(q).html() + '</em> の検索結果</section>');

		$('.chapterIndex').hide();
		$('article').hide();
		$('#searchResults').show();
		// SP SEARCH HIDE
		if ($('.spHeader').css('display') === 'block') {	// IF SP
			$('#spTopImage').hide();
			$('nav').hide();
		}

		// 検索キーワードに含まれた文字から登録語を案内
		var byAnyChance = "<section><p>こちらでは？：";
		for (var i = 0; i < $("div#regWord>div").length; i++) {
			var regWord_source = $("div#regWord>div>h1").eq(i).text();
			var regWord_dest = $("div#regWord>div>h2").eq(i).text();
			if (moji(q).convert("ZEtoHE").convert("HKtoZK").toString().match(RegExp(regWord_source,'igm')) != null) {
				console.log('Since ' + q + ' contains ' + regWord_source + ', I will guide ' + regWord_dest);
				regWord_dest_encode = '_search_' + encodeURI(regWord_dest);
				byAnyChance += ' <a href="#'+ regWord_dest_encode + '" class="regWordResult">' + regWord_dest + '</a>、';
			}
		}
		if (byAnyChance != "<section><p>こちらでは？：") {
			byAnyChance = byAnyChance.slice(0, -1); // 最後の、を削除
			byAnyChance += '</p></section>';
			$('#searchResultsArea>div.page').append(byAnyChance);
		}

		// 記事総当たり
		var resultHtml = '';
		for (var i = 0; i < $("article").length; i++) {
			var title = $("article").eq(i).children('h1').text();
			var link = $("article").eq(i).attr("id").substr(2);
			var str = $("article").eq(i).text().replace(/[\n\r\t]/g, "");
			var result = str.match(reand);
			var result2 = str.match(RegExp(qarr[0],'igm')); // これを挟むことで、結果生成のlastMatchをマシにする
			// 結果生成
			if (result) {
				var text = RegExp.leftContext.substr(-80) + RegExp.lastMatch + RegExp.rightContext.substr(0, 80);
				text = text.replace(reor, function () {
					return "<em>" + arguments[1] + "</em>";
				});
				resultHtml += '<section>';
				resultHtml += '<h2><a href="#' + link + '" class="searchResults">' + title + '</a></h2>';
				resultHtml += '<p class="sub"><a href="#' + link + '" class="searchResults">' + text + '</a></p>';
				resultHtml += '</section>';
			}
		}

		// 結果なし
		if (resultHtml === '') {
			var gaquery;
			gaquery = q + '__NotApplicable__' + $('div#title').text();
			console.log('GA_SEND-> ' + gaquery);
			ga('send', 'event', 'search', 'result', gaquery, true);
			resultHtml += '<section>';
			resultHtml += '<em>' + $('<span/>').text(q).html() + '</em> に一致する結果は見つかりませんでした。';
			resultHtml += '</section>';
			searchQuery = '';
		} else {
			// 履歴保存
			var c = q;
			if ($.cookie(cookieName)) {
				searchHistory = decodeURI($.cookie(cookieName)).split('|||||');
				// 同じ履歴が合ったら削除
				for (var i = 0; i < searchHistoryNum; i++) {
					if (searchHistory[i] === q) {
						searchHistory.splice(i, 1);
					}
				}

				for (i = 0; i < searchHistoryNum - 1; i++) {
					if (searchHistory[i]) {
						c += '|||||';
						c += searchHistory[i];
					} else {
						break;
					}
				}
			}
			console.log('SEARCH HISTORY: ' + c);
			$.cookie(cookieName, encodeURI(c));
			searchHistoryCreate();
		}

		$('#searchResultsArea>div.page').append(resultHtml);
		$("input").val(q);
		// NAVサイド色戻す
		$('nav>ul>li>ul>li>span>a').css('border-left', '11px solid #8fa2cc');
		// NAVサイドTRI戻す
		$('nav>ul>li>ul>li').removeClass('now');
	}


	// RESIZED
	$(window).resize(function () {
		navDispSwitch(nowIn);
	});
	checkTop(null);
	$(window).scroll(checkTop);
	$(window).resize(checkTop);
	function checkTop(e) {
		if ($(window).scrollTop() > 0) {
			$('#topButton').fadeIn(100);
		} else {
			$('#topButton').fadeOut(100);
		}
	}


	// HASH CHECK
	function hashCheck() {
		console.log('----------- HASH CHANGED: ' + location.hash + ' -----------');
		if (location.hash) {
			nowIn = location.hash.substr(1);
		} else {
			//location.hash = 'index';
		}
		// 検索離脱時GAキック
		if (searchQuery !== '' && !searchMatch) {
			var gaquery;
			gaquery = searchQuery + '__useless__' + nowIn + '_' + $('div#title').text();
			console.log('GA_SEND-> ' + gaquery);
			ga('send', 'event', 'search', 'result', gaquery, true);
		}
		searchMatch = false;
		if (nowIn.match(/^_search_/)) {
			// 検索かどうか
			console.log('||||| SEARCH MODE |||||');
			search(decodeURI(nowIn.split(/^_search_/)[1]));
		} else if (nowIn.match(/^index__/)) {
			// INDEX NAVかどうか
			console.log('||||| INDEX NAV MODE |||||');
			move(nowIn);
		} else if (nowIn.match(/^chapter_/)) {
			// チャプター目次かどうか
			console.log('||||| CHAPTER INDEX MODE |||||');
			chapterIndex();
		} else if (nowIn.match(/^redirect__/)) {
			// リダイレクトかどうか
			console.log('||||| REDIRECT MODE |||||');
			redirect(decodeURI(nowIn.split(/^redirect__/)[1]));
		} else {
			console.log('||||| MOVE MODE |||||');
			// 存在チェック
			//console.log($('article#c_' + nowIn.split('__')[0]).length);
			if (!$('article#c_' + nowIn.split('__')[0].length)) {
				location.hash = 'index';
			} else {
				move(nowIn);
			}
		}
	}
	$(window).hashchange(function () {
		hashCheck();
	});


	// ナビ固定
	function navFix() {
		var marginTop = 10;
		var startPoint = $('#nav').offset().top - marginTop;
		var scroll = $(window).scrollTop();
		if ($('nav').height() < $('#content').height()) {
			if (scroll > startPoint) {
				if (scroll + $('nav').height() < $('#content').offset().top + $('#content').height()) {
					//console.log('fixed');
					$('nav').css({'position': 'fixed', 'top': marginTop + 'px'});
				} else {
					//console.log('bottom');
					$('nav').css({'position': 'relative', 'top': $('#content').height() - $('nav').height() + 'px'});
				}
			} else {
				//console.log('relative');
				$('nav').css({'position': 'relative', 'top': '0px'});
			}
		} else {
			//console.log('default');
			$('nav').css({'position': 'relative', 'top': '0px'});
		}
	}
	$(window).scroll(function () {
		if ($('.spHeader').css('display') !== 'block') {
			navFix();
		}
	});


	// アコーディオンテーブル
	$('.accordionTable>dd').hide();
	$(document).on('click', '.accordionTable>dt', function () {
		console.log('accordion open');
		var p = $(this).parent();
		if ($('+dd', this).css('display') !== 'none') {
			$('+dd', this).stop(true, true).slideUp(300);
			$(this).removeClass('nowOpen');
		} else {
			$('>dt', p).removeClass('nowOpen');
			$('>dd', p).each(function () {
				if ($(this).css('display') !== 'none') {
					$(this).stop(true, true).slideUp(300);
				}
			});
			$('+dd', this).stop(true, true).slideDown(300);
			$(this).addClass('nowOpen');
		}
	});


	// 画像拡大用にaタグを追加
	//$('article').not('a').find('img:not(.nolity)').wrap(function(){
	$('article').find('img:not(a img,.nolity)').wrap(function () {
		if (!$(this).attr("data-original")) {
			return '<a href="' + $(this).attr("src") + '" data-lity>';
		} else {
			return '<a href="' + $(this).attr("data-original") + '" data-lity>';
		}
	});


	// アンケートクリック追跡
	$(document).on('click', '#enquete>a', function (e) {
		var enquetequery = location.hash + "__" + $('div#title').text();
		console.log("アンケートクリック：" + enquetequery);
		ga('send', 'event', 'enquete', 'click', enquetequery, true);
	});


	// ダウンロードクリック追跡
	$(document).on('click', '#downloadAll>a', function (e) {
		var dlquery = "download__" + $('#downloadAll>a').attr('href') + "__" + $('div#title').text();
		console.log("ダウンロードクリック：" + dlquery);
		ga('send', 'event', 'download', 'click', dlquery, true);
	});


	// チャプターもくじ表示
	function chapterIndex() {
		console.log('chapterIndex:' + nowIn);

		navDispSwitch(nowIn);

		// NAV全閉
		$('nav>ul>li>span>a>em').text('▶');
		$('nav>ul>li>ul').hide();
		$('nav>ul>li').eq(nowIn.split('chapter_')[1]).children('ul').show();

		$('#searchResults').hide();
		$('.chapterIndex').hide();
		$('article').hide();

		$('#' + nowIn).show();

		// NAVサイド色戻す
		$('nav>ul>li>ul>li>span>a').css('border-left', '11px solid #8fa2cc');
		// NAVサイドTRI戻す
		$('nav>ul>li>ul>li').removeClass('now');

	}


	// リダイレクト動作
	function redirect(q) {
		// リダイレクトワードからリダイレクト先を取得
		var rdrctDstntn = "";
		var refUrl = document.referrer;
		if (refUrl=="") {refUrl = "Direct";}
		for (var i = 0; i < $("div#rdrctWord>div").length; i++) {
			var rdrctSource = $("div#rdrctWord>div>h1").eq(i).text();
			if (rdrctSource == q) {
				rdrctDstntn = $("div#rdrctWord>div>h2").eq(i).text();
				console.log('redirectSource:' + q + ' -> ' + rdrctDstntn + '__<referrer>__' + refUrl + '__' + $('div#title').text());
				history.replaceState(null, null, 'index.html#' + rdrctDstntn);
				ga('send', 'event', 'reDirect', 'Success', q + ' -> ' + rdrctDstntn + '__<referrer>__' + refUrl + '__' + $('div#title').text(), true);
				move(rdrctDstntn)
				break;
			}
		}
		// リダイレクトワード該当なし
		if (rdrctDstntn == "") {
			console.log('### No redirectWord ###');
			ga('send', 'event', 'reDirect', 'Error', q + '__<referrer>__' + refUrl + '__' + $('div#title').text(), true);
			document.location.hash = "index";
		}

	}


});
