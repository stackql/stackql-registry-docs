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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>transit_gateway</code> resource, use <code>transit_gateways</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EC2::TransitGateway</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="association_default_route_table_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_accept_shared_attachments" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="transit_gateway_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_route_table_propagation" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="transit_gateway_cidr_blocks" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="propagation_default_route_table_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_route_table_association" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="vpn_ecmp_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dns_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="multicast_support" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="amazon_side_asn" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.ec2.transit_gateway
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

