# vimms_django
SG=StarGate，SGScrapy工程主要是后端抓取、入库功能

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

2. 打开本地安装的mass_spec_utils的gnps.py文件：
比如我的在： /usr/local/lib/python3.7/site-packages/mass_spec_utils/library_matching/gnps.py
的代码有bug：from .spectrum import SpectralRecord 改为from spectrum import SpectralRecord

3. 
vimms_django/vimms_django/documents/simple_ms1/example_data/hmdb_compounds.p 

4. time to process , take too long
DataGenerator.py  need to speedup function: extract_hmdb_metabolite
from line 19, extract_hmdb_metabolite function change into:

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




5. /usr/local/lib/python3.7/site-packages/vimms-1.1.0-py3.7.egg/vimms/Controller/tree.py
    nedd to change line 36:
            # rt = self.last_ms1_scan.rt
            rt = self.scan_to_process.rt

            # then get the last ms1 scan, select bin walls and create scan locations
            # mzs = self.last_ms1_scan.mzs
            mzs = self.scan_to_process.mzs

6. /usr/local/lib/python3.7/site-packages/vimms-1.1.0-py3.7.egg/vimms/MassSpec.py
line 145 add following init function logic: 
        if self.get(ScanParameters.PRECURSOR_MZ) is None:
            return [[(0, 0)]]