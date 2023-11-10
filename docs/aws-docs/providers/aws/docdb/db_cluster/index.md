---
title: db_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - db_cluster
  - docdb
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>db_cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>db_cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.docdb.db_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>storage_encrypted</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>restore_to_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>snapshot_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>d_bcluster_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_backup_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cluster_resource_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>copy_tags_to_snapshot</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>restore_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>availability_zones</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>d_bsubnet_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>deletion_protection</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>use_latest_restorable_time</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>master_user_password</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_db_cluster_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>master_username</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>read_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>d_bcluster_parameter_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>backup_retention_period</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_cloudwatch_logs_exports</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
storage_encrypted,
restore_to_time,
snapshot_identifier,
port,
d_bcluster_identifier,
preferred_backup_window,
cluster_resource_id,
endpoint,
vpc_security_group_ids,
copy_tags_to_snapshot,
restore_type,
tags,
engine_version,
kms_key_id,
availability_zones,
preferred_maintenance_window,
d_bsubnet_group_name,
deletion_protection,
use_latest_restorable_time,
master_user_password,
source_db_cluster_identifier,
master_username,
read_endpoint,
d_bcluster_parameter_group_name,
backup_retention_period,
id,
enable_cloudwatch_logs_exports
FROM aws.docdb.db_cluster
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
