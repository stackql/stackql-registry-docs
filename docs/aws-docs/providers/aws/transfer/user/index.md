---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - transfer
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
<tr><td><b>Id</b></td><td><code>aws.transfer.user</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>policy</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>home_directory</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>home_directory_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>user_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>home_directory_mappings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>posix_profile</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ssh_public_keys</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
policy,
role,
home_directory,
home_directory_type,
server_id,
user_name,
home_directory_mappings,
posix_profile,
ssh_public_keys,
id,
arn,
tags
FROM aws.transfer.user
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
