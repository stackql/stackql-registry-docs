---
title: rule_group
hide_title: false
hide_table_of_contents: false
keywords:
  - rule_group
  - networkfirewall
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

Gets or operates on an individual <code>rule_group</code> resource, use <code>rule_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::RuleGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.rule_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rule_group_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_group_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_group_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_group" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
rule_group_name,
rule_group_arn,
rule_group_id,
rule_group,
type,
capacity,
description,
tags
FROM aws.networkfirewall.rule_group
WHERE data__Identifier = '<RuleGroupArn>';
```

## Permissions

To operate on the <code>rule_group</code> resource, the following permissions are required:

### Read
```json
network-firewall:DescribeRuleGroup,
network-firewall:ListTagsForResources
```

### Update
```json
network-firewall:UpdateRuleGroup,
network-firewall:DescribeRuleGroup,
network-firewall:TagResource,
network-firewall:UntagResource,
iam:CreateServiceLinkedRole,
ec2:GetManagedPrefixListEntries
```

### Delete
```json
network-firewall:DeleteRuleGroup,
network-firewall:DescribeRuleGroup,
network-firewall:UntagResource
```

