---
title: rule_groups_namespace
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups_namespace
  - aps
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>rule_groups_namespace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups_namespace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>RuleGroupsNamespace schema for cloudformation.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.aps.rule_groups_namespace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace</code></td><td><code>string</code></td><td>Required to identify a specific APS Workspace associated with this RuleGroupsNamespace.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The RuleGroupsNamespace name.</td></tr>
<tr><td><code>data</code></td><td><code>string</code></td><td>The RuleGroupsNamespace data.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The RuleGroupsNamespace ARN.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
workspace,
name,
data,
arn,
tags
FROM aws.aps.rule_groups_namespace
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>rule_groups_namespace</code> resource, the following permissions are required:

### Read
```json
aps:DescribeRuleGroupsNamespace,
aps:ListTagsForResource
```

### Update
```json
aps:PutRuleGroupsNamespace,
aps:DescribeRuleGroupsNamespace,
aps:TagResource,
aps:UntagResource,
aps:ListTagsForResource
```

### Delete
```json
aps:DeleteRuleGroupsNamespace,
aps:DescribeRuleGroupsNamespace
```

