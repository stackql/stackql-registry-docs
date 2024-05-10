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

Use the following StackQL query and manifest file to create a new <code>firewall</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- firewall.iql (required properties only)
INSERT INTO aws.networkfirewall.firewalls (
 FirewallName,
 FirewallPolicyArn,
 VpcId,
 SubnetMappings,
 region
)
SELECT 
'{{ FirewallName }}',
 '{{ FirewallPolicyArn }}',
 '{{ VpcId }}',
 '{{ SubnetMappings }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- firewall.iql (all properties)
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
 '{{ FirewallName }}',
 '{{ FirewallPolicyArn }}',
 '{{ VpcId }}',
 '{{ SubnetMappings }}',
 '{{ DeleteProtection }}',
 '{{ SubnetChangeProtection }}',
 '{{ FirewallPolicyChangeProtection }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: firewall
    props:
      - name: FirewallName
        value: '{{ FirewallName }}'
      - name: FirewallPolicyArn
        value: '{{ FirewallPolicyArn }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: SubnetMappings
        value:
          - SubnetId: '{{ SubnetId }}'
            IPAddressType: '{{ IPAddressType }}'
      - name: DeleteProtection
        value: '{{ DeleteProtection }}'
      - name: SubnetChangeProtection
        value: '{{ SubnetChangeProtection }}'
      - name: FirewallPolicyChangeProtection
        value: '{{ FirewallPolicyChangeProtection }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

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

