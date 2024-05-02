---
title: internet_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateway
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
Gets an individual <code>internet_gateway</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>internet_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Allocates an internet gateway for use with a VPC. After creating the Internet gateway, you then attach it to a VPC.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.internet_gateway</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>internet_gateway_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Any tags to assign to the internet gateway.</td></tr>
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
internet_gateway_id,
tags
FROM aws.ec2.internet_gateway
WHERE data__Identifier = '<InternetGatewayId>';
```

## Permissions

To operate on the <code>internet_gateway</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeInternetGateways
```

### Delete
```json
ec2:DeleteInternetGateway,
ec2:DescribeInternetGateways
```

### Update
```json
ec2:DeleteTags,
ec2:CreateTags,
ec2:DescribeInternetGateways
```

