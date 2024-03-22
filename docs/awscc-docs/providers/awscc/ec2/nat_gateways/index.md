---
title: nat_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - nat_gateways
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
Retrieves a list of <code>nat_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nat_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>nat_gateways</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.nat_gateways</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>nat_gateway_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
nat_gateway_id
FROM awscc.ec2.nat_gateways
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>nat_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateNatGateway,
ec2:DescribeNatGateways,
ec2:CreateTags
```

### List
```json
ec2:DescribeNatGateways
```

