---
title: scheduling_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduling_policies
  - batch
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>scheduling_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduling_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scheduling_policies</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.batch.scheduling_policies</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>scheduling_policies</code> resource, the following permissions are required:

### Create
```json
Batch:CreateSchedulingPolicy,
Batch:TagResource
```

### List
```json
Batch:ListSchedulingPolicies,
Batch:DescribeSchedulingPolicies
```


## Example
```sql
SELECT
region,
arn
FROM awscc.batch.scheduling_policies
WHERE region = 'us-east-1'
```
