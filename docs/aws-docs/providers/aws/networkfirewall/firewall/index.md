---
title: firewall
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall
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
Gets an individual <code>firewall</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::Firewall</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkfirewall.firewall</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>firewall_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>firewall_policy_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_mappings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>delete_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>subnet_change_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>firewall_policy_change_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
firewall_name,
firewall_arn,
firewall_id,
firewall_policy_arn,
vpc_id,
subnet_mappings,
delete_protection,
subnet_change_protection,
firewall_policy_change_protection,
description,
endpoint_ids,
tags
FROM aws.networkfirewall.firewall
WHERE data__Identifier = '<FirewallArn>';
```

## Permissions

To operate on the <code>firewall</code> resource, the following permissions are required:

### Read
```json
network-firewall:DescribeFirewall,
network-firewall:ListTagsForResources
```

### Update
```json
network-firewall:AssociateSubnets,
network-firewall:DisassociateSubnets,
network-firewall:UpdateFirewallDescription,
network-firewall:UpdateFirewallDeleteProtection,
network-firewall:UpdateSubnetChangeProtection,
network-firewall:UpdateFirewallPolicyChangeProtection,
network-firewall:AssociateFirewallPolicy,
network-firewall:TagResource,
network-firewall:UntagResource,
network-firewall:DescribeFirewall
```

### Delete
```json
ec2:DeleteVpcEndpoints,
ec2:DescribeRouteTables,
logs:DescribeLogGroups,
logs:DescribeResourcePolicies,
logs:GetLogDelivery,
logs:ListLogDeliveries,
network-firewall:DeleteFirewall,
network-firewall:UntagResource,
network-firewall:DescribeFirewall
```

