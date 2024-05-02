---
title: inference_experiment
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_experiment
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
Gets an individual <code>inference_experiment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_experiment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::InferenceExperiment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.inference_experiment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the inference experiment.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name for the inference experiment.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the inference experiment that you want to run.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the inference experiment.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.</td></tr>
<tr><td><code>endpoint_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_metadata</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kms_key</code></td><td><code>string</code></td><td>The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</td></tr>
<tr><td><code>data_storage_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_variants</code></td><td><code>array</code></td><td>An array of ModelVariantConfig objects. Each ModelVariantConfig object in the array describes the infrastructure configuration for the corresponding variant.</td></tr>
<tr><td><code>shadow_mode_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The timestamp at which you created the inference experiment.</td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td>The timestamp at which you last modified the inference experiment.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the inference experiment.</td></tr>
<tr><td><code>status_reason</code></td><td><code>string</code></td><td>The error message or client-specified reason from the StopInferenceExperiment API, that explains the status of the inference experiment.</td></tr>
<tr><td><code>desired_state</code></td><td><code>string</code></td><td>The desired state of the experiment after starting or stopping operation.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.sagemaker.inference_experiment
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>inference_experiment</code> resource, the following permissions are required:

### Delete
```json
sagemaker:DeleteInferenceExperiment,
sagemaker:DescribeInferenceExperiment,
sagemaker:StopInferenceExperiment,
sagemaker:ListTags
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

