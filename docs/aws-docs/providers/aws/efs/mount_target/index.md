---
title: mount_target
hide_title: false
hide_table_of_contents: false
keywords:
  - mount_target
  - efs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>mount_target</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mount_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>mount_target</td></tr>
<tr><td><b>Id</b></td><td><code>aws.efs.mount_target</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ip_address</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>file_system_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>security_groups</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>subnet_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
ip_address,
file_system_id,
security_groups,
subnet_id
FROM aws.efs.mount_target
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
