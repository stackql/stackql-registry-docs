---
title: customer_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateways
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
Retrieves a list of <code>customer_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>customer_gateways</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.customer_gateways</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>customer_gateway_id</code></td><td><code>string</code></td><td>CustomerGateway ID generated after customer gateway is created. Each customer gateway has a unique ID.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
customer_gateway_id
FROM awscc.ec2.customer_gateways
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>customer_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateCustomerGateway,
ec2:DescribeCustomerGateways
```

### List
```json
ec2:DescribeCustomerGateways
```

