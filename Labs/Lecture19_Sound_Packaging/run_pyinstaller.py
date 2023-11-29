import os
import shutil
import tomllib
import PyInstaller.__main__
import importlib

def get_module_installation_path(module_name):
    try:
        module_spec = importlib.util.find_spec(module_name)
        if module_spec is not None:
            return os.path.dirname(os.path.abspath(module_spec.origin))
    except ImportError:
        pass

    return None



print(' py to exe with PyInstaller '.center(80, '='))

settings_file = 'pyinstaller_settings.toml'
print(f'1. 설정 파일 {settings_file} 을 분석합니다......')
try:
    f = open(settings_file, 'rb')
    config = tomllib.load(f)
    main_file = config['main_file']
    data_files = config['data_files']
    data_folders = config['data_folders']
except:
    print(f'설정 파일 {settings_file} 파일을 읽는 과정에서 문제가 발생했습니다. 파일 존재 및 이상 여부를 확인하세요. 변환을 중단합니다.')
    exit(-1)


# 설정된 파일들이 실제 존재하는지 체크

print(f'메인 소스 파일: {main_file}')
print(f'데이터 파일: {data_files}')
print(f'데이터 폴더: {data_folders}')

if not os.path.exists(main_file):
    print(f'메인 파일 {main_file}이 존재하지 않습니다. 변환을 중단합니다.')
    exit(-1)

for fn in data_files:
    if not os.path.exists(fn):
        print(f'데이터 파일 {fn}이 존재하지 않습니다. 변환을 중단합니다.')
        exit(-1)

for dn in data_folders:
    if not os.path.exists(dn):
        print(f'데이터 폴더 {dn}이 존재하지 않습니다. 변환을 중단합니다.')
        exit(-1)

print('2. 변환 중입니다......')
dist_path = os.path.expanduser('~') + '/Documents/pyinstaller/dist'
work_path = os.path.expanduser('~') + '/Documents/pyinstaller/build'

# dist_path = dist_path.replace('\\', '/')
# work_path = work_path.replace('\\', '/')


PyInstaller.__main__.run([
    main_file,
    '--clean',
    '--noconfirm',
    '--log-level=ERROR',
    '--python-option=O',
    f'--distpath={dist_path}',
    f'--workpath={work_path}',
    '--noconsole'
])

print('3. 관련 파일들을 복사합니다......')

# sdl dll 파일들을 찾아서, pico2d 폴더로 복사
sdl2dll_path = get_module_installation_path('sdl2dll')+'/dll'
main_name = os.path.splitext(main_file)[0]
dist_path += f'/{main_name}'
shutil.copytree(sdl2dll_path, dist_path + '/pico2d')
print(f'Pico2d 복사: {sdl2dll_path} -----> {dist_path + "/pico2d"}')
for fn in data_files:
    shutil.copy(fn, dist_path)
    print(f'데이터 파일 복사: {fn} -----> {dist_path}')

for dn in data_folders:
    shutil.copytree(dn, f'{dist_path}/{dn}')
    print(f'데이터 폴더 복사: {dn} -----> {dist_path}/{dn}')


print('4. 변환이 완료됐습니다......')
print(f'출력 폴더: File "{dist_path}", line {0}')

