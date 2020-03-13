import boto3
client = boto3.client('logs')
paginator = client.get_paginator('describe_log_groups')

def get_log_groups_list(paginator):
    log_groups_list = []
    for response in paginator.paginate():
        for log_group in response['logGroups']:
            log_groups_list.append(log_group)
    return log_groups_list

def delete_log_groups(log_groups_list):
    for log_group in log_groups_list:
        log_group_name = log_group['logGroupName']
        print(log_group_name) 
        response = client.delete_log_group(
                logGroupName=log_group_name
            )

log_groups = get_log_groups_list(paginator)
delete_log_groups(log_groups)