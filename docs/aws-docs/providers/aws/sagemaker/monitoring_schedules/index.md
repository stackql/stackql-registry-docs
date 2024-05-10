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


Used to retrieve a list of <code>monitoring_schedules</code> in a region or to create or delete a <code>monitoring_schedules</code> resource, use <code>monitoring_schedule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitoring_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::MonitoringSchedule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.monitoring_schedules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="monitoring_schedule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the monitoring schedule.</td></tr>
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
monitoring_schedule_arn
FROM aws.sagemaker.monitoring_schedules
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
 "MonitoringScheduleName": "{{ MonitoringScheduleName }}",
 "MonitoringScheduleConfig": {
  "MonitoringJobDefinition": {
   "BaselineConfig": {
    "ConstraintsResource": {
     "S3Uri": "{{ S3Uri }}"
    },
    "StatisticsResource": {
     "S3Uri": null
    }
   },
   "Environment": {},
   "MonitoringAppSpecification": {
    "ContainerArguments": [
     "{{ ContainerArguments[0] }}"
    ],
    "ContainerEntrypoint": [
     "{{ ContainerEntrypoint[0] }}"
    ],
    "ImageUri": "{{ ImageUri }}",
    "PostAnalyticsProcessorSourceUri": null,
    "RecordPreprocessorSourceUri": null
   },
   "MonitoringInputs": [
    {
     "EndpointInput": {
      "EndpointName": "{{ EndpointName }}",
      "LocalPath": "{{ LocalPath }}",
      "S3DataDistributionType": "{{ S3DataDistributionType }}",
      "S3InputMode": "{{ S3InputMode }}",
      "ExcludeFeaturesAttribute": "{{ ExcludeFeaturesAttribute }}"
     },
     "BatchTransformInput": {
      "DataCapturedDestinationS3Uri": "{{ DataCapturedDestinationS3Uri }}",
      "DatasetFormat": {
       "Csv": {
        "Header": "{{ Header }}"
       },
       "Json": {
        "Line": "{{ Line }}"
       },
       "Parquet": "{{ Parquet }}"
      },
      "LocalPath": "{{ LocalPath }}",
      "S3DataDistributionType": "{{ S3DataDistributionType }}",
      "S3InputMode": "{{ S3InputMode }}",
      "ExcludeFeaturesAttribute": "{{ ExcludeFeaturesAttribute }}"
     }
    }
   ],
   "MonitoringOutputConfig": {
    "KmsKeyId": "{{ KmsKeyId }}",
    "MonitoringOutputs": [
     {
      "S3Output": {
       "LocalPath": "{{ LocalPath }}",
       "S3UploadMode": "{{ S3UploadMode }}",
       "S3Uri": "{{ S3Uri }}"
      }
     }
    ]
   },
   "MonitoringResources": {
    "ClusterConfig": {
     "InstanceCount": "{{ InstanceCount }}",
     "InstanceType": "{{ InstanceType }}",
     "VolumeKmsKeyId": "{{ VolumeKmsKeyId }}",
     "VolumeSizeInGB": "{{ VolumeSizeInGB }}"
    }
   },
   "NetworkConfig": {
    "EnableInterContainerTrafficEncryption": "{{ EnableInterContainerTrafficEncryption }}",
    "EnableNetworkIsolation": "{{ EnableNetworkIsolation }}",
    "VpcConfig": {
     "SecurityGroupIds": [
      "{{ SecurityGroupIds[0] }}"
     ],
     "Subnets": [
      "{{ Subnets[0] }}"
     ]
    }
   },
   "RoleArn": "{{ RoleArn }}",
   "StoppingCondition": {
    "MaxRuntimeInSeconds": "{{ MaxRuntimeInSeconds }}"
   }
  },
  "MonitoringJobDefinitionName": "{{ MonitoringJobDefinitionName }}",
  "MonitoringType": "{{ MonitoringType }}",
  "ScheduleConfig": {
   "ScheduleExpression": "{{ ScheduleExpression }}",
   "DataAnalysisStartTime": "{{ DataAnalysisStartTime }}",
   "DataAnalysisEndTime": null
  }
 }
}
>>>
--required properties only
INSERT INTO aws.sagemaker.monitoring_schedules (
 MonitoringScheduleName,
 MonitoringScheduleConfig,
 region
)
SELECT 
{{ MonitoringScheduleName }},
 {{ MonitoringScheduleConfig }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "MonitoringScheduleName": "{{ MonitoringScheduleName }}",
 "MonitoringScheduleConfig": {
  "MonitoringJobDefinition": {
   "BaselineConfig": {
    "ConstraintsResource": {
     "S3Uri": "{{ S3Uri }}"
    },
    "StatisticsResource": {
     "S3Uri": null
    }
   },
   "Environment": {},
   "MonitoringAppSpecification": {
    "ContainerArguments": [
     "{{ ContainerArguments[0] }}"
    ],
    "ContainerEntrypoint": [
     "{{ ContainerEntrypoint[0] }}"
    ],
    "ImageUri": "{{ ImageUri }}",
    "PostAnalyticsProcessorSourceUri": null,
    "RecordPreprocessorSourceUri": null
   },
   "MonitoringInputs": [
    {
     "EndpointInput": {
      "EndpointName": "{{ EndpointName }}",
      "LocalPath": "{{ LocalPath }}",
      "S3DataDistributionType": "{{ S3DataDistributionType }}",
      "S3InputMode": "{{ S3InputMode }}",
      "ExcludeFeaturesAttribute": "{{ ExcludeFeaturesAttribute }}"
     },
     "BatchTransformInput": {
      "DataCapturedDestinationS3Uri": "{{ DataCapturedDestinationS3Uri }}",
      "DatasetFormat": {
       "Csv": {
        "Header": "{{ Header }}"
       },
       "Json": {
        "Line": "{{ Line }}"
       },
       "Parquet": "{{ Parquet }}"
      },
      "LocalPath": "{{ LocalPath }}",
      "S3DataDistributionType": "{{ S3DataDistributionType }}",
      "S3InputMode": "{{ S3InputMode }}",
      "ExcludeFeaturesAttribute": "{{ ExcludeFeaturesAttribute }}"
     }
    }
   ],
   "MonitoringOutputConfig": {
    "KmsKeyId": "{{ KmsKeyId }}",
    "MonitoringOutputs": [
     {
      "S3Output": {
       "LocalPath": "{{ LocalPath }}",
       "S3UploadMode": "{{ S3UploadMode }}",
       "S3Uri": "{{ S3Uri }}"
      }
     }
    ]
   },
   "MonitoringResources": {
    "ClusterConfig": {
     "InstanceCount": "{{ InstanceCount }}",
     "InstanceType": "{{ InstanceType }}",
     "VolumeKmsKeyId": "{{ VolumeKmsKeyId }}",
     "VolumeSizeInGB": "{{ VolumeSizeInGB }}"
    }
   },
   "NetworkConfig": {
    "EnableInterContainerTrafficEncryption": "{{ EnableInterContainerTrafficEncryption }}",
    "EnableNetworkIsolation": "{{ EnableNetworkIsolation }}",
    "VpcConfig": {
     "SecurityGroupIds": [
      "{{ SecurityGroupIds[0] }}"
     ],
     "Subnets": [
      "{{ Subnets[0] }}"
     ]
    }
   },
   "RoleArn": "{{ RoleArn }}",
   "StoppingCondition": {
    "MaxRuntimeInSeconds": "{{ MaxRuntimeInSeconds }}"
   }
  },
  "MonitoringJobDefinitionName": "{{ MonitoringJobDefinitionName }}",
  "MonitoringType": "{{ MonitoringType }}",
  "ScheduleConfig": {
   "ScheduleExpression": "{{ ScheduleExpression }}",
   "DataAnalysisStartTime": "{{ DataAnalysisStartTime }}",
   "DataAnalysisEndTime": null
  }
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "EndpointName": null,
 "FailureReason": "{{ FailureReason }}",
 "LastMonitoringExecutionSummary": {
  "CreationTime": "{{ CreationTime }}",
  "EndpointName": null,
  "FailureReason": "{{ FailureReason }}",
  "LastModifiedTime": "{{ LastModifiedTime }}",
  "MonitoringExecutionStatus": "{{ MonitoringExecutionStatus }}",
  "MonitoringScheduleName": null,
  "ProcessingJobArn": "{{ ProcessingJobArn }}",
  "ScheduledTime": "{{ ScheduledTime }}"
 },
 "MonitoringScheduleStatus": "{{ MonitoringScheduleStatus }}"
}
>>>
--all properties
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
 {{ MonitoringScheduleName }},
 {{ MonitoringScheduleConfig }},
 {{ Tags }},
 {{ EndpointName }},
 {{ FailureReason }},
 {{ LastMonitoringExecutionSummary }},
 {{ MonitoringScheduleStatus }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

