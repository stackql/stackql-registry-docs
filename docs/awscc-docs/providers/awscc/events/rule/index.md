---
title: rule
hide_title: false
hide_table_of_contents: false
keywords:
  - rule
  - events
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
<tr><td><b>Id</b></td><td><code>awscc.events.rule</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>event_bus_name</code></td><td><code>string</code></td><td>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</td></tr>
<tr><td><code>event_pattern</code></td><td><code>object</code></td><td>The event pattern of the rule. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide.</td></tr>
<tr><td><code>schedule_expression</code></td><td><code>string</code></td><td>The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)". For more information, see Creating an Amazon EventBridge rule that runs on a schedule.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the rule.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the rule.</td></tr>
<tr><td><code>targets</code></td><td><code>array</code></td><td>Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.&lt;br&#x2F;&gt;Targets are the resources that are invoked when a rule is triggered.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the rule, such as arn:aws:events:us-east-2:123456789012:rule&#x2F;example.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the role that is used for target invocation.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the rule.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
event_bus_name,
event_pattern,
schedule_expression,
description,
state,
targets,
arn,
role_arn,
name
FROM awscc.events.rule
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>rule</code> resource, the following permissions are required:

### Read
```json
iam:PassRole,
events:DescribeRule,
events:ListTargetsByRule
```

### Update
```json
iam:PassRole,
events:DescribeRule,
events:PutRule,
events:RemoveTargets,
events:PutTargets
```

### Delete
```json
iam:PassRole,
events:DescribeRule,
events:DeleteRule,
events:RemoveTargets,
events:ListTargetsByRule
```

