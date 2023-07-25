#!/usr/bin/perl
system ("/bin/sh /virtual/yasyasyu/public_html/data/target.sh");
if ($? == 0) {
	print "Content-type: text/html\n\n";
	print "<html>\n";
	print "<body>\n";
	print "hoge\n";
	print "</body>\n";
	print "</html>\n";
} else {
	print "Content-type: text/html\n\n";
	print "<html>\n";
	print "<body>\n";
	print "err\n";
	print "</body>\n";
	print "</html>\n";
}