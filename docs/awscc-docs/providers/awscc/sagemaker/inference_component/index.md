---
title: inference_component
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_component
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
Gets an individual <code>inference_component</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_component</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>inference_component</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.sagemaker.inference_component</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>inference_component_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>inference_component_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>variant_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>failure_reason</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>specification</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>runtime_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>inference_component_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_modified_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>inference_component</code> resource, the following permissions are required:

### Update
```json
sagemaker:UpdateInferenceComponent,
sagemaker:UpdateInferenceComponentRuntimeConfig,
sagemaker:DescribeInferenceComponent,
sagemaker:AddTags,
sagemaker:ListTags,
sagemaker:DeleteTags
```

### Delete
```json
sagemaker:DescribeInferenceComponent,
sagemaker:DeleteInferenceComponent,
sagemaker:DeleteTags
```

### Read
```json
sagemaker:DescribeInferenceComponent,
sagemaker:ListTags
```


## Example
```sql
SELECT
region,
inference_component_arn,
inference_component_name,
endpoint_arn,
endpoint_name,
variant_name,
failure_reason,
specification,
runtime_config,
inference_component_status,
creation_time,
last_modified_time,
tags
FROM awscc.sagemaker.inference_component
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;InferenceComponentArn&gt;'
```
