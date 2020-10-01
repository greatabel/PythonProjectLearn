# vimms_django


original requirements：
需求详细描述：已经有源码的python软件（Vimms 一个质谱模拟器）将其变成一个web应用程序（django），
可以上传数据（file）然后运行它以观察从不同数据采集参数获得的输出。
注意事项及程序环境：ViMMS是Python软件包，可以从Python脚本和交互式环境（如Jupyter Notebook）中访问，
用户可以在其中指向自己的光谱文件或化合物列表，以开始对自己的数据使用ViMMS。 
输出有几种不同数据的采集参数选择


************** attention please **************

vimms库还非常不成熟，因此移植时候需要修复移植库的bug：
1. exmaple在最新的代码上运行不起来，不要使用pip安装，也不要使用github上master分支1.0.0, 1.1.0，
  而要去客户发给我的工程代码解压后本地安装（发过来的应该是1.1.0的某个分支代码）：
（比如我的在你传给我的文件解压下 vimms-master 有setup.py的目录下执行：）
先执行 python3 setup.py build
然后执行 python3 setup.py install


2. vimms包作者使用的一个他自己写的库（打开本地安装的mass_spec_utils的gnps）有bug，移植需要修复：

打开本地安装的mass_spec_utils的gnps.py文件，比如我的python包装在/usr/local/lib/python3.7/site-packages下，
所以去： /usr/local/lib/python3.7/site-packages/mass_spec_utils/library_matching/gnps.py
的代码有bug修复下：from .spectrum import SpectralRecord 改为 from spectrum import SpectralRecord

----------- start 题外话 --------
如果你部署在linux上想查看python的包路径,可以进入python然后执行：
from distutils.sysconfig import get_python_lib
print(get_python_lib())
----------- end 题外话 --------

3.  要想能上传 处理整个你email附件发给我的example_data.zip 压缩包，需要有hmdb_compounds.p文件
    

    把 hmdb_compounds.p 从 hmdb_metabolites.xml （一个超过4G大小的xml）
    中解压和处理在intel i7 + 8G内存上耗费3-4小时，太长时间了。

    最好使用我已经处理好的hmdb_compounds.p（我会打包发给你），放在
    自己本机相关目录中，相对路径为：
    vimms_django/vimms_django/documents/simple_ms1/example_data/hmdb_compounds.p 
    
    具体工程路径层次截图为：
    ![image][requirement_docs/readme0.jpg]
 
    如果学校想看如果自己要复现从压缩包处理出hmdb_compounds.p，需要做如下处理：
    3.1 配置位置：修改工程中pre_proces.py中的24行 =>
   url = '/Users/abel/Downloads/hmdb_metabolites.xml' 为你自己本地文件中hmdb_metabolites.xml的位置，
   hmdb_metabolites.xml为从hmdb_metabolites.zip中解压，根据vimms文档，需要从：
   http://www.hmdb.ca/system/downloads/current/hmdb_metabolites.zip 下载该zip包。

    3.2 就需要改进vimms包作者相关代码，让代码可以处理巨大的xml文件：
    比如我的该文件在：/usr/local/lib/python3.7/site-packages/vimms-1.1.0-py3.7.egg/vimms/DataGenerator.py
    DataGenerator.py  need to speedup function: extract_hmdb_metabolite
    从 line 19, extract_hmdb_metabolite function 修改为:

def extract_hmdb_metabolite(in_file, delete=True):
    logger.debug('Extracting HMDB metabolites from %s' % in_file)

    count = 0
    # loops through file and extract the necessary element text to create a DatabaseCompound
    db = xml.etree.ElementTree.parse(f).getroot()
    logger.debug('##')
    compounds = []
    prefix = '{http://www.hmdb.ca}'
    for metabolite_element in db:
        count += 1
        if count % 1000 == 0:
            logger.debug('count=%s' % count)
        row = [None, None, None, None, None, None]
        for element in metabolite_element:
            if element.tag == (prefix + 'name'):
                row[0] = element.text
            elif element.tag == (prefix + 'chemical_formula'):
                row[1] = element.text
            elif element.tag == (prefix + 'monisotopic_molecular_weight'):
                row[2] = element.text
            elif element.tag == (prefix + 'smiles'):
                row[3] = element.text
            elif element.tag == (prefix + 'inchi'):
                row[4] = element.text
            elif element.tag == (prefix + 'inchikey'):
                row[5] = element.text

        # if all fields are present, then add them as a DatabaseCompound
        if None not in row:
            compound = DatabaseCompound(row[0], row[1], row[2], row[3], row[4], row[5])
            compounds.append(compound)
    logger.info('Loaded %d DatabaseCompounds from %s' % (len(compounds), in_file))

    # f.close()
    # if zf is not None:
    #     zf.close()

    if delete:
        logger.info('Deleting %s' % in_file)
        os.remove(in_file)

    return compounds





4. /usr/local/lib/python3.7/site-packages/vimms-1.1.0-py3.7.egg/vimms/Controller/tree.py
   需要修复vimms包的bug，位置 line 36:
            # rt = self.last_ms1_scan.rt
            rt = self.scan_to_process.rt

            # then get the last ms1 scan, select bin walls and create scan locations
            # mzs = self.last_ms1_scan.mzs
            mzs = self.scan_to_process.mzs


5. /usr/local/lib/python3.7/site-packages/vimms-1.1.0-py3.7.egg/vimms/MassSpec.py
   需要修复vimms包的bug，位置 line 145 add 添加 init function logic: 
        if self.get(ScanParameters.PRECURSOR_MZ) is None:
            return [[(0, 0)]]


6. （暂时可能不需要了，防止将来万一需要）如果后续需要跑vary n in topn, 注意就需要配置R环境运行相关 vimms包的R脚本才可以
R脚本包作者放在：example_data/results/beer1pos 的 extract_peaks.R
运行：RScript extract_peaks.R
提前需要装好所有运行extract_peaks.R所需要的R库的依赖，需要使用BiocManager安装依赖，在RScript的
解释器中执行：
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("xcms")


7. 执行test需要到有manager.py的目录(相对工程目录为vimms_django/vimms_django下），
然后bash命令行中执行：python3 manage.py test
如果正常反馈为：

Destroying test database for alias 'default'...
(samaritan1)abeltekiMacBook-Pro:vimms_django abel$ python3 manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.004s

OK

如果错误反馈为：
ERROR: test_model_use (vimms_app.tests.DocumentModelTestCase)
Document upload/download are correctly identified

----------------------------------------------------------------------
Ran 1 test in 0.010s

FAILED (errors=1)
Destroying test database for alias 'default'...