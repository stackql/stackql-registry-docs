---
title: workflow
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow
  - omics
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
<tr><td><b>Id</b></td><td><code>awscc.omics.workflow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>definition_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>main</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>parameter_template</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>accelerators</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>storage_capacity</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>workflow</code> resource, the following permissions are required:

### Read
```json
omics:GetWorkflow
```

### Update
```json
omics:UpdateWorkflow,
omics:GetWorkflow,
omics:TagResource,
omics:ListTagsForResource,
omics:UntagResource
```

### Delete
```json
omics:DeleteWorkflow,
omics:GetWorkflow
```


## Example
```sql
SELECT
region,
arn,
creation_time,
definition_uri,
description,
engine,
id,
main,
name,
parameter_template,
status,
accelerators,
storage_capacity,
tags,
type
FROM awscc.omics.workflow
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
