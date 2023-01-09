---
title: user_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - user_permissions
  - tagmanager
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.user_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accountId` | `string` | The Account ID uniquely identifies the GTM Account. |
| `containerAccess` | `array` | GTM Container access permissions. @mutable tagmanager.accounts.permissions.create @mutable tagmanager.accounts.permissions.update |
| `emailAddress` | `string` | User's email address. @mutable tagmanager.accounts.permissions.create |
| `path` | `string` | GTM UserPermission's API relative path. |
| `accountAccess` | `object` | Defines the Google Tag Manager Account access permissions. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_user_permissions_get` | `SELECT` | `accountsId, user_permissionsId` | Gets a user's Account & Container access. |
| `accounts_user_permissions_list` | `SELECT` | `accountsId` | List all users that have access to the account along with Account and Container user access granted to each of them. |
| `accounts_user_permissions_create` | `INSERT` | `accountsId` | Creates a user's Account & Container access. |
| `accounts_user_permissions_delete` | `DELETE` | `accountsId, user_permissionsId` | Removes a user from the account, revoking access to it and all of its containers. |
| `accounts_user_permissions_update` | `EXEC` | `accountsId, user_permissionsId` | Updates a user's Account & Container access. |
