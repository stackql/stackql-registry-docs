---
title: parameter_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - parameter_groups
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

Creates, updates, deletes or gets a <code>parameter_group</code> resource or lists <code>parameter_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameter_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElastiCache::ParameterGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.parameter_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for this cache parameter group.</td></tr>
<tr><td><CopyableCode code="properties" /></td><td><code>object</code></td><td>A comma-delimited list of parameter name/value pairs. For more information see ModifyCacheParameterGroup in the Amazon ElastiCache API Reference Guide.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags are composed of a Key/Value pair. You can use tags to categorize and track each parameter group. The tag value null is permitted.</td></tr>
<tr><td><CopyableCode code="cache_parameter_group_name" /></td><td><code>string</code></td><td>The name of the Cache Parameter Group.</td></tr>
<tr><td><CopyableCode code="cache_parameter_group_family" /></td><td><code>string</code></td><td>The name of the cache parameter group family that this cache parameter group is compatible with.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-parametergroup.html"><code>AWS::ElastiCache::ParameterGroup</code></a>.

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
    <td><CopyableCode code="Description, CacheParameterGroupFamily, region" /></td>
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
Gets all <code>parameter_groups</code> in a region.
```sql
SELECT
region,
description,
properties,
tags,
cache_parameter_group_name,
cache_parameter_group_family
FROM aws.elasticache.parameter_groups
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>parameter_group</code>.
```sql
SELECT
region,
description,
properties,
tags,
cache_parameter_group_name,
cache_parameter_group_family
FROM aws.elasticache.parameter_groups
WHERE region = 'us-east-1' AND data__Identifier = '<CacheParameterGroupName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>parameter_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticache.parameter_groups (
 Description,
 CacheParameterGroupFamily,
 region
)
SELECT 
'{{ Description }}',
 '{{ CacheParameterGroupFamily }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticache.parameter_groups (
 Description,
 Properties,
 Tags,
 CacheParameterGroupFamily,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Properties }}',
 '{{ Tags }}',
 '{{ CacheParameterGroupFamily }}',
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
  - name: parameter_group
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Properties
        value: {}
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CacheParameterGroupFamily
        value: '{{ CacheParameterGroupFamily }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticache.parameter_groups
WHERE data__Identifier = '<CacheParameterGroupName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>parameter_groups</code> resource, the following permissions are required:

### Create
```json
ElastiCache:CreateCacheParameterGroup,
ElastiCache:DescribeCacheParameterGroups,
ElastiCache:AddTagsToResource,
ElastiCache:ModifyCacheParameterGroup,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy
```

### Read
```json
ElastiCache:DescribeCacheParameterGroups,
ElastiCache:DescribeCacheParameters,
ElastiCache:ListTagsForResource
```

### Update
```json
ElastiCache:ModifyCacheParameterGroup,
ElastiCache:DescribeCacheParameterGroups,
ElastiCache:DescribeCacheParameters,
ElastiCache:DescribeEngineDefaultParameters,
ElastiCache:AddTagsToResource,
ElastiCache:RemoveTagsFromResource
```

### Delete
```json
ElastiCache:DescribeCacheParameterGroups,
ElastiCache:DeleteCacheParameterGroup
```

### List
```json
ElastiCache:DescribeCacheParameterGroups
```
