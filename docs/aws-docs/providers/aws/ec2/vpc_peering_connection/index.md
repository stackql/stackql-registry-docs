---
title: vpc_peering_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_peering_connection
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
Gets an individual <code>vpc_peering_connection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_peering_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::VPCPeeringConnection</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_peering_connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>peer_owner_id</code></td><td><code>string</code></td><td>The AWS account ID of the owner of the accepter VPC.</td></tr>
<tr><td><code>peer_region</code></td><td><code>string</code></td><td>The Region code for the accepter VPC, if the accepter VPC is located in a Region other than the Region in which you make the request.</td></tr>
<tr><td><code>peer_role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the VPC peer role for the peering connection in another AWS account.</td></tr>
<tr><td><code>peer_vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC with which you are creating the VPC peering connection. You must specify this parameter in the request.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
peer_owner_id,
peer_region,
peer_role_arn,
peer_vpc_id,
vpc_id,
tags
FROM aws.ec2.vpc_peering_connection
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>vpc_peering_connection</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeVpcPeeringConnections
```

### Update
```json
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeVpcPeeringConnections
```

### Delete
```json
ec2:DeleteVpcPeeringConnection,
ec2:DescribeVpcPeeringConnections
```

