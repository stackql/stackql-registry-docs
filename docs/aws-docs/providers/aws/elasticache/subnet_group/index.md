---
title: subnet_group
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_group
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


Gets or updates an individual <code>subnet_group</code> resource, use <code>subnet_groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElastiCache::SubnetGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.subnet_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the cache subnet group.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The EC2 subnet IDs for the cache subnet group.</td></tr>
<tr><td><CopyableCode code="cache_subnet_group_name" /></td><td><code>string</code></td><td>The name for the cache subnet group. This value is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
description,
subnet_ids,
cache_subnet_group_name,
tags
FROM aws.elasticache.subnet_group
WHERE region = 'us-east-1' AND data__Identifier = '<CacheSubnetGroupName>';
```


## Permissions

To operate on the <code>subnet_group</code> resource, the following permissions are required:

### Read
```json
elasticache:DescribeCacheSubnetGroups,
elasticache:ListTagsForResource
```

### Update
```json
elasticache:ModifyCacheSubnetGroup,
elasticache:DescribeCacheSubnetGroups,
elasticache:AddTagsToResource,
elasticache:RemoveTagsFromResource
```

