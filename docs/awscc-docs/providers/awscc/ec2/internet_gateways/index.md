---
title: internet_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - internet_gateways
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
Retrieves a list of <code>internet_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>internet_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>internet_gateways</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.internet_gateways</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>internet_gateway_id</code></td><td><code>string</code></td><td>ID of internet gateway.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
internet_gateway_id
FROM awscc.ec2.internet_gateways
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>internet_gateways</code> resource, the following permissions are required:

### Create
```json
ec2:CreateInternetGateway,
ec2:CreateTags,
ec2:DescribeInternetGateways
```

### List
```json
ec2:DescribeInternetGateways
```

