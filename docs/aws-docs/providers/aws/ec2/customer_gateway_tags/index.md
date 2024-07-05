---
title: customer_gateway_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateway_tags
  - ec2
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

Expands all tag keys and values for <code>customer_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a customer gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.customer_gateway_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of VPN connection that this customer gateway supports (<code>ipsec.1</code>).</td></tr>
<tr><td><CopyableCode code="customer_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_address" /></td><td><code>string</code></td><td>IPv4 address for the customer gateway device's outside interface. The address must be static.</td></tr>
<tr><td><CopyableCode code="bgp_asn_extended" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="bgp_asn" /></td><td><code>integer</code></td><td>For devices that support BGP, the customer gateway's BGP ASN.<br />Default: 65000</td></tr>
<tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="device_name" /></td><td><code>string</code></td><td>The name of customer gateway device.</td></tr>
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
Expands tags for all <code>customer_gateways</code> in a region.
```sql
SELECT
region,
type,
customer_gateway_id,
ip_address,
bgp_asn_extended,
bgp_asn,
certificate_arn,
device_name,
tag_key,
tag_value
FROM aws.ec2.customer_gateway_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>customer_gateway_tags</code> resource, see <a href="/providers/aws/ec2/customer_gateways/#permissions"><code>customer_gateways</code></a>


