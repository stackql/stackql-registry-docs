---
title: file_system
hide_title: false
hide_table_of_contents: false
keywords:
  - file_system
  - fsx
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>file_system</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_system</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>file_system</td></tr>
<tr><td><b>Id</b></td><td><code>aws.fsx.file_system</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>storage_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>storage_capacity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>root_volume_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>lustre_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>backup_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ontap_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>d_ns_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>subnet_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>security_group_ids</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>windows_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>file_system_type_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>open_zf_sconfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>resource_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>file_system_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>lustre_mount_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
storage_type,
kms_key_id,
storage_capacity,
root_volume_id,
lustre_configuration,
backup_id,
ontap_configuration,
d_ns_name,
subnet_ids,
security_group_ids,
windows_configuration,
file_system_type_version,
open_zf_sconfiguration,
resource_ar_n,
file_system_type,
id,
lustre_mount_name,
tags
FROM aws.fsx.file_system
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
