--- 
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - user
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.user.users" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_users"
    values={[
        { label: 'list_users', value: 'list_users' },
        { label: 'fetch_user', value: 'fetch_user' }
    ]}
>
<TabItem value="list_users">

Properties of user.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>User name (example: jackpatel)</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td>Display name</td>
</tr>
<tr>
    <td><CopyableCode code="first_name" /></td>
    <td><code>string</code></td>
    <td>First name</td>
</tr>
<tr>
    <td><CopyableCode code="last_name" /></td>
    <td><code>string</code></td>
    <td>Last name</td>
</tr>
<tr>
    <td><CopyableCode code="login_name" /></td>
    <td><code>string</code></td>
    <td>Login name</td>
</tr>
<tr>
    <td><CopyableCode code="middle_name" /></td>
    <td><code>string</code></td>
    <td>Middle name</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment about the user. (example: A distinguished user)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_landing_page_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_landing_page_url_flush_next_ui_load" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not to flush the custom landing page of the user on next UI load</td>
</tr>
<tr>
    <td><CopyableCode code="days_to_expiry" /></td>
    <td><code>integer</code></td>
    <td>How many days until this user expires</td>
</tr>
<tr>
    <td><CopyableCode code="default_namespace" /></td>
    <td><code>string</code></td>
    <td>The default namespace to use when this user starts a session</td>
</tr>
<tr>
    <td><CopyableCode code="default_role" /></td>
    <td><code>string</code></td>
    <td>The default role to use when this user starts a session</td>
</tr>
<tr>
    <td><CopyableCode code="default_secondary_roles" /></td>
    <td><code>string</code></td>
    <td>The default secondary roles of this user to use when starting a session. Only valid set values are ALL or NONE. Default is ALL after 2024-07 BCR. (default: ALL)</td>
</tr>
<tr>
    <td><CopyableCode code="default_warehouse" /></td>
    <td><code>string</code></td>
    <td>The default warehouse to use when this user starts a session</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><code>boolean</code></td>
    <td>Has this user been disabled from the system</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>Email address</td>
</tr>
<tr>
    <td><CopyableCode code="enable_unredacted_query_syntax_error" /></td>
    <td><code>boolean</code></td>
    <td>Whether to show unredacted query syntax errors in the query history.</td>
</tr>
<tr>
    <td><CopyableCode code="expires_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ext_authn_duo" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ext_authn_uid" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="has_password" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="has_rsa_public_key" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_successful_login" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="locked_until" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mins_to_bypass_mfa" /></td>
    <td><code>integer</code></td>
    <td>How many minutes until MFA is required again</td>
</tr>
<tr>
    <td><CopyableCode code="mins_to_bypass_network_policy" /></td>
    <td><code>integer</code></td>
    <td>Temporary bypass network policy on the user for a specified number of minutes</td>
</tr>
<tr>
    <td><CopyableCode code="mins_to_unlock" /></td>
    <td><code>integer</code></td>
    <td>How many minutes until the account is unlocked after multiple failed logins</td>
</tr>
<tr>
    <td><CopyableCode code="must_change_password" /></td>
    <td><code>boolean</code></td>
    <td>Does this user need to change their password (e.g., after assigning a temp password)</td>
</tr>
<tr>
    <td><CopyableCode code="network_policy" /></td>
    <td><code>string</code></td>
    <td>Specifies an existing network policy is active for the user. Otherwise, use account default.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string (password)</code></td>
    <td>Password</td>
</tr>
<tr>
    <td><CopyableCode code="password_last_set" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rsa_public_key" /></td>
    <td><code>string</code></td>
    <td>RSA public key of the user</td>
</tr>
<tr>
    <td><CopyableCode code="rsa_public_key_2" /></td>
    <td><code>string</code></td>
    <td>Second RSA public key of the user</td>
</tr>
<tr>
    <td><CopyableCode code="rsa_public_key_2_fp" /></td>
    <td><code>string</code></td>
    <td>Fingerprint of the user&#039;s second RSA public key</td>
</tr>
<tr>
    <td><CopyableCode code="rsa_public_key_fp" /></td>
    <td><code>string</code></td>
    <td>Fingerprint of the user&#039;s RSA public key</td>
</tr>
<tr>
    <td><CopyableCode code="snowflake_lock" /></td>
    <td><code>boolean</code></td>
    <td>Whether the user, account, or organization is locked by Snowflake.</td>
</tr>
<tr>
    <td><CopyableCode code="snowflake_support" /></td>
    <td><code>boolean</code></td>
    <td>Whether Snowflake Support is allowed to use the user or account</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of user (PERSON | SERVICE | LEGACY_SERVICE)</td>
</tr>
</tbody>
</table>
</TabItem>
<TabItem value="fetch_user">

Properties of user.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>User name (example: jackpatel)</td>
</tr>
<tr>
    <td><CopyableCode code="display_name" /></td>
    <td><code>string</code></td>
    <td>Display name</td>
</tr>
<tr>
    <td><CopyableCode code="first_name" /></td>
    <td><code>string</code></td>
    <td>First name</td>
</tr>
<tr>
    <td><CopyableCode code="last_name" /></td>
    <td><code>string</code></td>
    <td>Last name</td>
</tr>
<tr>
    <td><CopyableCode code="login_name" /></td>
    <td><code>string</code></td>
    <td>Login name</td>
</tr>
<tr>
    <td><CopyableCode code="middle_name" /></td>
    <td><code>string</code></td>
    <td>Middle name</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Comment about the user. (example: A distinguished user)</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_landing_page_url" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="custom_landing_page_url_flush_next_ui_load" /></td>
    <td><code>boolean</code></td>
    <td>Whether or not to flush the custom landing page of the user on next UI load</td>
</tr>
<tr>
    <td><CopyableCode code="days_to_expiry" /></td>
    <td><code>integer</code></td>
    <td>How many days until this user expires</td>
</tr>
<tr>
    <td><CopyableCode code="default_namespace" /></td>
    <td><code>string</code></td>
    <td>The default namespace to use when this user starts a session</td>
</tr>
<tr>
    <td><CopyableCode code="default_role" /></td>
    <td><code>string</code></td>
    <td>The default role to use when this user starts a session</td>
</tr>
<tr>
    <td><CopyableCode code="default_secondary_roles" /></td>
    <td><code>string</code></td>
    <td>The default secondary roles of this user to use when starting a session. Only valid set values are ALL or NONE. Default is ALL after 2024-07 BCR. (default: ALL)</td>
</tr>
<tr>
    <td><CopyableCode code="default_warehouse" /></td>
    <td><code>string</code></td>
    <td>The default warehouse to use when this user starts a session</td>
</tr>
<tr>
    <td><CopyableCode code="disabled" /></td>
    <td><code>boolean</code></td>
    <td>Has this user been disabled from the system</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>Email address</td>
</tr>
<tr>
    <td><CopyableCode code="enable_unredacted_query_syntax_error" /></td>
    <td><code>boolean</code></td>
    <td>Whether to show unredacted query syntax errors in the query history.</td>
</tr>
<tr>
    <td><CopyableCode code="expires_at" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ext_authn_duo" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="ext_authn_uid" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="has_password" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="has_rsa_public_key" /></td>
    <td><code>boolean</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="last_successful_login" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="locked_until" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="mins_to_bypass_mfa" /></td>
    <td><code>integer</code></td>
    <td>How many minutes until MFA is required again</td>
</tr>
<tr>
    <td><CopyableCode code="mins_to_bypass_network_policy" /></td>
    <td><code>integer</code></td>
    <td>Temporary bypass network policy on the user for a specified number of minutes</td>
</tr>
<tr>
    <td><CopyableCode code="mins_to_unlock" /></td>
    <td><code>integer</code></td>
    <td>How many minutes until the account is unlocked after multiple failed logins</td>
</tr>
<tr>
    <td><CopyableCode code="must_change_password" /></td>
    <td><code>boolean</code></td>
    <td>Does this user need to change their password (e.g., after assigning a temp password)</td>
</tr>
<tr>
    <td><CopyableCode code="network_policy" /></td>
    <td><code>string</code></td>
    <td>Specifies an existing network policy is active for the user. Otherwise, use account default.</td>
</tr>
<tr>
    <td><CopyableCode code="owner" /></td>
    <td><code>string</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="password" /></td>
    <td><code>string (password)</code></td>
    <td>Password</td>
</tr>
<tr>
    <td><CopyableCode code="password_last_set" /></td>
    <td><code>string (date-time)</code></td>
    <td></td>
</tr>
<tr>
    <td><CopyableCode code="rsa_public_key" /></td>
    <td><code>string</code></td>
    <td>RSA public key of the user</td>
</tr>
<tr>
    <td><CopyableCode code="rsa_public_key_2" /></td>
    <td><code>string</code></td>
    <td>Second RSA public key of the user</td>
</tr>
<tr>
    <td><CopyableCode code="rsa_public_key_2_fp" /></td>
    <td><code>string</code></td>
    <td>Fingerprint of the user&#039;s second RSA public key</td>
</tr>
<tr>
    <td><CopyableCode code="rsa_public_key_fp" /></td>
    <td><code>string</code></td>
    <td>Fingerprint of the user&#039;s RSA public key</td>
</tr>
<tr>
    <td><CopyableCode code="snowflake_lock" /></td>
    <td><code>boolean</code></td>
    <td>Whether the user, account, or organization is locked by Snowflake.</td>
</tr>
<tr>
    <td><CopyableCode code="snowflake_support" /></td>
    <td><code>boolean</code></td>
    <td>Whether Snowflake Support is allowed to use the user or account</td>
</tr>
<tr>
    <td><CopyableCode code="type" /></td>
    <td><code>string</code></td>
    <td>Indicates the type of user (PERSON | SERVICE | LEGACY_SERVICE)</td>
</tr>
</tbody>
</table>
</TabItem>
</Tabs>

## Methods

The following methods are available for this resource:

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
    <th>Optional Params</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr>
    <td><a href="#list_users"><CopyableCode code="list_users" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-like"><code>like</code></a>, <a href="#parameter-startsWith"><code>startsWith</code></a>, <a href="#parameter-showLimit"><code>showLimit</code></a>, <a href="#parameter-fromName"><code>fromName</code></a></td>
    <td>Lists the users in the system.</td>
</tr>
<tr>
    <td><a href="#fetch_user"><CopyableCode code="fetch_user" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Fetch user information using the result of the DESCRIBE command</td>
</tr>
<tr>
    <td><a href="#create_user"><CopyableCode code="create_user" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-createMode"><code>createMode</code></a></td>
    <td>Create a user according to the parameters given</td>
</tr>
<tr>
    <td><a href="#create_or_alter_user"><CopyableCode code="create_or_alter_user" /></a></td>
    <td><CopyableCode code="replace" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td></td>
    <td>Create a (or alter an existing) user. Even if the operation is just an alter, the full property set must be provided. Note that password is not currently altered by this operation but is supported for a newly-created object.</td>
</tr>
<tr>
    <td><a href="#delete_user"><CopyableCode code="delete_user" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name"><code>name</code></a>, <a href="#parameter-endpoint"><code>endpoint</code></a></td>
    <td><a href="#parameter-ifExists"><code>ifExists</code></a></td>
    <td>Delete a user with the given name.</td>
</tr>
</tbody>
</table>

## Parameters

Parameters can be passed in the `WHERE` clause of a query. Check the [Methods](#methods) section to see which parameters are required or optional for each operation.

<table>
<thead>
    <tr>
    <th>Name</th>
    <th>Datatype</th>
    <th>Description</th>
    </tr>
</thead>
<tbody>
<tr id="parameter-endpoint">
    <td><CopyableCode code="endpoint" /></td>
    <td><code>string</code></td>
    <td>Organization and Account Name (default: orgid-acctid)</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource.</td>
</tr>
<tr id="parameter-createMode">
    <td><CopyableCode code="createMode" /></td>
    <td><code>string</code></td>
    <td>Query parameter allowing support for different modes of resource creation. Possible values include: - <code>errorIfExists</code>: Throws an error if you try to create a resource that already exists. - <code>orReplace</code>: Automatically replaces the existing resource with the current one. - <code>ifNotExists</code>: Creates a new resource when an alter is requested for a non-existent resource.</td>
</tr>
<tr id="parameter-fromName">
    <td><CopyableCode code="fromName" /></td>
    <td><code>string</code></td>
    <td>Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - <code>true</code>: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - <code>false</code>: The endpoint throws an error if the resource doesn't exist.</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters.</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command.</td>
</tr>
<tr id="parameter-startsWith">
    <td><CopyableCode code="startsWith" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching.</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_users"
    values={[
        { label: 'list_users', value: 'list_users' },
        { label: 'fetch_user', value: 'fetch_user' }
    ]}
>
<TabItem value="list_users">

Lists the users in the system.

```sql
SELECT
name,
display_name,
first_name,
last_name,
login_name,
middle_name,
comment,
created_on,
custom_landing_page_url,
custom_landing_page_url_flush_next_ui_load,
days_to_expiry,
default_namespace,
default_role,
default_secondary_roles,
default_warehouse,
disabled,
email,
enable_unredacted_query_syntax_error,
expires_at,
ext_authn_duo,
ext_authn_uid,
has_password,
has_rsa_public_key,
last_successful_login,
locked_until,
mins_to_bypass_mfa,
mins_to_bypass_network_policy,
mins_to_unlock,
must_change_password,
network_policy,
owner,
password,
password_last_set,
rsa_public_key,
rsa_public_key_2,
rsa_public_key_2_fp,
rsa_public_key_fp,
snowflake_lock,
snowflake_support,
type
FROM snowflake.user.users
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND startsWith = '{{ startsWith }}'
AND showLimit = '{{ showLimit }}'
AND fromName = '{{ fromName }}';
```
</TabItem>
<TabItem value="fetch_user">

Fetch user information using the result of the DESCRIBE command

```sql
SELECT
name,
display_name,
first_name,
last_name,
login_name,
middle_name,
comment,
created_on,
custom_landing_page_url,
custom_landing_page_url_flush_next_ui_load,
days_to_expiry,
default_namespace,
default_role,
default_secondary_roles,
default_warehouse,
disabled,
email,
enable_unredacted_query_syntax_error,
expires_at,
ext_authn_duo,
ext_authn_uid,
has_password,
has_rsa_public_key,
last_successful_login,
locked_until,
mins_to_bypass_mfa,
mins_to_bypass_network_policy,
mins_to_unlock,
must_change_password,
network_policy,
owner,
password,
password_last_set,
rsa_public_key,
rsa_public_key_2,
rsa_public_key_2_fp,
rsa_public_key_fp,
snowflake_lock,
snowflake_support,
type
FROM snowflake.user.users
WHERE name = '{{ name }}' -- required
AND endpoint = '{{ endpoint }}' -- required;
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_user"
    values={[
        { label: 'create_user', value: 'create_user' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_user">

Create a user according to the parameters given

```sql
INSERT INTO snowflake.user.users (
data__name,
data__password,
data__login_name,
data__display_name,
data__first_name,
data__middle_name,
data__last_name,
data__email,
data__must_change_password,
data__disabled,
data__days_to_expiry,
data__mins_to_unlock,
data__default_warehouse,
data__default_namespace,
data__default_role,
data__default_secondary_roles,
data__mins_to_bypass_mfa,
data__rsa_public_key,
data__rsa_public_key_2,
data__comment,
data__type,
data__enable_unredacted_query_syntax_error,
data__network_policy,
endpoint,
createMode
)
SELECT 
'{{ name }}',
'{{ password }}',
'{{ login_name }}',
'{{ display_name }}',
'{{ first_name }}',
'{{ middle_name }}',
'{{ last_name }}',
'{{ email }}',
{{ must_change_password }},
{{ disabled }},
{{ days_to_expiry }},
{{ mins_to_unlock }},
'{{ default_warehouse }}',
'{{ default_namespace }}',
'{{ default_role }}',
'{{ default_secondary_roles }}',
{{ mins_to_bypass_mfa }},
'{{ rsa_public_key }}',
'{{ rsa_public_key_2 }}',
'{{ comment }}',
'{{ type }}',
{{ enable_unredacted_query_syntax_error }},
'{{ network_policy }}',
'{{ endpoint }}',
'{{ createMode }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: users
  props:
    - name: endpoint
      value: string
      description: Required parameter for the users resource.
    - name: name
      value: string
      description: >
        User name
        
    - name: password
      value: string
      description: >
        Password
        
    - name: login_name
      value: string
      description: >
        Login name
        
    - name: display_name
      value: string
      description: >
        Display name
        
    - name: first_name
      value: string
      description: >
        First name
        
    - name: middle_name
      value: string
      description: >
        Middle name
        
    - name: last_name
      value: string
      description: >
        Last name
        
    - name: email
      value: string
      description: >
        Email address
        
    - name: must_change_password
      value: boolean
      description: >
        Does this user need to change their password (e.g., after assigning a temp password)
        
    - name: disabled
      value: boolean
      description: >
        Has this user been disabled from the system
        
    - name: days_to_expiry
      value: integer
      description: >
        How many days until this user expires
        
    - name: mins_to_unlock
      value: integer
      description: >
        How many minutes until the account is unlocked after multiple failed logins
        
    - name: default_warehouse
      value: string
      description: >
        The default warehouse to use when this user starts a session
        
    - name: default_namespace
      value: string
      description: >
        The default namespace to use when this user starts a session
        
    - name: default_role
      value: string
      description: >
        The default role to use when this user starts a session
        
    - name: default_secondary_roles
      value: string
      description: >
        The default secondary roles of this user to use when starting a session. Only valid set values are ALL or NONE. Default is ALL after 2024-07 BCR.
        
      valid_values: ['ALL', 'NONE']
      default: ALL
    - name: mins_to_bypass_mfa
      value: integer
      description: >
        How many minutes until MFA is required again
        
    - name: rsa_public_key
      value: string
      description: >
        RSA public key of the user
        
    - name: rsa_public_key_2
      value: string
      description: >
        Second RSA public key of the user
        
    - name: comment
      value: string
      description: >
        Comment about the user.
        
    - name: type
      value: string
      description: >
        Indicates the type of user (PERSON | SERVICE | LEGACY_SERVICE)
        
    - name: enable_unredacted_query_syntax_error
      value: boolean
      description: >
        Whether to show unredacted query syntax errors in the query history.
        
    - name: network_policy
      value: string
      description: >
        Specifies an existing network policy is active for the user. Otherwise, use account default.
        
    - name: createMode
      value: string
      description: Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource.
```
</TabItem>
</Tabs>


## `REPLACE` examples

<Tabs
    defaultValue="create_or_alter_user"
    values={[
        { label: 'create_or_alter_user', value: 'create_or_alter_user' }
    ]}
>
<TabItem value="create_or_alter_user">

Create a (or alter an existing) user. Even if the operation is just an alter, the full property set must be provided. Note that password is not currently altered by this operation but is supported for a newly-created object.

```sql
REPLACE snowflake.user.users
SET 
data__name = '{{ name }}',
data__password = '{{ password }}',
data__login_name = '{{ login_name }}',
data__display_name = '{{ display_name }}',
data__first_name = '{{ first_name }}',
data__middle_name = '{{ middle_name }}',
data__last_name = '{{ last_name }}',
data__email = '{{ email }}',
data__must_change_password = {{ must_change_password }},
data__disabled = {{ disabled }},
data__days_to_expiry = {{ days_to_expiry }},
data__mins_to_unlock = {{ mins_to_unlock }},
data__default_warehouse = '{{ default_warehouse }}',
data__default_namespace = '{{ default_namespace }}',
data__default_role = '{{ default_role }}',
data__default_secondary_roles = '{{ default_secondary_roles }}',
data__mins_to_bypass_mfa = {{ mins_to_bypass_mfa }},
data__rsa_public_key = '{{ rsa_public_key }}',
data__rsa_public_key_2 = '{{ rsa_public_key_2 }}',
data__comment = '{{ comment }}',
data__type = '{{ type }}',
data__enable_unredacted_query_syntax_error = {{ enable_unredacted_query_syntax_error }},
data__network_policy = '{{ network_policy }}'
WHERE 
name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND data__name = '{{ name }}' --required;
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_user"
    values={[
        { label: 'delete_user', value: 'delete_user' }
    ]}
>
<TabItem value="delete_user">

Delete a user with the given name.

```sql
DELETE FROM snowflake.user.users
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>
