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
Retrieves a list of <code>subnet_route_table_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_route_table_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates a subnet with a route table. The subnet and route table must be in the same VPC. This association causes traffic originating from the subnet to be routed according to the routes in the route table. A route table can be associated with multiple subnets. To create a route table, see &#91;AWS::EC2::RouteTable&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-resource-ec2-routetable.html).</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.subnet_route_table_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.ec2.subnet_route_table_associations
WHERE region = 'us-east-1'
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

### List
```json
ec2:DescribeRouteTables
```

