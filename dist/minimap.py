import subprocess
import os
try:
    from js import runMinimap2JS
    from pyodide.ffi import to_js
    # pyodide context
    async def runMinimap2(args):
        js_args = to_js(args)
        jsProxy = await runMinimap2JS(js_args)
        result = jsProxy.stdout
        del jsProxy
        del js_args
        return result
except ImportError:
    def runMinimap2(args):
        with open(os.devnull, 'w') as dev_null:
            out = subprocess.check_output(['minimap2'] + args, stderr=dev_null)
        return out.decode('utf-8')

async def main():
    target = 'target.fasta'
    reads = 'reads.fasta'
    threads = 1
    minimap2_args = ['-c', '-x', 'map-ont', '-t', str(threads), str(target), str(reads)]
    out = await runMinimap2(minimap2_args)
    print(out)