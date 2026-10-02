import subprocess
import sys
import logging
import time

# Configure enterprise-standard console logging layout
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def run_pipeline_stage(script_name, description):
    """
    Executes a specific script stage in the data architecture sequence
    and captures standard output buffers safely.
    """
    logging.info(f"INITIATING STAGE: {description} ({script_name})")
    
    try:
        # Execute script as a standalone background subprocess
        result = subprocess.run(
            [sys.executable, script_name], 
            check=True, 
            capture_output=True, 
            text=True
        )
        
        # Stream clean execution logs to console output
        for line in result.stdout.split('\n'):
            if line.strip():
                print(f"    | {line.strip()}")
                
        logging.info(f"SUCCESS: Stage completed smoothly.\n")
        
    except subprocess.CalledProcessError as err:
        logging.error(f"CRITICAL FAILURE during stage execution: {description}")
        logging.error(f"Process Error Stream:\n{err.stderr}")
        sys.exit(1)

if __name__ == "__main__":
    logging.info("========================================================")
    logging.info("   STARTING ENTERPRISE CORE ETL & ANALYTICS PIPELINE   ")
    logging.info("========================================================")
    
    pipeline_start = time.time()
    
    # Stage 1: Ingest mock transactions into relational data layer
    run_pipeline_stage("generate_data.py", "Data Generation & Local OLTP Ingestion")
    
    # Stage 2: Move records to centralized cloud storage data warehouse
    run_pipeline_stage("migrate_data.py", "Cloud Ingestion ETL - MySQL to Snowflake")
    
    # Stage 3: Train predictive analytical model structures
    run_pipeline_stage("predict_churn.py", "Machine Learning Training - XGBoost Customer Churn")
    
    # Stage 4: Trigger local flat-file extraction system loops
    run_pipeline_stage("export_data.py", "Flat File Backup Generation Sequence")
    
    total_execution_time = time.time() - pipeline_start
    
    logging.info("========================================================")
    logging.info(f"PIPELINE EXECUTION COMPLETE | Total Duration: {total_execution_time:.2f}s")
    logging.info("========================================================")
