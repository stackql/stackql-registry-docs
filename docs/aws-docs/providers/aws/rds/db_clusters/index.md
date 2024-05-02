---
title: db_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - db_clusters
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
Retrieves a list of <code>db_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.db_clusters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>db_cluster_identifier</code></td><td><code>string</code></td><td>The DB cluster identifier. This parameter is stored as a lowercase string.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
db_cluster_identifier
FROM aws.rds.db_clusters
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>db_clusters</code> resource, the following permissions are required:

### Create
```json
iam:CreateServiceLinkedRole,
iam:PassRole,
rds:AddRoleToDBCluster,
rds:AddTagsToResource,
rds:CreateDBCluster,
rds:CreateDBInstance,
rds:DescribeDBClusters,
rds:DescribeEvents,
rds:EnableHttpEndpoint,
rds:ModifyDBCluster,
rds:RestoreDBClusterFromSnapshot,
rds:RestoreDBClusterToPointInTime,
secretsmanager:CreateSecret,
secretsmanager:TagResource
```

### List
```json
rds:DescribeDBClusters
```

