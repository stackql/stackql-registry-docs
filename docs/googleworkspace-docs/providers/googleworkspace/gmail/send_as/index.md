---
title: send_as
hide_title: false
hide_table_of_contents: false
keywords:
  - send_as
  - gmail
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>send_as</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.send_as</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `isDefault` | `boolean` | Whether this address is selected as the default "From:" address in situations such as composing a new message or sending a vacation auto-reply. Every Gmail account has exactly one default send-as address, so the only legal value that clients may write to this field is `true`. Changing this from `false` to `true` for an address will result in this field becoming `false` for the other previous default address. |
| `isPrimary` | `boolean` | Whether this address is the primary address used to login to the account. Every Gmail account has exactly one primary address, and it cannot be deleted from the collection of send-as aliases. This field is read-only. |
| `sendAsEmail` | `string` | The email address that appears in the "From:" header for mail sent using this alias. This is read-only for all operations except create. |
| `replyToAddress` | `string` | An optional email address that is included in a "Reply-To:" header for mail sent using this alias. If this is empty, Gmail will not generate a "Reply-To:" header. |
| `displayName` | `string` | A name that appears in the "From:" header for mail sent using this alias. For custom "from" addresses, when this is empty, Gmail will populate the "From:" header with the name that is used for the primary address associated with the account. If the admin has disabled the ability for users to update their name format, requests to update this field for the primary login will silently fail. |
| `signature` | `string` | An optional HTML signature that is included in messages composed with this alias in the Gmail web UI. This signature is added to new emails only. |
| `smtpMsa` | `object` | Configuration for communication with an SMTP service. |
| `treatAsAlias` | `boolean` | Whether Gmail should treat this address as an alias for the user's primary email address. This setting only applies to custom "from" aliases. |
| `verificationStatus` | `string` | Indicates whether this address has been verified for use as a send-as alias. Read-only. This setting only applies to custom "from" aliases. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_settings_sendAs_get` | `SELECT` | `sendAsEmail, userId` | Gets the specified send-as alias. Fails with an HTTP 404 error if the specified address is not a member of the collection. |
| `users_settings_sendAs_list` | `SELECT` | `userId` | Lists the send-as aliases for the specified account. The result includes the primary send-as address associated with the account as well as any custom "from" aliases. |
| `users_settings_sendAs_create` | `INSERT` | `userId` | Creates a custom "from" send-as alias. If an SMTP MSA is specified, Gmail will attempt to connect to the SMTP service to validate the configuration before creating the alias. If ownership verification is required for the alias, a message will be sent to the email address and the resource's verification status will be set to `pending`; otherwise, the resource will be created with verification status set to `accepted`. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias. This method is only available to service account clients that have been delegated domain-wide authority. |
| `users_settings_sendAs_delete` | `DELETE` | `sendAsEmail, userId` | Deletes the specified send-as alias. Revokes any verification that may have been required for using it. This method is only available to service account clients that have been delegated domain-wide authority. |
| `users_settings_sendAs_patch` | `EXEC` | `sendAsEmail, userId` | Patch the specified send-as alias. |
| `users_settings_sendAs_update` | `EXEC` | `sendAsEmail, userId` | Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias. Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority. |
| `users_settings_sendAs_verify` | `EXEC` | `sendAsEmail, userId` | Sends a verification email to the specified send-as alias address. The verification status must be `pending`. This method is only available to service account clients that have been delegated domain-wide authority. |
