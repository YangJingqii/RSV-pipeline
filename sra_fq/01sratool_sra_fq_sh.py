
#01 分组数据
#01sratool_sra_fq_sh.py运行sartoolkit,sra转fastq
import os
wenjianjia_list = os.listdir('/mnt/alamo01/users/yangjingqi/RSV_sra/yjq_sra_bioproject_rsv')
#新建分组的文件夹
for i in wenjianjia_list:
    dirs = f'/mnt/alamo01/users/yangjingqi/RSV_sra/group/fastq_result/{i}'
    if not os.path.exists(dirs):
        os.makedirs(dirs)

        
for i in wenjianjia_list:
    with open(f'/mnt/alamo01/users/yangjingqi/RSV_sra/group/script/sra_fq/01sratool_sra_fq_sh/{i}.sh','w')as f:
        prj_path = f'/mnt/alamo01/users/yangjingqi/RSV_sra/yjq_sra_bioproject_rsv/{i}'
        sra_list = os.listdir(prj_path)
        
        for n in sra_list:
            sra_path = f'/mnt/alamo01/users/yangjingqi/RSV_sra/yjq_sra_bioproject_rsv/{i}/{n}'
            f.write(f'/mnt/alamo01/users/yangjingqi/app/sratoolkit/sratoolkit.3.0.5-centos_linux64/bin/fastq-dump --gzip --split-3 -X 25000 -O /mnt/alamo01/users/yangjingqi/RSV_sra/group/fastq_result/{i} /mnt/alamo01/users/yangjingqi/RSV_sra/yjq_sra_bioproject_rsv/{i}/{n}\n')
        























