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


Used to retrieve a list of <code>routes</code> in a region or to create or delete a <code>routes</code> resource, use <code>route</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a route in a route table. For more information, see &#91;Routes&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;VPC_Route_Tables.html#route-table-routes) in the *Amazon VPC User Guide*.&lt;br&#x2F;&gt; You must specify either a destination CIDR block or prefix list ID. You must also specify exactly one of the resources as the target.&lt;br&#x2F;&gt; If you create a route that references a transit gateway in the same template where you create the transit gateway, you must declare a dependency on the transit gateway attachment. The route table cannot use the transit gateway until it has successfully attached to the VPC. Add a &#91;DependsOn Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-dependson.html) in the ``AWS::EC2::Route`` resource to explicitly declare a dependency on the ``AWS::EC2::TransitGatewayAttachment`` resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.routes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="route_table_id" /></td><td><code>string</code></td><td>The ID of the route table for the route.</td></tr>
<tr><td><CopyableCode code="cidr_block" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
route_table_id,
cidr_block
FROM aws.ec2.routes
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "RouteTableId": "{{ RouteTableId }}"
}
>>>
--required properties only
INSERT INTO aws.ec2.routes (
 RouteTableId,
 region
)
SELECT 
{{ .RouteTableId }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "CarrierGatewayId": "{{ CarrierGatewayId }}",
 "CoreNetworkArn": "{{ CoreNetworkArn }}",
 "DestinationCidrBlock": "{{ DestinationCidrBlock }}",
 "DestinationIpv6CidrBlock": "{{ DestinationIpv6CidrBlock }}",
 "DestinationPrefixListId": "{{ DestinationPrefixListId }}",
 "EgressOnlyInternetGatewayId": "{{ EgressOnlyInternetGatewayId }}",
 "GatewayId": "{{ GatewayId }}",
 "InstanceId": "{{ InstanceId }}",
 "LocalGatewayId": "{{ LocalGatewayId }}",
 "NatGatewayId": "{{ NatGatewayId }}",
 "NetworkInterfaceId": "{{ NetworkInterfaceId }}",
 "RouteTableId": "{{ RouteTableId }}",
 "TransitGatewayId": "{{ TransitGatewayId }}",
 "VpcEndpointId": "{{ VpcEndpointId }}",
 "VpcPeeringConnectionId": "{{ VpcPeeringConnectionId }}"
}
>>>
--all properties
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
 {{ .CarrierGatewayId }},
 {{ .CoreNetworkArn }},
 {{ .DestinationCidrBlock }},
 {{ .DestinationIpv6CidrBlock }},
 {{ .DestinationPrefixListId }},
 {{ .EgressOnlyInternetGatewayId }},
 {{ .GatewayId }},
 {{ .InstanceId }},
 {{ .LocalGatewayId }},
 {{ .NatGatewayId }},
 {{ .NetworkInterfaceId }},
 {{ .RouteTableId }},
 {{ .TransitGatewayId }},
 {{ .VpcEndpointId }},
 {{ .VpcPeeringConnectionId }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
ec2:DeleteRoute,
ec2:DescribeRouteTables
```

### List
```json
ec2:DescribeRouteTables
```

