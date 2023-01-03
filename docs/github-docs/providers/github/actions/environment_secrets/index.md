---
title: environment_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - actions
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.environment_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the secret. |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_environment_secret` | `SELECT` | `environment_name, repository_id, secret_name` | Gets a single environment secret without revealing its encrypted value. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint. |
| `list_environment_secrets` | `SELECT` | `environment_name, repository_id` | Lists all secrets available in an environment without revealing their encrypted values. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint. |
| `create_or_update_environment_secret` | `INSERT` | `environment_name, repository_id, secret_name, data__encrypted_value, data__key_id` | Creates or updates an environment secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access<br />token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use<br />this endpoint.<br /><br />#### Example encrypting a secret using Node.js<br /><br />Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.<br /><br />```<br />const sodium = require('tweetsodium');<br /><br />const key = "base64-encoded-public-key";<br />const value = "plain-text-secret";<br /><br />// Convert the message and key to Uint8Array's (Buffer implements that interface)<br />const messageBytes = Buffer.from(value);<br />const keyBytes = Buffer.from(key, 'base64');<br /><br />// Encrypt using LibSodium.<br />const encryptedBytes = sodium.seal(messageBytes, keyBytes);<br /><br />// Base64 the encrypted secret<br />const encrypted = Buffer.from(encryptedBytes).toString('base64');<br /><br />console.log(encrypted);<br />```<br /><br /><br />#### Example encrypting a secret using Python<br /><br />Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-sealedbox) with Python 3.<br /><br />```<br />from base64 import b64encode<br />from nacl import encoding, public<br /><br />def encrypt(public_key: str, secret_value: str) -&#x7D; str:<br />  """Encrypt a Unicode string using the public key."""<br />  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())<br />  sealed_box = public.SealedBox(public_key)<br />  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))<br />  return b64encode(encrypted).decode("utf-8")<br />```<br /><br />#### Example encrypting a secret using C#<br /><br />Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.<br /><br />```<br />var secretValue = System.Text.Encoding.UTF8.GetBytes("mySecret");<br />var publicKey = Convert.FromBase64String("2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=");<br /><br />var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);<br /><br />Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));<br />```<br /><br />#### Example encrypting a secret using Ruby<br /><br />Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.<br /><br />```ruby<br />require "rbnacl"<br />require "base64"<br /><br />key = Base64.decode64("+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=")<br />public_key = RbNaCl::PublicKey.new(key)<br /><br />box = RbNaCl::Boxes::Sealed.from_public_key(public_key)<br />encrypted_secret = box.encrypt("my_secret")<br /><br /># Print the base64 encoded secret<br />puts Base64.strict_encode64(encrypted_secret)<br />``` |
| `delete_environment_secret` | `DELETE` | `environment_name, repository_id, secret_name` | Deletes a secret in an environment using the secret name. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `secrets` repository permission to use this endpoint. |
