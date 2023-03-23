#!/usr/bin/env python3

"""
ecs-task-template.py - Copyright 2023 A Place For Mom Inc.
Authors:
  Mike 'Fuzzy' Partin <mike.partin@aplaceformom.com>
  Jugal Patel <jugal.patel@aplaceformom.com>

This script will templatize out the environment and secret portions
of an ECS task definition for consumption by the re-usable workflows
in GH actions.
"""

# Stdlib
import os
import sys
import json
import types
import datetime
import argparse

# 3rd party
import boto3


# Globals (ikk I threw up in my mouth a little)
AWS_REGION = os.getenv("AWS_REGION", "us-west-2")


def get_env(svc, tkn=" "):
    global AWS_REGION
    retv = []
    ssm = boto3.client("ssm", region_name=AWS_REGION)
    args = {
        "Path": f"/{svc}",
        "Recursive": True,
        "WithDecryption": True,
        "MaxResults": 10,
    }
    pgr = ssm.get_paginator("get_parameters_by_path")
    for page in pgr.paginate(**args).build_full_result()["Parameters"]:
        retv.append(types.SimpleNamespace(**page))
    return retv


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ECS environment and secret configuration generator."
    )
    parser.add_argument(
        "-A", "--appName", help="Specify the name of the service", required=True
    )
    args = parser.parse_args()
    print(args)
    output = json.loads(
        """{"family": "", "taskRoleArn": "", "executionRoleArn": "", "networkMode": "none", "containerDefinitions": [{"name": "", "image": "", "repositoryCredentials": {"credentialsParameter": ""}, "cpu": 0, "memory": 0, "memoryReservation": 0, "links": [""], "portMappings": [{"containerPort": 0, "hostPort": 0, "protocol": "udp", "name": "", "appProtocol": "http2", "containerPortRange": ""}], "essential": true, "entryPoint": [""], "command": [""], "environment": [], "environmentFiles": [{"value": "", "type": "s3"}], "mountPoints": [{"sourceVolume": "", "containerPath": "", "readOnly": true}], "volumesFrom": [{"sourceContainer": "", "readOnly": true}], "linuxParameters": {"capabilities": {"add": [""], "drop": [""]}, "devices": [{"hostPath": "", "containerPath": "", "permissions": ["write"]}], "initProcessEnabled": true, "sharedMemorySize": 0, "tmpfs": [{"containerPath": "", "size": 0, "mountOptions": [""]}], "maxSwap": 0, "swappiness": 0}, "secrets": [], "dependsOn": [{"containerName": "", "condition": "SUCCESS"}], "startTimeout": 0, "stopTimeout": 0, "hostname": "", "user": "", "workingDirectory": "", "disableNetworking": true, "privileged": true, "readonlyRootFilesystem": true, "dnsServers": [""], "dnsSearchDomains": [""], "extraHosts": [{"hostname": "", "ipAddress": ""}], "dockerSecurityOptions": [""], "interactive": true, "pseudoTerminal": true, "dockerLabels": {"KeyName": ""}, "ulimits": [{"name": "core", "softLimit": 0, "hardLimit": 0}], "logConfiguration": {"logDriver": "gelf", "options": {"KeyName": ""}, "secretOptions": [{"name": "", "valueFrom": ""}]}, "healthCheck": {"command": [""], "interval": 0, "timeout": 0, "retries": 0, "startPeriod": 0}, "systemControls": [{"namespace": "", "value": ""}], "resourceRequirements": [{"value": "", "type": "GPU"}], "firelensConfiguration": {"type": "fluentd", "options": {"KeyName": ""}}}], "volumes": [{"name": "", "host": {"sourcePath": ""}, "dockerVolumeConfiguration": {"scope": "shared", "autoprovision": true, "driver": "", "driverOpts": {"KeyName": ""}, "labels": {"KeyName": ""}}, "efsVolumeConfiguration": {"fileSystemId": "", "rootDirectory": "", "transitEncryption": "DISABLED", "transitEncryptionPort": 0, "authorizationConfig": {"accessPointId": "", "iam": "ENABLED"}}, "fsxWindowsFileServerVolumeConfiguration": {"fileSystemId": "", "rootDirectory": "", "authorizationConfig": {"credentialsParameter": "", "domain": ""}}}], "placementConstraints": [{"type": "memberOf", "expression": ""}], "requiresCompatibilities": ["EC2"], "cpu": "", "memory": "", "tags": [{"key": "", "value": ""}], "pidMode": "task", "ipcMode": "task", "proxyConfiguration": {"type": "APPMESH", "containerName": "", "properties": [{"name": "", "value": ""}]}, "inferenceAccelerators": [{"deviceName": "", "deviceType": ""}], "ephemeralStorage": {"sizeInGiB": 0}, "runtimePlatform": {"cpuArchitecture": "", "operatingSystemFamily": ""}}"""
    )
    for p in get_env(args.appName):
        print(p.Name)
        print(f"{p.Name.split('/')[-1]} = foo")
        section = p.Name.split("/")[-2]
        keyName = p.Name.split("/")[-1]
        sect = None
        if section in ("config", "environment", "environ", "env"):
            sect = "environment"
        elif section in ("secret", "secrets"):
            sect = "secrets"
        output["containerDefinitions"][0][sect].append(
            {"name": keyName, "valueFrom": p.ARN, "value": p.Value}
        )
    print(json.dumps(output, indent=2))
