---
title: monitoring_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - monitoring_schedules
  - sagemaker
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

Creates, updates, deletes or gets a <code>monitoring_schedule</code> resource or lists <code>monitoring_schedules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::MonitoringSchedule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.monitoring_schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="monitoring_schedule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the monitoring schedule.</td></tr>
<tr><td><CopyableCode code="monitoring_schedule_name" /></td><td><code>string</code></td><td>The name of the monitoring schedule.</td></tr>
<tr><td><CopyableCode code="monitoring_schedule_config" /></td><td><code>object</code></td><td>The configuration object that specifies the monitoring schedule and defines the monitoring job.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the schedule was created.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint used to run the monitoring job.</td></tr>
<tr><td><CopyableCode code="failure_reason" /></td><td><code>string</code></td><td>Contains the reason a monitoring job failed, if it failed.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td>A timestamp that indicates the last time the monitoring job was modified.</td></tr>
<tr><td><CopyableCode code="last_monitoring_execution_summary" /></td><td><code>object</code></td><td>Describes metadata on the last execution to run, if there was one.</td></tr>
<tr><td><CopyableCode code="monitoring_schedule_status" /></td><td><code>string</code></td><td>The status of a schedule job.</td></tr>
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
    <td><CopyableCode code="MonitoringScheduleConfig, MonitoringScheduleName, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>monitoring_schedules</code> in a region.
```sql
SELECT
region,
monitoring_schedule_arn
FROM aws.sagemaker.monitoring_schedules
WHERE region = 'us-east-1';
```
Gets all properties from a <code>monitoring_schedule</code>.
```sql
SELECT
region,
monitoring_schedule_arn,
monitoring_schedule_name,
monitoring_schedule_config,
tags,
creation_time,
endpoint_name,
failure_reason,
last_modified_time,
last_monitoring_execution_summary,
monitoring_schedule_status
FROM aws.sagemaker.monitoring_schedules
WHERE region = 'us-east-1' AND data__Identifier = '<MonitoringScheduleArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>monitoring_schedule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.monitoring_schedules (
 MonitoringScheduleName,
 MonitoringScheduleConfig,
 region
)
SELECT 
'{{ MonitoringScheduleName }}',
 '{{ MonitoringScheduleConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.monitoring_schedules (
 MonitoringScheduleName,
 MonitoringScheduleConfig,
 Tags,
 EndpointName,
 FailureReason,
 LastMonitoringExecutionSummary,
 MonitoringScheduleStatus,
 region
)
SELECT 
 '{{ MonitoringScheduleName }}',
 '{{ MonitoringScheduleConfig }}',
 '{{ Tags }}',
 '{{ EndpointName }}',
 '{{ FailureReason }}',
 '{{ LastMonitoringExecutionSummary }}',
 '{{ MonitoringScheduleStatus }}',
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
  - name: monitoring_schedule
    props:
      - name: MonitoringScheduleName
        value: '{{ MonitoringScheduleName }}'
      - name: MonitoringScheduleConfig
        value:
          MonitoringJobDefinition:
            BaselineConfig:
              ConstraintsResource:
                S3Uri: '{{ S3Uri }}'
              StatisticsResource:
                S3Uri: null
            Environment: {}
            MonitoringAppSpecification:
              ContainerArguments:
                - '{{ ContainerArguments[0] }}'
              ContainerEntrypoint:
                - '{{ ContainerEntrypoint[0] }}'
              ImageUri: '{{ ImageUri }}'
              PostAnalyticsProcessorSourceUri: null
              RecordPreprocessorSourceUri: null
            MonitoringInputs:
              - EndpointInput:
                  EndpointName: '{{ EndpointName }}'
                  LocalPath: '{{ LocalPath }}'
                  S3DataDistributionType: '{{ S3DataDistributionType }}'
                  S3InputMode: '{{ S3InputMode }}'
                  ExcludeFeaturesAttribute: '{{ ExcludeFeaturesAttribute }}'
                BatchTransformInput:
                  DataCapturedDestinationS3Uri: '{{ DataCapturedDestinationS3Uri }}'
                  DatasetFormat:
                    Csv:
                      Header: '{{ Header }}'
                    Json:
                      Line: '{{ Line }}'
                    Parquet: '{{ Parquet }}'
                  LocalPath: '{{ LocalPath }}'
                  S3DataDistributionType: '{{ S3DataDistributionType }}'
                  S3InputMode: '{{ S3InputMode }}'
                  ExcludeFeaturesAttribute: '{{ ExcludeFeaturesAttribute }}'
            MonitoringOutputConfig:
              KmsKeyId: '{{ KmsKeyId }}'
              MonitoringOutputs:
                - S3Output:
                    LocalPath: '{{ LocalPath }}'
                    S3UploadMode: '{{ S3UploadMode }}'
                    S3Uri: '{{ S3Uri }}'
            MonitoringResources:
              ClusterConfig:
                InstanceCount: '{{ InstanceCount }}'
                InstanceType: '{{ InstanceType }}'
                VolumeKmsKeyId: '{{ VolumeKmsKeyId }}'
                VolumeSizeInGB: '{{ VolumeSizeInGB }}'
            NetworkConfig:
              EnableInterContainerTrafficEncryption: '{{ EnableInterContainerTrafficEncryption }}'
              EnableNetworkIsolation: '{{ EnableNetworkIsolation }}'
              VpcConfig:
                SecurityGroupIds:
                  - '{{ SecurityGroupIds[0] }}'
                Subnets:
                  - '{{ Subnets[0] }}'
            RoleArn: '{{ RoleArn }}'
            StoppingCondition:
              MaxRuntimeInSeconds: '{{ MaxRuntimeInSeconds }}'
          MonitoringJobDefinitionName: '{{ MonitoringJobDefinitionName }}'
          MonitoringType: '{{ MonitoringType }}'
          ScheduleConfig:
            ScheduleExpression: '{{ ScheduleExpression }}'
            DataAnalysisStartTime: '{{ DataAnalysisStartTime }}'
            DataAnalysisEndTime: null
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: EndpointName
        value: null
      - name: FailureReason
        value: '{{ FailureReason }}'
      - name: LastMonitoringExecutionSummary
        value:
          CreationTime: '{{ CreationTime }}'
          EndpointName: null
          FailureReason: '{{ FailureReason }}'
          LastModifiedTime: '{{ LastModifiedTime }}'
          MonitoringExecutionStatus: '{{ MonitoringExecutionStatus }}'
          MonitoringScheduleName: null
          ProcessingJobArn: '{{ ProcessingJobArn }}'
          ScheduledTime: '{{ ScheduledTime }}'
      - name: MonitoringScheduleStatus
        value: '{{ MonitoringScheduleStatus }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.monitoring_schedules
WHERE data__Identifier = '<MonitoringScheduleArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>monitoring_schedules</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateMonitoringSchedule,
sagemaker:DescribeMonitoringSchedule,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteMonitoringSchedule,
sagemaker:DescribeMonitoringSchedule
```

### List
```json
sagemaker:ListMonitoringSchedule
```

### Read
```json
sagemaker:DescribeMonitoringSchedule
```

### Update
```json
sagemaker:UpdateMonitoringSchedule,
sagemaker:DescribeMonitoringSchedule
```

