---
title: transit_gateway_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_attachment
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
Gets an individual <code>transit_gateway_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGatewayAttachment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transit_gateway_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>options</code></td><td><code>object</code></td><td>The options for the transit gateway vpc attachment.</td></tr>
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
transit_gateway_id,
vpc_id,
subnet_ids,
tags,
options
FROM aws.ec2.transit_gateway_attachment
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>transit_gateway_attachment</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeTags,
ec2:DescribeTransitGatewayAttachments,
ec2:ModifyTransitGatewayVpcAttachment
```

### Delete
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeTags,
ec2:DescribeTransitGatewayAttachments,
ec2:ModifyTransitGatewayVpcAttachment
```

### Update
```json
ec2:DescribeTransitGatewayAttachments,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:DescribeTags,
ec2:CreateTransitGatewayVpcAttachment,
ec2:CreateTags,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:DeleteTags,
ec2:ModifyTransitGatewayVpcAttachment
```

