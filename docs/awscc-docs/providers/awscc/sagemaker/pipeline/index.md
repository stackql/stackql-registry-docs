---
title: pipeline
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline
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
Gets an individual <code>pipeline</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>pipeline</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.pipeline</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>pipeline_name</code></td><td><code>string</code></td><td>The name of the Pipeline.</td></tr>
<tr><td><code>pipeline_display_name</code></td><td><code>string</code></td><td>The display name of the Pipeline.</td></tr>
<tr><td><code>pipeline_description</code></td><td><code>string</code></td><td>The description of the Pipeline.</td></tr>
<tr><td><code>pipeline_definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>parallelism_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>pipeline</code> resource, the following permissions are required:

### Read
```json
sagemaker:DescribePipeline,
sagemaker:ListTags
```

### Update
```json
iam:PassRole,
s3:GetObject,
sagemaker:UpdatePipeline,
sagemaker:DescribePipeline,
sagemaker:AddTags,
sagemaker:DeleteTags,
sagemaker:ListTags
```

### Delete
```json
sagemaker:DeletePipeline
```


## Example
```sql
SELECT
region,
pipeline_name,
pipeline_display_name,
pipeline_description,
pipeline_definition,
role_arn,
tags,
parallelism_configuration
FROM awscc.sagemaker.pipeline
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;PipelineName&gt;'
```
