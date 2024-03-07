---
title: state_machine_version
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machine_version
  - stepfunctions
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>state_machine_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machine_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>state_machine_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.stepfunctions.state_machine_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>state_machine_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>state_machine_revision_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
state_machine_arn,
state_machine_revision_id,
description
FROM awscc.stepfunctions.state_machine_version
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>state_machine_version</code> resource, the following permissions are required:

### Read
```json
states:DescribeStateMachine
```

### Delete
```json
states:DeleteStateMachineVersion,
states:DescribeStateMachine
```

