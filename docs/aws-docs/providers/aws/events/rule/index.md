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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>rule</code> resource, use <code>rules</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Rule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.rule" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="event_bus_name" /></td><td><code>string</code></td><td>The name or ARN of the event bus associated with the rule. If you omit this, the default event bus is used.</td></tr>
<tr><td><CopyableCode code="event_pattern" /></td><td><code>object</code></td><td>The event pattern of the rule. For more information, see Events and Event Patterns in the Amazon EventBridge User Guide.</td></tr>
<tr><td><CopyableCode code="schedule_expression" /></td><td><code>string</code></td><td>The scheduling expression. For example, "cron(0 20 * * ? *)", "rate(5 minutes)". For more information, see Creating an Amazon EventBridge rule that runs on a schedule.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the rule.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the rule.</td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>array</code></td><td>Adds the specified targets to the specified rule, or updates the targets if they are already associated with the rule.&lt;br&#x2F;&gt;Targets are the resources that are invoked when a rule is triggered.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the rule, such as arn:aws:events:us-east-2:123456789012:rule&#x2F;example.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the role that is used for target invocation.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the rule.</td></tr>
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
event_bus_name,
event_pattern,
schedule_expression,
description,
state,
targets,
arn,
role_arn,
name
FROM aws.events.rule
WHERE data__Identifier = '<Arn>';
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

