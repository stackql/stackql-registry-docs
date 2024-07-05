---
title: cluster_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_tags
  - docdbelastic
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

Expands all tag keys and values for <code>clusters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::DocDBElastic::Cluster Amazon DocumentDB (with MongoDB compatibility) Elastic Scale resource describes a Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.docdbelastic.cluster_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="cluster_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cluster_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="admin_user_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="admin_user_password" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="shard_capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="shard_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_maintenance_window" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="preferred_backup_window" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="backup_retention_period" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="shard_instance_count" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>clusters</code> in a region.
```sql
SELECT
region,
cluster_name,
cluster_arn,
cluster_endpoint,
admin_user_name,
admin_user_password,
shard_capacity,
shard_count,
vpc_security_group_ids,
subnet_ids,
preferred_maintenance_window,
preferred_backup_window,
backup_retention_period,
shard_instance_count,
kms_key_id,
auth_type,
tag_key,
tag_value
FROM aws.docdbelastic.cluster_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>cluster_tags</code> resource, see <a href="/providers/aws/docdbelastic/clusters/#permissions"><code>clusters</code></a>


