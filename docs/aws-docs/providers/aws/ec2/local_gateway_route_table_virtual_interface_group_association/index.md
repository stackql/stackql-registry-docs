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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>local_gateway_route_table_virtual_interface_group_association</code> resource, use <code>local_gateway_route_table_virtual_interface_group_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_table_virtual_interface_group_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes a local gateway route table virtual interface group association for a local gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.local_gateway_route_table_virtual_interface_group_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="local_gateway_route_table_virtual_interface_group_association_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="local_gateway_id" /></td><td><code>string</code></td><td>The ID of the local gateway.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_arn" /></td><td><code>string</code></td><td>The ARN of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_virtual_interface_group_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table virtual interface group.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>The owner of the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the local gateway route table virtual interface group association.</td></tr>
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
local_gateway_route_table_virtual_interface_group_association_id,
local_gateway_id,
local_gateway_route_table_id,
local_gateway_route_table_arn,
local_gateway_virtual_interface_group_id,
owner_id,
state,
tags
FROM aws.ec2.local_gateway_route_table_virtual_interface_group_association
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

