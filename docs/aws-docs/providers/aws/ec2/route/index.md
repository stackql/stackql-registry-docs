---
title: route
hide_title: false
hide_table_of_contents: false
keywords:
  - route
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

Gets or operates on an individual <code>route</code> resource, use <code>routes</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a route in a route table. For more information, see &#91;Routes&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;VPC_Route_Tables.html#route-table-routes) in the *Amazon VPC User Guide*.&lt;br&#x2F;&gt; You must specify either a destination CIDR block or prefix list ID. You must also specify exactly one of the resources as the target.&lt;br&#x2F;&gt; If you create a route that references a transit gateway in the same template where you create the transit gateway, you must declare a dependency on the transit gateway attachment. The route table cannot use the transit gateway until it has successfully attached to the VPC. Add a &#91;DependsOn Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-dependson.html) in the ``AWS::EC2::Route`` resource to explicitly declare a dependency on the ``AWS::EC2::TransitGatewayAttachment`` resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.route" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="carrier_gateway_id" /></td><td><code>string</code></td><td>The ID of the carrier gateway.&lt;br&#x2F;&gt; You can only use this option when the VPC contains a subnet which is associated with a Wavelength Zone.</td></tr>
<tr><td><CopyableCode code="cidr_block" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the core network.</td></tr>
<tr><td><CopyableCode code="destination_cidr_block" /></td><td><code>string</code></td><td>The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18&#x2F;18``, we modify it to ``100.68.0.0&#x2F;18``.</td></tr>
<tr><td><CopyableCode code="destination_ipv6_cidr_block" /></td><td><code>string</code></td><td>The IPv6 CIDR block used for the destination match. Routing decisions are based on the most specific match.</td></tr>
<tr><td><CopyableCode code="destination_prefix_list_id" /></td><td><code>string</code></td><td>The ID of a prefix list used for the destination match.</td></tr>
<tr><td><CopyableCode code="egress_only_internet_gateway_id" /></td><td><code>string</code></td><td>&#91;IPv6 traffic only&#93; The ID of an egress-only internet gateway.</td></tr>
<tr><td><CopyableCode code="gateway_id" /></td><td><code>string</code></td><td>The ID of an internet gateway or virtual private gateway attached to your VPC.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of a NAT instance in your VPC. The operation fails if you specify an instance ID unless exactly one network interface is attached.</td></tr>
<tr><td><CopyableCode code="local_gateway_id" /></td><td><code>string</code></td><td>The ID of the local gateway.</td></tr>
<tr><td><CopyableCode code="nat_gateway_id" /></td><td><code>string</code></td><td>&#91;IPv4 traffic only&#93; The ID of a NAT gateway.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of a network interface.</td></tr>
<tr><td><CopyableCode code="route_table_id" /></td><td><code>string</code></td><td>The ID of the route table for the route.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of a transit gateway.</td></tr>
<tr><td><CopyableCode code="vpc_endpoint_id" /></td><td><code>string</code></td><td>The ID of a VPC endpoint. Supported for Gateway Load Balancer endpoints only.</td></tr>
<tr><td><CopyableCode code="vpc_peering_connection_id" /></td><td><code>string</code></td><td>The ID of a VPC peering connection.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
carrier_gateway_id,
cidr_block,
core_network_arn,
destination_cidr_block,
destination_ipv6_cidr_block,
destination_prefix_list_id,
egress_only_internet_gateway_id,
gateway_id,
instance_id,
local_gateway_id,
nat_gateway_id,
network_interface_id,
route_table_id,
transit_gateway_id,
vpc_endpoint_id,
vpc_peering_connection_id
FROM aws.ec2.route
WHERE data__Identifier = '<RouteTableId>|<CidrBlock>';
```

## Permissions

To operate on the <code>route</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeRouteTables
```

### Update
```json
ec2:ReplaceRoute,
ec2:DescribeRouteTables,
ec2:DescribeNetworkInterfaces
```

### Delete
```json
ec2:DeleteRoute,
ec2:DescribeRouteTables
```

