---
title: global_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - global_cluster
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
Gets an individual <code>global_cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>global_cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.global_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td>The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).&lt;br&#x2F;&gt;If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td>The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><code>deletion_protection</code></td><td><code>boolean</code></td><td>The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.</td></tr>
<tr><td><code>global_cluster_identifier</code></td><td><code>string</code></td><td>The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.</td></tr>
<tr><td><code>source_db_cluster_identifier</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.</td></tr>
<tr><td><code>storage_encrypted</code></td><td><code>boolean</code></td><td> The storage encryption setting for the new global database cluster.&lt;br&#x2F;&gt;If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
engine,
engine_version,
deletion_protection,
global_cluster_identifier,
source_db_cluster_identifier,
storage_encrypted
FROM aws.rds.global_cluster
WHERE region = 'us-east-1'
AND data__Identifier = '<GlobalClusterIdentifier>'
```
