---
title: local_gateway_route_table_virtual_interface_group_association
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_table_virtual_interface_group_association
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
Gets an individual <code>local_gateway_route_table_virtual_interface_group_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_table_virtual_interface_group_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>local_gateway_route_table_virtual_interface_group_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.local_gateway_route_table_virtual_interface_group_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>local_gateway_route_table_virtual_interface_group_association_id</code></td><td><code>string</code></td><td>The ID of the local gateway route table virtual interface group association.</td></tr>
<tr><td><code>local_gateway_id</code></td><td><code>string</code></td><td>The ID of the local gateway.</td></tr>
<tr><td><code>local_gateway_route_table_id</code></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><code>local_gateway_route_table_arn</code></td><td><code>string</code></td><td>The ARN of the local gateway route table.</td></tr>
<tr><td><code>local_gateway_virtual_interface_group_id</code></td><td><code>string</code></td><td>The ID of the local gateway route table virtual interface group.</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>The owner of the local gateway route table virtual interface group association.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the local gateway route table virtual interface group association.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the local gateway route table virtual interface group association.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
local_gateway_route_table_virtual_interface_group_association_id,
local_gateway_id,
local_gateway_route_table_id,
local_gateway_route_table_arn,
local_gateway_virtual_interface_group_id,
owner_id,
state,
tags
FROM awscc.ec2.local_gateway_route_table_virtual_interface_group_association
WHERE data__Identifier = '<LocalGatewayRouteTableVirtualInterfaceGroupAssociationId>';
```

## Permissions

To operate on the <code>local_gateway_route_table_virtual_interface_group_association</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations
```

### Update
```json
ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation,
ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations,
ec2:DeleteTags
```

