---
title: logins
hide_title: false
hide_table_of_contents: false
keywords:
  - logins
  - account
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.account.logins</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique ID of this login object.<br /> |
| `ip` | `string` | The remote IP address that requested the login.<br /> |
| `restricted` | `boolean` | True if the User that attempted the login was a restricted User, false otherwise.<br /> |
| `status` | `string` | Whether the login attempt succeeded or failed.<br /> |
| `username` | `string` | The username of the User that attempted the login.<br /> |
| `datetime` | `string` | When the login was initiated.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getAccountLogin` | `SELECT` | `loginId` | Returns a Login object that displays information about a successful login. The logins that can be viewed can be for any user on the account, and are not limited to only the logins of the user that is accessing this API endpoint. This command can only be accessed by the unrestricted users of the account.<br /> |
| `getAccountLogins` | `SELECT` |  | Returns a collection of successful logins for all users on the account during the last 90 days. This command can only be accessed by the unrestricted users of an account.<br /> |
| `_getAccountLogin` | `EXEC` | `loginId` | Returns a Login object that displays information about a successful login. The logins that can be viewed can be for any user on the account, and are not limited to only the logins of the user that is accessing this API endpoint. This command can only be accessed by the unrestricted users of the account.<br /> |
| `_getAccountLogins` | `EXEC` |  | Returns a collection of successful logins for all users on the account during the last 90 days. This command can only be accessed by the unrestricted users of an account.<br /> |
