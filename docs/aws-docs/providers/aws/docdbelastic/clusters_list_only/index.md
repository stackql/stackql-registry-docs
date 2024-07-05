---
title: clusters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters_list_only
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

Lists <code>clusters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/clusters/"><code>clusters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::DocDBElastic::Cluster Amazon DocumentDB (with MongoDB compatibility) Elastic Scale resource describes a Cluster</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.docdbelastic.clusters_list_only" /></td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>clusters</code> in a region.
```sql
SELECT
region,
cluster_arn
FROM aws.docdbelastic.clusters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>clusters_list_only</code> resource, see <a href="/providers/aws/docdbelastic/clusters/#permissions"><code>clusters</code></a>


