---
title: scheduling_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduling_policy
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
Gets an individual <code>scheduling_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduling_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>scheduling_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.batch.scheduling_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of Scheduling Policy.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>fairshare_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>scheduling_policy</code> resource, the following permissions are required:

### Read
```json
Batch:DescribeSchedulingPolicies
```

### Update
```json
Batch:UpdateSchedulingPolicy,
Batch:TagResource,
Batch:UnTagResource
```

### Delete
```json
Batch:DescribeSchedulingPolicies,
Batch:DeleteSchedulingPolicy
```


## Example
```sql
SELECT
region,
name,
arn,
fairshare_policy,
tags
FROM awscc.batch.scheduling_policy
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
