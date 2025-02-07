import os, base64, string, random, shutil, autopep8, time, sys, zipfile, re, base58, subprocess, py_compile
from pathlib import Path
from pathlib import Path
from datetime import datetime, timedelta
import string as st
base64Enc = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"
def xor_encrypt(data: str, key: str) -> bytes:
    data_bytes = data.encode('utf-8')
    key_bytes = key.encode('utf-8')
    return bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data_bytes)])

def xor_decrypt(encrypted_data: bytes, key: str) -> str:
    key_bytes = key.encode('utf-8')
    decrypted_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(encrypted_data)])
    return decrypted_bytes.decode('utf-8')

def encrypt_code(source_code: str, key: str) -> str:
    encrypted_data = xor_encrypt(source_code, key)
    base64_encoded = base64.b64encode(encrypted_data).decode('utf-8')
    return base64_encoded
zip_path='Joker'
R='.ELF/arm64-v8a'
T='.ELF/armeabi-v7a'
Ff ='''E=print
B=''
A=chr
import zipfile as I,os as C,shutil as K,tempfile as L,sys as D,platform as M
def F():
	N=C.path.dirname(C.path.abspath(D.argv[0]));G=L.mkdtemp()
	try:
		O=C.path.abspath(D.argv[0])
		with I.ZipFile(O,'r')as P:P.extractall(G)
		F=M.machine();J={(lambda s:B.join(A(B^151)for B in s))([246,229,250,225,160,251]):(lambda s:B.join(A(B^11)for B in s))([106,121,102,110,106,105,98,38,125,60,106]),(lambda s:B.join(A(B^69)for B in s))([36,55,40,51,125,41]):(lambda s:B.join(A(B^179)for B in s))([210,193,222,214,210,209,218,158,197,132,210]),(lambda s:B.join(A(B^134)for B in s))([231,244,235]):(lambda s:B.join(A(B^177)for B in s))([208,195,220,212,208,211,216,156,199,134,208]),(lambda s:B.join(A(B^54)for B in s))([87,87,68,85,94,0,2]):(lambda s:B.join(A(B^4)for B in s))([101,118,105,50,48,41,114,60,101]),(lambda s:B.join(A(B^130)for B in s))([227,240,239,180,182]):(lambda s:B.join(A(B^199)for B in s))([166,181,170,241,243,234,177,255,166]),(lambda s:B.join(A(B^189)for B in s))([197,133,139]):(lambda s:B.join(A(B^200)for B in s))([176,240,254]),(lambda s:B.join(A(B^108)for B in s))([5,90,84,90]):(lambda s:B.join(A(B^39)for B in s))([95,31,17]),(lambda s:B.join(A(B^173)for B in s))([213,149,155,242,155,153]):(lambda s:B.join(A(B^71)for B in s))([63,127,113,24,113,115]),(lambda s:B.join(A(B^208)for B in s))([177,189,180,230,228]):(lambda s:B.join(A(B^176)for B in s))([200,136,134,239,134,132])}
		if F not in J:E((lambda s:B.join(A(B^171)for B in s))([254,197,216,222,219,219,196,217,223,206,207,139,202,217,200,195,194,223,206,200,223,222,217,206,145,139,142,216])%F);D.exit(1)
		Q=J[F];H=C.path.join(G,Q)
		if not C.path.exists(H):E((lambda s:B.join(A(B^97)for B in s))([52,15,18,20,17,17,14,19,21,4,5,65,0,19,2,9,8,21,4,2,21,20,19,4,91,65,68,18])%F);D.exit(1)
		C.chmod(H,493);C.chdir(N);R=(lambda s:B.join(A(B^128)for B in s))([229,248,240,239,242,244,160,204,196,223,204,201,194,210,193,210,217,223,208,193,212,200,189,164,204,196,223,204,201,194,210,193,210,217,223,208,193,212,200,186,165,243,175,236,233,226,160,166,166,160,229,248,240,239,242,244,160,208,217,212,200,207,206,200,207,205,197,189,165,243,160,166,166,160,229,248,240,239,242,244,160,208,217,212,200,207,206,223,197,216,197,195,213,212,193,194,204,197,189,165,243,160,166,166,160,165,243,160,165,243])%(D.prefix,D.prefix,D.executable,H,' '.join(D.argv[1:]));C.system(R)
	except I.BadZipFile:E((lambda s:B.join(A(B^206)for B in s))([139,188,188,161,188,244,238,154,166,171,238,180,167,190,238,168,167,162,171,238,167,189,238,173,161,188,188,187,190,186,171,170,238,161,188,238,160,161,186,238,175,238,180,167,190,238,168,167,162,171,224]))
	except Exception as S:E((lambda s:B.join(A(B^195)for B in s))([130,173,227,166,177,177,172,177,227,172,160,160,182,177,177,166,167,249,227,230,176])%S)
	finally:K.rmtree(G)
if __name__==(lambda s:B.join(A(B^30)for B in s))([65,65,115,127,119,112,65,65]):F()'''
#if len(sys.argv) < 2:
    #print("python JokerPy Filename.py Out.py")
#else:
file="enc.py"
Bo_name="ENC-BY-JOKER.py"
def gw(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def gw2(length):
    return ''.join(random.choices(string.ascii_letters, k=length))
def JokerPyObfuscateExit(data, key):
    Layers = len(key)
    encrypted_text = ''.join(chr(ord(c) ^ ord(key[i % Layers])) for i, c in enumerate(data))
    merged_text = ''.join(encrypted_text[i] + key[i % Layers] for i in range(len(encrypted_text)))
    return merged_text
def generate_random_name(size=8):
    return ''.join(random.choices(string.ascii_letters, k=size))
def JokerNinja(data, key):
    Layers = len(key)
    encrypted_text = ''.join(chr(ord(c) ^ ord(key[i % Layers])) for i, c in enumerate(data))
    merged_text = ''.join(encrypted_text[i] + key[i % Layers] for i in range(len(encrypted_text)))
    return merged_text
def remove_comments(input_file, output_file):
    with open(input_file, 'r') as input_f:
        content=input_f.read()
    output_content=''
    in_comment=False
    i=0
    while i < len(content):
        if content[i:i+2] == '/*':
            in_comment=True
            i += 2
            continue
        elif content[i:i+2] == '*/':
            in_comment=False 
            i += 2
            continue
        if not in_comment:
            output_content += content[i]
        i += 1
    with open(output_file, 'w') as output_f:
        output_f.write(output_content)
if not os.path.exists("Nawabi/"):
    os.mkdir("Nawabi")
if not os.path.exists("Elf/"):
    os.mkdir("Elf")
def g(name):
    with open(f"Nawabi/{name}", "r") as w:
        a=w.read()
    key = '\u200b'
    Text = JokerPyObfuscateExit(a, key)
    cod = f'''
def JokerPyObfuscateExit(data_with_key, Layers):
    encrypted_text = ''.join(data_with_key[i*2] for i in range(len(data_with_key) // 2))
    key = ''.join(data_with_key[i*2 + 1] for i in range(len(data_with_key) // 2))
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(encrypted_text))
Layers = {len(key)}
Enc = {Text!r}
Obfuscate = JokerPyObfuscateExit(Enc, Layers)
exec(compile(code:=Obfuscate, filename="<lambda>", mode="exec"))'''
    print("\x1b[1;92m\x1b[38;5;49mENCRYPTING...!!")
    os.remove(f"Nawabi/{name}")
    with open(f"Nawabi/{name}", 'w') as o: 
        o.write(cod)
    print("\x1b[1;92m\x1b[38;5;48mADDING CYTHON LAYER..! ")
    print('\033[0m')
    try:
        subprocess.run(f"cythonize Nawabi/{name}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print('THERE IS A SYNTEX ERROR.')
    name2=name.replace(".py", ".c")
    with open(f"Nawabi/{name2}", "r") as f:
        if len(f.read()) < 1000:
            print("failed cython error")
            exit()
    remove_comments(f"Nawabi/{name2}", f"Nawabi/{name2}")
    name2=name.replace(".py", "")
    c='''
#ifdef __FreeBSD__
#include <dede.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(Win32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m=fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m=NULL;
      __pyx_module_is_main_'''+name2+'''=1;
      #if PY_MAJOR_VERSION < 3
          init'''+name2+'''();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m=PyInit_'''+name2+'''();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef=(PyModuleDef *) m;
              PyObject *modname=PyUnicode_FromString("__main__");
              m=NULL;
              if (modname) {
                  m=PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m=PyInit_'''+name2+'''();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(Win32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize=strlen(arg);
#else
    size_t argsize=mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res=(wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count=mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp=res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize=strlen(arg) + 1;
    res=(wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in=(unsigned char*)arg;
    out=res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted=mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++=0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++=0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res=(wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in=(unsigned char*)arg;
    out=res;
    while(*in)
        if(*in < 128)
            *out++=*in++;
        else
            *out++=0xdc00 + *in++;
    *out=0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy=(wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2=(wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc=strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res=0;
        setlocale(LC_ALL, "");
        for (i=0; i < argc; i++) {
            argv_copy2[i]=argv_copy[i]=__Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res=1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res=__Pyx_main(argc, argv_copy);
        for (i=0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif
'''
    with open(f"Nawabi/{name2}.c", 'r') as input_f:
        co=input_f.read() + c + "\"\"\""
    a=f'''import os
import sys
PREFIX=sys.prefix
EXECUTE_FILE=".ELF/armeabi-v7a"
EXPORT_PYTHONHOME ="export PYTHONHOME="+sys.prefix
EXPORT_PYTHON_EXECUTABLE ="export PYTHON_EXECUTABLE="+ sys.executable
RUN="./"+ EXECUTE_FILE
if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME +"&&"+ EXPORT_PYTHON_EXECUTABLE +"&&"+ RUN)
    exit(0)
C_SOURCE=r"""'''
    b=f'''
C_FILE ="{name2}.c"
PYTHON_VERSION=".".join(sys.version.split(" ")[0].split(".")[:-1]) 
COMPILE_FILE=('gcc -I ' + PREFIX + '/include/python' + PYTHON_VERSION +  ' -o ' + EXECUTE_FILE + ' ' + C_FILE + ' -I' + PREFIX + '/lib -lpython' + PYTHON_VERSION)
with open(C_FILE,'w') as f:
    f.write(C_SOURCE)
os.makedirs(os.path.dirname(EXECUTE_FILE),exist_ok=True)
os.system(EXPORT_PYTHONHOME +"&&"+ EXPORT_PYTHON_EXECUTABLE +"&&" + COMPILE_FILE +"&&"+ RUN)
os.remove(C_FILE)'''
    o=f'''import os
import sys
PREFIX=sys.prefix
EXECUTE_FILE=".ELF/arm64-v8a"
EXPORT_PYTHONHOME ="export PYTHONHOME="+sys.prefix
EXPORT_PYTHON_EXECUTABLE ="export PYTHON_EXECUTABLE="+ sys.executable
RUN="./"+ EXECUTE_FILE
if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME +"&&"+ EXPORT_PYTHON_EXECUTABLE +"&&"+ RUN)
    exit(0)
C_SOURCE=r"""'''
    iu=f'''
C_FILE ="{name2}.c"
PYTHON_VERSION=".".join(sys.version.split(" ")[0].split(".")[:-1]) 
COMPILE_FILE=('gcc -I' + PREFIX + '/include/python' + PYTHON_VERSION +  ' -o ' + EXECUTE_FILE + ' ' + C_FILE + ' -I' + PREFIX + '/lib -lpython' + PYTHON_VERSION)
with open(C_FILE,'w') as f:
    f.write(C_SOURCE)
os.makedirs(os.path.dirname(EXECUTE_FILE),exist_ok=True)
os.system(EXPORT_PYTHONHOME +"&&"+ EXPORT_PYTHON_EXECUTABLE +"&&" + COMPILE_FILE +"&&"+ RUN)
os.remove(C_FILE)'''
    code=a + co + b
    code1=o + co + iu
    with open('Elf/T.py', 'w') as output_f:
        output_f.write(code)
    with open('Elf/R.py', 'w') as output_f:
        output_f.write(code1)
    os.system('python3.9 Elf/T.py')
    os.system('python3.11 Elf/R.py')
    with open(R,'rb') as f: 
        D=f.read()
    with open(T,'rb') as f: 
        Y=f.read()
    def create_zip_with_so_files_and_main(zip_path):
        with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as zipf:
            zipf.writestr('__main__.py',Ff)
            zipf.writestr('arm64-v8a',D)
            zipf.writestr('armeabi-v7a',Y)
    create_zip_with_so_files_and_main(zip_path)
    with open('Joker','rb') as F:
        j=F.read()
    V=base64.b64encode(j)
    v=f'''
from os import system as NAWABI
from base64 import b64decode as JOKER64
JOKER={V}
with open('.FUCK','wb')as HA:HA.write(JOKER64(JOKER));NAWABI('python .FUCK')'''
    with open(f'ENC-BY-JOKER.py','w') as F:
        F.write(v)
    print(f'Done Encode Save In done1.py')
    return f"Nawabi/{name}"
name=file.split("/")[-1]
name2=gw(4) + ".py"
shutil.copyfile(file, f"Nawabi/{name2}")
a=g(name2)
m=f'Nawabi/{name2}'
n=f'Nawabi/{name2}.c'
os.remove(m)
n=n.replace('.py','')
os.remove(n)
shutil.rmtree('.ELF')
os.remove(zip_path)
shutil.rmtree('Elf')