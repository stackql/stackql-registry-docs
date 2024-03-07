---
title: workflow
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow
  - transfer
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
<tr><td><b>Id</b></td><td><code>awscc.transfer.workflow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>on_exception_steps</code></td><td><code>array</code></td><td>Specifies the steps (actions) to take if any errors are encountered during execution of the workflow.</td></tr>
<tr><td><code>steps</code></td><td><code>array</code></td><td>Specifies the details for the steps that are in the specified workflow.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A textual description for the workflow.</td></tr>
<tr><td><code>workflow_id</code></td><td><code>string</code></td><td>A unique identifier for the workflow.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the workflow.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
on_exception_steps,
steps,
tags,
description,
workflow_id,
arn
FROM awscc.transfer.workflow
WHERE region = 'us-east-1'
AND data__Identifier = '{WorkflowId}';
```

## Permissions

To operate on the <code>workflow</code> resource, the following permissions are required:

### Read
```json
transfer:DescribeWorkflow
```

### Delete
```json
transfer:DeleteWorkflow
```

### Update
```json
transfer:UnTagResource,
transfer:TagResource
```

