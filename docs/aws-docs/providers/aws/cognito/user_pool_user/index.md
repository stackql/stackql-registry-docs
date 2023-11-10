---
title: user_pool_user
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_user
  - cognito
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user_pool_user</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_pool_user</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_user</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>validation_data</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>username</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>message_action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_metadata</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>desired_delivery_mediums</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>force_alias_creation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>user_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
validation_data,
user_pool_id,
username,
message_action,
client_metadata,
id,
desired_delivery_mediums,
force_alias_creation,
user_attributes
FROM aws.cognito.user_pool_user
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
