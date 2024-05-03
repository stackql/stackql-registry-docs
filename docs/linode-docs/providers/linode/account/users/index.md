---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.account.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="email" /> | `string` | The email address for the User. Linode sends emails to this address for account management communications. May be used for other communications as configured.<br /> |
| <CopyableCode code="restricted" /> | `boolean` | If true, the User must be granted access to perform actions or access entities on this Account. See User Grants View ([GET /account/users/&#123;username&#125;/grants](/docs/api/account/#users-grants-view)) for details on how to configure grants for a restricted User.<br /> |
| <CopyableCode code="ssh_keys" /> | `array` | A list of SSH Key labels added by this User.<br /><br />Users can add keys with the SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) command.<br /><br />These keys are deployed when this User is included in the `authorized_users`<br />field of the following requests:<br />- Linode Create ([POST /linode/instances](/docs/api/linode-instances/#linode-create))<br />- Linode Rebuild ([POST /linode/instances/&#123;linodeId&#125;/rebuild](/docs/api/linode-instances/#linode-rebuild))<br />- Disk Create ([POST /linode/instances/&#123;linodeId&#125;/disks](/docs/api/linode-instances/#disk-create))<br /> |
| <CopyableCode code="tfa_enabled" /> | `boolean` | A boolean value indicating if the User has Two Factor Authentication (TFA) enabled. See the Create Two Factor Secret ([POST /profile/tfa-enable](/docs/api/profile/#two-factor-secret-create)) endpoint to enable TFA.<br /> |
| <CopyableCode code="username" /> | `string` | The User's username. This is used for logging in, and may also be displayed alongside actions the User performs (for example, in Events or public StackScripts).<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getUser" /> | `SELECT` | <CopyableCode code="username" /> | Returns information about a single User on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="getUsers" /> | `SELECT` |  | Returns a paginated list of Users on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /><br />Users may access all or part of your Account based on their restricted status and grants.  An unrestricted User may access everything on the account, whereas restricted User may only access entities or perform actions they've been given specific grants to.<br /> |
| <CopyableCode code="createUser" /> | `INSERT` | <CopyableCode code="data__email, data__username" /> | Creates a User on your Account. Once created, a confirmation message containing<br />password creation and login instructions is sent to the User's email address.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /><br />The User's account access is determined by whether or not they are restricted,<br />and what grants they have been given.<br /> |
| <CopyableCode code="deleteUser" /> | `DELETE` | <CopyableCode code="username" /> | Deletes a User. The deleted User will be immediately logged out and<br />may no longer log in or perform any actions. All of the User's Grants<br />will be removed.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getUser" /> | `EXEC` | <CopyableCode code="username" /> | Returns information about a single User on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getUserGrants" /> | `EXEC` | <CopyableCode code="username" /> | Returns the full grants structure for the specified account User<br />(other than the account owner, see below for details). This includes all entities<br />on the Account alongside the level of access this User has to each of them.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /><br />The current authenticated User, including the account owner, may view their<br />own grants at the [/profile/grants](/docs/api/profile/#grants-list)<br />endpoint, but will not see entities that they do not have access to.<br /> |
| <CopyableCode code="_getUsers" /> | `EXEC` |  | Returns a paginated list of Users on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /><br />Users may access all or part of your Account based on their restricted status and grants.  An unrestricted User may access everything on the account, whereas restricted User may only access entities or perform actions they've been given specific grants to.<br /> |
| <CopyableCode code="getUserGrants" /> | `EXEC` | <CopyableCode code="username" /> | Returns the full grants structure for the specified account User<br />(other than the account owner, see below for details). This includes all entities<br />on the Account alongside the level of access this User has to each of them.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /><br />The current authenticated User, including the account owner, may view their<br />own grants at the [/profile/grants](/docs/api/profile/#grants-list)<br />endpoint, but will not see entities that they do not have access to.<br /> |
| <CopyableCode code="updateUser" /> | `EXEC` | <CopyableCode code="username" /> | Update information about a User on your Account. This can be used to<br />change the restricted status of a User. When making a User restricted,<br />no grants will be configured by default and you must then set up grants<br />in order for the User to access anything on the Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="updateUserGrants" /> | `EXEC` | <CopyableCode code="username" /> | Update the grants a User has. This can be used to give a User access<br />to new entities or actions, or take access away.  You do not need to<br />include the grant for every entity on the Account in this request; any<br />that are not included will remain unchanged.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
