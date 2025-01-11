---
title: nat_gateway_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateway_tags
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

Expands all tag keys and values for <code>nat_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_gateway_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a network address translation (NAT) gateway in the specified subnet. You can create either a public NAT gateway or a private NAT gateway. The default is a public NAT gateway. If you create a public NAT gateway, you must specify an elastic IP address.<br />With a NAT gateway, instances in a private subnet can connect to the internet, other AWS services, or an on-premises network using the IP address of the NAT gateway. For more information, see &#91;NAT gateways&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*.<br />If you add a default route (<code>AWS::EC2::Route</code> resource) that points to a NAT gateway, specify the NAT gateway ID for the route's <code>NatGatewayId</code> property.<br />When you associate an Elastic IP address or secondary Elastic IP address with a public NAT gateway, the network border group of the Elastic IP address must match the network border group of the Availability Zone (AZ) that the public NAT gateway is in. Otherwise, the NAT gateway fails to launch. You can see the network border group for the AZ by viewing the details of the subnet. Similarly, you can view the network border group for the Elastic IP address by viewing its details. For more information, see &#91;Allocate an Elastic IP address&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#allocate-eip) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.nat_gateway_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="secondary_allocation_ids" /></td><td><code>array</code></td><td>Secondary EIP allocation IDs. For more information, see &#91;Create a NAT gateway&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><CopyableCode code="private_ip_address" /></td><td><code>string</code></td><td>The private IPv4 address to assign to the NAT gateway. If you don't provide an address, a private IPv4 address will be automatically assigned.</td></tr>
<tr><td><CopyableCode code="connectivity_type" /></td><td><code>string</code></td><td>Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity.</td></tr>
<tr><td><CopyableCode code="secondary_private_ip_addresses" /></td><td><code>array</code></td><td>Secondary private IPv4 addresses. For more information about secondary addresses, see &#91;Create a NAT gateway&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon Virtual Private Cloud User Guide*.<br /><code>SecondaryPrivateIpAddressCount</code> and <code>SecondaryPrivateIpAddresses</code> cannot be set at the same time.</td></tr>
<tr><td><CopyableCode code="secondary_private_ip_address_count" /></td><td><code>integer</code></td><td>&#91;Private NAT gateway only&#93; The number of secondary private IPv4 addresses you want to assign to the NAT gateway. For more information about secondary addresses, see &#91;Create a NAT gateway&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon Virtual Private Cloud User Guide*.<br /><code>SecondaryPrivateIpAddressCount</code> and <code>SecondaryPrivateIpAddresses</code> cannot be set at the same time.</td></tr>
<tr><td><CopyableCode code="allocation_id" /></td><td><code>string</code></td><td>&#91;Public NAT gateway only&#93; The allocation ID of the Elastic IP address that's associated with the NAT gateway. This property is required for a public NAT gateway and cannot be specified with a private NAT gateway.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet in which the NAT gateway is located.</td></tr>
<tr><td><CopyableCode code="nat_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_drain_duration_seconds" /></td><td><code>integer</code></td><td>The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in progress. Default value is 350 seconds.</td></tr>
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
Expands tags for all <code>nat_gateways</code> in a region.
```sql
SELECT
region,
secondary_allocation_ids,
private_ip_address,
connectivity_type,
secondary_private_ip_addresses,
secondary_private_ip_address_count,
allocation_id,
subnet_id,
nat_gateway_id,
max_drain_duration_seconds,
tag_key,
tag_value
FROM aws.ec2.nat_gateway_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>nat_gateway_tags</code> resource, see <a href="/providers/aws/ec2/nat_gateways/#permissions"><code>nat_gateways</code></a>

