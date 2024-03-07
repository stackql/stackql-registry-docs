---
title: global_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - global_clusters
  - rds
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>global_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>global_clusters</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.global_clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>global_cluster_identifier</code></td><td><code>string</code></td><td>The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
global_cluster_identifier
FROM awscc.rds.global_clusters
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>global_clusters</code> resource, the following permissions are required:

### Create
```json
rds:CreateGlobalCluster,
rds:DescribeDBClusters,
rds:DescribeGlobalClusters
```

### List
```json
rds:DescribeGlobalClusters
```

