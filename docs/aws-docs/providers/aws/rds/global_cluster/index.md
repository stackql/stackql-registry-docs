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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>global_cluster</code> resource, use <code>global_clusters</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RDS::GlobalCluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.global_cluster" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).&lt;br&#x2F;&gt;If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="deletion_protection" /></td><td><code>boolean</code></td><td>The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.</td></tr>
<tr><td><CopyableCode code="global_cluster_identifier" /></td><td><code>string</code></td><td>The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="source_db_cluster_identifier" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="storage_encrypted" /></td><td><code>boolean</code></td><td> The storage encryption setting for the new global database cluster.&lt;br&#x2F;&gt;If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalClusterIdentifier>';
```


## Permissions

To operate on the <code>global_cluster</code> resource, the following permissions are required:

### Read
```json
rds:DescribeGlobalClusters
```

### Update
```json
rds:ModifyGlobalCluster,
rds:DescribeGlobalClusters
```

