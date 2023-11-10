---
title: broker
hide_title: false
hide_table_of_contents: false
keywords:
  - broker
  - amazonmq
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>broker</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>broker</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>broker</td></tr>
<tr><td><b>Id</b></td><td><code>aws.amazonmq.broker</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>authentication_strategy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>users</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>stomp_endpoints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>mqtt_endpoints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>amqp_endpoints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>deployment_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>encryption_options</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>configuration_revision</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>storage_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>maintenance_window_start_time</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>host_instance_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_minor_version_upgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>logs</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>configuration_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>broker_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>wss_endpoints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ip_addresses</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>open_wire_endpoints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ldap_server_metadata</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>publicly_accessible</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
security_groups,
configuration,
authentication_strategy,
users,
subnet_ids,
stomp_endpoints,
mqtt_endpoints,
amqp_endpoints,
deployment_mode,
engine_type,
encryption_options,
tags,
configuration_revision,
storage_type,
engine_version,
maintenance_window_start_time,
host_instance_type,
auto_minor_version_upgrade,
logs,
configuration_id,
broker_name,
wss_endpoints,
ip_addresses,
open_wire_endpoints,
ldap_server_metadata,
publicly_accessible,
id,
arn
FROM aws.amazonmq.broker
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
