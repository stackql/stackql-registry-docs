---
title: customer_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateway
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


Gets or updates an individual <code>customer_gateway</code> resource, use <code>customer_gateways</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a customer gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.customer_gateway" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="customer_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bgp_asn" /></td><td><code>integer</code></td><td>For devices that support BGP, the customer gateway's BGP ASN.&lt;br&#x2F;&gt; Default: 65000</td></tr>
<tr><td><CopyableCode code="ip_address" /></td><td><code>string</code></td><td>IPv4 address for the customer gateway device's outside interface. The address must be static.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags for the customer gateway.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of VPN connection that this customer gateway supports (<code>ipsec.1</code>).</td></tr>
<tr><td><CopyableCode code="device_name" /></td><td><code>string</code></td><td>The name of customer gateway device.</td></tr>
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
certificate_arn,
customer_gateway_id,
bgp_asn,
ip_address,
tags,
type,
device_name
FROM aws.ec2.customer_gateway
WHERE region = 'us-east-1' AND data__Identifier = '<CustomerGatewayId>';
```


## Permissions

To operate on the <code>customer_gateway</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeCustomerGateways
```

### Update
```json
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeCustomerGateways
```

