---
title: subnet_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_groups
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

Creates, updates, deletes or gets a <code>subnet_group</code> resource or lists <code>subnet_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElastiCache::SubnetGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.subnet_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the cache subnet group.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The EC2 subnet IDs for the cache subnet group.</td></tr>
<tr><td><CopyableCode code="cache_subnet_group_name" /></td><td><code>string</code></td><td>The name for the cache subnet group. This value is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-subnetgroup.html"><code>AWS::ElastiCache::SubnetGroup</code></a>.

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
    <td><CopyableCode code="Description, SubnetIds, region" /></td>
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
Gets all <code>subnet_groups</code> in a region.
```sql
SELECT
region,
description,
subnet_ids,
cache_subnet_group_name,
tags
FROM aws.elasticache.subnet_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>subnet_group</code>.
```sql
SELECT
region,
description,
subnet_ids,
cache_subnet_group_name,
tags
FROM aws.elasticache.subnet_groups
WHERE region = 'us-east-1' AND data__Identifier = '<CacheSubnetGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subnet_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticache.subnet_groups (
 Description,
 SubnetIds,
 region
)
SELECT 
'{{ Description }}',
 '{{ SubnetIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticache.subnet_groups (
 Description,
 SubnetIds,
 CacheSubnetGroupName,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ SubnetIds }}',
 '{{ CacheSubnetGroupName }}',
 '{{ Tags }}',
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
  - name: subnet_group
    props:
      - name: Description
        value: '{{ Description }}'
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: CacheSubnetGroupName
        value: '{{ CacheSubnetGroupName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticache.subnet_groups
WHERE data__Identifier = '<CacheSubnetGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>subnet_groups</code> resource, the following permissions are required:

### Create
```json
elasticache:CreateCacheSubnetGroup,
elasticache:AddTagsToResource,
elasticache:DescribeCacheSubnetGroups,
elasticache:ListTagsForResource
```

### Read
```json
elasticache:DescribeCacheSubnetGroups,
elasticache:ListTagsForResource
```

### Delete
```json
elasticache:DeleteCacheSubnetGroup,
elasticache:DescribeCacheSubnetGroups,
elasticache:ListTagsForResource
```

### List
```json
elasticache:DescribeCacheSubnetGroups
```

### Update
```json
elasticache:ModifyCacheSubnetGroup,
elasticache:DescribeCacheSubnetGroups,
elasticache:AddTagsToResource,
elasticache:RemoveTagsFromResource
```
