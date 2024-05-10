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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>firewall_policy</code> resource, use <code>firewall_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::FirewallPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.firewall_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="firewall_policy_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_policy_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_policy_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
firewall_policy_name,
firewall_policy_arn,
firewall_policy,
firewall_policy_id,
description,
tags
FROM aws.networkfirewall.firewall_policy
WHERE region = 'us-east-1' AND data__Identifier = '<FirewallPolicyArn>';
```


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

