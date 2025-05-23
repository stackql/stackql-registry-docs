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

Creates, updates, deletes, gets or lists a <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.account.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="account_locator" /> | `string` | System-assigned identifier of the acccount. |
| <CopyableCode code="account_locator_url" /> | `string` | Legacy Snowflake account URL syntax that includes the region_name and account_locator. |
| <CopyableCode code="account_old_url_last_used" /> | `string` | If the original account URL was saved when the account was renamed, indicates the last time the account was accessed using the original URL. |
| <CopyableCode code="account_old_url_saved_on" /> | `string` | If the original account URL was saved when the account was renamed, provides the date and time when the original account URL was saved. |
| <CopyableCode code="account_url" /> | `string` | Preferred Snowflake account URL that includes the values of organization_name and account_name. |
| <CopyableCode code="admin_name" /> | `string` | Name of the account administrator. |
| <CopyableCode code="admin_password" /> | `string` | Password for the account administrator. |
| <CopyableCode code="admin_rsa_public_key" /> | `string` | RSA public key for the account administrator. |
| <CopyableCode code="admin_user_type" /> | `string` | User type of the account administrator. |
| <CopyableCode code="comment" /> | `string` | Optional comment in which to store information related to the account. |
| <CopyableCode code="consumption_billing_entity_name" /> | `string` | Name of the consumption billing entity. |
| <CopyableCode code="created_on" /> | `string` | Date and time the account was created. |
| <CopyableCode code="dropped_on" /> | `string` | Date and time the account was dropped. |
| <CopyableCode code="edition" /> | `string` | Snowflake Edition of the account. |
| <CopyableCode code="email" /> | `string` | Email address of the account administrator. |
| <CopyableCode code="first_name" /> | `string` | First name of the account administrator. |
| <CopyableCode code="is_events_account" /> | `boolean` | Indicates whether an account is an events account. For more information, see Set up logging and event sharing for an application. |
| <CopyableCode code="is_org_admin" /> | `boolean` | Indicates whether the ORGADMIN role is enabled in an account. If TRUE, the role is enabled. |
| <CopyableCode code="last_name" /> | `string` | Last name of the account administrator. |
| <CopyableCode code="managed_accounts" /> | `integer` | Indicates how many managed accounts have been created by the account. |
| <CopyableCode code="marketplace_consumer_billing_entity_name" /> | `string` | Name of the marketplace consumer billing entity. |
| <CopyableCode code="marketplace_provider_billing_entity_name" /> | `string` | Name of the marketplace provider billing entity. |
| <CopyableCode code="moved_on" /> | `string` | Date and time when the account was moved to a different organization. |
| <CopyableCode code="moved_to_organization" /> | `string` | If the account was moved to a different organization, provides the name of that organization. |
| <CopyableCode code="must_change_password" /> | `boolean` | Indicates whether the account administrator must change the password at the next login. |
| <CopyableCode code="old_account_url" /> | `string` | If the original account URL was saved when the account was renamed, provides the original URL. If the original account URL was dropped, the value is NULL even if the account was renamed |
| <CopyableCode code="organization_URL_expiration_on" /> | `string` | If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, provides the date and time when the original account URL will be dropped. Dropped URLs cannot be used to access the account. |
| <CopyableCode code="organization_name" /> | `string` | Name of the organization. |
| <CopyableCode code="organization_old_url" /> | `string` | If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, provides the original account URL. If the original account URL was dropped, the value is NULL even if the organization changed. |
| <CopyableCode code="organization_old_url_last_used" /> | `string` | If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, indicates the last time the account was accessed using the original account URL. |
| <CopyableCode code="organization_old_url_saved_on" /> | `string` | If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, provides the date and time when the original account URL was saved. |
| <CopyableCode code="polaris" /> | `boolean` | Indicates whether the account is a Polaris account. |
| <CopyableCode code="region" /> | `string` | Snowflake Region where the account is located. A Snowflake Region is a distinct location within a cloud platform region that is isolated from other Snowflake Regions. A Snowflake Region can be either multi-tenant or single-tenant (for a Virtual Private Snowflake account). |
| <CopyableCode code="region_group" /> | `string` | Region group where the account is located. Note - This column is only displayed for organizations that span multiple region groups. |
| <CopyableCode code="restored_on" /> | `string` | Date and time when the account was last restored. |
| <CopyableCode code="retention_time" /> | `integer` | Number of days that historical data is retained for Time Travel. |
| <CopyableCode code="scheduled_deletion_time" /> | `string` | Date and time when the account is scheduled to be permanently deleted. Accounts are deleted within one hour after the scheduled time. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_accounts" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" />, <CopyableCode code="showLimit" />, <CopyableCode code="history" /> | Lists the accessible accounts. |
| <CopyableCode code="create_account" /> | `INSERT` | <CopyableCode code="data__admin_name, data__edition, data__email, data__name, endpoint" /> | - | Creates a account. You must provide the full account definition when creating a account. |
| <CopyableCode code="delete_account" /> | `DELETE` | <CopyableCode code="gracePeriodInDays, name, endpoint" /> | <CopyableCode code="ifExists" /> | Deletes the specified account. If you enable the `ifExists` parameter, the operation succeeds even if the account does not exist. Otherwise, a 404 failure is returned if the account does not exist. if the drop is unsuccessful. |
| <CopyableCode code="undrop_account" /> | `EXEC` | <CopyableCode code="name, endpoint" /> | - | Restores a dropped account that has not yet been permanently deleted (a dropped account that is within its grace period). |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="history" /> | Optionally includes dropped accounts that have not yet been purged. | `boolean` | `-` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |

</details>

## `SELECT` examples

Lists the accessible accounts.


```sql
SELECT
name,
account_locator,
account_locator_url,
account_old_url_last_used,
account_old_url_saved_on,
account_url,
admin_name,
admin_password,
admin_rsa_public_key,
admin_user_type,
comment,
consumption_billing_entity_name,
created_on,
dropped_on,
edition,
email,
first_name,
is_events_account,
is_org_admin,
last_name,
managed_accounts,
marketplace_consumer_billing_entity_name,
marketplace_provider_billing_entity_name,
moved_on,
moved_to_organization,
must_change_password,
old_account_url,
organization_URL_expiration_on,
organization_name,
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
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>accounts</code> resource.

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
'{{ must_change_password }}',
'{{ polaris }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.account.accounts (
data__name,
data__admin_name,
data__email,
data__edition,
endpoint
)
SELECT 
'{{ name }}',
'{{ admin_name }}',
'{{ email }}',
'{{ edition }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: accounts
  props:
    - name: data__admin_name
      value: string
    - name: data__edition
      value: string
    - name: data__email
      value: string
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
      description: >-
        A Snowflake object identifier. If the identifier contains spaces or
        special characters, the entire string must be enclosed in double quotes.
        Identifiers enclosed in double quotes are also case-sensitive.
    - name: region_group
      value: string
      description: >-
        Region group where the account is located. Note - This column is only
        displayed for organizations that span multiple region groups.
    - name: region
      value: string
      description: >-
        Snowflake Region where the account is located. A Snowflake Region is a
        distinct location within a cloud platform region that is isolated from
        other Snowflake Regions. A Snowflake Region can be either multi-tenant
        or single-tenant (for a Virtual Private Snowflake account).
    - name: edition
      value: string
      description: Snowflake Edition of the account.
    - name: comment
      value: string
      description: Optional comment in which to store information related to the account.
    - name: admin_name
      value: string
      description: Name of the account administrator.
    - name: admin_password
      value: string
      description: Password for the account administrator.
    - name: admin_rsa_public_key
      value: string
      description: RSA public key for the account administrator.
    - name: admin_user_type
      value: string
      description: User type of the account administrator.
    - name: first_name
      value: string
      description: First name of the account administrator.
    - name: last_name
      value: string
      description: Last name of the account administrator.
    - name: email
      value: string
      description: Email address of the account administrator.
    - name: must_change_password
      value: boolean
      description: >-
        Indicates whether the account administrator must change the password at
        the next login.
    - name: polaris
      value: boolean
      description: Indicates whether the account is a Polaris account.
```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>accounts</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.account.accounts
WHERE gracePeriodInDays = '{{ gracePeriodInDays }}'
AND name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
