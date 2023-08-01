---
title: logins
hide_title: false
hide_table_of_contents: false
keywords:
  - logins
  - profile
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
<tr><td><b>Id</b></td><td><code>linode.profile.logins</code></td></tr>
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
| `getProfileLogin` | `SELECT` | `loginId` | Returns a login object displaying information about a successful account login from this user.<br /> |
| `getProfileLogins` | `SELECT` |  | Returns a collection of successful account logins from this user during the last 90 days.<br /> |
| `_getProfileLogin` | `EXEC` | `loginId` | Returns a login object displaying information about a successful account login from this user.<br /> |
| `_getProfileLogins` | `EXEC` |  | Returns a collection of successful account logins from this user during the last 90 days.<br /> |
