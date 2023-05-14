---
title: sshkeys
hide_title: false
hide_table_of_contents: false
keywords:
  - sshkeys
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
<tr><td><b>Name</b></td><td><code>sshkeys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.profile.sshkeys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique identifier of an SSH Key object.<br /> |
| `created` | `string` | The date this key was added.<br /> |
| `label` | `string` | A label for the SSH Key.<br /> |
| `ssh_key` | `string` | The public SSH Key, which is used to authenticate to the root user of the Linodes you deploy.<br /><br />Accepted formats:<br />* ssh-dss<br />* ssh-rsa<br />* ecdsa-sha2-nistp<br />* ssh-ed25519<br />* sk-ecdsa-sha2-nistp256 (Akamai-specific)<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getSSHKey` | `SELECT` | `sshKeyId` | Returns a single SSH Key object identified by `id` that you have access to view.<br /> |
| `getSSHKeys` | `SELECT` |  | Returns a collection of SSH Keys you've added to your Profile.<br /> |
| `addSSHKey` | `INSERT` |  | Adds an SSH Key to your Account profile.<br /> |
| `deleteSSHKey` | `DELETE` | `sshKeyId` | Deletes an SSH Key you have access to.<br /><br />**Note:** deleting an SSH Key will *not* remove it from any Linode or Disk that was deployed with `authorized_keys`. In those cases, the keys must be manually deleted on the Linode or Disk. This endpoint will only delete the key's association from your Profile.<br /> |
| `_getSSHKey` | `EXEC` | `sshKeyId` | Returns a single SSH Key object identified by `id` that you have access to view.<br /> |
| `_getSSHKeys` | `EXEC` |  | Returns a collection of SSH Keys you've added to your Profile.<br /> |
| `updateSSHKey` | `EXEC` | `sshKeyId` | Updates an SSH Key that you have permission to `read_write`.<br /><br />Only SSH key labels can be updated.<br /> |
