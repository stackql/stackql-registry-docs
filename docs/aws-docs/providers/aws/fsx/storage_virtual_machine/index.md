---
title: storage_virtual_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_virtual_machine
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
Gets an individual <code>storage_virtual_machine</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_virtual_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>storage_virtual_machine</td></tr>
<tr><td><b>Id</b></td><td><code>aws.fsx.storage_virtual_machine</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>resource_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>svm_admin_password</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>storage_virtual_machine_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>active_directory_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>root_volume_security_style</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>file_system_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>u_ui_d</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
resource_ar_n,
svm_admin_password,
storage_virtual_machine_id,
active_directory_configuration,
root_volume_security_style,
file_system_id,
u_ui_d,
tags,
name
FROM aws.fsx.storage_virtual_machine
WHERE region = 'us-east-1'
AND data__Identifier = '<StorageVirtualMachineId>'
```
