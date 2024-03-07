---
title: rule
hide_title: false
hide_table_of_contents: false
keywords:
  - rule
  - connect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>rule</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rule</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the rule.</td></tr>
<tr><td><code>rule_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the rule.</td></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><code>trigger_event_source</code></td><td><code>object</code></td><td>The event source that triggers the rule.</td></tr>
<tr><td><code>function</code></td><td><code>string</code></td><td>The conditions of a rule.</td></tr>
<tr><td><code>actions</code></td><td><code>object</code></td><td>The list of actions that will be executed when a rule is triggered.</td></tr>
<tr><td><code>publish_status</code></td><td><code>string</code></td><td>The publish status of a rule, either draft or published.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
rule_arn,
instance_arn,
trigger_event_source,
function,
actions,
publish_status,
tags
FROM awscc.connect.rule
WHERE region = 'us-east-1'
AND data__Identifier = '{RuleArn}';
```

## Permissions

To operate on the <code>rule</code> resource, the following permissions are required:

### Read
```json
connect:DescribeRule
```

### Delete
```json
connect:DeleteRule,
connect:UntagResource
```

### Update
```json
connect:UpdateRule,
cases:GetTemplate,
cases:ListFields,
cases:ListFieldOptions,
connect:TagResource,
connect:UntagResource
```

