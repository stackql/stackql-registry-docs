---
title: identities
hide_title: false
hide_table_of_contents: false
keywords:
  - identities
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
<tr><td><b>Name</b></td><td><code>identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmail.identities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `emailAddress` | `string` | The email address for the sending identity. The email address must be the primary email address of the authenticated user. |
| `primaryKeyPairId` | `string` | If a key pair is associated, the identifier of the key pair, CseKeyPair. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_settings_cse_identities_get` | `SELECT` | `cseEmailAddress, userId` | Retrieves a client-side encryption identity configuration. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_identities_list` | `SELECT` | `userId` | Lists the client-side encrypted identities for an authenticated user. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_identities_create` | `INSERT` | `userId` | Creates and configures a client-side encryption identity that's authorized to send mail from the user account. Google publishes the S/MIME certificate to a shared domain-wide directory so that people within a Google Workspace organization can encrypt and send mail to the identity. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_identities_delete` | `DELETE` | `cseEmailAddress, userId` | Deletes a client-side encryption identity. The authenticated user can no longer use the identity to send encrypted messages. You cannot restore the identity after you delete it. Instead, use the CreateCseIdentity method to create another identity with the same configuration. [Beta](https://workspace.google.com/terms/service-terms/index.html). |
| `users_settings_cse_identities_patch` | `EXEC` | `emailAddress, userId` | Associates a different key pair with an existing client-side encryption identity. The updated key pair must validate against Google's [S/MIME certificate profiles](https://support.google.com/a/answer/7300887). [Beta](https://workspace.google.com/terms/service-terms/index.html). |
