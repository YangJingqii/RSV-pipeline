
docker run -id -v /mnt/alamo01/users/yangjingqi/RSV_sra/group/08workflow_result_pair_each_project/12consensus_bcf/04consensus_all_in_one/cdhit/iqtree/iqtree_right:/data registry.servicemgr.biohpc:5000/library/iqtree:1.6.7 iqtree -s /data/RSV_all_with_ref_986_out.fasta -nt AUTO -bb 1000 -m GTR+F+G4
