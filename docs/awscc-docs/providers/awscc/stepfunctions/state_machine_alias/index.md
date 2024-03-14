---
title: state_machine_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machine_alias
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
Gets an individual <code>state_machine_alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machine_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>state_machine_alias</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.stepfunctions.state_machine_alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the alias.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The alias name.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>An optional description of the alias.</td></tr>
<tr><td><code>routing_configuration</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>deployment_preference</code></td><td><code>object</code></td><td></td></tr>
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
description,
routing_configuration,
deployment_preference
FROM awscc.stepfunctions.state_machine_alias
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>state_machine_alias</code> resource, the following permissions are required:

### Read
```json
states:DescribeStateMachineAlias
```

### Update
```json
cloudwatch:DescribeAlarms,
states:UpdateStateMachineAlias,
states:DescribeStateMachineAlias
```

### Delete
```json
states:DescribeStateMachineAlias,
states:DeleteStateMachineAlias
```

