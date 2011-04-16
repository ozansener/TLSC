# -*- coding: utf-8 -*-

import classify_lang

c = classify_lang.classify_lang("abc.xml")

#cumle = "State media reported that small demonstrations had taken place in different parts of the country and security forces did not intervene"

cumle =  "Gaziantepte Kaçakçılık ve Organize Suçlarla Mücadele Büro Amirliği ekipleri, uyuşturucu madde satışı yapıldığına dair bir istihbaratı değerlendirerek Vatan Mahallesi, 92. Sokak üzerinde belirlenen adrese baskın yapmak için bölgeye gitti. Sokağın alt tarafında tedbirler alındıktan sonra bir sivil polis memuru keşif yapmak için sokağa girdi. Bu sırada daha önce kızlarının kaçırılacağı yönünde duyum alınan ve isimleri açıklanmayan şahıslar, sivil polisi kızlarını kaçırmak üzere gelen kişi olduğunu zannederek kovalamaya başladı. Sivil polis sokağın alt tarafında bekleyen ekip arkadaşlarının yanına dönmek için koşmaya başlayınca, bu kez kendisini kovalayan şahıslar üzerlerinde taşıdıkları silahla ateş etti. Açılan ateş sonucu seken kurşunlar parkta oturan 40 yaşındaki 7 çocuk annesi Ayşe Kartal ile 2 yaşındaki kızı Büşra Kartal'a isabet etti. Anne ve kızı yaralanırken, silah sesleri üzerine sokağın altında bekleyen diğer polis memurları, hemen sokak içerisine girerek silahlı saldırıya uğrayan arkadaşlarını yara almadan kurtardı."

cumle = cumle.decode("utf-8")

c.classify(cumle)
