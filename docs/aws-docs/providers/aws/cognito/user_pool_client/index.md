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
Gets or operates on an individual <code>user_pool_client</code> resource, use <code>user_pool_clients</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_client</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolClient</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_client</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>client_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>explicit_auth_flows</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>generate_secret</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>read_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>auth_session_validity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>refresh_token_validity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>access_token_validity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>id_token_validity</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>token_validity_units</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>user_pool_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>write_attributes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>allowed_oauth_flows</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>allowed_oauth_flows_user_pool_client</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>allowed_oauth_scopes</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>callback_urls</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>default_redirect_uri</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>logout_urls</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>supported_identity_providers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>analytics_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>prevent_user_existence_errors</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enable_token_revocation</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>enable_propagate_additional_user_context_data</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_secret</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>client_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
client_name,
explicit_auth_flows,
generate_secret,
read_attributes,
auth_session_validity,
refresh_token_validity,
access_token_validity,
id_token_validity,
token_validity_units,
user_pool_id,
write_attributes,
allowed_oauth_flows,
allowed_oauth_flows_user_pool_client,
allowed_oauth_scopes,
callback_urls,
default_redirect_uri,
logout_urls,
supported_identity_providers,
analytics_configuration,
prevent_user_existence_errors,
enable_token_revocation,
enable_propagate_additional_user_context_data,
name,
client_secret,
client_id
FROM aws.cognito.user_pool_client
WHERE data__Identifier = '<UserPoolId>|<ClientId>';
```

## Permissions

To operate on the <code>user_pool_client</code> resource, the following permissions are required:

### Read
```json
cognito-idp:DescribeUserPoolClient
```

### Update
```json
cognito-idp:UpdateUserPoolClient,
iam:PassRole,
iam:PutRolePolicy
```

### Delete
```json
cognito-idp:DeleteUserPoolClient,
iam:PutRolePolicy,
iam:DeleteRolePolicy
```

