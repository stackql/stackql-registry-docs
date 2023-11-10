---
title: volume
hide_title: false
hide_table_of_contents: false
keywords:
  - volume
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
Gets an individual <code>volume</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>volume</td></tr>
<tr><td><b>Id</b></td><td><code>aws.fsx.volume</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>open_zf_sconfiguration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>resource_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>volume_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>volume_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>backup_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ontap_configuration</code></td><td><code>object</code></td><td></td></tr>
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
open_zf_sconfiguration,
resource_ar_n,
volume_id,
volume_type,
backup_id,
ontap_configuration,
u_ui_d,
tags,
name
FROM aws.fsx.volume
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;VolumeId&gt;'
```
