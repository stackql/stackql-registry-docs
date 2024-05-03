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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>pipeline</code> resource, use <code>pipelines</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Pipeline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.pipeline" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="pipeline_name" /></td><td><code>string</code></td><td>The name of the Pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_display_name" /></td><td><code>string</code></td><td>The display name of the Pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_description" /></td><td><code>string</code></td><td>The description of the Pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="parallelism_configuration" /></td><td><code>object</code></td><td></td></tr>
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
pipeline_name,
pipeline_display_name,
pipeline_description,
pipeline_definition,
role_arn,
tags,
parallelism_configuration
FROM aws.sagemaker.pipeline
WHERE data__Identifier = '<PipelineName>';
```

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

