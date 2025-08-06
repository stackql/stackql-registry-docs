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

The following fields are returned by `SELECT` queries:

<Tabs
    defaultValue="list_managed_accounts"
    values={[
        { label: 'list_managed_accounts', value: 'list_managed_accounts' }
    ]}
>
<TabItem value="list_managed_accounts">

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
    <td><CopyableCode code="account_locator_url" /></td>
    <td><code>string</code></td>
    <td>Account URL that is used to connect to the account, in the legacy account locator format.</td>
</tr>
<tr>
    <td><CopyableCode code="account_type" /></td>
    <td><code>string</code></td>
    <td>Type of the account. (default: READER)</td>
</tr>
<tr>
    <td><CopyableCode code="admin_password" /></td>
    <td><code>string (password)</code></td>
    <td>Password for the account administrator.</td>
</tr>
<tr>
    <td><CopyableCode code="cloud" /></td>
    <td><code>string</code></td>
    <td>Cloud in which the managed account is located. For reader accounts, this is always the same as the cloud for the provider account.</td>
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
    <td><CopyableCode code="locator" /></td>
    <td><code>string</code></td>
    <td>Legacy identifier for the account.</td>
</tr>
<tr>
    <td><CopyableCode code="region" /></td>
    <td><code>string</code></td>
    <td>Region in which the managed account is located. For reader accounts, this is always the same as the region for the provider account.</td>
</tr>
<tr>
    <td><CopyableCode code="url" /></td>
    <td><code>string</code></td>
    <td>Account URL that is used to connect to the account, in the account name format. The account identifier in this format follows the pattern &lt;orgname&gt;-&lt;account_name&gt;.</td>
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
    <td><a href="#list_managed_accounts"><CopyableCode code="list_managed_accounts" /></a></td>
    <td><CopyableCode code="select" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td><a href="#parameter-like">like</a></td>
    <td>Lists the accessible managed accounts.</td>
</tr>
<tr>
    <td><a href="#create_managed_account"><CopyableCode code="create_managed_account" /></a></td>
    <td><CopyableCode code="insert" /></td>
    <td><a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Creates a managed account. You must provide the full managed account definition when creating a managed account.</td>
</tr>
<tr>
    <td><a href="#delete_managed_account"><CopyableCode code="delete_managed_account" /></a></td>
    <td><CopyableCode code="delete" /></td>
    <td><a href="#parameter-name">name</a>, <a href="#parameter-endpoint">endpoint</a></td>
    <td></td>
    <td>Removes a managed account, including all objects created in the account, and immediately restricts access to the account. Currently used by data providers to create reader accounts for their consumers. For more details, see Manage reader accounts.</td>
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
<tr id="parameter-name">
    <td><CopyableCode code="name" /></td>
    <td><code>string</code></td>
    <td>Identifier (i.e. name) for the resource. (pattern: ^"([^"]|"")+"|[a-zA-Z_][a-zA-Z0-9_$]*$, example: TEST_NAME)</td>
</tr>
<tr id="parameter-like">
    <td><CopyableCode code="like" /></td>
    <td><code>string</code></td>
    <td>Query parameter to filter the command output by resource name. Uses case-insensitive pattern matching, with support for SQL wildcard characters. (example: test_%)</td>
</tr>
</tbody>
</table>

## `SELECT` examples

<Tabs
    defaultValue="list_managed_accounts"
    values={[
        { label: 'list_managed_accounts', value: 'list_managed_accounts' }
    ]}
>
<TabItem value="list_managed_accounts">

Lists the accessible managed accounts.

```sql
SELECT
name,
admin_name,
account_locator_url,
account_type,
admin_password,
cloud,
comment,
created_on,
locator,
region,
url
FROM snowflake.managed_account.managed_accounts
WHERE endpoint = '{{ endpoint }}' -- required
AND like = '{{ like }}';
```
</TabItem>
</Tabs>


## `INSERT` examples

<Tabs
    defaultValue="create_managed_account"
    values={[
        { label: 'create_managed_account', value: 'create_managed_account' },
        { label: 'Manifest', value: 'manifest' }
    ]}
>
<TabItem value="create_managed_account">

Creates a managed account. You must provide the full managed account definition when creating a managed account.

```sql
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
<TabItem value="manifest">

```yaml
# Description fields are for documentation purposes
- name: managed_accounts
  props:
    - name: endpoint
      value: string
      description: Required parameter for the managed_accounts resource.
    - name: name
      value: string
      description: >
        A Snowflake object identifier. If the identifier contains spaces or special characters,  the entire string must be enclosed in double quotes.  Identifiers enclosed in double quotes are also case-sensitive.

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
        
    - name: account_type
      value: string
      description: >
        Type of the account.
        
      valid_values: ['READER']
      default: READER
```
</TabItem>
</Tabs>


## `DELETE` examples

<Tabs
    defaultValue="delete_managed_account"
    values={[
        { label: 'delete_managed_account', value: 'delete_managed_account' }
    ]}
>
<TabItem value="delete_managed_account">

Removes a managed account, including all objects created in the account, and immediately restricts access to the account. Currently used by data providers to create reader accounts for their consumers. For more details, see Manage reader accounts.

```sql
DELETE FROM snowflake.managed_account.managed_accounts
WHERE name = '{{ name }}' --required
AND endpoint = '{{ endpoint }}' --required;
```
</TabItem>
</Tabs>
