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
Retrieves a list of <code>subnet_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subnet_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>subnet_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticache.subnet_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cache_subnet_group_name</code></td><td><code>string</code></td><td>The name for the cache subnet group. This value is stored as a lowercase string.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>subnet_groups</code> resource, the following permissions are required:

### Create
<pre>
elasticache:CreateCacheSubnetGroup,
elasticache:AddTagsToResource,
elasticache:DescribeCacheSubnetGroups,
elasticache:ListTagsForResource</pre>

### List
<pre>
elasticache:DescribeCacheSubnetGroups</pre>


## Example
```sql
SELECT
region,
cache_subnet_group_name
FROM awscc.elasticache.subnet_groups
WHERE region = 'us-east-1'
```
