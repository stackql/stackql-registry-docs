---
title: managed_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_accounts
  - managed_account
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

Creates, updates, deletes, gets or lists a <code>managed_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.managed_account.managed_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive. |
| <CopyableCode code="account_locator_url" /> | `string` | Account URL that is used to connect to the account, in the legacy account locator format. |
| <CopyableCode code="account_type" /> | `string` | Type of the account. |
| <CopyableCode code="admin_name" /> | `string` | Name of the account administrator. |
| <CopyableCode code="admin_password" /> | `string` | Password for the account administrator. |
| <CopyableCode code="cloud" /> | `string` | Cloud in which the managed account is located. For reader accounts, this is always the same as the cloud for the provider account. |
| <CopyableCode code="comment" /> | `string` | Optional comment in which to store information related to the account. |
| <CopyableCode code="created_on" /> | `string` | Date and time the account was created. |
| <CopyableCode code="locator" /> | `string` | Legacy identifier for the account. |
| <CopyableCode code="region" /> | `string` | Region in which the managed account is located. For reader accounts, this is always the same as the region for the provider account. |
| <CopyableCode code="url" /> | `string` | Account URL that is used to connect to the account, in the account name format. The account identifier in this format follows the pattern {orgname}-{account_name}. |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_managed_accounts" /> | `SELECT` | <CopyableCode code="endpoint" /> | <CopyableCode code="like" /> | Lists the accessible managed accounts. |
| <CopyableCode code="create_managed_account" /> | `INSERT` | <CopyableCode code="data__account_type, data__admin_name, data__admin_password, data__name, endpoint" /> | - | Creates a managed account. You must provide the full managed account definition when creating a managed account. |
| <CopyableCode code="delete_managed_account" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | - | Removes a managed account, including all objects created in the account, and immediately restricts access to the account. Currently used by data providers to create reader accounts for their consumers. For more details, see Manage reader accounts. |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="like" /> | Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. | `string` | `-` |

</details>

## `SELECT` examples

Lists the accessible managed accounts.


```sql
SELECT
name,
account_locator_url,
account_type,
admin_name,
admin_password,
cloud,
comment,
created_on,
locator,
region,
url
FROM snowflake.managed_account.managed_accounts
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_accounts</code> resource.

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
INSERT INTO snowflake.managed_account.managed_accounts (
data__name,
data__comment,
data__admin_name,
data__admin_password,
data__account_type,
endpoint
)
SELECT 
'{{ name }}',
'{{ comment }}',
'{{ admin_name }}',
'{{ admin_password }}',
'{{ account_type }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.managed_account.managed_accounts (
data__name,
data__admin_name,
data__admin_password,
data__account_type,
endpoint
)
SELECT 
'{{ name }}',
'{{ admin_name }}',
'{{ admin_password }}',
'{{ account_type }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: managed_accounts
  props:
    - name: data__account_type
      value: string
    - name: data__admin_name
      value: string
    - name: data__admin_password
      value: string
    - name: data__name
      value: string
    - name: endpoint
      value: string
    - name: name
      value: string
      description: A Snowflake object identifier. If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.
    - name: comment
      value: string
      description: Optional comment in which to store information related to the account.
    - name: admin_name
      value: string
      description: Name of the account administrator.
    - name: admin_password
      value: string
      description: Password for the account administrator.
    - name: account_type
      value: string
      description: Type of the account.

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>managed_accounts</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.managed_account.managed_accounts
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
