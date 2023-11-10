---
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
  - workspaces
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>workspace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workspace</td></tr>
<tr><td><b>Id</b></td><td><code>aws.workspaces.workspace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bundle_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>directory_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>root_volume_encryption_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_volume_encryption_enabled</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>volume_encryption_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>workspace_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
bundle_id,
directory_id,
root_volume_encryption_enabled,
tags,
user_name,
user_volume_encryption_enabled,
volume_encryption_key,
workspace_properties
FROM aws.workspaces.workspace
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
