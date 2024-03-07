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
Retrieves a list of <code>model_explainability_job_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_explainability_job_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>model_explainability_job_definitions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.model_explainability_job_definitions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>job_definition_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of job definition.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>model_explainability_job_definitions</code> resource, the following permissions are required:

### Create
<pre>
sagemaker:CreateModelExplainabilityJobDefinition,
sagemaker:DescribeModelExplainabilityJobDefinition,
iam:PassRole,
sagemaker:AddTags</pre>

### List
<pre>
sagemaker:ListModelExplainabilityJobDefinitions,
sagemaker:ListTags</pre>


## Example
```sql
SELECT
region,
job_definition_arn
FROM awscc.sagemaker.model_explainability_job_definitions
WHERE region = 'us-east-1'
```
