








label replay_A2:
    call iscene ("A2") from _call_iscene_623
    call iscene ("A2b") from _call_iscene_624
    call iscene ("A2c") from _call_iscene_625
    call iscene ("A2d") from _call_iscene_626
    call iscene ("A2f") from _call_iscene_627
    $ replay_end()



label replay_A8:
    call iscene ("A8") from _call_iscene_628
    call imenu ("choiceA8") from _call_imenu_52
    if _return == m1:
        call iscene ("A8a") from _call_iscene_629
        call iscene ("A8aa") from _call_iscene_630
        call iscene ("A8ab") from _call_iscene_631
    else:
        call iscene ("A8b") from _call_iscene_632
    call iscene ("A8c") from _call_iscene_633
    if seen_scene ("A8a"):
        call iscene ("A8d") from _call_iscene_634
    else:
        call iscene ("A8e") from _call_iscene_635
    call iscene ("A8f") from _call_iscene_636
    $ replay_end()



label replay_A10:
    call iscene ("A10") from _call_iscene_637
    call imenu ("choiceA10a") from _call_imenu_53
    if _return == m1:
        call iscene ("A10a") from _call_iscene_638
    elif _return == m2:
        call iscene ("A10b") from _call_iscene_639
    else:
        call iscene ("A10c") from _call_iscene_640
    $ replay_end()

label replay_A11_1:
    call iscene ("A11") from _call_iscene_641
    call iscene ("A11a") from _call_iscene_642
    call iscene ("A11b") from _call_iscene_643
    call iscene ("A11x") from _call_iscene_644
    $ replay_end()


label replay_A19:
    call iscene ("A19") from _call_iscene_645
    call iscene ("A19a") from _call_iscene_646
    call iscene ("A19c") from _call_iscene_647
    call iscene ("A19j") from _call_iscene_648
    call iscene ("A19d") from _call_iscene_649
    call iscene ("A19f") from _call_iscene_650
    call iscene ("A19g") from _call_iscene_651
    $ replay_end()


label replay_A21:
    call iscene ("A21") from _call_iscene_652
    call imenu ("choiceA21") from _call_imenu_54
    if _return == m1:
        call iscene ("A21a") from _call_iscene_653
        $ replay_end()
    call iscene ("A21b") from _call_iscene_654
    call iscene ("A21c") from _call_iscene_655
    $ replay_end()

label replay_A22:
    call iscene ("A22") from _call_iscene_656
    call iscene ("A22a") from _call_iscene_657
    $ replay_end()

label replay_A23_1:
    call iscene ("A23") from _call_iscene_658
    $ replay_end()

label replay_A23_2:
    call iscene ("A23a") from _call_iscene_659
    $ replay_end()


label replay_A24:
    call iscene ("A24") from _call_iscene_660
    call iscene ("A24d") from _call_iscene_661
    call iscene ("A24e") from _call_iscene_662
    $ replay_end()


label replay_A26:
    call iscene ("A26") from _call_iscene_663
    call iscene ("A26a") from _call_iscene_664
    call iscene ("A26e") from _call_iscene_665
    $ replay_end()

label replay_A26_1:
    call iscene ("A26b") from _call_iscene_666
    call imenu ("choiceA26") from _call_imenu_55
    if _return == m1:
        call iscene ("A26c") from _call_iscene_667
        $ replay_end()
    call iscene ("A26d") from _call_iscene_668
    $ replay_end()

label replay_A27_1:
    call iscene ("A27") from _call_iscene_669
    call iscene ("A27a") from _call_iscene_670
    call imenu ("choiceA27") from _call_imenu_56
    if _return == m1:
        call iscene ("A27b") from _call_iscene_671
        $ attraction_kenji += 1
        call iscene ("A27f") from _call_iscene_672
        $ replay_end()
    call iscene ("A27c") from _call_iscene_673
    call imenu ("choice2A27") from _call_imenu_57
    if _return == m1:
        call iscene ("A27h") from _call_iscene_674
        call iscene ("A27e") from _call_iscene_675
        $ replay_end()
    call iscene ("A27i") from _call_iscene_676
    jump_out A28

label replay_A27_2:
    call iscene ("A27d") from _call_iscene_677
    call iscene ("A27e") from _call_iscene_678
    $ replay_end()

label replay_A28:
    call iscene ("A28") from _call_iscene_679
    call iscene ("A28a") from _call_iscene_680
    call iscene ("A28b") from _call_iscene_681
    $ replay_end()

label replay_A29:
    call iscene ("A29") from _call_iscene_682
    call iscene ("A29x") from _call_iscene_683
    call iscene ("A29b") from _call_iscene_684
    call iscene ("A29c") from _call_iscene_685
    $ replay_end()

label replay_A30:
    call iscene ("A30") from _call_iscene_686
    call imenu ("choiceA30") from _call_imenu_58
    if _return == m2:
        call iscene ("A30a") from _call_iscene_687
        $ replay_end()
    call iscene ("A30b") from _call_iscene_688
    call iscene ("A30c") from _call_iscene_689
    call iscene ("A30d") from _call_iscene_690
    $ replay_end()


label replay_A31:
    call iscene ("A31") from _call_iscene_691
    call iscene ("A31c") from _call_iscene_692
    call iscene ("A31d") from _call_iscene_693
    call iscene ("A31e") from _call_iscene_694
    $ replay_end()


label replay_A38:
    call iscene ("A38") from _call_iscene_695
    $ replay_end()



label replay_H7:
    call iscene ("H7") from _call_iscene_696
    call iscene ("H7a") from _call_iscene_697
    call iscene ("H7c") from _call_iscene_698
    $ replay_end()

label replay_H22:
    call iscene ("H22") from _call_iscene_699
    call imenu ("choiceH22") from _call_imenu_59
    if _return == m1:
        call iscene ("H22a") from _call_iscene_700
    else:
        call iscene ("H22c") from _call_iscene_701
    $ replay_end()

label replay_H25:
    call iscene ("H25") from _call_iscene_702
    call iscene ("H25a") from _call_iscene_703
    call iscene ("H25c") from _call_iscene_704
    $ replay_end()




label replay_E11:
    call iscene ("E11a") from _call_iscene_705
    call iscene ("E11x") from _call_iscene_706
    call iscene ("E11z") from _call_iscene_707
    call imenu ("choiceE11") from _call_imenu_60
    if _return == m1:
        call iscene ("E11b") from _call_iscene_708
    else:
        call iscene ("E11c") from _call_iscene_709
    call iscene ("E11d") from _call_iscene_710
    $ replay_end()

label replay_E12:
    call iscene ("E12a") from _call_iscene_711
    call iscene ("E12b") from _call_iscene_712
    call iscene ("E12d") from _call_iscene_713
    $ replay_end()

label replay_E18:
    call iscene ("E18") from _call_iscene_714
    call iscene ("E18a") from _call_iscene_715
    call iscene ("E18x") from _call_iscene_716
    $ replay_end()

label replay_E26:
    call iscene ("E26") from _call_iscene_717
    call iscene ("E26a") from _call_iscene_718
    call iscene ("E26b") from _call_iscene_719
    call iscene ("E26e") from _call_iscene_720
    call iscene ("E26f") from _call_iscene_721
    call imenu ("choiceE26") from _call_imenu_61
    if _return == m2:
        call iscene ("E26d") from _call_iscene_722
        $ replay_end()
    call iscene ("E26c") from _call_iscene_723
    $ replay_end()

label replay_E30:
    call iscene ("E30") from _call_iscene_724
    call iscene ("E30a") from _call_iscene_725
    call iscene ("E30b") from _call_iscene_726
    call iscene ("E30d") from _call_iscene_727
    call iscene ("E30e") from _call_iscene_728
    $ replay_end()



label replay_R11:
    call iscene ("R11") from _call_iscene_729
    call imenu ("choiceR11aaa") from _call_imenu_62
    if _return == m1:
        call iscene ("R11a") from _call_iscene_730
        call iscene ("R11g") from _call_iscene_731
    elif _return == m2:
        call iscene ("R11b") from _call_iscene_732
        call iscene ("R11i") from _call_iscene_733
    elif _return == m3:
        call iscene ("R11c") from _call_iscene_734
        call iscene ("R11h") from _call_iscene_735
    elif _return == m4:
        call iscene ("R11d") from _call_iscene_736
        call iscene ("R11i") from _call_iscene_737
    elif _return == m5:
        call iscene ("R11e") from _call_iscene_738
        call iscene ("R11h") from _call_iscene_739
    else:
        call iscene ("R11f") from _call_iscene_740
        call iscene ("R11g") from _call_iscene_741
    call iscene ("R11j") from _call_iscene_742
    $ replay_end()

label replay_R12:
    call iscene ("R12") from _call_iscene_743
    call iscene ("R12b") from _call_iscene_744
    call iscene ("R12c") from _call_iscene_745
    call iscene ("R12e") from _call_iscene_746
    call iscene ("R12f") from _call_iscene_747
    $ replay_end()

label replay_R16:
    call iscene ("R16") from _call_iscene_748
    call imenu ("choiceR16") from _call_imenu_63
    if _return == m1:
        call iscene ("R16a") from _call_iscene_749
    else:
        call iscene ("R16b") from _call_iscene_750
    call iscene ("R16c") from _call_iscene_751
    call iscene ("R16d") from _call_iscene_752
    call iscene ("R16e") from _call_iscene_753
    $ replay_end()

label replay_R19:
    call iscene ("R19") from _call_iscene_754
    call iscene ("R19a") from _call_iscene_755
    call iscene ("R19b") from _call_iscene_756
    $ replay_end()

label replay_R28:
    call iscene ("R28") from _call_iscene_757
    call imenu ("choiceR28_1") from _call_imenu_64
    if _return == m1:
        call iscene ("R28a") from _call_iscene_758
    elif _return == m2:
        call iscene ("R28b") from _call_iscene_759
    else:
        $ replay_end()
    call iscene ("R28c") from _call_iscene_760
    $ replay_end()

label replay_R30:
    call iscene ("R30") from _call_iscene_761
    call iscene ("R30y") from _call_iscene_762
    call iscene ("R30z") from _call_iscene_763
    $ replay_end()

label replay_R36:
    call iscene ("R36") from _call_iscene_764
    call iscene ("R36a") from _call_iscene_765
    call iscene ("R36x") from _call_iscene_766
    $ replay_end()


label replay_S17:
    call iscene ("S17") from _call_iscene_767
    call iscene ("S17a") from _call_iscene_768
    call iscene ("S17x") from _call_iscene_769
    $ replay_end()

label replay_S22:
    call iscene ("S22") from _call_iscene_770
    call iscene ("S22a") from _call_iscene_771
    call iscene ("S22c") from _call_iscene_772
    call iscene ("S22h", is_h=True) from _call_iscene_773
    call iscene ("S22x") from _call_iscene_774
    $ replay_end()

label replay_S23:
    call iscene ("timeskip") from _call_iscene_775
    call iscene ("S23") from _call_iscene_776
    call iscene ("S23a") from _call_iscene_777
    call iscene ("S23x") from _call_iscene_778
    $ replay_end()

label replay_S26:
    call iscene ("S26") from _call_iscene_779
    call iscene ("S26a") from _call_iscene_780
    call iscene ("S26c") from _call_iscene_781
    $ replay_end()

label replay_S29_2:
    call iscene ("S29") from _call_iscene_782
    call iscene ("S29b") from _call_iscene_783
    call iscene ("S29x") from _call_iscene_784
    call iscene ("S29xb") from _call_iscene_785
    call iscene ("S29xba") from _call_iscene_786
    call iscene ("S29xbc") from _call_iscene_787
    call iscene ("S29y") from _call_iscene_788
    call iscene ("S29yb") from _call_iscene_789
    $ replay_end()

label replay_S34:
    call iscene ("S34") from _call_iscene_790
    call iscene ("S34b") from _call_iscene_791
    call iscene ("S34c") from _call_iscene_792
    $ replay_end()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
