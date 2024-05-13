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
<tr><td><b>Description</b></td><td>Specifies a route in a route table. For more information, see &#91;Routes&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;vpc&#x2F;latest&#x2F;userguide&#x2F;VPC_Route_Tables.html#route-table-routes) in the *Amazon VPC User Guide*.&lt;br&#x2F;&gt; You must specify either a destination CIDR block or prefix list ID. You must also specify exactly one of the resources as the target.&lt;br&#x2F;&gt; If you create a route that references a transit gateway in the same template where you create the transit gateway, you must declare a dependency on the transit gateway attachment. The route table cannot use the transit gateway until it has successfully attached to the VPC. Add a &#91;DependsOn Attribute&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-attribute-dependson.html) in the <code>AWS::EC2::Route</code> resource to explicitly declare a dependency on the <code>AWS::EC2::TransitGatewayAttachment</code> resource.</td></tr>
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
    <td><CopyableCode code="RouteTableId, region" /></td>
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

## `DELETE` Example

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

### Delete
```json
ec2:DeleteRoute,
ec2:DescribeRouteTables
```

### List
```json
ec2:DescribeRouteTables
```

