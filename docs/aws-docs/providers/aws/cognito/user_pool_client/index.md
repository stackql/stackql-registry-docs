---
title: user_pool_client
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_client
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
Gets an individual <code>user_pool_client</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_client</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_pool_client</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_client</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>analytics_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>generate_secret</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>callback_ur_ls</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id_token_validity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>token_validity_units</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>read_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>allowed_oauth_flows_user_pool_client</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>default_redirect_ur_i</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>explicit_auth_flows</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>access_token_validity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>enable_token_revocation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_propagate_additional_user_context_data</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>auth_session_validity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>allowed_oauth_scopes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>supported_identity_providers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>allowed_oauth_flows</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>client_secret</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>logout_ur_ls</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>refresh_token_validity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>write_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>prevent_user_existence_errors</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
analytics_configuration,
generate_secret,
callback_ur_ls,
id_token_validity,
token_validity_units,
read_attributes,
allowed_oauth_flows_user_pool_client,
default_redirect_ur_i,
name,
client_name,
explicit_auth_flows,
access_token_validity,
enable_token_revocation,
enable_propagate_additional_user_context_data,
auth_session_validity,
allowed_oauth_scopes,
supported_identity_providers,
user_pool_id,
allowed_oauth_flows,
client_secret,
logout_ur_ls,
refresh_token_validity,
id,
write_attributes,
prevent_user_existence_errors
FROM aws.cognito.user_pool_client
WHERE region = 'us-east-1'
AND data__Identifier = '<Id>'
```
