---
title: inference_components
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_components
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
Retrieves a list of <code>inference_components</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>inference_components</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.inference_components</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>inference_component_arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>inference_components</code> resource, the following permissions are required:

### Create
```json
sagemaker:AddTags,
sagemaker:ListTags,
sagemaker:CreateInferenceComponent,
sagemaker:DescribeInferenceComponent
```

### List
```json
sagemaker:ListInferenceComponents,
sagemaker:DescribeInferenceComponent,
sagemaker:ListTags
```


## Example
```sql
SELECT
region,
inference_component_arn
FROM awscc.sagemaker.inference_components
WHERE region = 'us-east-1'
```
