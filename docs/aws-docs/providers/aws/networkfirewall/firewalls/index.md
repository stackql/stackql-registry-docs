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

Creates, updates, deletes or gets a <code>firewall</code> resource or lists <code>firewalls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::Firewall</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.firewalls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="firewall_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_arn" /></td><td><code>A resource ARN.</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_policy_arn" /></td><td><code>A resource ARN.</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_mappings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="delete_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_change_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_policy_change_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_ids" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="FirewallName, FirewallPolicyArn, VpcId, SubnetMappings, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>firewalls</code> in a region.
```sql
SELECT
region,
firewall_arn
FROM aws.networkfirewall.firewalls
WHERE region = 'us-east-1';
```
Gets all properties from a <code>firewall</code>.
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
FROM aws.networkfirewall.firewalls
WHERE region = 'us-east-1' AND data__Identifier = '<FirewallArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewall</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### List
```json
network-firewall:ListFirewalls
```

