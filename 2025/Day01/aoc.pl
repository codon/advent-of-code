#!/usr/bin/env perl

use strict;
use warnings;

$\ = $/;
$| = 1;

use Getopt::Long;
GetOptions(
    'debug!'  => \my $debug,
    'test!'   => \my $test,
    'part=i'  => \my $part,
    'start=i' => \my $start,
);

$start //= 0;
$part //= 1;

my $input_file = sprintf('input/%s.txt', $test ? 'test' : 'input');
my $func = $part == 2 ? \&part_2 : \&part_2;
print "part: $part; func: $func" if $debug;

my $pos = $start;
my $check = 0;
open my $input, '<', "$input_file" or die "cannot open $input_file: $!\n";
for my $line (<$input>) {
    chomp $line;
    print $line if $debug;
    my($dir, $clicks) = split('', $line, 2);

    $clicks = -$clicks if ($dir eq 'L');

#    print "<< $dir: $clicks" if $debug;
    my $val = $part == 1 ? part_1(\$pos, $clicks) : part_2(\$pos, $clicks);
    $check += $val;
}

print "checksum: $check";

sub part_1 {
    my ($pos, $clicks) = @_;
    print "pos: $pos => $$pos; clicks: $clicks" if $debug;
    my $new_pos = ($$pos + $clicks) % 100;

    $$pos = $new_pos;
    return $new_pos == 0 ? 1 : 0;
}

sub part_2 {
    my ($pos, $clicks) = @_;
#    print "pos: $pos => $$pos; clicks: $clicks" if $debug;
    my $zero_count = 0;

    my $new_pos = ($$pos + $clicks);
    if ($new_pos < 0 and $$pos != 0) {
        $zero_count++;
    }

    if ($new_pos >= 100) {
        $zero_count += int($new_pos / 100);
    }
    elsif ($new_pos <= -100) {
        $zero_count -= int($new_pos / 100);
    }
    elsif ($new_pos == 0) {
        $zero_count++;
    }

    $new_pos %= 100;

    print ">> $$pos + $clicks => $new_pos; zero count: $zero_count" if $debug;

    $$pos = $new_pos;
    return $zero_count;
}

