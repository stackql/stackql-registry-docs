---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
  - managed
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
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.managed.credentials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This Credential's unique ID.<br /> |
| `label` | `string` | The unique label for this Credential. This is for display purposes only.<br /> |
| `last_decrypted` | `string` | The date this Credential was last decrypted by a member of Linode special forces.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getManagedCredential` | `SELECT` | `credentialId` | Returns a single Managed Credential.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `getManagedCredentials` | `SELECT` |  | Returns a paginated list of Managed Credentials on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `createManagedCredential` | `INSERT` | `data__label, data__password` | Creates a Managed Credential. A Managed Credential is stored securely<br />to allow Linode special forces to access your Managed Services and resolve<br />issues.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `_getManagedCredential` | `EXEC` | `credentialId` | Returns a single Managed Credential.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `_getManagedCredentials` | `EXEC` |  | Returns a paginated list of Managed Credentials on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `_viewManagedSSHKey` | `EXEC` |  | Returns the unique SSH public key assigned to your Linode account's<br />Managed service. If you [add this public key](/docs/guides/linode-managed/#adding-the-public-key) to a Linode on your account,<br />Linode special forces will be able to log in to the Linode with this key<br />when attempting to resolve issues.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `deleteManagedCredential` | `EXEC` | `credentialId` | Deletes a Managed Credential.  Linode special forces will no longer<br />have access to this Credential when attempting to resolve issues.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `updateManagedCredential` | `EXEC` | `credentialId` | Updates the label of a Managed Credential. This endpoint does not update the username and password for a Managed Credential. To do this, use the Managed Credential Username and Password Update ([POST /managed/credentials/&#123;credentialId&#125;/update](/docs/api/managed/#managed-credential-username-and-password-update)) endpoint instead.<br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `updateManagedCredentialUsernamePassword` | `EXEC` | `credentialId, data__password` | Updates the username and password for a Managed Credential.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| `viewManagedSSHKey` | `EXEC` |  | Returns the unique SSH public key assigned to your Linode account's<br />Managed service. If you [add this public key](/docs/guides/linode-managed/#adding-the-public-key) to a Linode on your account,<br />Linode special forces will be able to log in to the Linode with this key<br />when attempting to resolve issues.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
