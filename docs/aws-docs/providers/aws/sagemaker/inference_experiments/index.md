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
Retrieves a list of <code>inference_experiments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.sagemaker.inference_experiments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the inference experiment.</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>The name for the inference experiment.</td></tr>
<tr><td><code>Type</code></td><td><code>string</code></td><td>The type of the inference experiment that you want to run.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>The description of the inference experiment.</td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to access model artifacts and container images, and manage Amazon SageMaker Inference endpoints for model deployment.</td></tr>
<tr><td><code>EndpointName</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>EndpointMetadata</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Schedule</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>KmsKey</code></td><td><code>string</code></td><td>The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint.</td></tr>
<tr><td><code>DataStorageConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>ModelVariants</code></td><td><code>array</code></td><td>An array of ModelVariantConfig objects. Each ModelVariantConfig object in the array describes the infrastructure configuration for the corresponding variant.</td></tr>
<tr><td><code>ShadowModeConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>CreationTime</code></td><td><code>string</code></td><td>The timestamp at which you created the inference experiment.</td></tr>
<tr><td><code>LastModifiedTime</code></td><td><code>string</code></td><td>The timestamp at which you last modified the inference experiment.</td></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td>The status of the inference experiment.</td></tr>
<tr><td><code>StatusReason</code></td><td><code>string</code></td><td>The error message or client-specified reason from the StopInferenceExperiment API, that explains the status of the inference experiment.</td></tr>
<tr><td><code>DesiredState</code></td><td><code>string</code></td><td>The desired state of the experiment after starting or stopping operation.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.inference_experiments
WHERE region = 'us-east-1'
</pre>
