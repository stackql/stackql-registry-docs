---
title: virtual_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_cluster
  - emrcontainers
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>virtual_cluster</code> resource, use <code>virtual_clusters</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema of AWS::EMRContainers::VirtualCluster Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.emrcontainers.virtual_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>container_provider</code></td><td><code>object</code></td><td>Container provider of the virtual cluster.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the virtual cluster.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of the virtual cluster.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this virtual cluster.</td></tr>
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
arn,
container_provider,
id,
name,
tags
FROM aws.emrcontainers.virtual_cluster
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>virtual_cluster</code> resource, the following permissions are required:

### Read
```json
emr-containers:DescribeVirtualCluster
```

### Delete
```json
emr-containers:DeleteVirtualCluster
```

### Update
```json
emr-containers:DescribeVirtualCluster,
emr-containers:ListTagsForResource,
emr-containers:TagResource,
emr-containers:UntagResource
```

