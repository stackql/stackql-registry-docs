---
title: vpc_gateway_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_gateway_attachment
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
Gets an individual <code>vpc_gateway_attachment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_gateway_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>vpc_gateway_attachment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.vpc_gateway_attachment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>attachment_type</code></td><td><code>string</code></td><td>Used to identify if this resource is an Internet Gateway or Vpn Gateway Attachment </td></tr>
<tr><td><code>internet_gateway_id</code></td><td><code>string</code></td><td>The ID of the internet gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><code>vpn_gateway_id</code></td><td><code>string</code></td><td>The ID of the virtual private gateway. You must specify either InternetGatewayId or VpnGatewayId, but not both.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
attachment_type,
internet_gateway_id,
vpc_id,
vpn_gateway_id
FROM awscc.ec2.vpc_gateway_attachment
WHERE data__Identifier = '<AttachmentType>|<VpcId>';
```

## Permissions

To operate on the <code>vpc_gateway_attachment</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeInternetGateways,
ec2:DescribeVpnGateways
```

### Update
```json
ec2:AttachInternetGateway,
ec2:AttachVpnGateway,
ec2:DetachInternetGateway,
ec2:DetachVpnGateway,
ec2:DescribeInternetGateways,
ec2:DescribeVpnGateways
```

### Delete
```json
ec2:DetachInternetGateway,
ec2:DetachVpnGateway,
ec2:DescribeInternetGateways,
ec2:DescribeVpnGateways
```

