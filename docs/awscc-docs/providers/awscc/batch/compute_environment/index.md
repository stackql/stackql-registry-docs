---
title: compute_environment
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_environment
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
Gets an individual <code>compute_environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>compute_environment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.batch.compute_environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>compute_environment_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compute_environment_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compute_resources</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>replace_compute_environment</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>service_role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>update_policy</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>unmanagedv_cpus</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>eks_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
compute_environment_arn,
compute_environment_name,
compute_resources,
replace_compute_environment,
service_role,
state,
tags,
type,
update_policy,
unmanagedv_cpus,
eks_configuration
FROM awscc.batch.compute_environment
WHERE data__Identifier = '<ComputeEnvironmentArn>';
```

## Permissions

To operate on the <code>compute_environment</code> resource, the following permissions are required:

### Read
```json
Batch:DescribeComputeEnvironments
```

### Update
```json
Batch:UpdateComputeEnvironment,
Batch:DescribeComputeEnvironments,
Batch:TagResource,
Batch:UnTagResource,
Iam:PassRole,
Eks:DescribeCluster
```

### Delete
```json
Batch:DeleteComputeEnvironment,
Batch:DescribeComputeEnvironments,
Batch:UpdateComputeEnvironment,
Iam:PassRole,
Eks:DescribeCluster
```

