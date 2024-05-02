---
title: vpc_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_connection
  - msk
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>vpc_connection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::VpcConnection</td></tr>
<tr><td><b>Id</b></td><td><code>aws.msk.vpc_connection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authentication</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_subnets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>target_cluster_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the target cluster</td></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
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
arn,
authentication,
client_subnets,
target_cluster_arn,
security_groups,
tags,
vpc_id
FROM aws.msk.vpc_connection
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>vpc_connection</code> resource, the following permissions are required:

### Read
```json
kafka:DescribeVpcConnection,
kms:CreateGrant,
kms:DescribeKey
```

### Update
```json
kafka:DescribeVpcConnection,
kms:CreateGrant,
kms:DescribeKey,
kafka:TagResource,
kafka:UntagResource
```

### Delete
```json
ec2:DeleteVpcEndpoint,
ec2:DeleteVpcEndpoints,
ec2:DescribeVpcEndpoints,
ec2:DescribeVpcEndpointConnections,
kafka:DeleteVpcConnection,
kafka:DescribeVpcConnection,
kms:CreateGrant,
kms:DescribeKey
```

