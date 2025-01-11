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

Creates, updates, deletes or gets a <code>global_cluster</code> resource or lists <code>global_clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::RDS::GlobalCluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.global_clusters" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).<br />If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="engine_lifecycle_support" /></td><td><code>string</code></td><td>The life cycle type of the global cluster. You can use this setting to enroll your global cluster into Amazon RDS Extended Support.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="deletion_protection" /></td><td><code>boolean</code></td><td>The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.</td></tr>
<tr><td><CopyableCode code="global_cluster_identifier" /></td><td><code>string</code></td><td>The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="source_db_cluster_identifier" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="storage_encrypted" /></td><td><code>boolean</code></td><td>The storage encryption setting for the new global database cluster.<br />If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.</td></tr>
<tr><td><CopyableCode code="global_endpoint" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html"><code>AWS::RDS::GlobalCluster</code></a>.

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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>global_clusters</code> in a region.
```sql
SELECT
region,
engine,
tags,
engine_lifecycle_support,
engine_version,
deletion_protection,
global_cluster_identifier,
source_db_cluster_identifier,
storage_encrypted,
global_endpoint
FROM aws.rds.global_clusters
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>global_cluster</code>.
```sql
SELECT
region,
engine,
tags,
engine_lifecycle_support,
engine_version,
deletion_protection,
global_cluster_identifier,
source_db_cluster_identifier,
storage_encrypted,
global_endpoint
FROM aws.rds.global_clusters
WHERE region = 'us-east-1' AND data__Identifier = '<GlobalClusterIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>global_cluster</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.rds.global_clusters (
 Engine,
 Tags,
 EngineLifecycleSupport,
 EngineVersion,
 DeletionProtection,
 GlobalClusterIdentifier,
 SourceDBClusterIdentifier,
 StorageEncrypted,
 GlobalEndpoint,
 region
)
SELECT 
'{{ Engine }}',
 '{{ Tags }}',
 '{{ EngineLifecycleSupport }}',
 '{{ EngineVersion }}',
 '{{ DeletionProtection }}',
 '{{ GlobalClusterIdentifier }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ StorageEncrypted }}',
 '{{ GlobalEndpoint }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.global_clusters (
 Engine,
 Tags,
 EngineLifecycleSupport,
 EngineVersion,
 DeletionProtection,
 GlobalClusterIdentifier,
 SourceDBClusterIdentifier,
 StorageEncrypted,
 GlobalEndpoint,
 region
)
SELECT 
 '{{ Engine }}',
 '{{ Tags }}',
 '{{ EngineLifecycleSupport }}',
 '{{ EngineVersion }}',
 '{{ DeletionProtection }}',
 '{{ GlobalClusterIdentifier }}',
 '{{ SourceDBClusterIdentifier }}',
 '{{ StorageEncrypted }}',
 '{{ GlobalEndpoint }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: global_cluster
    props:
      - name: Engine
        value: '{{ Engine }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: EngineLifecycleSupport
        value: '{{ EngineLifecycleSupport }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: DeletionProtection
        value: '{{ DeletionProtection }}'
      - name: GlobalClusterIdentifier
        value: '{{ GlobalClusterIdentifier }}'
      - name: SourceDBClusterIdentifier
        value: '{{ SourceDBClusterIdentifier }}'
      - name: StorageEncrypted
        value: '{{ StorageEncrypted }}'
      - name: GlobalEndpoint
        value:
          Address: '{{ Address }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
rds:DescribeGlobalClusters
```

### Update
```json
rds:ModifyGlobalCluster,
rds:DescribeGlobalClusters,
rds:AddTagsToResource,
rds:RemoveTagsFromResource
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
