---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - user
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.user.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="activated" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="credentials" /> | `object` |
| <CopyableCode code="lastLogin" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="passwordChanged" /> | `string` |
| <CopyableCode code="profile" /> | `object` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="statusChanged" /> | `string` |
| <CopyableCode code="transitioningToStatus" /> | `string` |
| <CopyableCode code="type" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="userId, subdomain" /> | Fetches a user from your Okta organization. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subdomain" /> | Lists users in your organization with pagination in most cases.  A subset of users can be returned that match a supported filter expression or search criteria. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="subdomain" /> | Creates a new user in your Okta organization with or without credentials. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="userId, subdomain" /> | Deletes a user permanently.  This operation can only be performed on users that have a `DEPROVISIONED` status.  **This action cannot be recovered!** |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="sendEmail, userId, subdomain" /> | Activates a user.  This operation can only be performed on users with a `STAGED` status.  Activation of a user is an asynchronous operation. The user will have the `transitioningToStatus` property with a value of `ACTIVE` during activation to indicate that the user hasn't completed the asynchronous operation.  The user will have a status of `ACTIVE` when the activation process is complete. |
| <CopyableCode code="changePassword" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Changes a user's password by validating the user's current password. This operation can only be performed on users in `STAGED`, `ACTIVE`, `PASSWORD_EXPIRED`, or `RECOVERY` status that have a valid password credential |
| <CopyableCode code="changeRecoveryQuestion" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Changes a user's recovery question & answer credential by validating the user's current password.  This operation can only be performed on users in **STAGED**, **ACTIVE** or **RECOVERY** `status` that have a valid password credential |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Deactivates a user.  This operation can only be performed on users that do not have a `DEPROVISIONED` status.  Deactivation of a user is an asynchronous operation.  The user will have the `transitioningToStatus` property with a value of `DEPROVISIONED` during deactivation to indicate that the user hasn't completed the asynchronous operation.  The user will have a status of `DEPROVISIONED` when the deactivation process is complete. |
| <CopyableCode code="expirePassword" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | This operation transitions the user to the status of `PASSWORD_EXPIRED` so that the user is required to change their password at their next login. |
| <CopyableCode code="expirePasswordTemp" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | This operation transitions the user to the status of `PASSWORD_EXPIRED` and the user's password is reset to a temporary password that is returned. |
| <CopyableCode code="forgotPassword" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> |  |
| <CopyableCode code="reactivate" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Reactivates a user.  This operation can only be performed on users with a `PROVISIONED` status.  This operation restarts the activation workflow if for some reason the user activation was not completed when using the activationToken from [Activate User](#activate-user). |
| <CopyableCode code="resetFactors" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | This operation resets all factors for the specified user. All MFA factor enrollments returned to the unenrolled state. The user's status remains ACTIVE. This link is present only if the user is currently enrolled in one or more MFA factors. |
| <CopyableCode code="resetPassword" /> | `EXEC` | <CopyableCode code="sendEmail, userId, subdomain" /> | Generates a one-time token (OTT) that can be used to reset a user's password.  The OTT link can be automatically emailed to the user or returned to the API caller and distributed using a custom flow. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Suspends a user.  This operation can only be performed on users with an `ACTIVE` status.  The user will have a status of `SUSPENDED` when the process is complete. |
| <CopyableCode code="unlock" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Unlocks a user with a `LOCKED_OUT` status and returns them to `ACTIVE` status.  Users will be able to login with their current password. |
| <CopyableCode code="unsuspend" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Unsuspends a user and returns them to the `ACTIVE` state.  This operation can only be performed on users that have a `SUSPENDED` status. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="userId, subdomain" /> | Update a user's profile and/or credentials using strict-update semantics. |
