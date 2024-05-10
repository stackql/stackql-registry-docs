---
title: pipes
hide_title: false
hide_table_of_contents: false
keywords:
  - pipes
  - pipes
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>pipes</code> in a region or to create or delete a <code>pipes</code> resource, use <code>pipe</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Pipes::Pipe Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pipes.pipes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
name
FROM aws.pipes.pipes
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "RoleArn": "{{ RoleArn }}",
 "Source": "{{ Source }}",
 "Target": "{{ Target }}"
}
>>>
--required properties only
INSERT INTO aws.pipes.pipes (
 RoleArn,
 Source,
 Target,
 region
)
SELECT 
{{ .RoleArn }},
 {{ .Source }},
 {{ .Target }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Description": "{{ Description }}",
 "DesiredState": "{{ DesiredState }}",
 "Enrichment": "{{ Enrichment }}",
 "EnrichmentParameters": {
  "InputTemplate": "{{ InputTemplate }}",
  "HttpParameters": {
   "PathParameterValues": [
    "{{ PathParameterValues[0] }}"
   ],
   "HeaderParameters": {},
   "QueryStringParameters": {}
  }
 },
 "LogConfiguration": {
  "S3LogDestination": {
   "BucketName": "{{ BucketName }}",
   "Prefix": "{{ Prefix }}",
   "BucketOwner": "{{ BucketOwner }}",
   "OutputFormat": "{{ OutputFormat }}"
  },
  "FirehoseLogDestination": {
   "DeliveryStreamArn": "{{ DeliveryStreamArn }}"
  },
  "CloudwatchLogsLogDestination": {
   "LogGroupArn": "{{ LogGroupArn }}"
  },
  "Level": "{{ Level }}",
  "IncludeExecutionData": [
   "{{ IncludeExecutionData[0] }}"
  ]
 },
 "Name": "{{ Name }}",
 "RoleArn": "{{ RoleArn }}",
 "Source": "{{ Source }}",
 "SourceParameters": {
  "FilterCriteria": {
   "Filters": [
    {
     "Pattern": "{{ Pattern }}"
    }
   ]
  },
  "KinesisStreamParameters": {
   "BatchSize": "{{ BatchSize }}",
   "DeadLetterConfig": {
    "Arn": "{{ Arn }}"
   },
   "OnPartialBatchItemFailure": "{{ OnPartialBatchItemFailure }}",
   "MaximumBatchingWindowInSeconds": "{{ MaximumBatchingWindowInSeconds }}",
   "MaximumRecordAgeInSeconds": "{{ MaximumRecordAgeInSeconds }}",
   "MaximumRetryAttempts": "{{ MaximumRetryAttempts }}",
   "ParallelizationFactor": "{{ ParallelizationFactor }}",
   "StartingPosition": "{{ StartingPosition }}",
   "StartingPositionTimestamp": "{{ StartingPositionTimestamp }}"
  },
  "DynamoDBStreamParameters": {
   "BatchSize": "{{ BatchSize }}",
   "DeadLetterConfig": null,
   "OnPartialBatchItemFailure": null,
   "MaximumBatchingWindowInSeconds": "{{ MaximumBatchingWindowInSeconds }}",
   "MaximumRecordAgeInSeconds": "{{ MaximumRecordAgeInSeconds }}",
   "MaximumRetryAttempts": "{{ MaximumRetryAttempts }}",
   "ParallelizationFactor": "{{ ParallelizationFactor }}",
   "StartingPosition": "{{ StartingPosition }}"
  },
  "SqsQueueParameters": {
   "BatchSize": "{{ BatchSize }}",
   "MaximumBatchingWindowInSeconds": "{{ MaximumBatchingWindowInSeconds }}"
  },
  "ActiveMQBrokerParameters": {
   "Credentials": null,
   "QueueName": "{{ QueueName }}",
   "BatchSize": "{{ BatchSize }}",
   "MaximumBatchingWindowInSeconds": "{{ MaximumBatchingWindowInSeconds }}"
  },
  "RabbitMQBrokerParameters": {
   "Credentials": null,
   "QueueName": "{{ QueueName }}",
   "VirtualHost": "{{ VirtualHost }}",
   "BatchSize": "{{ BatchSize }}",
   "MaximumBatchingWindowInSeconds": "{{ MaximumBatchingWindowInSeconds }}"
  },
  "ManagedStreamingKafkaParameters": {
   "TopicName": "{{ TopicName }}",
   "StartingPosition": "{{ StartingPosition }}",
   "BatchSize": "{{ BatchSize }}",
   "MaximumBatchingWindowInSeconds": "{{ MaximumBatchingWindowInSeconds }}",
   "ConsumerGroupID": "{{ ConsumerGroupID }}",
   "Credentials": null
  },
  "SelfManagedKafkaParameters": {
   "TopicName": "{{ TopicName }}",
   "StartingPosition": "{{ StartingPosition }}",
   "AdditionalBootstrapServers": [
    "{{ AdditionalBootstrapServers[0] }}"
   ],
   "BatchSize": "{{ BatchSize }}",
   "MaximumBatchingWindowInSeconds": "{{ MaximumBatchingWindowInSeconds }}",
   "ConsumerGroupID": "{{ ConsumerGroupID }}",
   "Credentials": null,
   "ServerRootCaCertificate": "{{ ServerRootCaCertificate }}",
   "Vpc": {
    "Subnets": [
     "{{ Subnets[0] }}"
    ],
    "SecurityGroup": [
     "{{ SecurityGroup[0] }}"
    ]
   }
  }
 },
 "Tags": {},
 "Target": "{{ Target }}",
 "TargetParameters": {
  "InputTemplate": "{{ InputTemplate }}",
  "LambdaFunctionParameters": {
   "InvocationType": "{{ InvocationType }}"
  },
  "StepFunctionStateMachineParameters": {
   "InvocationType": null
  },
  "KinesisStreamParameters": {
   "PartitionKey": "{{ PartitionKey }}"
  },
  "EcsTaskParameters": {
   "TaskDefinitionArn": "{{ TaskDefinitionArn }}",
   "TaskCount": "{{ TaskCount }}",
   "LaunchType": "{{ LaunchType }}",
   "NetworkConfiguration": {
    "AwsvpcConfiguration": {
     "Subnets": [
      "{{ Subnets[0] }}"
     ],
     "SecurityGroups": [
      "{{ SecurityGroups[0] }}"
     ],
     "AssignPublicIp": "{{ AssignPublicIp }}"
    }
   },
   "PlatformVersion": "{{ PlatformVersion }}",
   "Group": "{{ Group }}",
   "CapacityProviderStrategy": [
    {
     "CapacityProvider": "{{ CapacityProvider }}",
     "Weight": "{{ Weight }}",
     "Base": "{{ Base }}"
    }
   ],
   "EnableECSManagedTags": "{{ EnableECSManagedTags }}",
   "EnableExecuteCommand": "{{ EnableExecuteCommand }}",
   "PlacementConstraints": [
    {
     "Type": "{{ Type }}",
     "Expression": "{{ Expression }}"
    }
   ],
   "PlacementStrategy": [
    {
     "Type": "{{ Type }}",
     "Field": "{{ Field }}"
    }
   ],
   "PropagateTags": "{{ PropagateTags }}",
   "ReferenceId": "{{ ReferenceId }}",
   "Overrides": {
    "ContainerOverrides": [
     {
      "Command": [
       "{{ Command[0] }}"
      ],
      "Cpu": "{{ Cpu }}",
      "Environment": [
       {
        "Name": "{{ Name }}",
        "Value": "{{ Value }}"
       }
      ],
      "EnvironmentFiles": [
       {
        "Type": "{{ Type }}",
        "Value": "{{ Value }}"
       }
      ],
      "Memory": "{{ Memory }}",
      "MemoryReservation": "{{ MemoryReservation }}",
      "Name": "{{ Name }}",
      "ResourceRequirements": [
       {
        "Type": "{{ Type }}",
        "Value": "{{ Value }}"
       }
      ]
     }
    ],
    "Cpu": "{{ Cpu }}",
    "EphemeralStorage": {
     "SizeInGiB": "{{ SizeInGiB }}"
    },
    "ExecutionRoleArn": "{{ ExecutionRoleArn }}",
    "InferenceAcceleratorOverrides": [
     {
      "DeviceName": "{{ DeviceName }}",
      "DeviceType": "{{ DeviceType }}"
     }
    ],
    "Memory": "{{ Memory }}",
    "TaskRoleArn": "{{ TaskRoleArn }}"
   },
   "Tags": [
    {
     "Key": "{{ Key }}",
     "Value": "{{ Value }}"
    }
   ]
  },
  "BatchJobParameters": {
   "JobDefinition": "{{ JobDefinition }}",
   "JobName": "{{ JobName }}",
   "ArrayProperties": {
    "Size": "{{ Size }}"
   },
   "RetryStrategy": {
    "Attempts": "{{ Attempts }}"
   },
   "ContainerOverrides": {
    "Command": [
     "{{ Command[0] }}"
    ],
    "Environment": [
     {
      "Name": "{{ Name }}",
      "Value": "{{ Value }}"
     }
    ],
    "InstanceType": "{{ InstanceType }}",
    "ResourceRequirements": [
     {
      "Type": "{{ Type }}",
      "Value": "{{ Value }}"
     }
    ]
   },
   "DependsOn": [
    {
     "JobId": "{{ JobId }}",
     "Type": "{{ Type }}"
    }
   ],
   "Parameters": {}
  },
  "SqsQueueParameters": {
   "MessageGroupId": "{{ MessageGroupId }}",
   "MessageDeduplicationId": "{{ MessageDeduplicationId }}"
  },
  "HttpParameters": {
   "PathParameterValues": [
    "{{ PathParameterValues[0] }}"
   ],
   "HeaderParameters": null,
   "QueryStringParameters": null
  },
  "RedshiftDataParameters": {
   "SecretManagerArn": "{{ SecretManagerArn }}",
   "Database": "{{ Database }}",
   "DbUser": "{{ DbUser }}",
   "StatementName": "{{ StatementName }}",
   "WithEvent": "{{ WithEvent }}",
   "Sqls": [
    "{{ Sqls[0] }}"
   ]
  },
  "SageMakerPipelineParameters": {
   "PipelineParameterList": [
    {
     "Name": "{{ Name }}",
     "Value": "{{ Value }}"
    }
   ]
  },
  "EventBridgeEventBusParameters": {
   "EndpointId": "{{ EndpointId }}",
   "DetailType": "{{ DetailType }}",
   "Source": "{{ Source }}",
   "Resources": [
    "{{ Resources[0] }}"
   ],
   "Time": "{{ Time }}"
  },
  "CloudWatchLogsParameters": {
   "LogStreamName": "{{ LogStreamName }}",
   "Timestamp": "{{ Timestamp }}"
  }
 }
}
>>>
--all properties
INSERT INTO aws.pipes.pipes (
 Description,
 DesiredState,
 Enrichment,
 EnrichmentParameters,
 LogConfiguration,
 Name,
 RoleArn,
 Source,
 SourceParameters,
 Tags,
 Target,
 TargetParameters,
 region
)
SELECT 
 {{ .Description }},
 {{ .DesiredState }},
 {{ .Enrichment }},
 {{ .EnrichmentParameters }},
 {{ .LogConfiguration }},
 {{ .Name }},
 {{ .RoleArn }},
 {{ .Source }},
 {{ .SourceParameters }},
 {{ .Tags }},
 {{ .Target }},
 {{ .TargetParameters }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.pipes.pipes
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pipes</code> resource, the following permissions are required:

### Create
```json
pipes:CreatePipe,
pipes:DescribePipe,
pipes:TagResource,
iam:PassRole,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
iam:CreateServiceLinkedRole,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
firehose:TagDeliveryStream
```

### Delete
```json
pipes:DeletePipe,
pipes:DescribePipe,
logs:CreateLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries
```

### List
```json
pipes:ListPipes
```

