
import os
from pathlib import Path



def md2html(fpath0, fpath1=None, template='bootstrap_menu'):
    '''
    Templates are available in:
    /Users/todd/.pandoc/templates/
    
    template options:
    - bootstrap_menu
    - clean_menu
    - easy_template
    - elegant_bootstrap_menu
    - uikit
    
    '''
    # cmd = f'pandoc -t html --embed-resources --standalone {fpathMD} -o {fpathHTML}'
    # cmd = f'pandoc -t html --embed-resources --standalone {fpathMD} -o {fpathHTML} --template=elegant_bootstrap_menu.html --toc'
    dir1   = os.path.join( os.path.dirname(fpath0), 'html')
    if not os.path.exists(dir0):
        os.mkdir( dir1 )
    
    if fpath1 is None:
        fpath1 = Path(fpath0).with_suffix('.html')
        fname1 = os.path.split(fpath1)[-1]
        fpath1 = os.path.join(dir1, fname1)
    cmd = f'pandoc -t html --embed-resources --standalone  --template={template}.html --toc {fpath0} -o {fpath1}'
    os.system( cmd )





dir0      = os.path.dirname( __file__ )
fpath     = os.path.join( dir0, '0_overview.md')
fpath     = os.path.join( dir0, '1_object_transformations.md')
fpath     = os.path.join( dir0, '2_mesh_modify.md')
fpath     = os.path.join( dir0, '3_curve2mesh.md')
md2html( fpath )








