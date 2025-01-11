---
title: inference_experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_experiments
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

Creates, updates, deletes or gets an <code>inference_experiment</code> resource or lists <code>inference_experiments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::InferenceExperiment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.inference_experiments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the inference experiment.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the inference experiment.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the inference experiment that you want to run.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the inference experiment.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.</td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td>The name of the endpoint used to run the monitoring job.</td></tr>
<tr><td><CopyableCode code="endpoint_metadata" /></td><td><code>object</code></td><td>The metadata of the endpoint on which the inference experiment ran.</td></tr>
<tr><td><CopyableCode code="schedule" /></td><td><code>object</code></td><td>The duration for which you want the inference experiment to run.</td></tr>
<tr><td><CopyableCode code="kms_key" /></td><td><code>string</code></td><td>The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</td></tr>
<tr><td><CopyableCode code="data_storage_config" /></td><td><code>object</code></td><td>The Amazon S3 location and configuration for storing inference request and response data.</td></tr>
<tr><td><CopyableCode code="model_variants" /></td><td><code>array</code></td><td>An array of ModelVariantConfig objects. Each ModelVariantConfig object in the array describes the infrastructure configuration for the corresponding variant.</td></tr>
<tr><td><CopyableCode code="shadow_mode_config" /></td><td><code>object</code></td><td>The configuration of ShadowMode inference experiment type. Use this field to specify a production variant which takes all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant also specify the percentage of requests that Amazon SageMaker replicates.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The timestamp at which you created the inference experiment.</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td>The timestamp at which you last modified the inference experiment.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the inference experiment.</td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td>The error message or client-specified reason from the StopInferenceExperiment API, that explains the status of the inference experiment.</td></tr>
<tr><td><CopyableCode code="desired_state" /></td><td><code>string</code></td><td>The desired state of the experiment after starting or stopping operation.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-inferenceexperiment.html"><code>AWS::SageMaker::InferenceExperiment</code></a>.

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
    <td><CopyableCode code="Name, Type, RoleArn, EndpointName, ModelVariants, region" /></td>
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
Gets all <code>inference_experiments</code> in a region.
```sql
SELECT
region,
arn,
name,
type,
description,
role_arn,
endpoint_name,
endpoint_metadata,
schedule,
kms_key,
data_storage_config,
model_variants,
shadow_mode_config,
tags,
creation_time,
last_modified_time,
status,
status_reason,
desired_state
FROM aws.sagemaker.inference_experiments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>inference_experiment</code>.
```sql
SELECT
region,
arn,
name,
type,
description,
role_arn,
endpoint_name,
endpoint_metadata,
schedule,
kms_key,
data_storage_config,
model_variants,
shadow_mode_config,
tags,
creation_time,
last_modified_time,
status,
status_reason,
desired_state
FROM aws.sagemaker.inference_experiments
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>inference_experiment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sagemaker.inference_experiments (
 Name,
 Type,
 RoleArn,
 EndpointName,
 ModelVariants,
 region
)
SELECT 
'{{ Name }}',
 '{{ Type }}',
 '{{ RoleArn }}',
 '{{ EndpointName }}',
 '{{ ModelVariants }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.inference_experiments (
 Name,
 Type,
 Description,
 RoleArn,
 EndpointName,
 Schedule,
 KmsKey,
 DataStorageConfig,
 ModelVariants,
 ShadowModeConfig,
 Tags,
 StatusReason,
 DesiredState,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Type }}',
 '{{ Description }}',
 '{{ RoleArn }}',
 '{{ EndpointName }}',
 '{{ Schedule }}',
 '{{ KmsKey }}',
 '{{ DataStorageConfig }}',
 '{{ ModelVariants }}',
 '{{ ShadowModeConfig }}',
 '{{ Tags }}',
 '{{ StatusReason }}',
 '{{ DesiredState }}',
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
  - name: inference_experiment
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
      - name: Description
        value: '{{ Description }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: EndpointName
        value: '{{ EndpointName }}'
      - name: Schedule
        value:
          StartTime: '{{ StartTime }}'
          EndTime: '{{ EndTime }}'
      - name: KmsKey
        value: '{{ KmsKey }}'
      - name: DataStorageConfig
        value:
          Destination: '{{ Destination }}'
          KmsKey: '{{ KmsKey }}'
          ContentType:
            CsvContentTypes:
              - '{{ CsvContentTypes[0] }}'
            JsonContentTypes:
              - '{{ JsonContentTypes[0] }}'
      - name: ModelVariants
        value:
          - ModelName: '{{ ModelName }}'
            VariantName: '{{ VariantName }}'
            InfrastructureConfig:
              InfrastructureType: '{{ InfrastructureType }}'
              RealTimeInferenceConfig:
                InstanceType: '{{ InstanceType }}'
                InstanceCount: '{{ InstanceCount }}'
      - name: ShadowModeConfig
        value:
          SourceModelVariantName: '{{ SourceModelVariantName }}'
          ShadowModelVariants:
            - ShadowModelVariantName: '{{ ShadowModelVariantName }}'
              SamplingPercentage: '{{ SamplingPercentage }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: StatusReason
        value: '{{ StatusReason }}'
      - name: DesiredState
        value: '{{ DesiredState }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.inference_experiments
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>inference_experiments</code> resource, the following permissions are required:

### Create
```json
sagemaker:CreateInferenceExperiment,
sagemaker:DescribeInferenceExperiment,
sagemaker:AddTags,
sagemaker:ListTags,
iam:PassRole
```

### Delete
```json
sagemaker:DeleteInferenceExperiment,
sagemaker:DescribeInferenceExperiment,
sagemaker:StopInferenceExperiment,
sagemaker:ListTags
```

### List
```json
sagemaker:ListInferenceExperiments
```

### Read
```json
sagemaker:DescribeInferenceExperiment,
sagemaker:ListTags
```

### Update
```json
sagemaker:UpdateInferenceExperiment,
sagemaker:StartInferenceExperiment,
sagemaker:StopInferenceExperiment,
sagemaker:DescribeInferenceExperiment,
sagemaker:AddTags,
sagemaker:DeleteTags,
sagemaker:ListTags
```
