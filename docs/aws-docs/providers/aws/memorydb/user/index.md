---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - memorydb
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
<tr><td><b>Id</b></td><td><code>aws.memorydb.user</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>Indicates the user status. Can be "active", "modifying" or "deleting".</td></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td>The name of the user.</td></tr>
<tr><td><code>access_string</code></td><td><code>string</code></td><td>Access permissions string used for this user account.</td></tr>
<tr><td><code>authentication_mode</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the user account.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this user.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
status,
user_name,
access_string,
authentication_mode,
arn,
tags
FROM aws.memorydb.user
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;UserName&gt;'
```
