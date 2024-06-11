---
title: local_gateway_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_routes
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

Creates, updates, deletes or gets a <code>local_gateway_route</code> resource or lists <code>local_gateway_routes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes a route for a local gateway route table.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.local_gateway_routes" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="destination_cidr_block" /></td><td><code>string</code></td><td>The CIDR block used for destination matches.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_virtual_interface_group_id" /></td><td><code>string</code></td><td>The ID of the virtual interface group.</td></tr>
<tr><td><CopyableCode code="network_interface_id" /></td><td><code>string</code></td><td>The ID of the network interface.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the route.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The route type.</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>local_gateway_routes</code> in a region.
```sql
SELECT
region,
destination_cidr_block,
local_gateway_route_table_id
FROM aws.ec2.local_gateway_routes
WHERE region = 'us-east-1';
```
Gets all properties from a <code>local_gateway_route</code>.
```sql
SELECT
region,
destination_cidr_block,
local_gateway_route_table_id,
local_gateway_virtual_interface_group_id,
network_interface_id,
state,
type
FROM aws.ec2.local_gateway_routes
WHERE region = 'us-east-1' AND data__Identifier = '<DestinationCidrBlock>|<LocalGatewayRouteTableId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>local_gateway_route</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.local_gateway_routes (
 DestinationCidrBlock,
 LocalGatewayRouteTableId,
 LocalGatewayVirtualInterfaceGroupId,
 NetworkInterfaceId,
 region
)
SELECT 
'{{ DestinationCidrBlock }}',
 '{{ LocalGatewayRouteTableId }}',
 '{{ LocalGatewayVirtualInterfaceGroupId }}',
 '{{ NetworkInterfaceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.local_gateway_routes (
 DestinationCidrBlock,
 LocalGatewayRouteTableId,
 LocalGatewayVirtualInterfaceGroupId,
 NetworkInterfaceId,
 region
)
SELECT 
 '{{ DestinationCidrBlock }}',
 '{{ LocalGatewayRouteTableId }}',
 '{{ LocalGatewayVirtualInterfaceGroupId }}',
 '{{ NetworkInterfaceId }}',
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
  - name: local_gateway_route
    props:
      - name: DestinationCidrBlock
        value: '{{ DestinationCidrBlock }}'
      - name: LocalGatewayRouteTableId
        value: '{{ LocalGatewayRouteTableId }}'
      - name: LocalGatewayVirtualInterfaceGroupId
        value: '{{ LocalGatewayVirtualInterfaceGroupId }}'
      - name: NetworkInterfaceId
        value: '{{ NetworkInterfaceId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.local_gateway_routes
WHERE data__Identifier = '<DestinationCidrBlock|LocalGatewayRouteTableId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>local_gateway_routes</code> resource, the following permissions are required:

### Create
```json
ec2:CreateLocalGatewayRoute,
ec2:SearchLocalGatewayRoutes
```

### Read
```json
ec2:SearchLocalGatewayRoutes
```

### Delete
```json
ec2:DeleteLocalGatewayRoute,
ec2:SearchLocalGatewayRoutes
```

### List
```json
ec2:DescribeLocalGatewayRouteTables,
ec2:SearchLocalGatewayRoutes
```

### Update
```json
ec2:ModifyLocalGatewayRoute,
ec2:SearchLocalGatewayRoutes
```

