---
title: subnet_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - subnet_group_tags
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

Expands all tag keys and values for <code>subnet_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElastiCache::SubnetGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.subnet_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description for the cache subnet group.</td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>The EC2 subnet IDs for the cache subnet group.</td></tr>
<tr><td><CopyableCode code="cache_subnet_group_name" /></td><td><code>string</code></td><td>The name for the cache subnet group. This value is stored as a lowercase string.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>subnet_groups</code> in a region.
```sql
SELECT
region,
description,
subnet_ids,
cache_subnet_group_name,
tag_key,
tag_value
FROM aws.elasticache.subnet_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>subnet_group_tags</code> resource, see <a href="/providers/aws/elasticache/subnet_groups/#permissions"><code>subnet_groups</code></a>

