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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.profile.logins" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The unique ID of this login object.<br /> |
| <CopyableCode code="datetime" /> | `string` | When the login was initiated.<br /> |
| <CopyableCode code="ip" /> | `string` | The remote IP address that requested the login.<br /> |
| <CopyableCode code="restricted" /> | `boolean` | True if the User that attempted the login was a restricted User, false otherwise.<br /> |
| <CopyableCode code="status" /> | `string` | Whether the login attempt succeeded or failed.<br /> |
| <CopyableCode code="username" /> | `string` | The username of the User that attempted the login.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getProfileLogin" /> | `SELECT` | <CopyableCode code="loginId" /> | Returns a login object displaying information about a successful account login from this user.<br /> |
| <CopyableCode code="getProfileLogins" /> | `SELECT` |  | Returns a collection of successful account logins from this user during the last 90 days.<br /> |
| <CopyableCode code="_getProfileLogin" /> | `EXEC` | <CopyableCode code="loginId" /> | Returns a login object displaying information about a successful account login from this user.<br /> |
| <CopyableCode code="_getProfileLogins" /> | `EXEC` |  | Returns a collection of successful account logins from this user during the last 90 days.<br /> |
