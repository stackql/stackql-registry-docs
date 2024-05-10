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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>global_clusters</code> in a region or to create or delete a <code>global_clusters</code> resource, use <code>global_cluster</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RDS::GlobalCluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.global_clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="global_cluster_identifier" /></td><td><code>string</code></td><td>The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
global_cluster_identifier
FROM aws.rds.global_clusters
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "Engine": "{{ Engine }}",
 "EngineVersion": "{{ EngineVersion }}",
 "DeletionProtection": "{{ DeletionProtection }}",
 "GlobalClusterIdentifier": "{{ GlobalClusterIdentifier }}",
 "SourceDBClusterIdentifier": "{{ SourceDBClusterIdentifier }}",
 "StorageEncrypted": "{{ StorageEncrypted }}"
}
>>>
--required properties only
INSERT INTO aws.rds.global_clusters (
 Engine,
 EngineVersion,
 DeletionProtection,
 GlobalClusterIdentifier,
 SourceDBClusterIdentifier,
 StorageEncrypted,
 region
)
SELECT 
{{ .Engine }},
 {{ .EngineVersion }},
 {{ .DeletionProtection }},
 {{ .GlobalClusterIdentifier }},
 {{ .SourceDBClusterIdentifier }},
 {{ .StorageEncrypted }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Engine": "{{ Engine }}",
 "EngineVersion": "{{ EngineVersion }}",
 "DeletionProtection": "{{ DeletionProtection }}",
 "GlobalClusterIdentifier": "{{ GlobalClusterIdentifier }}",
 "SourceDBClusterIdentifier": "{{ SourceDBClusterIdentifier }}",
 "StorageEncrypted": "{{ StorageEncrypted }}"
}
>>>
--all properties
INSERT INTO aws.rds.global_clusters (
 Engine,
 EngineVersion,
 DeletionProtection,
 GlobalClusterIdentifier,
 SourceDBClusterIdentifier,
 StorageEncrypted,
 region
)
SELECT 
 {{ .Engine }},
 {{ .EngineVersion }},
 {{ .DeletionProtection }},
 {{ .GlobalClusterIdentifier }},
 {{ .SourceDBClusterIdentifier }},
 {{ .StorageEncrypted }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rds.global_clusters
WHERE data__Identifier = '<GlobalClusterIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>global_clusters</code> resource, the following permissions are required:

### Create
```json
rds:CreateGlobalCluster,
rds:DescribeDBClusters,
rds:DescribeGlobalClusters
```

### Delete
```json
rds:DescribeGlobalClusters,
rds:DeleteGlobalCluster,
rds:RemoveFromGlobalCluster,
rds:DescribeDBClusters
```

### List
```json
rds:DescribeGlobalClusters
```

