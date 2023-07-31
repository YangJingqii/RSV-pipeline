#01批量提交至qsub的脚本
#先生成然后复制

import os
list_dir = os.listdir('/mnt/alamo01/users/yangjingqi/RSV_sra/group/script/sra_fq/01sratool_sra_fq_sh')
with open('/mnt/alamo01/users/yangjingqi/RSV_sra/group/script/sra_fq/batch_qsub.txt','w')as f:
    for i in list_dir:
        f.write(f'qsub -o /mnt/alamo01/users/yangjingqi/RSV_sra/group/script/sra_fq/output.txt -e /mnt/alamo01/users/yangjingqi/RSV_sra/group/script/sra_fq/error.txt -V /mnt/alamo01/users/yangjingqi/RSV_sra/group/script/sra_fq/01sratool_sra_fq_sh/{i}\n')

