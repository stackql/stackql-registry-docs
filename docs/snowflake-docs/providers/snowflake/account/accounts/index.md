--- 
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - account
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

Creates, updates, deletes, gets or lists an <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.account.accounts" /></td></tr>
</tbody></table>

## Fields

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_accounts"
    values={[
        { label: 'list_accounts', value: 'list_accounts' }
    ]}
>
<TabItem value="list_accounts">

Snowflake account object.

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
    <td>A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.  (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr>
    <td><CopyableCode code="admin_name" /></td>
    <td><code>string</code></td>
    <td>Name of the account administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="consumption_billing_entity_name" /></td>
    <td><code>string</code></td>
    <td>Name of the consumption billing entity.</td>
</tr>
<tr>
    <td><CopyableCode code="first_name" /></td>
    <td><code>string</code></td>
    <td>First name of the account administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="last_name" /></td>
    <td><code>string</code></td>
    <td>Last name of the account administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplace_consumer_billing_entity_name" /></td>
    <td><code>string</code></td>
    <td>Name of the marketplace consumer billing entity.</td>
</tr>
<tr>
    <td><CopyableCode code="marketplace_provider_billing_entity_name" /></td>
    <td><code>string</code></td>
    <td>Name of the marketplace provider billing entity.</td>
</tr>
<tr>
    <td><CopyableCode code="organization_name" /></td>
    <td><code>string</code></td>
    <td>Name of the organization.</td>
</tr>
<tr>
    <td><CopyableCode code="account_locator" /></td>
    <td><code>string</code></td>
    <td>System-assigned identifier of the acccount.</td>
</tr>
<tr>
    <td><CopyableCode code="account_locator_url" /></td>
    <td><code>string</code></td>
    <td>Legacy Snowflake account URL syntax that includes the region_name and account_locator.</td>
</tr>
<tr>
    <td><CopyableCode code="account_old_url_last_used" /></td>
    <td><code>string (date-time)</code></td>
    <td>If the original account URL was saved when the account was renamed, indicates the last time the account was accessed using the original URL.</td>
</tr>
<tr>
    <td><CopyableCode code="account_old_url_saved_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>If the original account URL was saved when the account was renamed, provides the date and time when the original account URL was saved.</td>
</tr>
<tr>
    <td><CopyableCode code="account_url" /></td>
    <td><code>string</code></td>
    <td>Preferred Snowflake account URL that includes the values of organization_name and account_name.</td>
</tr>
<tr>
    <td><CopyableCode code="admin_password" /></td>
    <td><code>string (password)</code></td>
    <td>Password for the account administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="admin_rsa_public_key" /></td>
    <td><code>string (password)</code></td>
    <td>RSA public key for the account administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="admin_user_type" /></td>
    <td><code>string</code></td>
    <td>User type of the account administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="comment" /></td>
    <td><code>string</code></td>
    <td>Optional comment in which to store information related to the account.</td>
</tr>
<tr>
    <td><CopyableCode code="created_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the account was created.</td>
</tr>
<tr>
    <td><CopyableCode code="dropped_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time the account was dropped.</td>
</tr>
<tr>
    <td><CopyableCode code="edition" /></td>
    <td><code>string</code></td>
    <td>Snowflake Edition of the account.</td>
</tr>
<tr>
    <td><CopyableCode code="email" /></td>
    <td><code>string</code></td>
    <td>Email address of the account administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="is_events_account" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether an account is an events account. For more information, see Set up logging and event sharing for an application.</td>
</tr>
<tr>
    <td><CopyableCode code="is_org_admin" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the ORGADMIN role is enabled in an account. If TRUE, the role is enabled.</td>
</tr>
<tr>
    <td><CopyableCode code="managed_accounts" /></td>
    <td><code>integer (int64)</code></td>
    <td>Indicates how many managed accounts have been created by the account.</td>
</tr>
<tr>
    <td><CopyableCode code="moved_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the account was moved to a different organization.</td>
</tr>
<tr>
    <td><CopyableCode code="moved_to_organization" /></td>
    <td><code>string</code></td>
    <td>If the account was moved to a different organization, provides the name of that organization.</td>
</tr>
<tr>
    <td><CopyableCode code="must_change_password" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the account administrator must change the password at the next login.</td>
</tr>
<tr>
    <td><CopyableCode code="old_account_url" /></td>
    <td><code>string</code></td>
    <td>If the original account URL was saved when the account was renamed, provides the original URL. If the original account URL was dropped, the value is NULL even if the account was renamed</td>
</tr>
<tr>
    <td><CopyableCode code="organization_URL_expiration_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, provides the date and time when the original account URL will be dropped. Dropped URLs cannot be used to access the account.</td>
</tr>
<tr>
    <td><CopyableCode code="organization_old_url" /></td>
    <td><code>string</code></td>
    <td>If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, provides the original account URL. If the original account URL was dropped, the value is NULL even if the organization changed.</td>
</tr>
<tr>
    <td><CopyableCode code="organization_old_url_last_used" /></td>
    <td><code>string (date-time)</code></td>
    <td>If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, indicates the last time the account was accessed using the original account URL.</td>
</tr>
<tr>
    <td><CopyableCode code="organization_old_url_saved_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, provides the date and time when the original account URL was saved.</td>
</tr>
<tr>
    <td><CopyableCode code="polaris" /></td>
    <td><code>boolean</code></td>
    <td>Indicates whether the account is a Polaris account.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Snowflake Region where the account is located. A Snowflake Region is a distinct location within a cloud platform region that is isolated from other Snowflake Regions. A Snowflake Region can be either multi-tenant or single-tenant (for a Virtual Private Snowflake account).</td>
</tr>
<tr>
    <td><CopyableCode code="region_group" /></td>
    <td><code>string</code></td>
    <td>Region group where the account is located. Note - This column is only displayed for organizations that span multiple region groups.</td>
</tr>
<tr>
    <td><CopyableCode code="restored_on" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the account was last restored.</td>
</tr>
<tr>
    <td><CopyableCode code="retention_time" /></td>
    <td><code>integer</code></td>
    <td>Number of days that historical data is retained for Time Travel.</td>
</tr>
<tr>
    <td><CopyableCode code="scheduled_deletion_time" /></td>
    <td><code>string (date-time)</code></td>
    <td>Date and time when the account is scheduled to be permanently deleted. Accounts are deleted within one hour after the scheduled time.</td>
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
    <td><a href="#list_accounts"><CopyableCode code="list_accounts" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a>, <a href="#parameter-showLimit">showLimit</a>, <a href="#parameter-history">history</a></td>
    <td>Lists the accessible accounts.</td>
</tr>
<tr>
    <td><a href="#create_account"><CopyableCode code="create_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Creates a account. You must provide the full account definition when creating a account.</td>
</tr>
<tr>
    <td><a href="#delete_account"><CopyableCode code="delete_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-gracePeriodInDays">gracePeriodInDays</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-ifExists">ifExists</a></td>
    <td>Deletes the specified account. If you enable the `ifExists` parameter, the operation succeeds even if the account does not exist. Otherwise, a 404 failure is returned if the account does not exist. if the drop is unsuccessful.</td>
</tr>
<tr>
    <td><a href="#undrop_account"><CopyableCode code="undrop_account" /></a></td>
    <td><CopyableCode code="exec" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Restores a dropped account that has not yet been permanently deleted (a dropped account that is within its grace period).</td>
</tr>
</tbody>
</table>## Parameters

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
<tr id="parameter-gracePeriodInDays">
    <td><CopyableCode code="gracePeriodInDays" /></td>
    <td><code>integer</code></td>
    <td>Specifies the number of days during which the account can be restored (“undropped”). The minimum is 3 days and the maximum is 90 days.</td>
</tr>
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource. (pattern: ^&quot;([^&quot;]|&quot;&quot;)+&quot;|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-history">
    <td><CopyableCode code="history" /></td>
    <td><code>boolean</code></td>
    <td>Optionally includes dropped accounts that have not yet been purged.</td>
</tr>
<tr id="parameter-ifExists">
    <td><CopyableCode code="ifExists" /></td>
    <td><code>boolean</code></td>
    <td>Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. (example: true, default: false)</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. (example: test_%)</td>
</tr>
<tr id="parameter-showLimit">
    <td><CopyableCode code="showLimit" /></td>
    <td><code>integer</code></td>
    <td>Query parameter to limit the maximum number of rows returned by a command. (example: 10, minimum: 1, maximum: 10000)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_accounts"
    values={[
        { label: 'list_accounts', value: 'list_accounts' }
    ]}
>
<TabItem value="list_accounts">

Lists the accessible accounts.

```sql
SELECT
name,
admin_name,
consumption_billing_entity_name,
first_name,
last_name,
marketplace_consumer_billing_entity_name,
marketplace_provider_billing_entity_name,
organization_name,
account_locator,
account_locator_url,
account_old_url_last_used,
account_old_url_saved_on,
account_url,
admin_password,
admin_rsa_public_key,
admin_user_type,
comment,
created_on,
dropped_on,
edition,
email,
is_events_account,
is_org_admin,
managed_accounts,
moved_on,
moved_to_organization,
must_change_password,
old_account_url,
organization_URL_expiration_on,
organization_old_url,
organization_old_url_last_used,
organization_old_url_saved_on,
polaris,
region,
region_group,
restored_on,
retention_time,
scheduled_deletion_time
FROM snowflake.account.accounts
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}'
AND showLimit = '{{ showLimit }}'
AND history = '{{ history }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_account"
    values={[
        { label: 'create_account', value: 'create_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_account">

Creates a account. You must provide the full account definition when creating a account.

```sql
INSERT INTO snowflake.account.accounts (
data__name,
data__region_group,
data__region,
data__edition,
data__comment,
data__admin_name,
data__admin_password,
data__admin_rsa_public_key,
data__admin_user_type,
data__first_name,
data__last_name,
data__email,
data__must_change_password,
data__polaris,
endpoint
)
SELECT 
'{{ name }}',
'{{ region_group }}',
'{{ region }}',
'{{ edition }}',
'{{ comment }}',
'{{ admin_name }}',
'{{ admin_password }}',
'{{ admin_rsa_public_key }}',
'{{ admin_user_type }}',
'{{ first_name }}',
'{{ last_name }}',
'{{ email }}',
{{ must_change_password }},
{{ polaris }},
'{{ endpoint }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: accounts
  props:
    - name: endpoint
      value: string
      description: Required parameter for the accounts resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

    - name: region_group
      value: string
      description: >
        Region group where the account is located. Note - This column is only displayed for organizations that span multiple region groups.
        
    - name: region
      value: string
      description: >
        Snowflake Region where the account is located. A Snowflake Region is a distinct location within a cloud platform region that is isolated from other Snowflake Regions. A Snowflake Region can be either multi-tenant or single-tenant (for a Virtual Private Snowflake account).
        
    - name: edition
      value: string
      description: >
        Snowflake Edition of the account.
        
      valid_values: ['STANDARD', 'ENTERPRISE', 'BUSINESS_CRITICAL']
    - name: comment
      value: string
      description: >
        Optional comment in which to store information related to the account.
        
    - name: admin_name
      value: string
      description: >
        Name of the account administrator.
        
    - name: admin_password
      value: string
      description: >
        Password for the account administrator.
        
    - name: admin_rsa_public_key
      value: string
      description: >
        RSA public key for the account administrator.
        
    - name: admin_user_type
      value: string
      description: >
        User type of the account administrator.
        
    - name: first_name
      value: string
      description: >
        First name of the account administrator.
        
    - name: last_name
      value: string
      description: >
        Last name of the account administrator.
        
    - name: email
      value: string
      description: >
        Email address of the account administrator.
        
    - name: must_change_password
      value: boolean
      description: >
        Indicates whether the account administrator must change the password at the next login.
        
      default: false
    - name: polaris
      value: boolean
      description: >
        Indicates whether the account is a Polaris account.
        
      default: false
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_account"
    values={[
        { label: 'delete_account', value: 'delete_account' }
    ]}
>
<TabItem value="delete_account">

Deletes the specified account. If you enable the `ifExists` parameter, the operation succeeds even if the account does not exist. Otherwise, a 404 failure is returned if the account does not exist. if the drop is unsuccessful.

```sql
DELETE FROM snowflake.account.accounts
WHERE name = '{{ name }}' --required
AND gracePeriodInDays = '{{ gracePeriodInDays }}' --required
AND endpoint = '{{ endpoint }}' --required
AND ifExists = '{{ ifExists }}';
```
</TabItem>
</Tabs>


## Lifecycle Methods

<Tabs
    defaultValue="undrop_account"
    values={[
        { label: 'undrop_account', value: 'undrop_account' }
    ]}
>
<TabItem value="undrop_account">

Restores a dropped account that has not yet been permanently deleted (a dropped account that is within its grace period).

```sql
EXEC snowflake.account.accounts.undrop_account 
@name='{{ name }}' --required, 
@endpoint='{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
