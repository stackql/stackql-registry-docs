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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_user" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | Fetch user information using the result of the DESCRIBE command |
| <CopyableCode code="list_users" /> | `SELECT` | <CopyableCode code="endpoint" /> | Lists the users in the system. |
| <CopyableCode code="create_user" /> | `INSERT` | <CopyableCode code="data__name, endpoint" /> | Create a user according to the parameters given |
| <CopyableCode code="delete_user" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | Delete a user with the given name. |
| <CopyableCode code="create_or_alter_user" /> | `REPLACE` | <CopyableCode code="name, data__name, endpoint" /> | Create a (or alter an existing) user. Even if the operation is just an alter, the full property set must be provided. Note that password is not currently altered by this operation but is supported for a newly-created object. |

## `SELECT` examples

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
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>users</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.user.users (
endpoint,
data__name
)
SELECT 
'{ name }',
'{ endpoint }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: users
  props:
  - name: data__name
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>users</code> resource.

```sql
/*+ update */
REPLACE snowflake.user.users
SET 

WHERE 
name = '{ name }' AND data__name = '{ data__name }' AND endpoint = '{ endpoint }';
```

## `DELETE` example

Deletes the specified <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.user.users
WHERE name = '{ name }' AND endpoint = '{ endpoint }';
```
