---
title: multicast_groups_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - multicast_groups_list_only
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

Lists <code>multicast_groups</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/multicast_groups/"><code>multicast_groups</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multicast_groups_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage Multicast groups.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.multicast_groups_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of Multicast group</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Multicast group description</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>Multicast group LoRaWAN</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Multicast group arn. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Multicast group id. Returned after successful create.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the Multicast group.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Multicast group status. Returned after successful read.</td></tr>
<tr><td><CopyableCode code="associate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to associate. Only for update request.</td></tr>
<tr><td><CopyableCode code="disassociate_wireless_device" /></td><td><code>string</code></td><td>Wireless device to disassociate. Only for update request.</td></tr>
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
Lists all <code>multicast_groups</code> in a region.
```sql
SELECT
region,
id
FROM aws.iotwireless.multicast_groups_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>multicast_groups_list_only</code> resource, see <a href="/providers/aws/iotwireless/multicast_groups/#permissions"><code>multicast_groups</code></a>


