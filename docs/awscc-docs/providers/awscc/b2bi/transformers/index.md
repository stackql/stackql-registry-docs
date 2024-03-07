---
title: transformers
hide_title: false
hide_table_of_contents: false
keywords:
  - transformers
  - b2bi
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>transformers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transformers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transformers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.b2bi.transformers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>transformer_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>transformers</code> resource, the following permissions are required:

### Create
```json
b2bi:CreateTransformer,
b2bi:TagResource,
b2bi:UpdateTransformer,
logs:CreateLogDelivery,
logs:CreateLogGroup,
logs:CreateLogStream,
logs:DescribeLogGroups,
logs:DescribeLogStreams,
logs:DescribeResourcePolicies,
logs:ListLogDeliveries,
logs:PutLogEvents,
logs:PutResourcePolicy
```

### List
```json
b2bi:ListTransformers
```


## Example
```sql
SELECT
region,
transformer_id
FROM awscc.b2bi.transformers
WHERE region = 'us-east-1'
```
