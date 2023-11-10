---
title: replication_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_instance
  - dms
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>replication_instance</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>replication_instance</td></tr>
<tr><td><b>Id</b></td><td><code>aws.dms.replication_instance</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>replication_instance_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>availability_zone</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preferred_maintenance_window</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>auto_minor_version_upgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>replication_subnet_group_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>replication_instance_private_ip_addresses</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>allocated_storage</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>resource_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>vpc_security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>allow_major_version_upgrade</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>replication_instance_class</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>publicly_accessible</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>multi_az</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>replication_instance_public_ip_addresses</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
replication_instance_identifier,
engine_version,
kms_key_id,
availability_zone,
preferred_maintenance_window,
auto_minor_version_upgrade,
replication_subnet_group_identifier,
replication_instance_private_ip_addresses,
allocated_storage,
resource_identifier,
vpc_security_group_ids,
allow_major_version_upgrade,
replication_instance_class,
publicly_accessible,
id,
multi_az,
replication_instance_public_ip_addresses,
tags
FROM aws.dms.replication_instance
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
