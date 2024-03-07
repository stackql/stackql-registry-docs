---
title: firewall_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy
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
Gets an individual <code>firewall_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkfirewall.firewall_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>firewall_policy_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_policy_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>firewall_policy_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>firewall_policy</code> resource, the following permissions are required:

### Read
```json
network-firewall:DescribeFirewallPolicy,
network-firewall:ListTagsForResources
```

### Update
```json
network-firewall:UpdateFirewallPolicy,
network-firewall:DescribeFirewallPolicy,
network-firewall:TagResource,
network-firewall:UntagResource,
network-firewall:ListRuleGroups,
network-firewall:ListTLSInspectionConfigurations
```

### Delete
```json
network-firewall:DeleteFirewallPolicy,
network-firewall:DescribeFirewallPolicy,
network-firewall:UntagResource
```


## Example
```sql
SELECT
region,
firewall_policy_name,
firewall_policy_arn,
firewall_policy,
firewall_policy_id,
description,
tags
FROM awscc.networkfirewall.firewall_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;FirewallPolicyArn&gt;'
```
