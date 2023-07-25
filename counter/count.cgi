#!/usr/bin/perl

main();
exit;

sub main{
    $suffer = "0";
    $ip_visit = &GetHostByAddr($ENV{'REMOTE_ADDR'});
    $ip_visit = "$ip_visit\n";
    if(open (IN,"ip_visited.txt")){
        @ip_visited = <IN>;
    close (IN);
    }
    foreach my $ipad (@ip_visited){
        if($ip_visit eq $ipad){
            $suffer = "1";
        }
    }
    push(@ip_visited, "$ip_visit\n");
    if($suffer eq 0){
        print $write = countnumber();
        open (OUT, ">ip_visited.txt");
        print OUT @ip_visited;
        close (OUT);

        print "Content-Type: application/x-javascript\n\n";
        print $ip_visit;
        print "var p=\"$write\";\n";
        print "document.write(p);\n";

        if (open(FH, ">counter.txt")) {
            print FH $count;
            close(FH);
        } else {
            print "<p>�t�@�C���ɏ������߂܂���B</p>";
        }
    }else{
        $write = number();
        print "Content-Type: application/x-javascript\n\n";
        print $ip_visit;
        print "var p=\"$write\";\n";
        print "document.write(p);\n";
    }
}


sub GetHostByAddr {
    my($ip) = @_;
    my @addr = split(/\./, $ip);
    $ip = "@addr[0]@addr[1]@addr[2]@addr[3]";
    return $ip;
}

sub countnumber {
    if (open(FH, "counter.txt")) {
    $count = <FH>;
        close(FH);
    $count++;
    }
    return $count
}
sub number {
    if (open(FH, "counter.txt")) {
    $count = <FH>;
        close(FH);}
    return $count
}

