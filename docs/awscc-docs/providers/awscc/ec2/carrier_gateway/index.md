---
title: carrier_gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - carrier_gateway
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
Gets an individual <code>carrier_gateway</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>carrier_gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>carrier_gateway</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.carrier_gateway</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>carrier_gateway_id</code></td><td><code>string</code></td><td>The ID of the carrier gateway.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the carrier gateway.</td></tr>
<tr><td><code>vpc_id</code></td><td><code>string</code></td><td>The ID of the VPC.</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>The ID of the owner.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the carrier gateway.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
carrier_gateway_id,
state,
vpc_id,
owner_id,
tags
FROM awscc.ec2.carrier_gateway
WHERE data__Identifier = '<CarrierGatewayId>';
```

## Permissions

To operate on the <code>carrier_gateway</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeCarrierGateways
```

### Update
```json
ec2:DescribeCarrierGateways,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteCarrierGateway,
ec2:DescribeCarrierGateways
```

