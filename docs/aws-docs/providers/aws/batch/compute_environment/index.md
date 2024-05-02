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
Gets or operates on an individual <code>compute_environment</code> resource, use <code>compute_environments</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>compute_environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Batch::ComputeEnvironment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.batch.compute_environment</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.batch.compute_environment
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

