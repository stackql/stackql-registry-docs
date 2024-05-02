---
title: transit_gateway_route_table_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_route_table_associations
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
Used to retrieve a list of <code>transit_gateway_route_table_associations</code> in a region or create a <code>transit_gateway_route_table_associations</code> resource, use <code>transit_gateway_route_table_association</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_route_table_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGatewayRouteTableAssociation</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_route_table_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>transit_gateway_route_table_id</code></td><td><code>string</code></td><td>The ID of transit gateway route table.</td></tr>
<tr><td><code>transit_gateway_attachment_id</code></td><td><code>string</code></td><td>The ID of transit gateway attachment.</td></tr>
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
transit_gateway_route_table_id,
transit_gateway_attachment_id
FROM aws.ec2.transit_gateway_route_table_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>transit_gateway_route_table_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateTransitGatewayRouteTable,
ec2:GetTransitGatewayRouteTableAssociations
```

### List
```json
ec2:GetTransitGatewayRouteTableAssociations
```

