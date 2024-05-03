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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>rule</code> resource, use <code>rules</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS:Connect::Rule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.rule" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the rule.</td></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the rule.</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the instance.</td></tr>
<tr><td><CopyableCode code="trigger_event_source" /></td><td><code>object</code></td><td>The event source that triggers the rule.</td></tr>
<tr><td><CopyableCode code="function" /></td><td><code>string</code></td><td>The conditions of a rule.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>object</code></td><td>The list of actions that will be executed when a rule is triggered.</td></tr>
<tr><td><CopyableCode code="publish_status" /></td><td><code>string</code></td><td>The publish status of a rule, either draft or published.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
name,
rule_arn,
instance_arn,
trigger_event_source,
function,
actions,
publish_status,
tags
FROM aws.connect.rule
WHERE data__Identifier = '<RuleArn>';
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

