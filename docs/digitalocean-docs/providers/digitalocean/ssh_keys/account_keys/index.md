---
title: account_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - account_keys
  - ssh_keys
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.ssh_keys.account_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique identification number for this key. Can be used to embed a  specific SSH key into a Droplet. |
| `name` | `string` | A human-readable display name for this key, used to easily identify the SSH keys when they are displayed. |
| `public_key` | `string` | The entire public key string that was uploaded. Embedded into the root user's `authorized_keys` file if you include this key during Droplet creation. |
| `fingerprint` | `string` | A unique identifier that differentiates this key from other keys using  a format that SSH recognizes. The fingerprint is created when the key is added to your account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `sshKeys_get` | `SELECT` | `ssh_key_identifier` | To get information about a key, send a GET request to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`.<br />The response will be a JSON object with the key `ssh_key` and value an ssh_key object which contains the standard ssh_key attributes. |
| `sshKeys_list` | `SELECT` |  | To list all of the keys in your account, send a GET request to `/v2/account/keys`. The response will be a JSON object with a key set to `ssh_keys`. The value of this will be an array of ssh_key objects, each of which contains the standard ssh_key attributes. |
| `sshKeys_create` | `INSERT` | `data__name, data__public_key` | To add a new SSH public key to your DigitalOcean account, send a POST request to `/v2/account/keys`. Set the `name` attribute to the name you wish to use and the `public_key` attribute to the full public key you are adding. |
| `sshKeys_delete` | `DELETE` | `ssh_key_identifier` | To destroy a public SSH key that you have in your account, send a DELETE request to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`.<br />A 204 status will be returned, indicating that the action was successful and that the response body is empty. |
| `_sshKeys_get` | `EXEC` | `ssh_key_identifier` | To get information about a key, send a GET request to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`.<br />The response will be a JSON object with the key `ssh_key` and value an ssh_key object which contains the standard ssh_key attributes. |
| `_sshKeys_list` | `EXEC` |  | To list all of the keys in your account, send a GET request to `/v2/account/keys`. The response will be a JSON object with a key set to `ssh_keys`. The value of this will be an array of ssh_key objects, each of which contains the standard ssh_key attributes. |
| `sshKeys_update` | `EXEC` | `ssh_key_identifier` | To update the name of an SSH key, send a PUT request to either `/v2/account/keys/$SSH_KEY_ID` or `/v2/account/keys/$SSH_KEY_FINGERPRINT`. Set the `name` attribute to the new name you want to use. |
