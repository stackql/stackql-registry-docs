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


Used to retrieve a list of <code>serverless_caches</code> in a region or to create or delete a <code>serverless_caches</code> resource, use <code>serverless_cach</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ElastiCache::ServerlessCache resource creates an Amazon ElastiCache Serverless Cache.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.serverless_caches" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="serverless_cache_name" /></td><td><code>string</code></td><td>The name of the Serverless Cache. This value must be unique.</td></tr>
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
    <td><CopyableCode code="ServerlessCacheName, Engine, region" /></td>
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
serverless_cache_name
FROM aws.elasticache.serverless_caches
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

