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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.logins" /></td></tr>
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
| <CopyableCode code="getAccountLogin" /> | `SELECT` | <CopyableCode code="loginId" /> | Returns a Login object that displays information about a successful login. The logins that can be viewed can be for any user on the account, and are not limited to only the logins of the user that is accessing this API endpoint. This command can only be accessed by the unrestricted users of the account.<br /> |
| <CopyableCode code="getAccountLogins" /> | `SELECT` |  | Returns a collection of successful logins for all users on the account during the last 90 days. This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getAccountLogin" /> | `EXEC` | <CopyableCode code="loginId" /> | Returns a Login object that displays information about a successful login. The logins that can be viewed can be for any user on the account, and are not limited to only the logins of the user that is accessing this API endpoint. This command can only be accessed by the unrestricted users of the account.<br /> |
| <CopyableCode code="_getAccountLogins" /> | `EXEC` |  | Returns a collection of successful logins for all users on the account during the last 90 days. This command can only be accessed by the unrestricted users of an account.<br /> |
