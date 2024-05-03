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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>inference_component</code> resource, use <code>inference_components</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_component</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::InferenceComponent</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.inference_component" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="inference_component_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="inference_component_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="variant_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="failure_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="specification" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="runtime_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="inference_component_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.sagemaker.inference_component
WHERE data__Identifier = '<InferenceComponentArn>';
```

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

