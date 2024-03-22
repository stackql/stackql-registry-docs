---
title: carrier_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - carrier_gateways
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
Retrieves a list of <code>carrier_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>carrier_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>carrier_gateways</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.carrier_gateways</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>carrier_gateway_id</code></td><td><code>string</code></td><td>The ID of the carrier gateway.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
carrier_gateway_id
FROM awscc.ec2.carrier_gateways
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>carrier_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateCarrierGateway,
ec2:DescribeCarrierGateways,
ec2:CreateTags
```

### List
```json
ec2:DescribeCarrierGateways
```

