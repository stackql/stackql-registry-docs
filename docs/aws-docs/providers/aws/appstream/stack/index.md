---
title: stack
hide_title: false
hide_table_of_contents: false
keywords:
  - stack
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>stack</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>stack</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>stack</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.stack</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>storage_connectors</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>delete_storage_connectors</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>embed_host_domains</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>user_settings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>attributes_to_delete</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>redirect_ur_l</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>streaming_experience_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>feedback_ur_l</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>access_endpoints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
description,
storage_connectors,
delete_storage_connectors,
embed_host_domains,
user_settings,
attributes_to_delete,
redirect_ur_l,
streaming_experience_settings,
name,
feedback_ur_l,
application_settings,
display_name,
id,
tags,
access_endpoints
FROM aws.appstream.stack
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
