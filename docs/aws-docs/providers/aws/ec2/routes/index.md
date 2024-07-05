---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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

Creates, updates, deletes or gets a <code>route</code> resource or lists <code>routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a route in a route table. For more information, see &#91;Routes&#93;(https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-table-routes) in the *Amazon VPC User Guide*.<br />You must specify either a destination CIDR block or prefix list ID. You must also specify exactly one of the resources as the target.<br />If you create a route that references a transit gateway in the same template where you create the transit gateway, you must declare a dependency on the transit gateway attachment. The route table cannot use the transit gateway until it has successfully attached to the VPC. Add a &#91;DependsOn Attribute&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html) in the <code>AWS::EC2::Route</code> resource to explicitly declare a dependency on the <code>AWS::EC2::TransitGatewayAttachment</code> resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.routes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="carrier_gateway_id" /></td><td><code>string</code></td><td>The ID of the carrier gateway.<br />You can only use this option when the VPC contains a subnet which is associated with a Wavelength Zone.</td></tr>
<tr><td><CopyableCode code="cidr_block" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="core_network_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the core network.</td></tr>
<tr><td><CopyableCode code="destination_cidr_block" /></td><td><code>string</code></td><td>The IPv4 CIDR address block used for the destination match. Routing decisions are based on the most specific match. We modify the specified CIDR block to its canonical form; for example, if you specify <code>100.68.0.18/18</code>, we modify it to <code>100.68.0.0/18</code>.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="RouteTableId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>routes</code> in a region.
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
FROM aws.ec2.routes
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>route</code>.
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
FROM aws.ec2.routes
WHERE region = 'us-east-1' AND data__Identifier = '<RouteTableId>|<CidrBlock>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>route</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.ec2.routes (
 RouteTableId,
 region
)
SELECT 
'{{ RouteTableId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.routes (
 CarrierGatewayId,
 CoreNetworkArn,
 DestinationCidrBlock,
 DestinationIpv6CidrBlock,
 DestinationPrefixListId,
 EgressOnlyInternetGatewayId,
 GatewayId,
 InstanceId,
 LocalGatewayId,
 NatGatewayId,
 NetworkInterfaceId,
 RouteTableId,
 TransitGatewayId,
 VpcEndpointId,
 VpcPeeringConnectionId,
 region
)
SELECT 
 '{{ CarrierGatewayId }}',
 '{{ CoreNetworkArn }}',
 '{{ DestinationCidrBlock }}',
 '{{ DestinationIpv6CidrBlock }}',
 '{{ DestinationPrefixListId }}',
 '{{ EgressOnlyInternetGatewayId }}',
 '{{ GatewayId }}',
 '{{ InstanceId }}',
 '{{ LocalGatewayId }}',
 '{{ NatGatewayId }}',
 '{{ NetworkInterfaceId }}',
 '{{ RouteTableId }}',
 '{{ TransitGatewayId }}',
 '{{ VpcEndpointId }}',
 '{{ VpcPeeringConnectionId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: route
    props:
      - name: CarrierGatewayId
        value: '{{ CarrierGatewayId }}'
      - name: CoreNetworkArn
        value: '{{ CoreNetworkArn }}'
      - name: DestinationCidrBlock
        value: '{{ DestinationCidrBlock }}'
      - name: DestinationIpv6CidrBlock
        value: '{{ DestinationIpv6CidrBlock }}'
      - name: DestinationPrefixListId
        value: '{{ DestinationPrefixListId }}'
      - name: EgressOnlyInternetGatewayId
        value: '{{ EgressOnlyInternetGatewayId }}'
      - name: GatewayId
        value: '{{ GatewayId }}'
      - name: InstanceId
        value: '{{ InstanceId }}'
      - name: LocalGatewayId
        value: '{{ LocalGatewayId }}'
      - name: NatGatewayId
        value: '{{ NatGatewayId }}'
      - name: NetworkInterfaceId
        value: '{{ NetworkInterfaceId }}'
      - name: RouteTableId
        value: '{{ RouteTableId }}'
      - name: TransitGatewayId
        value: '{{ TransitGatewayId }}'
      - name: VpcEndpointId
        value: '{{ VpcEndpointId }}'
      - name: VpcPeeringConnectionId
        value: '{{ VpcPeeringConnectionId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.routes
WHERE data__Identifier = '<RouteTableId|CidrBlock>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>routes</code> resource, the following permissions are required:

### Create
```json
ec2:CreateRoute,
ec2:DescribeRouteTables,
ec2:DescribeNetworkInterfaces
```

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

### List
```json
ec2:DescribeRouteTables
```

