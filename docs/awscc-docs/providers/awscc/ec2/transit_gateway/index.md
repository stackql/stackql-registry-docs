---
title: transit_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway
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
Gets an individual <code>transit_gateway</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transit_gateway</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.transit_gateway</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>association_default_route_table_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_accept_shared_attachments</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transit_gateway_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_route_table_propagation</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transit_gateway_cidr_blocks</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>propagation_default_route_table_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>default_route_table_association</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpn_ecmp_support</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dns_support</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>multicast_support</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>amazon_side_asn</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
association_default_route_table_id,
auto_accept_shared_attachments,
transit_gateway_arn,
default_route_table_propagation,
transit_gateway_cidr_blocks,
propagation_default_route_table_id,
default_route_table_association,
id,
vpn_ecmp_support,
dns_support,
multicast_support,
amazon_side_asn,
tags
FROM awscc.ec2.transit_gateway
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>transit_gateway</code> resource, the following permissions are required:

### Read
```json
ec2:CreateTransitGateway,
ec2:CreateTags,
ec2:DescribeTransitGateways,
ec2:DescribeTags,
ec2:DeleteTransitGateway,
ec2:DeleteTags,
ec2:ModifyTransitGateway,
ec2:ModifyTransitGatewayOptions
```

### Update
```json
ec2:CreateTransitGateway,
ec2:CreateTags,
ec2:DescribeTransitGateways,
ec2:DescribeTags,
ec2:DeleteTransitGateway,
ec2:DeleteTags,
ec2:ModifyTransitGateway,
ec2:ModifyTransitGatewayOptions
```

### Delete
```json
ec2:CreateTransitGateway,
ec2:CreateTags,
ec2:DescribeTransitGateways,
ec2:DescribeTags,
ec2:DeleteTransitGateway,
ec2:DeleteTags,
ec2:ModifyTransitGateway,
ec2:ModifyTransitGatewayOptions
```

