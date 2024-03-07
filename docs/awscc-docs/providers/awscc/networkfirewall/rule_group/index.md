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
Gets an individual <code>rule_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rule_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>rule_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkfirewall.rule_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>rule_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_group_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_group_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>rule_group</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>rule_group</code> resource, the following permissions are required:

### Read
<pre>
network-firewall:DescribeRuleGroup,
network-firewall:ListTagsForResources</pre>

### Update
<pre>
network-firewall:UpdateRuleGroup,
network-firewall:DescribeRuleGroup,
network-firewall:TagResource,
network-firewall:UntagResource,
iam:CreateServiceLinkedRole,
ec2:GetManagedPrefixListEntries</pre>

### Delete
<pre>
network-firewall:DeleteRuleGroup,
network-firewall:DescribeRuleGroup,
network-firewall:UntagResource</pre>


## Example
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
FROM awscc.networkfirewall.rule_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;RuleGroupArn&gt;'
```
