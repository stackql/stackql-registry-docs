---
title: nat_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateway
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
Gets an individual <code>nat_gateway</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>nat_gateway</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.nat_gateway</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td>The ID of the subnet in which the NAT gateway is located.</td></tr>
<tr><td><code>nat_gateway_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>connectivity_type</code></td><td><code>string</code></td><td>Indicates whether the NAT gateway supports public or private connectivity. The default is public connectivity.</td></tr>
<tr><td><code>private_ip_address</code></td><td><code>string</code></td><td>The private IPv4 address to assign to the NAT gateway. If you don't provide an address, a private IPv4 address will be automatically assigned.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the NAT gateway.</td></tr>
<tr><td><code>allocation_id</code></td><td><code>string</code></td><td>&#91;Public NAT gateway only&#93; The allocation ID of the Elastic IP address that's associated with the NAT gateway. This property is required for a public NAT gateway and cannot be specified with a private NAT gateway.</td></tr>
<tr><td><code>secondary_allocation_ids</code></td><td><code>array</code></td><td>Secondary EIP allocation IDs. For more information, see &#91;Create a NAT gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon VPC User Guide*.</td></tr>
<tr><td><code>secondary_private_ip_addresses</code></td><td><code>array</code></td><td>Secondary private IPv4 addresses. For more information about secondary addresses, see &#91;Create a NAT gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon Virtual Private Cloud User Guide*.&lt;br&#x2F;&gt; ``SecondaryPrivateIpAddressCount`` and ``SecondaryPrivateIpAddresses`` cannot be set at the same time.</td></tr>
<tr><td><code>secondary_private_ip_address_count</code></td><td><code>integer</code></td><td>&#91;Private NAT gateway only&#93; The number of secondary private IPv4 addresses you want to assign to the NAT gateway. For more information about secondary addresses, see &#91;Create a NAT gateway&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon Virtual Private Cloud User Guide*.&lt;br&#x2F;&gt; ``SecondaryPrivateIpAddressCount`` and ``SecondaryPrivateIpAddresses`` cannot be set at the same time.</td></tr>
<tr><td><code>max_drain_duration_seconds</code></td><td><code>integer</code></td><td>The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in progress. Default value is 350 seconds.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
subnet_id,
nat_gateway_id,
connectivity_type,
private_ip_address,
tags,
allocation_id,
secondary_allocation_ids,
secondary_private_ip_addresses,
secondary_private_ip_address_count,
max_drain_duration_seconds
FROM awscc.ec2.nat_gateway
WHERE data__Identifier = '<NatGatewayId>';
```

## Permissions

To operate on the <code>nat_gateway</code> resource, the following permissions are required:

### Delete
```json
ec2:DeleteNatGateway,
ec2:DescribeNatGateways
```

### Read
```json
ec2:DescribeNatGateways
```

### Update
```json
ec2:DescribeNatGateways,
ec2:CreateTags,
ec2:DeleteTags,
ec2:AssociateNatGatewayAddress,
ec2:DisassociateNatGatewayAddress,
ec2:AssignPrivateNatGatewayAddress,
ec2:UnassignPrivateNatGatewayAddress
```

