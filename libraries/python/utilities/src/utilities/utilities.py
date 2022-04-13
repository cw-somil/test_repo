import boto3
import consulate
import yaml
import re


def lower_and_strip(val: str) -> str:
    """Lowercase and remove trailing spaces from string

    Args:
        val: input string

    Returns:
        cleaned string

    """
    return val.strip().lower()


def get_value_from_label(label: str, key: str, default='') -> str:
    """UDF utility. Gets value from pipe separated key value string.

    Args:
        label: The pipe separated string to be passed.
        key: The key whose value is to be returned.
        default: returns default if key not found.

    Returns:
        the value corresponding to the key in the label.
    """

    pairs = [tuple(map(lower_and_strip, pair.split("="))) for pair in label.strip().split("|")]
    for pair in pairs:
        if len(pair) == 2 and pair[0] == key.lower():
            return pair[1]
    return default


def get_value_from_cookie(cookie, key, default=''):
    key_pattern = re.compile(key + "=(.*?)(?=;\\s[^;\\s=]*=|;?$)")
    if key_pattern.search(cookie):
        return key_pattern.search(cookie).group(1)
    return default


def load_config(file_name="config.yaml"):
    with open(file_name, "r") as f:
        return yaml.safe_load(f)


def get_consul_key(consul_ip, key):
    consul = consulate.Consul(consul_ip)
    val = consul.kv[key]
    print(f"Consul IP : {consul_ip} Key: {key} Value: {val}")
    # Get the value for the release_flag, if not set, raises AttributeError
    return val


def get_s3_object(bucket, key, public_key, secret_key, region_name="ap-south-1"):
    if public_key and secret_key:
        session = boto3.Session(aws_access_key_id=public_key,
                                aws_secret_access_key=secret_key)
    else:
        session = boto3.Session()
    s3 = session.resource("s3", region_name=region_name)
    res = s3.Object(bucket, key)
    return res.get()['Body'].read().decode('utf-8')

# if __name__ == "__main__":
#     consul_ip = "10.10.20.113"
#     public_key = get_consul_key(consul_ip, "KMSAccessKeys/dev/KMSAccessKey")
#     secret_key = get_consul_key(consul_ip, "KMSAccessKeys/dev/KMSAccessSecret")
#     data = get_s3_object("cw-dev-config-keys", "AB_ConnectionMySqlMasterAutobiz", public_key, secret_key)
#     print(data)
