---
title: subnet_route_table_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_route_table_associations
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

Creates, updates, deletes or gets a <code>subnet_route_table_association</code> resource or lists <code>subnet_route_table_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_route_table_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a subnet with a route table. The subnet and route table must be in the same VPC. This association causes traffic originating from the subnet to be routed according to the routes in the route table. A route table can be associated with multiple subnets. To create a route table, see &#91;AWS::EC2::RouteTable&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-routetable.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.subnet_route_table_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="route_table_id" /></td><td><code>string</code></td><td>The ID of the route table.<br/> The physical ID changes when the route table ID is changed.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The ID of the subnet.</td></tr>
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
    <td><CopyableCode code="RouteTableId, SubnetId, region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>subnet_route_table_associations</code> in a region.
```sql
SELECT
region,
id
FROM aws.ec2.subnet_route_table_associations
WHERE region = 'us-east-1';
```
Gets all properties from a <code>subnet_route_table_association</code>.
```sql
SELECT
region,
id,
route_table_id,
subnet_id
FROM aws.ec2.subnet_route_table_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subnet_route_table_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.subnet_route_table_associations (
 RouteTableId,
 SubnetId,
 region
)
SELECT 
'{{ RouteTableId }}',
 '{{ SubnetId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.subnet_route_table_associations (
 RouteTableId,
 SubnetId,
 region
)
SELECT 
 '{{ RouteTableId }}',
 '{{ SubnetId }}',
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
  - name: subnet_route_table_association
    props:
      - name: RouteTableId
        value: '{{ RouteTableId }}'
      - name: SubnetId
        value: '{{ SubnetId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.subnet_route_table_associations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subnet_route_table_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateRouteTable,
ec2:ReplaceRouteTableAssociation,
ec2:DescribeSubnets,
ec2:DescribeRouteTables
```

### Read
```json
ec2:DescribeRouteTables
```

### Delete
```json
ec2:DisassociateRouteTable,
ec2:DescribeSubnets,
ec2:DescribeRouteTables
```

### List
```json
ec2:DescribeRouteTables
```

