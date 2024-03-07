---
title: compute_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_environments
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
Retrieves a list of <code>compute_environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>compute_environments</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.batch.compute_environments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>compute_environment_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>compute_environments</code> resource, the following permissions are required:

### Create
```json
Batch:CreateComputeEnvironment,
Batch:TagResource,
Batch:DescribeComputeEnvironments,
iam:CreateServiceLinkedRole,
Iam:PassRole,
Eks:DescribeCluster
```

### List
```json
Batch:DescribeComputeEnvironments
```


## Example
```sql
SELECT
region,
compute_environment_arn
FROM awscc.batch.compute_environments
WHERE region = 'us-east-1'
```
