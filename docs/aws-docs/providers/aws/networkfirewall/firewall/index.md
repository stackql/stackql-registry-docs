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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>firewall</code> resource, use <code>firewalls</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::Firewall</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.firewall" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="firewall_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_policy_arn" /></td><td><code>string</code></td><td></td></tr>
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
WHERE region = 'us-east-1' AND data__Identifier = '<FirewallArn>';
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

