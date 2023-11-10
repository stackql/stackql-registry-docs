---
title: model_bias_job_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - model_bias_job_definition
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
Gets an individual <code>model_bias_job_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_bias_job_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model_bias_job_definition</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.model_bias_job_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>job_definition_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of job definition.</td></tr>
<tr><td><code>job_definition_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>model_bias_baseline_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_bias_app_specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_bias_job_input</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>model_bias_job_output_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>job_resources</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>network_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>endpoint_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</td></tr>
<tr><td><code>stopping_condition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The time at which the job definition was created.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
job_definition_arn,
job_definition_name,
model_bias_baseline_config,
model_bias_app_specification,
model_bias_job_input,
model_bias_job_output_config,
job_resources,
network_config,
endpoint_name,
role_arn,
stopping_condition,
tags,
creation_time
FROM aws.sagemaker.model_bias_job_definition
WHERE region = 'us-east-1'
AND data__Identifier = '<JobDefinitionArn>'
```
