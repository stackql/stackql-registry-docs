---
title: firewall_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_tags
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

Expands all tag keys and values for <code>firewalls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::NetworkFirewall::Firewall</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.networkfirewall.firewall_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="firewall_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="firewall_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_policy_arn" /></td><td><code>string</code></td><td>A resource ARN.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_mappings" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="delete_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_change_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="firewall_policy_change_protection" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>firewalls</code> in a region.
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
tag_key,
tag_value
FROM aws.networkfirewall.firewall_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>firewall_tags</code> resource, see <a href="/providers/aws/networkfirewall/firewalls/#permissions"><code>firewalls</code></a>

