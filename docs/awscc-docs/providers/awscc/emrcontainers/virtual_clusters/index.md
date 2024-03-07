---
title: virtual_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_clusters
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
Retrieves a list of <code>virtual_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>virtual_clusters</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.emrcontainers.virtual_clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id of the virtual cluster.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>virtual_clusters</code> resource, the following permissions are required:

### Create
```json
emr-containers:CreateVirtualCluster,
emr-containers:TagResource,
iam:CreateServiceLinkedRole
```

### List
```json
emr-containers:ListVirtualClusters
```


## Example
```sql
SELECT
region,
id
FROM awscc.emrcontainers.virtual_clusters
WHERE region = 'us-east-1'
```
