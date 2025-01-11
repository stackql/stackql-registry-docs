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

Creates, updates, deletes or gets a <code>pipe</code> resource or lists <code>pipes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Pipes::Pipe Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.pipes.pipes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="current_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="desired_state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enrichment" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enrichment_parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="log_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="state_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="target" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_parameters" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pipes-pipe.html"><code>AWS::Pipes::Pipe</code></a>.

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
    <td><CopyableCode code="RoleArn, Source, Target, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>pipes</code> in a region.
```sql
SELECT
region,
arn,
creation_time,
current_state,
description,
desired_state,
enrichment,
enrichment_parameters,
kms_key_identifier,
last_modified_time,
log_configuration,
name,
role_arn,
source,
source_parameters,
state_reason,
tags,
target,
target_parameters
FROM aws.pipes.pipes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>pipe</code>.
```sql
SELECT
region,
arn,
creation_time,
current_state,
description,
desired_state,
enrichment,
enrichment_parameters,
kms_key_identifier,
last_modified_time,
log_configuration,
name,
role_arn,
source,
source_parameters,
state_reason,
tags,
target,
target_parameters
FROM aws.pipes.pipes
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipe</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.pipes.pipes (
 RoleArn,
 Source,
 Target,
 region
)
SELECT 
'{{ RoleArn }}',
 '{{ Source }}',
 '{{ Target }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.pipes.pipes (
 Description,
 DesiredState,
 Enrichment,
 EnrichmentParameters,
 KmsKeyIdentifier,
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
 '{{ Description }}',
 '{{ DesiredState }}',
 '{{ Enrichment }}',
 '{{ EnrichmentParameters }}',
 '{{ KmsKeyIdentifier }}',
 '{{ LogConfiguration }}',
 '{{ Name }}',
 '{{ RoleArn }}',
 '{{ Source }}',
 '{{ SourceParameters }}',
 '{{ Tags }}',
 '{{ Target }}',
 '{{ TargetParameters }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: pipe
    props:
      - name: Description
        value: '{{ Description }}'
      - name: DesiredState
        value: '{{ DesiredState }}'
      - name: Enrichment
        value: '{{ Enrichment }}'
      - name: EnrichmentParameters
        value:
          InputTemplate: '{{ InputTemplate }}'
          HttpParameters:
            PathParameterValues:
              - '{{ PathParameterValues[0] }}'
            HeaderParameters: {}
            QueryStringParameters: {}
      - name: KmsKeyIdentifier
        value: '{{ KmsKeyIdentifier }}'
      - name: LogConfiguration
        value:
          S3LogDestination:
            BucketName: '{{ BucketName }}'
            Prefix: '{{ Prefix }}'
            BucketOwner: '{{ BucketOwner }}'
            OutputFormat: '{{ OutputFormat }}'
          FirehoseLogDestination:
            DeliveryStreamArn: '{{ DeliveryStreamArn }}'
          CloudwatchLogsLogDestination:
            LogGroupArn: '{{ LogGroupArn }}'
          Level: '{{ Level }}'
          IncludeExecutionData:
            - '{{ IncludeExecutionData[0] }}'
      - name: Name
        value: '{{ Name }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Source
        value: '{{ Source }}'
      - name: SourceParameters
        value:
          FilterCriteria:
            Filters:
              - Pattern: '{{ Pattern }}'
          KinesisStreamParameters:
            BatchSize: '{{ BatchSize }}'
            DeadLetterConfig:
              Arn: '{{ Arn }}'
            OnPartialBatchItemFailure: '{{ OnPartialBatchItemFailure }}'
            MaximumBatchingWindowInSeconds: '{{ MaximumBatchingWindowInSeconds }}'
            MaximumRecordAgeInSeconds: '{{ MaximumRecordAgeInSeconds }}'
            MaximumRetryAttempts: '{{ MaximumRetryAttempts }}'
            ParallelizationFactor: '{{ ParallelizationFactor }}'
            StartingPosition: '{{ StartingPosition }}'
            StartingPositionTimestamp: '{{ StartingPositionTimestamp }}'
          DynamoDBStreamParameters:
            BatchSize: '{{ BatchSize }}'
            DeadLetterConfig: null
            OnPartialBatchItemFailure: null
            MaximumBatchingWindowInSeconds: '{{ MaximumBatchingWindowInSeconds }}'
            MaximumRecordAgeInSeconds: '{{ MaximumRecordAgeInSeconds }}'
            MaximumRetryAttempts: '{{ MaximumRetryAttempts }}'
            ParallelizationFactor: '{{ ParallelizationFactor }}'
            StartingPosition: '{{ StartingPosition }}'
          SqsQueueParameters:
            BatchSize: '{{ BatchSize }}'
            MaximumBatchingWindowInSeconds: '{{ MaximumBatchingWindowInSeconds }}'
          ActiveMQBrokerParameters:
            Credentials: null
            QueueName: '{{ QueueName }}'
            BatchSize: '{{ BatchSize }}'
            MaximumBatchingWindowInSeconds: '{{ MaximumBatchingWindowInSeconds }}'
          RabbitMQBrokerParameters:
            Credentials: null
            QueueName: '{{ QueueName }}'
            VirtualHost: '{{ VirtualHost }}'
            BatchSize: '{{ BatchSize }}'
            MaximumBatchingWindowInSeconds: '{{ MaximumBatchingWindowInSeconds }}'
          ManagedStreamingKafkaParameters:
            TopicName: '{{ TopicName }}'
            StartingPosition: '{{ StartingPosition }}'
            BatchSize: '{{ BatchSize }}'
            MaximumBatchingWindowInSeconds: '{{ MaximumBatchingWindowInSeconds }}'
            ConsumerGroupID: '{{ ConsumerGroupID }}'
            Credentials: null
          SelfManagedKafkaParameters:
            TopicName: '{{ TopicName }}'
            StartingPosition: '{{ StartingPosition }}'
            AdditionalBootstrapServers:
              - '{{ AdditionalBootstrapServers[0] }}'
            BatchSize: '{{ BatchSize }}'
            MaximumBatchingWindowInSeconds: '{{ MaximumBatchingWindowInSeconds }}'
            ConsumerGroupID: '{{ ConsumerGroupID }}'
            Credentials: null
            ServerRootCaCertificate: '{{ ServerRootCaCertificate }}'
            Vpc:
              Subnets:
                - '{{ Subnets[0] }}'
              SecurityGroup:
                - '{{ SecurityGroup[0] }}'
      - name: Tags
        value: {}
      - name: Target
        value: '{{ Target }}'
      - name: TargetParameters
        value:
          InputTemplate: '{{ InputTemplate }}'
          LambdaFunctionParameters:
            InvocationType: '{{ InvocationType }}'
          StepFunctionStateMachineParameters:
            InvocationType: null
          KinesisStreamParameters:
            PartitionKey: '{{ PartitionKey }}'
          EcsTaskParameters:
            TaskDefinitionArn: '{{ TaskDefinitionArn }}'
            TaskCount: '{{ TaskCount }}'
            LaunchType: '{{ LaunchType }}'
            NetworkConfiguration:
              AwsvpcConfiguration:
                Subnets:
                  - '{{ Subnets[0] }}'
                SecurityGroups:
                  - '{{ SecurityGroups[0] }}'
                AssignPublicIp: '{{ AssignPublicIp }}'
            PlatformVersion: '{{ PlatformVersion }}'
            Group: '{{ Group }}'
            CapacityProviderStrategy:
              - CapacityProvider: '{{ CapacityProvider }}'
                Weight: '{{ Weight }}'
                Base: '{{ Base }}'
            EnableECSManagedTags: '{{ EnableECSManagedTags }}'
            EnableExecuteCommand: '{{ EnableExecuteCommand }}'
            PlacementConstraints:
              - Type: '{{ Type }}'
                Expression: '{{ Expression }}'
            PlacementStrategy:
              - Type: '{{ Type }}'
                Field: '{{ Field }}'
            PropagateTags: '{{ PropagateTags }}'
            ReferenceId: '{{ ReferenceId }}'
            Overrides:
              ContainerOverrides:
                - Command:
                    - '{{ Command[0] }}'
                  Cpu: '{{ Cpu }}'
                  Environment:
                    - Name: '{{ Name }}'
                      Value: '{{ Value }}'
                  EnvironmentFiles:
                    - Type: '{{ Type }}'
                      Value: '{{ Value }}'
                  Memory: '{{ Memory }}'
                  MemoryReservation: '{{ MemoryReservation }}'
                  Name: '{{ Name }}'
                  ResourceRequirements:
                    - Type: '{{ Type }}'
                      Value: '{{ Value }}'
              Cpu: '{{ Cpu }}'
              EphemeralStorage:
                SizeInGiB: '{{ SizeInGiB }}'
              ExecutionRoleArn: '{{ ExecutionRoleArn }}'
              InferenceAcceleratorOverrides:
                - DeviceName: '{{ DeviceName }}'
                  DeviceType: '{{ DeviceType }}'
              Memory: '{{ Memory }}'
              TaskRoleArn: '{{ TaskRoleArn }}'
            Tags:
              - Key: '{{ Key }}'
                Value: '{{ Value }}'
          BatchJobParameters:
            JobDefinition: '{{ JobDefinition }}'
            JobName: '{{ JobName }}'
            ArrayProperties:
              Size: '{{ Size }}'
            RetryStrategy:
              Attempts: '{{ Attempts }}'
            ContainerOverrides:
              Command:
                - '{{ Command[0] }}'
              Environment:
                - Name: '{{ Name }}'
                  Value: '{{ Value }}'
              InstanceType: '{{ InstanceType }}'
              ResourceRequirements:
                - Type: '{{ Type }}'
                  Value: '{{ Value }}'
            DependsOn:
              - JobId: '{{ JobId }}'
                Type: '{{ Type }}'
            Parameters: {}
          SqsQueueParameters:
            MessageGroupId: '{{ MessageGroupId }}'
            MessageDeduplicationId: '{{ MessageDeduplicationId }}'
          HttpParameters:
            PathParameterValues:
              - '{{ PathParameterValues[0] }}'
            HeaderParameters: null
            QueryStringParameters: null
          RedshiftDataParameters:
            SecretManagerArn: '{{ SecretManagerArn }}'
            Database: '{{ Database }}'
            DbUser: '{{ DbUser }}'
            StatementName: '{{ StatementName }}'
            WithEvent: '{{ WithEvent }}'
            Sqls:
              - '{{ Sqls[0] }}'
          SageMakerPipelineParameters:
            PipelineParameterList:
              - Name: '{{ Name }}'
                Value: '{{ Value }}'
          EventBridgeEventBusParameters:
            EndpointId: '{{ EndpointId }}'
            DetailType: '{{ DetailType }}'
            Source: '{{ Source }}'
            Resources:
              - '{{ Resources[0] }}'
            Time: '{{ Time }}'
          CloudWatchLogsParameters:
            LogStreamName: '{{ LogStreamName }}'
            Timestamp: '{{ Timestamp }}'
          TimestreamParameters:
            TimeValue: '{{ TimeValue }}'
            EpochTimeUnit: '{{ EpochTimeUnit }}'
            TimeFieldType: '{{ TimeFieldType }}'
            TimestampFormat: '{{ TimestampFormat }}'
            VersionValue: '{{ VersionValue }}'
            DimensionMappings:
              - DimensionValue: '{{ DimensionValue }}'
                DimensionValueType: '{{ DimensionValueType }}'
                DimensionName: '{{ DimensionName }}'
            SingleMeasureMappings:
              - MeasureValue: '{{ MeasureValue }}'
                MeasureValueType: '{{ MeasureValueType }}'
                MeasureName: '{{ MeasureName }}'
            MultiMeasureMappings:
              - MultiMeasureName: '{{ MultiMeasureName }}'
                MultiMeasureAttributeMappings:
                  - MeasureValue: '{{ MeasureValue }}'
                    MeasureValueType: null
                    MultiMeasureAttributeName: '{{ MultiMeasureAttributeName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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
firehose:TagDeliveryStream,
kms:DescribeKey,
kms:Decrypt,
kms:GenerateDataKey
```

### Read
```json
pipes:DescribePipe,
kms:Decrypt
```

### Update
```json
pipes:UpdatePipe,
pipes:TagResource,
pipes:UntagResource,
pipes:DescribePipe,
iam:PassRole,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
iam:CreateServiceLinkedRole,
logs:CreateLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
firehose:TagDeliveryStream,
kms:DescribeKey,
kms:Decrypt,
kms:GenerateDataKey
```

### Delete
```json
pipes:DeletePipe,
pipes:DescribePipe,
pipes:UntagResource,
logs:CreateLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
kms:DescribeKey,
kms:Decrypt,
kms:GenerateDataKey
```

### List
```json
pipes:ListPipes
```
