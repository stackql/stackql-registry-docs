---
title: multicast_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - multicast_group_tags
  - iotwireless
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

Expands all tag keys and values for <code>multicast_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multicast_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage Multicast groups.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.multicast_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of Multicast group</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Multicast group description</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>Multicast group LoRaWAN</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Multicast group arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Multicast group id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Multicast group status. Returned after successful read.</td></tr>
<tr><td><CopyableCode code="associate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr>
<tr><td><CopyableCode code="disassociate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr>
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
Expands tags for all <code>multicast_groups</code> in a region.
```sql
SELECT
region,
name,
description,
lo_ra_wan,
arn,
id,
status,
associate_wireless_device,
disassociate_wireless_device,
tag_key,
tag_value
FROM aws.iotwireless.multicast_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>multicast_group_tags</code> resource, see <a href="/providers/aws/iotwireless/multicast_groups/#permissions"><code>multicast_groups</code></a>


