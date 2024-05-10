---
title: firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>firewalls</code> in a region or to create or delete a <code>firewalls</code> resource, use <code>firewall</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::Firewall</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.firewalls" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="firewall_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
firewall_arn
FROM aws.networkfirewall.firewalls
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "FirewallName": "{{ FirewallName }}",
 "FirewallPolicyArn": "{{ FirewallPolicyArn }}",
 "VpcId": "{{ VpcId }}",
 "SubnetMappings": [
  {
   "SubnetId": "{{ SubnetId }}",
   "IPAddressType": "{{ IPAddressType }}"
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.networkfirewall.firewalls (
 FirewallName,
 FirewallPolicyArn,
 VpcId,
 SubnetMappings,
 region
)
SELECT 
{{ .FirewallName }},
 {{ .FirewallPolicyArn }},
 {{ .VpcId }},
 {{ .SubnetMappings }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FirewallName": "{{ FirewallName }}",
 "FirewallPolicyArn": "{{ FirewallPolicyArn }}",
 "VpcId": "{{ VpcId }}",
 "SubnetMappings": [
  {
   "SubnetId": "{{ SubnetId }}",
   "IPAddressType": "{{ IPAddressType }}"
  }
 ],
 "DeleteProtection": "{{ DeleteProtection }}",
 "SubnetChangeProtection": "{{ SubnetChangeProtection }}",
 "FirewallPolicyChangeProtection": "{{ FirewallPolicyChangeProtection }}",
 "Description": "{{ Description }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.networkfirewall.firewalls (
 FirewallName,
 FirewallPolicyArn,
 VpcId,
 SubnetMappings,
 DeleteProtection,
 SubnetChangeProtection,
 FirewallPolicyChangeProtection,
 Description,
 Tags,
 region
)
SELECT 
 {{ .FirewallName }},
 {{ .FirewallPolicyArn }},
 {{ .VpcId }},
 {{ .SubnetMappings }},
 {{ .DeleteProtection }},
 {{ .SubnetChangeProtection }},
 {{ .FirewallPolicyChangeProtection }},
 {{ .Description }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.networkfirewall.firewalls
WHERE data__Identifier = '<FirewallArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>firewalls</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVpcEndpoint,
ec2:DescribeVpcEndpoints,
ec2:DescribeSubnets,
ec2:DescribeVpcs,
iam:CreateServiceLinkedRole,
network-firewall:CreateFirewall,
network-firewall:DescribeFirewallPolicy,
network-firewall:DescribeRuleGroup,
network-firewall:TagResource,
network-firewall:AssociateSubnets,
network-firewall:AssociateFirewallPolicy,
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

### List
```json
network-firewall:ListFirewalls
```

