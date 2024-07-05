---
title: model_quality_job_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - model_quality_job_definitions
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

Creates, updates, deletes or gets a <code>model_quality_job_definition</code> resource or lists <code>model_quality_job_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_quality_job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::ModelQualityJobDefinition</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.model_quality_job_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="job_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of job definition.</td></tr>
<tr><td><CopyableCode code="job_definition_name" /></td><td><code>string</code></td><td>The name of the job definition.</td></tr>
<tr><td><CopyableCode code="model_quality_baseline_config" /></td><td><code>object</code></td><td>Baseline configuration used to validate that the data conforms to the specified constraints and statistics.</td></tr>
<tr><td><CopyableCode code="model_quality_app_specification" /></td><td><code>object</code></td><td>Container image configuration object for the monitoring job.</td></tr>
<tr><td><CopyableCode code="model_quality_job_input" /></td><td><code>object</code></td><td>The inputs for a monitoring job.</td></tr>
<tr><td><CopyableCode code="model_quality_job_output_config" /></td><td><code>object</code></td><td>The output configuration for monitoring jobs.</td></tr>
<tr><td><CopyableCode code="job_resources" /></td><td><code>object</code></td><td>Identifies the resources to deploy for a monitoring job.</td></tr>
<tr><td><CopyableCode code="network_config" /></td><td><code>object</code></td><td>Networking options for a job, such as network traffic encryption between containers, whether to allow inbound and outbound network calls to and from containers, and the VPC subnets and security groups to use for VPC-enabled jobs.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint used to run the monitoring job.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</td></tr>
<tr><td><CopyableCode code="stopping_condition" /></td><td><code>object</code></td><td>Specifies a time limit for how long the monitoring job is allowed to run.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The time at which the job definition was created.</td></tr>
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
    <td><CopyableCode code="ModelQualityAppSpecification, ModelQualityJobInput, ModelQualityJobOutputConfig, JobResources, RoleArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>model_quality_job_definitions</code> in a region.
```sql
SELECT
region,
job_definition_arn,
job_definition_name,
model_quality_baseline_config,
model_quality_app_specification,
model_quality_job_input,
model_quality_job_output_config,
job_resources,
network_config,
endpoint_name,
role_arn,
stopping_condition,
tags,
creation_time
FROM aws.sagemaker.model_quality_job_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>model_quality_job_definition</code>.
```sql
SELECT
region,
job_definition_arn,
job_definition_name,
model_quality_baseline_config,
model_quality_app_specification,
model_quality_job_input,
model_quality_job_output_config,
job_resources,
network_config,
endpoint_name,
role_arn,
stopping_condition,
tags,
creation_time
FROM aws.sagemaker.model_quality_job_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<JobDefinitionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model_quality_job_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.model_quality_job_definitions (
 ModelQualityAppSpecification,
 ModelQualityJobInput,
 ModelQualityJobOutputConfig,
 JobResources,
 RoleArn,
 region
)
SELECT 
'{{ ModelQualityAppSpecification }}',
 '{{ ModelQualityJobInput }}',
 '{{ ModelQualityJobOutputConfig }}',
 '{{ JobResources }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.model_quality_job_definitions (
 JobDefinitionName,
 ModelQualityBaselineConfig,
 ModelQualityAppSpecification,
 ModelQualityJobInput,
 ModelQualityJobOutputConfig,
 JobResources,
 NetworkConfig,
 EndpointName,
 RoleArn,
 StoppingCondition,
 Tags,
 region
)
SELECT 
 '{{ JobDefinitionName }}',
 '{{ ModelQualityBaselineConfig }}',
 '{{ ModelQualityAppSpecification }}',
 '{{ ModelQualityJobInput }}',
 '{{ ModelQualityJobOutputConfig }}',
 '{{ JobResources }}',
 '{{ NetworkConfig }}',
 '{{ EndpointName }}',
 '{{ RoleArn }}',
 '{{ StoppingCondition }}',
 '{{ Tags }}',
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
  - name: model_quality_job_definition
    props:
      - name: JobDefinitionName
        value: '{{ JobDefinitionName }}'
      - name: ModelQualityBaselineConfig
        value:
          BaseliningJobName: '{{ BaseliningJobName }}'
          ConstraintsResource:
            S3Uri: '{{ S3Uri }}'
      - name: ModelQualityAppSpecification
        value:
          ContainerArguments:
            - '{{ ContainerArguments[0] }}'
          ContainerEntrypoint:
            - '{{ ContainerEntrypoint[0] }}'
          ImageUri: '{{ ImageUri }}'
          PostAnalyticsProcessorSourceUri: null
          RecordPreprocessorSourceUri: null
          Environment: {}
          ProblemType: '{{ ProblemType }}'
      - name: ModelQualityJobInput
        value:
          EndpointInput:
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
          GroundTruthS3Input:
            S3Uri: '{{ S3Uri }}'
      - name: ModelQualityJobOutputConfig
        value:
          KmsKeyId: '{{ KmsKeyId }}'
          MonitoringOutputs:
            - S3Output:
                LocalPath: '{{ LocalPath }}'
                S3UploadMode: '{{ S3UploadMode }}'
                S3Uri: '{{ S3Uri }}'
      - name: JobResources
        value:
          ClusterConfig:
            InstanceCount: '{{ InstanceCount }}'
            InstanceType: '{{ InstanceType }}'
            VolumeKmsKeyId: '{{ VolumeKmsKeyId }}'
            VolumeSizeInGB: '{{ VolumeSizeInGB }}'
      - name: NetworkConfig
        value:
          EnableInterContainerTrafficEncryption: '{{ EnableInterContainerTrafficEncryption }}'
          EnableNetworkIsolation: '{{ EnableNetworkIsolation }}'
          VpcConfig:
            SecurityGroupIds:
              - '{{ SecurityGroupIds[0] }}'
            Subnets:
              - '{{ Subnets[0] }}'
      - name: EndpointName
        value: null
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: StoppingCondition
        value:
          MaxRuntimeInSeconds: '{{ MaxRuntimeInSeconds }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.model_quality_job_definitions
WHERE data__Identifier = '<JobDefinitionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>model_quality_job_definitions</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateModelQualityJobDefinition,
sagemaker:DescribeModelQualityJobDefinition,
sagemaker:AddTags,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteModelQualityJobDefinition
```

### Read
```json
sagemaker:DescribeModelQualityJobDefinition
```

### List
```json
sagemaker:ListModelQualityJobDefinitions,
sagemaker:ListTags
```

