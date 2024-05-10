---
title: model_explainability_job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - model_explainability_job_definitions
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


Used to retrieve a list of <code>model_explainability_job_definitions</code> in a region or to create or delete a <code>model_explainability_job_definitions</code> resource, use <code>model_explainability_job_definition</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_explainability_job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelExplainabilityJobDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_explainability_job_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="job_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of job definition.</td></tr>
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
job_definition_arn
FROM aws.sagemaker.model_explainability_job_definitions
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
 "ModelExplainabilityAppSpecification": {
  "ImageUri": "{{ ImageUri }}",
  "ConfigUri": "{{ ConfigUri }}",
  "Environment": {}
 },
 "ModelExplainabilityJobInput": {
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
 },
 "ModelExplainabilityJobOutputConfig": {
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
 "JobResources": {
  "ClusterConfig": {
   "InstanceCount": "{{ InstanceCount }}",
   "InstanceType": "{{ InstanceType }}",
   "VolumeKmsKeyId": "{{ VolumeKmsKeyId }}",
   "VolumeSizeInGB": "{{ VolumeSizeInGB }}"
  }
 },
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.sagemaker.model_explainability_job_definitions (
 ModelExplainabilityAppSpecification,
 ModelExplainabilityJobInput,
 ModelExplainabilityJobOutputConfig,
 JobResources,
 RoleArn,
 region
)
SELECT 
{{ ModelExplainabilityAppSpecification }},
 {{ ModelExplainabilityJobInput }},
 {{ ModelExplainabilityJobOutputConfig }},
 {{ JobResources }},
 {{ RoleArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "JobDefinitionName": "{{ JobDefinitionName }}",
 "ModelExplainabilityBaselineConfig": {
  "BaseliningJobName": "{{ BaseliningJobName }}",
  "ConstraintsResource": {
   "S3Uri": "{{ S3Uri }}"
  }
 },
 "ModelExplainabilityAppSpecification": {
  "ImageUri": "{{ ImageUri }}",
  "ConfigUri": null,
  "Environment": {}
 },
 "ModelExplainabilityJobInput": {
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
 },
 "ModelExplainabilityJobOutputConfig": {
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
 "JobResources": {
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
 "EndpointName": null,
 "RoleArn": "{{ RoleArn }}",
 "StoppingCondition": {
  "MaxRuntimeInSeconds": "{{ MaxRuntimeInSeconds }}"
 },
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.sagemaker.model_explainability_job_definitions (
 JobDefinitionName,
 ModelExplainabilityBaselineConfig,
 ModelExplainabilityAppSpecification,
 ModelExplainabilityJobInput,
 ModelExplainabilityJobOutputConfig,
 JobResources,
 NetworkConfig,
 EndpointName,
 RoleArn,
 StoppingCondition,
 Tags,
 region
)
SELECT 
 {{ JobDefinitionName }},
 {{ ModelExplainabilityBaselineConfig }},
 {{ ModelExplainabilityAppSpecification }},
 {{ ModelExplainabilityJobInput }},
 {{ ModelExplainabilityJobOutputConfig }},
 {{ JobResources }},
 {{ NetworkConfig }},
 {{ EndpointName }},
 {{ RoleArn }},
 {{ StoppingCondition }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.sagemaker.model_explainability_job_definitions
WHERE data__Identifier = '<JobDefinitionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>model_explainability_job_definitions</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateModelExplainabilityJobDefinition,
sagemaker:DescribeModelExplainabilityJobDefinition,
iam:PassRole,
sagemaker:AddTags
```

### Delete
```json
sagemaker:DeleteModelExplainabilityJobDefinition
```

### List
```json
sagemaker:ListModelExplainabilityJobDefinitions,
sagemaker:ListTags
```

