
from utils.logging import set_logging_configuration
from hjaelpemiddelhuset_sms_sender import job

if __name__ == "__main__":
    set_logging_configuration()
    job()
