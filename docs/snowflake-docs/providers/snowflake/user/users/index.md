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
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | User name |
| <CopyableCode code="comment" /> | `string` | Comment about the user. |
| <CopyableCode code="created_on" /> | `string` |  |
| <CopyableCode code="custom_landing_page_url" /> | `string` |  |
| <CopyableCode code="custom_landing_page_url_flush_next_ui_load" /> | `boolean` | Whether or not to flush the custom landing page of the user on next UI load |
| <CopyableCode code="days_to_expiry" /> | `integer` | How many days until this user expires |
| <CopyableCode code="default_namespace" /> | `string` | The default namespace to use when this user starts a session |
| <CopyableCode code="default_role" /> | `string` | The default role to use when this user starts a session |
| <CopyableCode code="default_secondary_roles" /> | `string` | The default secondary roles of this user to use when starting a session. Only valid set values are ALL or NONE. Default is ALL after 2024-07 BCR. |
| <CopyableCode code="default_warehouse" /> | `string` | The default warehouse to use when this user starts a session |
| <CopyableCode code="disabled" /> | `boolean` | Has this user been disabled from the system |
| <CopyableCode code="display_name" /> | `string` | Display name |
| <CopyableCode code="email" /> | `string` | Email address |
| <CopyableCode code="enable_unredacted_query_syntax_error" /> | `boolean` | Whether to show unredacted query syntax errors in the query history. |
| <CopyableCode code="expires_at" /> | `string` |  |
| <CopyableCode code="ext_authn_duo" /> | `boolean` |  |
| <CopyableCode code="ext_authn_uid" /> | `string` |  |
| <CopyableCode code="first_name" /> | `string` | First name |
| <CopyableCode code="has_password" /> | `boolean` |  |
| <CopyableCode code="has_rsa_public_key" /> | `boolean` |  |
| <CopyableCode code="last_name" /> | `string` | Last name |
| <CopyableCode code="last_successful_login" /> | `string` |  |
| <CopyableCode code="locked_until" /> | `string` |  |
| <CopyableCode code="login_name" /> | `string` | Login name |
| <CopyableCode code="middle_name" /> | `string` | Middle name |
| <CopyableCode code="mins_to_bypass_mfa" /> | `integer` | How many minutes until MFA is required again |
| <CopyableCode code="mins_to_bypass_network_policy" /> | `integer` | Temporary bypass network policy on the user for a specified number of minutes |
| <CopyableCode code="mins_to_unlock" /> | `integer` | How many minutes until the account is unlocked after multiple failed logins |
| <CopyableCode code="must_change_password" /> | `boolean` | Does this user need to change their password (e.g., after assigning a temp password) |
| <CopyableCode code="network_policy" /> | `string` | Specifies an existing network policy is active for the user. Otherwise, use account default. |
| <CopyableCode code="owner" /> | `string` |  |
| <CopyableCode code="password" /> | `string` | Password |
| <CopyableCode code="password_last_set" /> | `string` |  |
| <CopyableCode code="rsa_public_key" /> | `string` | RSA public key of the user |
| <CopyableCode code="rsa_public_key_2" /> | `string` | Second RSA public key of the user |
| <CopyableCode code="rsa_public_key_2_fp" /> | `string` | Fingerprint of the user's second RSA public key |
| <CopyableCode code="rsa_public_key_fp" /> | `string` | Fingerprint of the user's RSA public key |
| <CopyableCode code="snowflake_lock" /> | `boolean` | Whether the user, account, or organization is locked by Snowflake. |
| <CopyableCode code="snowflake_support" /> | `boolean` | Whether Snowflake Support is allowed to use the user or account |
| <CopyableCode code="type" /> | `string` | Indicates the type of user (PERSON \| SERVICE \| LEGACY_SERVICE) |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_user" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | - | Fetch user information using the result of the DESCRIBE command |
| <CopyableCode code="list_users" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="startsWith" />, <CopyableCode code="showLimit" />, <CopyableCode code="fromName" /> | Lists the users in the system. |
| <CopyableCode code="create_user" /> | `INSERT` | <CopyableCode code="data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a user according to the parameters given |
| <CopyableCode code="delete_user" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a user with the given name. |
| <CopyableCode code="create_or_alter_user" /> | `REPLACE` | <CopyableCode code="name, data__name, endpoint" /> | - | Create a (or alter an existing) user. Even if the operation is just an alter, the full property set must be provided. Note that password is not currently altered by this operation but is supported for a newly-created object. |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="fromName" /> | Query parameter to enable fetching rows only following the first row whose object name matches the specified string. Case-sensitive and does not have to be the full name. | `string` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |
| <CopyableCode code="startsWith" /> | Query parameter to filter the command output based on the string of characters that appear at the beginning of the object name. Uses case-sensitive pattern matching. | `string` | `-` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_users"
    values={[
        { label: 'list_users', value: 'list_users' },
        { label: 'fetch_user', value: 'fetch_user' }
    ]
}>
<TabItem value="list_users">

Lists the users in the system.

```sql
SELECT
name,
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
display_name,
email,
enable_unredacted_query_syntax_error,
expires_at,
ext_authn_duo,
ext_authn_uid,
first_name,
has_password,
has_rsa_public_key,
last_name,
last_successful_login,
locked_until,
login_name,
middle_name,
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
WHERE endpoint = '{{ endpoint }}';
```
</TabItem>
<TabItem value="fetch_user">

Fetch user information using the result of the DESCRIBE command

```sql
SELECT
name,
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
display_name,
email,
enable_unredacted_query_syntax_error,
expires_at,
ext_authn_duo,
ext_authn_uid,
first_name,
has_password,
has_rsa_public_key,
last_name,
last_successful_login,
locked_until,
login_name,
middle_name,
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
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Create a user according to the parameters given

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
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
endpoint
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
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.user.users (
data__name,
endpoint
)
SELECT 
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: users
  props:
    - name: endpoint
      value: string
      description: Required parameter for the users resource.
    - name: name
      value: string
      description: User name (Required parameter for the users resource.)
    - name: password
      value: string
      description: Password
    - name: login_name
      value: string
      description: Login name
    - name: display_name
      value: string
      description: Display name
    - name: first_name
      value: string
      description: First name
    - name: middle_name
      value: string
      description: Middle name
    - name: last_name
      value: string
      description: Last name
    - name: email
      value: string
      description: Email address
    - name: must_change_password
      value: boolean
      description: >-
        Does this user need to change their password (e.g., after assigning a
        temp password)
    - name: disabled
      value: boolean
      description: Has this user been disabled from the system
    - name: days_to_expiry
      value: integer
      description: How many days until this user expires
    - name: mins_to_unlock
      value: integer
      description: >-
        How many minutes until the account is unlocked after multiple failed
        logins
    - name: default_warehouse
      value: string
      description: The default warehouse to use when this user starts a session
    - name: default_namespace
      value: string
      description: The default namespace to use when this user starts a session
    - name: default_role
      value: string
      description: The default role to use when this user starts a session
    - name: default_secondary_roles
      value: string
      description: >-
        The default secondary roles of this user to use when starting a session.
        Only valid set values are ALL or NONE. Default is ALL after 2024-07 BCR.
        (valid values: 'ALL', 'NONE')
      default: ALL
    - name: mins_to_bypass_mfa
      value: integer
      description: How many minutes until MFA is required again
    - name: rsa_public_key
      value: string
      description: RSA public key of the user
    - name: rsa_public_key_2
      value: string
      description: Second RSA public key of the user
    - name: comment
      value: string
      description: Comment about the user.
    - name: type
      value: string
      description: Indicates the type of user (PERSON \| SERVICE \| LEGACY_SERVICE)
    - name: enable_unredacted_query_syntax_error
      value: boolean
      description: Whether to show unredacted query syntax errors in the query history.
    - name: network_policy
      value: string
      description: >-
        Specifies an existing network policy is active for the user. Otherwise,
        use account default.
```
</TabItem>
</Tabs>

## `REPLACE` example

Create a (or alter an existing) user. Even if the operation is just an alter, the full property set must be provided. Note that password is not currently altered by this operation but is supported for a newly-created object.

```sql
/*+ update */
REPLACE snowflake.user.users
SET 
name = '{{ name }}',
password = '{{ password }}',
login_name = '{{ login_name }}',
display_name = '{{ display_name }}',
first_name = '{{ first_name }}',
middle_name = '{{ middle_name }}',
last_name = '{{ last_name }}',
email = '{{ email }}',
must_change_password = {{ must_change_password }},
disabled = {{ disabled }},
days_to_expiry = {{ days_to_expiry }},
mins_to_unlock = {{ mins_to_unlock }},
default_warehouse = '{{ default_warehouse }}',
default_namespace = '{{ default_namespace }}',
default_role = '{{ default_role }}',
default_secondary_roles = '{{ default_secondary_roles }}',
mins_to_bypass_mfa = {{ mins_to_bypass_mfa }},
rsa_public_key = '{{ rsa_public_key }}',
rsa_public_key_2 = '{{ rsa_public_key_2 }}',
comment = '{{ comment }}',
type = '{{ type }}',
enable_unredacted_query_syntax_error = {{ enable_unredacted_query_syntax_error }},
network_policy = '{{ network_policy }}'
WHERE 
name = '{{ name }}'
AND data__name = '{{ data__name }}'
AND endpoint = '{{ endpoint }}';
```

## `DELETE` example

Delete a user with the given name.

```sql
/*+ delete */
DELETE FROM snowflake.user.users
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
