---
title: model_quality_job_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - model_quality_job_definition
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
Gets an individual <code>model_quality_job_definition</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_quality_job_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.sagemaker.model_quality_job_definition</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>JobDefinitionArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of job definition.</td></tr><tr><td><code>JobDefinitionName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ModelQualityBaselineConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ModelQualityAppSpecification</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ModelQualityJobInput</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ModelQualityJobOutputConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>JobResources</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>NetworkConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>EndpointName</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</td></tr><tr><td><code>StoppingCondition</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr><tr><td><code>CreationTime</code></td><td><code>string</code></td><td>The time at which the job definition was created.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.model_quality_job_definition
WHERE region = 'us-east-1' AND data__Identifier = '{JobDefinitionArn}'
</pre>
