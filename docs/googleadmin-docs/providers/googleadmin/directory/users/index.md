---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID for the user. A user `id` can be used as a user request URI's `userKey`. |
| `name` | `object` |  |
| `posixAccounts` | `any` | The list of [POSIX](https://www.opengroup.org/austin/papers/posix_faq.html) account information for the user. |
| `isDelegatedAdmin` | `boolean` | Output only. Indicates if the user is a delegated administrator. Delegated administrators are supported by the API but cannot create or undelete users, or make users administrators. These requests are ignored by the API service. Roles and privileges for administrators are assigned using the [Admin console](https://support.google.com/a/answer/33325). |
| `kind` | `string` | Output only. The type of the API resource. For Users resources, the value is `admin#directory#user`. |
| `changePasswordAtNextLogin` | `boolean` | Indicates if the user is forced to change their password at next login. This setting doesn't apply when [the user signs in via a third-party identity provider](https://support.google.com/a/answer/60224). |
| `addresses` | `any` | The list of the user's addresses. The maximum allowed data size for this field is 10KB. |
| `notes` | `any` | Notes for the user. |
| `suspended` | `boolean` | Indicates if user is suspended. |
| `creationTime` | `string` | User's G Suite account creation time. (Read-only) |
| `isEnforcedIn2Sv` | `boolean` | Output only. Is 2-step verification enforced (Read-only) |
| `agreedToTerms` | `boolean` | Output only. This property is `true` if the user has completed an initial login and accepted the Terms of Service agreement. |
| `password` | `string` | User's password |
| `ims` | `any` | The list of the user's Instant Messenger (IM) accounts. A user account can have multiple ims properties. But, only one of these ims properties can be the primary IM contact. The maximum allowed data size for this field is 2KB. |
| `phones` | `any` | The list of the user's phone numbers. The maximum allowed data size for this field is 1KB. |
| `hashFunction` | `string` | Stores the hash format of the `password` property. The following `hashFunction` values are allowed: * `MD5` - Accepts simple hex-encoded values. * `SHA-1` - Accepts simple hex-encoded values. * `crypt` - Compliant with the [C crypt library](https://en.wikipedia.org/wiki/Crypt_%28C%29). Supports the DES, MD5 (hash prefix `$1$`), SHA-256 (hash prefix `$5$`), and SHA-512 (hash prefix `$6$`) hash algorithms. If rounds are specified as part of the prefix, they must be 10,000 or fewer. |
| `isEnrolledIn2Sv` | `boolean` | Output only. Is enrolled in 2-step verification (Read-only) |
| `languages` | `any` | The user's languages. The maximum allowed data size for this field is 1KB. |
| `recoveryEmail` | `string` | Recovery email of the user. |
| `orgUnitPath` | `string` | The full path of the parent organization associated with the user. If the parent organization is the top-level, it is represented as a forward slash (`/`). |
| `thumbnailPhotoUrl` | `string` | Output only. The URL of the user's profile photo. The URL might be temporary or private. |
| `lastLoginTime` | `string` | User's last login time. (Read-only) |
| `suspensionReason` | `string` | Output only. Has the reason a user account is suspended either by the administrator or by Google at the time of suspension. The property is returned only if the `suspended` property is `true`. |
| `locations` | `any` | The user's locations. The maximum allowed data size for this field is 10KB. |
| `organizations` | `any` | The list of organizations the user belongs to. The maximum allowed data size for this field is 10KB. |
| `emails` | `any` | The list of the user's email addresses. The maximum allowed data size for this field is 10KB. |
| `thumbnailPhotoEtag` | `string` | Output only. ETag of the user's photo (Read-only) |
| `etag` | `string` | Output only. ETag of the resource. |
| `customerId` | `string` | Output only. The customer ID to [retrieve all account users](/admin-sdk/directory/v1/guides/manage-users.html#get_all_users). You can use the alias `my_customer` to represent your account's `customerId`. As a reseller administrator, you can use the resold customer account's `customerId`. To get a `customerId`, use the account's primary domain in the `domain` parameter of a [users.list](/admin-sdk/directory/v1/reference/users/list) request. |
| `isMailboxSetup` | `boolean` | Output only. Indicates if the user's Google mailbox is created. This property is only applicable if the user has been assigned a Gmail license. |
| `primaryEmail` | `string` | The user's primary email address. This property is required in a request to create a user account. The `primaryEmail` must be unique and cannot be an alias of another user. |
| `gender` | `any` | The user's gender. The maximum allowed data size for this field is 1KB. |
| `deletionTime` | `string` |  |
| `archived` | `boolean` | Indicates if user is archived. |
| `externalIds` | `any` | The list of external IDs for the user, such as an employee or network ID. The maximum allowed data size for this field is 2KB. |
| `relations` | `any` | The list of the user's relationships to other users. The maximum allowed data size for this field is 2KB. |
| `customSchemas` | `object` | Custom fields of the user. The key is a `schema_name` and its values are `'field_name': 'field_value'`. |
| `keywords` | `any` | The list of the user's keywords. The maximum allowed data size for this field is 1KB. |
| `includeInGlobalAddressList` | `boolean` | Indicates if the user's profile is visible in the Google Workspace global address list when the contact sharing feature is enabled for the domain. For more information about excluding user profiles, see the [administration help center](https://support.google.com/a/answer/1285988). |
| `websites` | `any` | The user's websites. The maximum allowed data size for this field is 2KB. |
| `aliases` | `array` | Output only. The list of the user's alias email addresses. |
| `sshPublicKeys` | `any` | A list of SSH public keys. |
| `isAdmin` | `boolean` | Output only. Indicates a user with super admininistrator privileges. The `isAdmin` property can only be edited in the [Make a user an administrator](/admin-sdk/directory/v1/guides/manage-users.html#make_admin) operation ( [makeAdmin](/admin-sdk/directory/v1/reference/users/makeAdmin.html) method). If edited in the user [insert](/admin-sdk/directory/v1/reference/users/insert.html) or [update](/admin-sdk/directory/v1/reference/users/update.html) methods, the edit is ignored by the API service. |
| `recoveryPhone` | `string` | Recovery phone of the user. The phone number must be in the E.164 format, starting with the plus sign (+). Example: *+16506661212*. |
| `nonEditableAliases` | `array` | Output only. The list of the user's non-editable alias email addresses. These are typically outside the account's primary domain or sub-domain. |
| `ipWhitelisted` | `boolean` | If `true`, the user's IP address is subject to a deprecated IP address [`allowlist`](https://support.google.com/a/answer/60752) configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `userKey` | Retrieves a user. |
| `list` | `SELECT` | `domain` | Retrieves a paginated list of either deleted users or all users in a domain. |
| `insert` | `INSERT` |  | Creates a user. Mutate calls immediately following user creation might sometimes fail as the user isn't fully created due to propagation delay in our backends. Check the error details for the "User creation is not complete" message to see if this is the case. Retrying the calls after some time can help in this case. |
| `delete` | `DELETE` | `userKey` | Deletes a user. |
| `_list` | `EXEC` | `domain` | Retrieves a paginated list of either deleted users or all users in a domain. |
| `makeAdmin` | `EXEC` | `userKey` | Makes a user a super administrator. |
| `patch` | `EXEC` | `userKey` | Updates a user using patch semantics. The update method should be used instead, because it also supports patch semantics and has better performance. If you're mapping an external identity to a Google identity, use the [`update`](https://developers.google.com/admin-sdk/directory/v1/reference/users/update) method instead of the `patch` method. This method is unable to clear fields that contain repeated objects (`addresses`, `phones`, etc). Use the update method instead. |
| `signOut` | `EXEC` | `userKey` | Signs a user out of all web and device sessions and reset their sign-in cookies. User will have to sign in by authenticating again. |
| `undelete` | `EXEC` | `userKey` | Undeletes a deleted user. |
| `update` | `EXEC` | `userKey` | Updates a user. This method supports patch semantics, meaning that you only need to include the fields you wish to update. Fields that are not present in the request will be preserved, and fields set to `null` will be cleared. For repeating fields that contain arrays, individual items in the array can't be patched piecemeal; they must be supplied in the request body with the desired values for all items. See the [user accounts guide](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users#update_user) for more information. |
| `watch` | `EXEC` |  | Watches for changes in users list. |
