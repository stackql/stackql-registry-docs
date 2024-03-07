---
title: state_machine_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - state_machine_aliases
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
Retrieves a list of <code>state_machine_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>state_machine_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>state_machine_aliases</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.stepfunctions.state_machine_aliases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the alias.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>state_machine_aliases</code> resource, the following permissions are required:

### Create
<pre>
states:CreateStateMachineAlias,
states:DescribeStateMachineAlias</pre>

### List
<pre>
states:ListStateMachineAliases</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.stepfunctions.state_machine_aliases
WHERE region = 'us-east-1'
```
