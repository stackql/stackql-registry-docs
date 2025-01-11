---
title: gateway_route_table_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway_route_table_associations
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

Creates, updates, deletes or gets a <code>gateway_route_table_association</code> resource or lists <code>gateway_route_table_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateway_route_table_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a gateway with a route table. The gateway and route table must be in the same VPC. This association causes the incoming traffic to the gateway to be routed according to the routes in the route table.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.gateway_route_table_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="route_table_id" /></td><td><code>string</code></td><td>The ID of the route table.</td></tr>
<tr><td><CopyableCode code="gateway_id" /></td><td><code>string</code></td><td>The ID of the gateway.</td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td>The route table association ID.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-gatewayroutetableassociation.html"><code>AWS::EC2::GatewayRouteTableAssociation</code></a>.

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
    <td><CopyableCode code="RouteTableId, GatewayId, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>gateway_route_table_association</code>.
```sql
SELECT
region,
route_table_id,
gateway_id,
association_id
FROM aws.ec2.gateway_route_table_associations
WHERE region = 'us-east-1' AND data__Identifier = '<GatewayId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateway_route_table_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.gateway_route_table_associations (
 RouteTableId,
 GatewayId,
 region
)
SELECT 
'{{ RouteTableId }}',
 '{{ GatewayId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.gateway_route_table_associations (
 RouteTableId,
 GatewayId,
 region
)
SELECT 
 '{{ RouteTableId }}',
 '{{ GatewayId }}',
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
  - name: gateway_route_table_association
    props:
      - name: RouteTableId
        value: '{{ RouteTableId }}'
      - name: GatewayId
        value: '{{ GatewayId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.gateway_route_table_associations
WHERE data__Identifier = '<GatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>gateway_route_table_associations</code> resource, the following permissions are required:

### Create
```json
ec2:DescribeRouteTables,
ec2:AssociateRouteTable
```

### Read
```json
ec2:DescribeRouteTables
```

### Update
```json
ec2:DescribeRouteTables,
ec2:ReplaceRouteTableAssociation
```

### Delete
```json
ec2:DescribeRouteTables,
ec2:DisassociateRouteTable
```
