---
title: firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policies
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
Retrieves a list of <code>firewall_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>firewall_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkfirewall.firewall_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>firewall_policy_arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
firewall_policy_arn
FROM awscc.networkfirewall.firewall_policies
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>firewall_policies</code> resource, the following permissions are required:

### Create
```json
network-firewall:CreateFirewallPolicy,
network-firewall:DescribeFirewallPolicy,
network-firewall:ListTLSInspectionConfigurations,
network-firewall:TagResource,
network-firewall:ListRuleGroups
```

### List
```json
network-firewall:ListFirewallPolicies
```

