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

Used to retrieve a list of <code>serverless_caches</code> in a region or create a <code>serverless_caches</code> resource, use <code>serverless_cach</code> to operate on an individual resource.

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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
WHERE region = 'us-east-1'
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

### List
```json
elasticache:DescribeServerlessCaches,
elasticache:ListTagsForResource
```
