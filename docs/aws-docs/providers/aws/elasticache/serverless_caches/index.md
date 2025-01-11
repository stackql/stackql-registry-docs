---
title: serverless_caches
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_caches
  - elasticache
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

Creates, updates, deletes or gets a <code>serverless_cach</code> resource or lists <code>serverless_caches</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ElastiCache::ServerlessCache resource creates an Amazon ElastiCache Serverless Cache.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.serverless_caches" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="serverless_cache_name" /></td><td><code>string</code></td><td>The name of the Serverless Cache. This value must be unique.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The engine name of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="major_engine_version" /></td><td><code>string</code></td><td>The major engine version of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="full_engine_version" /></td><td><code>string</code></td><td>The full engine version of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="cache_usage_limits" /></td><td><code>object</code></td><td>The cache capacity limit of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The ID of the KMS key used to encrypt the cluster.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>One or more Amazon VPC security groups associated with this Serverless Cache.</td></tr>
<tr><td><CopyableCode code="snapshot_arns_to_restore" /></td><td><code>array</code></td><td>The ARN's of snapshot to restore Serverless Cache.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this Serverless Cache.</td></tr>
<tr><td><CopyableCode code="user_group_id" /></td><td><code>string</code></td><td>The ID of the user group.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The subnet id's of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="snapshot_retention_limit" /></td><td><code>integer</code></td><td>The snapshot retention limit of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="daily_snapshot_time" /></td><td><code>string</code></td><td>The daily time range (in UTC) during which the service takes automatic snapshot of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td>The creation time of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>object</code></td><td>The address and the port.</td></tr>
<tr><td><CopyableCode code="reader_endpoint" /></td><td><code>object</code></td><td>The address and the port.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Serverless Cache.</td></tr>
<tr><td><CopyableCode code="final_snapshot_name" /></td><td><code>string</code></td><td>The final snapshot name which is taken before Serverless Cache is deleted.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-serverlesscach.html"><code>AWS::ElastiCache::ServerlessCache</code></a>.

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
    <td><CopyableCode code="ServerlessCacheName, Engine, region" /></td>
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
Gets all <code>serverless_caches</code> in a region.
```sql
SELECT
region,
serverless_cache_name,
description,
engine,
major_engine_version,
full_engine_version,
cache_usage_limits,
kms_key_id,
security_group_ids,
snapshot_arns_to_restore,
tags,
user_group_id,
subnet_ids,
snapshot_retention_limit,
daily_snapshot_time,
create_time,
status,
endpoint,
reader_endpoint,
arn,
final_snapshot_name
FROM aws.elasticache.serverless_caches
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>serverless_cach</code>.
```sql
SELECT
region,
serverless_cache_name,
description,
engine,
major_engine_version,
full_engine_version,
cache_usage_limits,
kms_key_id,
security_group_ids,
snapshot_arns_to_restore,
tags,
user_group_id,
subnet_ids,
snapshot_retention_limit,
daily_snapshot_time,
create_time,
status,
endpoint,
reader_endpoint,
arn,
final_snapshot_name
FROM aws.elasticache.serverless_caches
WHERE region = 'us-east-1' AND data__Identifier = '<ServerlessCacheName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>serverless_cach</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticache.serverless_caches (
 ServerlessCacheName,
 Engine,
 region
)
SELECT 
'{{ ServerlessCacheName }}',
 '{{ Engine }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticache.serverless_caches (
 ServerlessCacheName,
 Description,
 Engine,
 MajorEngineVersion,
 CacheUsageLimits,
 KmsKeyId,
 SecurityGroupIds,
 SnapshotArnsToRestore,
 Tags,
 UserGroupId,
 SubnetIds,
 SnapshotRetentionLimit,
 DailySnapshotTime,
 Endpoint,
 ReaderEndpoint,
 FinalSnapshotName,
 region
)
SELECT 
 '{{ ServerlessCacheName }}',
 '{{ Description }}',
 '{{ Engine }}',
 '{{ MajorEngineVersion }}',
 '{{ CacheUsageLimits }}',
 '{{ KmsKeyId }}',
 '{{ SecurityGroupIds }}',
 '{{ SnapshotArnsToRestore }}',
 '{{ Tags }}',
 '{{ UserGroupId }}',
 '{{ SubnetIds }}',
 '{{ SnapshotRetentionLimit }}',
 '{{ DailySnapshotTime }}',
 '{{ Endpoint }}',
 '{{ ReaderEndpoint }}',
 '{{ FinalSnapshotName }}',
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
  - name: serverless_cach
    props:
      - name: ServerlessCacheName
        value: '{{ ServerlessCacheName }}'
      - name: Description
        value: '{{ Description }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: MajorEngineVersion
        value: '{{ MajorEngineVersion }}'
      - name: CacheUsageLimits
        value:
          DataStorage:
            Minimum: '{{ Minimum }}'
            Maximum: '{{ Maximum }}'
            Unit: '{{ Unit }}'
          ECPUPerSecond:
            Minimum: '{{ Minimum }}'
            Maximum: '{{ Maximum }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: SnapshotArnsToRestore
        value:
          - '{{ SnapshotArnsToRestore[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: UserGroupId
        value: '{{ UserGroupId }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: SnapshotRetentionLimit
        value: '{{ SnapshotRetentionLimit }}'
      - name: DailySnapshotTime
        value: '{{ DailySnapshotTime }}'
      - name: Endpoint
        value:
          Address: '{{ Address }}'
          Port: '{{ Port }}'
      - name: ReaderEndpoint
        value: null
      - name: FinalSnapshotName
        value: '{{ FinalSnapshotName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticache.serverless_caches
WHERE data__Identifier = '<ServerlessCacheName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>serverless_caches</code> resource, the following permissions are required:

### Create
```json
elasticache:CreateServerlessCache,
elasticache:DescribeServerlessCaches,
elasticache:AddTagsToResource,
elasticache:ListTagsForResource,
ec2:CreateTags,
ec2:CreateVpcEndpoint,
kms:CreateGrant,
kms:DescribeKey
```

### Read
```json
elasticache:DescribeServerlessCaches,
elasticache:ListTagsForResource
```

### Update
```json
elasticache:ModifyServerlessCache,
elasticache:DescribeServerlessCaches,
elasticache:AddTagsToResource,
elasticache:ListTagsForResource,
elasticache:RemoveTagsFromResource
```

### Delete
```json
elasticache:DeleteServerlessCache,
elasticache:DescribeServerlessCaches,
elasticache:ListTagsForResource
```

### List
```json
elasticache:DescribeServerlessCaches,
elasticache:ListTagsForResource
```
