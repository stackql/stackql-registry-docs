---
title: serverless_cache_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_cache_tags
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

Expands all tag keys and values for <code>serverless_caches</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serverless_cache_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ElastiCache::ServerlessCache resource creates an Amazon ElastiCache Serverless Cache.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticache.serverless_cache_tags" /></td></tr>
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
Expands tags for all <code>serverless_caches</code> in a region.
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
user_group_id,
subnet_ids,
snapshot_retention_limit,
daily_snapshot_time,
create_time,
status,
endpoint,
reader_endpoint,
arn,
final_snapshot_name,
tag_key,
tag_value
FROM aws.elasticache.serverless_cache_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>serverless_cache_tags</code> resource, see <a href="/providers/aws/elasticache/serverless_caches/#permissions"><code>serverless_caches</code></a>

