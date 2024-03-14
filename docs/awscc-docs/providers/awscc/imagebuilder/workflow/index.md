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
Gets an individual <code>workflow</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workflow</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.imagebuilder.workflow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the workflow.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the workflow.</td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td>The version of the workflow.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the workflow.</td></tr>
<tr><td><code>change_description</code></td><td><code>string</code></td><td>The change description of the workflow.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the workflow denotes whether the workflow is used to build, test, or distribute.</td></tr>
<tr><td><code>data</code></td><td><code>string</code></td><td>The data of the workflow.</td></tr>
<tr><td><code>uri</code></td><td><code>string</code></td><td>The uri of the workflow.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The KMS key identifier used to encrypt the workflow.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>The tags associated with the workflow.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.imagebuilder.workflow
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

