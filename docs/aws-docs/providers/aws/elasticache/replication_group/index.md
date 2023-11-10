---
title: replication_group
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_group
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
Gets an individual <code>replication_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replication_group</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticache.replication_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>preferred_cache_cluster_azs</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>primary_end_point_port</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cache_security_group_names</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>reader_end_point_port</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>node_group_configuration</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>snapshot_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>configuration_end_point_port</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>read_end_point_ports_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>num_node_groups</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>notification_topic_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>snapshot_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>automatic_failover_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>replicas_per_node_group</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>replication_group_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>reader_end_point_address</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>multi_az_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>transit_encryption_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>network_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>replication_group_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>num_cache_clusters</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>primary_end_point_address</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>global_replication_group_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>configuration_end_point_address</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cache_subnet_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cache_parameter_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>primary_cluster_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>read_end_point_ports</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>at_rest_encryption_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>auto_minor_version_upgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>snapshot_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transit_encryption_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cache_node_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>snapshot_retention_limit</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>read_end_point_addresses_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>snapshotting_cluster_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ip_discovery</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auth_token</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_tiering_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>log_delivery_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>read_end_point_addresses</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
preferred_cache_cluster_azs,
primary_end_point_port,
cache_security_group_names,
reader_end_point_port,
node_group_configuration,
snapshot_arns,
configuration_end_point_port,
port,
read_end_point_ports_list,
num_node_groups,
notification_topic_arn,
snapshot_name,
automatic_failover_enabled,
replicas_per_node_group,
replication_group_description,
reader_end_point_address,
multi_az_enabled,
transit_encryption_enabled,
network_type,
replication_group_id,
engine,
tags,
num_cache_clusters,
primary_end_point_address,
global_replication_group_id,
configuration_end_point_address,
engine_version,
kms_key_id,
cache_subnet_group_name,
cache_parameter_group_name,
preferred_maintenance_window,
primary_cluster_id,
read_end_point_ports,
at_rest_encryption_enabled,
auto_minor_version_upgrade,
security_group_ids,
snapshot_window,
transit_encryption_mode,
cache_node_type,
snapshot_retention_limit,
read_end_point_addresses_list,
snapshotting_cluster_id,
user_group_ids,
ip_discovery,
auth_token,
data_tiering_enabled,
log_delivery_configurations,
read_end_point_addresses
FROM aws.elasticache.replication_group
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ReplicationGroupId&gt;'
```
