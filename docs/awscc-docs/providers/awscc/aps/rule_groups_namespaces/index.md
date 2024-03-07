---
title: rule_groups_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_groups_namespaces
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
Retrieves a list of <code>rule_groups_namespaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_groups_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rule_groups_namespaces</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.aps.rule_groups_namespaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The RuleGroupsNamespace ARN.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn
FROM awscc.aps.rule_groups_namespaces
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>rule_groups_namespaces</code> resource, the following permissions are required:

### Create
```json
aps:CreateRuleGroupsNamespace,
aps:DescribeRuleGroupsNamespace,
aps:TagResource
```

### List
```json
aps:ListRuleGroupsNamespaces,
aps:ListTagsForResource
```

