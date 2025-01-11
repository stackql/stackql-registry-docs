---
title: local_gateway_route_table_virtual_interface_group_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - local_gateway_route_table_virtual_interface_group_associations
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

Creates, updates, deletes or gets a <code>local_gateway_route_table_virtual_interface_group_association</code> resource or lists <code>local_gateway_route_table_virtual_interface_group_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_gateway_route_table_virtual_interface_group_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Describes a local gateway route table virtual interface group association for a local gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.local_gateway_route_table_virtual_interface_group_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="local_gateway_route_table_virtual_interface_group_association_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="local_gateway_id" /></td><td><code>string</code></td><td>The ID of the local gateway.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_route_table_arn" /></td><td><code>string</code></td><td>The ARN of the local gateway route table.</td></tr>
<tr><td><CopyableCode code="local_gateway_virtual_interface_group_id" /></td><td><code>string</code></td><td>The ID of the local gateway route table virtual interface group.</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>The owner of the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the local gateway route table virtual interface group association.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-localgatewayroutetablevirtualinterfacegroupassociation.html"><code>AWS::EC2::LocalGatewayRouteTableVirtualInterfaceGroupAssociation</code></a>.

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
    <td><CopyableCode code="LocalGatewayRouteTableId, LocalGatewayVirtualInterfaceGroupId, region" /></td>
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
Gets all <code>local_gateway_route_table_virtual_interface_group_associations</code> in a region.
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
FROM aws.ec2.local_gateway_route_table_virtual_interface_group_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>local_gateway_route_table_virtual_interface_group_association</code>.
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
FROM aws.ec2.local_gateway_route_table_virtual_interface_group_associations
WHERE region = 'us-east-1' AND data__Identifier = '<LocalGatewayRouteTableVirtualInterfaceGroupAssociationId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>local_gateway_route_table_virtual_interface_group_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.local_gateway_route_table_virtual_interface_group_associations (
 LocalGatewayRouteTableId,
 LocalGatewayVirtualInterfaceGroupId,
 region
)
SELECT 
'{{ LocalGatewayRouteTableId }}',
 '{{ LocalGatewayVirtualInterfaceGroupId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.local_gateway_route_table_virtual_interface_group_associations (
 LocalGatewayRouteTableId,
 LocalGatewayVirtualInterfaceGroupId,
 Tags,
 region
)
SELECT 
 '{{ LocalGatewayRouteTableId }}',
 '{{ LocalGatewayVirtualInterfaceGroupId }}',
 '{{ Tags }}',
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
  - name: local_gateway_route_table_virtual_interface_group_association
    props:
      - name: LocalGatewayRouteTableId
        value: '{{ LocalGatewayRouteTableId }}'
      - name: LocalGatewayVirtualInterfaceGroupId
        value: '{{ LocalGatewayVirtualInterfaceGroupId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.local_gateway_route_table_virtual_interface_group_associations
WHERE data__Identifier = '<LocalGatewayRouteTableVirtualInterfaceGroupAssociationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>local_gateway_route_table_virtual_interface_group_associations</code> resource, the following permissions are required:

### Create
```json
ec2:CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation,
ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations,
ec2:CreateTags
```

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

### List
```json
ec2:DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations
```
