---
title: wireless_gateways_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - wireless_gateways_list_only
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

Lists <code>wireless_gateways</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/wireless_gateways/"><code>wireless_gateways</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>wireless_gateways_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Create and manage wireless gateways, including LoRa gateways.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.wireless_gateways_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of Wireless Gateway.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of Wireless Gateway.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the gateway.</td></tr>
<tr><td><CopyableCode code="lo_ra_wan" /></td><td><code>object</code></td><td>The combination of Package, Station and Model which represents the version of the LoRaWAN Wireless Gateway.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn for Wireless Gateway. Returned upon successful create.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id for Wireless Gateway. Returned upon successful create.</td></tr>
<tr><td><CopyableCode code="thing_arn" /></td><td><code>string</code></td><td>Thing Arn. Passed into Update to associate a Thing with the Wireless Gateway.</td></tr>
<tr><td><CopyableCode code="thing_name" /></td><td><code>string</code></td><td>Thing Name. If there is a Thing created, this can be returned with a Get call.</td></tr>
<tr><td><CopyableCode code="last_uplink_received_at" /></td><td><code>string</code></td><td>The date and time when the most recent uplink was received.</td></tr>
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
Lists all <code>wireless_gateways</code> in a region.
```sql
SELECT
region,
id
FROM aws.iotwireless.wireless_gateways_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>wireless_gateways_list_only</code> resource, see <a href="/providers/aws/iotwireless/wireless_gateways/#permissions"><code>wireless_gateways</code></a>


