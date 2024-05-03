---
title: workflow
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow
  - imagebuilder
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

Gets or operates on an individual <code>workflow</code> resource, use <code>workflows</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::ImageBuilder::Workflow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.imagebuilder.workflow" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the workflow.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the workflow.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the workflow.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the workflow.</td></tr>
<tr><td><CopyableCode code="change_description" /></td><td><code>string</code></td><td>The change description of the workflow.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the workflow denotes whether the workflow is used to build, test, or distribute.</td></tr>
<tr><td><CopyableCode code="data" /></td><td><code>string</code></td><td>The data of the workflow.</td></tr>
<tr><td><CopyableCode code="uri" /></td><td><code>string</code></td><td>The uri of the workflow.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The KMS key identifier used to encrypt the workflow.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The tags associated with the workflow.</td></tr>
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
arn,
name,
version,
description,
change_description,
type,
data,
uri,
kms_key_id,
tags
FROM aws.imagebuilder.workflow
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>workflow</code> resource, the following permissions are required:

### Read
```json
imagebuilder:GetWorkflow
```

### Delete
```json
imagebuilder:GetWorkflow,
imagebuilder:UnTagResource,
imagebuilder:DeleteWorkflow
```
