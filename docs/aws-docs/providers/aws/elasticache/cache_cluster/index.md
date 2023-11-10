---
title: cache_cluster
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_cluster
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
Gets an individual <code>cache_cluster</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cache_cluster</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cache_cluster</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticache.cache_cluster</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cache_security_group_names</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>snapshot_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>port</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>configuration_endpoint_address</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>notification_topic_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>num_cache_nodes</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>snapshot_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transit_encryption_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>network_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_availability_zones</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>vpc_security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>cluster_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>redis_endpoint_address</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>redis_endpoint_port</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cache_subnet_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cache_parameter_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_minor_version_upgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>preferred_availability_zone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>snapshot_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>cache_node_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>snapshot_retention_limit</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>configuration_endpoint_port</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ip_discovery</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>log_delivery_configurations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>a_zmode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
cache_security_group_names,
snapshot_arns,
port,
configuration_endpoint_address,
notification_topic_arn,
num_cache_nodes,
snapshot_name,
transit_encryption_enabled,
network_type,
preferred_availability_zones,
vpc_security_group_ids,
cluster_name,
redis_endpoint_address,
engine,
tags,
engine_version,
redis_endpoint_port,
cache_subnet_group_name,
cache_parameter_group_name,
preferred_maintenance_window,
auto_minor_version_upgrade,
preferred_availability_zone,
snapshot_window,
cache_node_type,
snapshot_retention_limit,
configuration_endpoint_port,
ip_discovery,
log_delivery_configurations,
id,
a_zmode
FROM aws.elasticache.cache_cluster
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
