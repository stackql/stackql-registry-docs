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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>firewall_policies</code> in a region or to create or delete a <code>firewall_policies</code> resource, use <code>firewall_policy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::FirewallPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.firewall_policies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="firewall_policy_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
firewall_policy_arn
FROM aws.networkfirewall.firewall_policies
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
 "FirewallPolicyName": "{{ FirewallPolicyName }}",
 "FirewallPolicy": {
  "FirewallPolicyName": "{{ FirewallPolicyName }}",
  "FirewallPolicy": null
 }
}
>>>
--required properties only
INSERT INTO aws.networkfirewall.firewall_policies (
 FirewallPolicyName,
 FirewallPolicy,
 region
)
SELECT 
{{ .FirewallPolicyName }},
 {{ .FirewallPolicy }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "FirewallPolicyName": "{{ FirewallPolicyName }}",
 "FirewallPolicy": {
  "FirewallPolicyName": "{{ FirewallPolicyName }}",
  "FirewallPolicy": null,
  "Description": "{{ Description }}",
  "Tags": [
   {
    "Key": "{{ Key }}",
    "Value": "{{ Value }}"
   }
  ]
 },
 "Description": "{{ Description }}",
 "Tags": [
  null
 ]
}
>>>
--all properties
INSERT INTO aws.networkfirewall.firewall_policies (
 FirewallPolicyName,
 FirewallPolicy,
 Description,
 Tags,
 region
)
SELECT 
 {{ .FirewallPolicyName }},
 {{ .FirewallPolicy }},
 {{ .Description }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.networkfirewall.firewall_policies
WHERE data__Identifier = '<FirewallPolicyArn>'
AND region = 'us-east-1';
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

### Delete
```json
network-firewall:DeleteFirewallPolicy,
network-firewall:DescribeFirewallPolicy,
network-firewall:UntagResource
```

### List
```json
network-firewall:ListFirewallPolicies
```

