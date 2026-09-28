from fastapi import APIRouter, Depends
import schemas, auth
import subprocess
import tempfile
import os
import time

router = APIRouter(prefix="/api/code", tags=["compiler"])

@router.post("/run", response_model=schemas.CodeRunResponse)
def run_code(request: schemas.CodeRunRequest):
    # DANGER: In a real production app, this MUST be sandboxed
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(request.code)
        temp_file_name = f.name
        
    start_time = time.time()
    try:
        process = subprocess.run(
            ['python', temp_file_name],
            input=request.input_data,
            capture_output=True,
            text=True,
            timeout=2.0
        )
        output = process.stdout
        error = process.stderr if process.stderr else None
    except subprocess.TimeoutExpired:
        output = ""
        error = "Execution timed out (2 seconds limit)"
    except Exception as e:
        output = ""
        error = str(e)
    finally:
        os.remove(temp_file_name)
        
    execution_time = time.time() - start_time
    
    return schemas.CodeRunResponse(
        output=output,
        error=error,
        execution_time=execution_time
    )
