---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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
Gets an individual <code>user</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.user</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>first_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>message_action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>last_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>authentication_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
user_name,
first_name,
message_action,
last_name,
authentication_type
FROM aws.appstream.user
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
