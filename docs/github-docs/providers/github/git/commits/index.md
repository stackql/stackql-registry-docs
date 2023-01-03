---
title: commits
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.git.commits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tree` | `object` |  |
| `parents` | `array` |  |
| `committer` | `object` | Identifying information for the git-user |
| `message` | `string` | Message describing the purpose of the commit |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `author` | `object` | Identifying information for the git-user |
| `verification` | `object` |  |
| `sha` | `string` | SHA for the commit |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_commit` | `SELECT` | `commit_sha, owner, repo` | Gets a Git [commit object](https://git-scm.com/book/en/v1/Git-Internals-Git-Objects#Commit-Objects).<br /><br />**Signature verification object**<br /><br />The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:<br /><br />\| Name \| Type \| Description \|<br />\| ---- \| ---- \| ----------- \|<br />\| `verified` \| `boolean` \| Indicates whether GitHub considers the signature in this commit to be verified. \|<br />\| `reason` \| `string` \| The reason for verified value. Possible values and their meanings are enumerated in table below. \|<br />\| `signature` \| `string` \| The signature that was extracted from the commit. \|<br />\| `payload` \| `string` \| The value that was signed. \|<br /><br />These are the possible values for `reason` in the `verification` object:<br /><br />\| Value \| Description \|<br />\| ----- \| ----------- \|<br />\| `expired_key` \| The key that made the signature is expired. \|<br />\| `not_signing_key` \| The "signing" flag is not among the usage flags in the GPG key that made the signature. \|<br />\| `gpgverify_error` \| There was an error communicating with the signature verification service. \|<br />\| `gpgverify_unavailable` \| The signature verification service is currently unavailable. \|<br />\| `unsigned` \| The object does not include a signature. \|<br />\| `unknown_signature_type` \| A non-PGP signature was found in the commit. \|<br />\| `no_user` \| No user was associated with the `committer` email address in the commit. \|<br />\| `unverified_email` \| The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. \|<br />\| `bad_email` \| The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. \|<br />\| `unknown_key` \| The key that made the signature has not been registered with any user's account. \|<br />\| `malformed_signature` \| There was an error parsing the signature. \|<br />\| `invalid` \| The signature could not be cryptographically verified using the key whose key-id was found in the signature. \|<br />\| `valid` \| None of the above errors applied, so the signature is considered to be verified. \| |
| `create_commit` | `INSERT` | `owner, repo, data__message, data__tree` | Creates a new Git [commit object](https://git-scm.com/book/en/v1/Git-Internals-Git-Objects#Commit-Objects).<br /><br />**Signature verification object**<br /><br />The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:<br /><br />\| Name \| Type \| Description \|<br />\| ---- \| ---- \| ----------- \|<br />\| `verified` \| `boolean` \| Indicates whether GitHub considers the signature in this commit to be verified. \|<br />\| `reason` \| `string` \| The reason for verified value. Possible values and their meanings are enumerated in table below. \|<br />\| `signature` \| `string` \| The signature that was extracted from the commit. \|<br />\| `payload` \| `string` \| The value that was signed. \|<br /><br />These are the possible values for `reason` in the `verification` object:<br /><br />\| Value \| Description \|<br />\| ----- \| ----------- \|<br />\| `expired_key` \| The key that made the signature is expired. \|<br />\| `not_signing_key` \| The "signing" flag is not among the usage flags in the GPG key that made the signature. \|<br />\| `gpgverify_error` \| There was an error communicating with the signature verification service. \|<br />\| `gpgverify_unavailable` \| The signature verification service is currently unavailable. \|<br />\| `unsigned` \| The object does not include a signature. \|<br />\| `unknown_signature_type` \| A non-PGP signature was found in the commit. \|<br />\| `no_user` \| No user was associated with the `committer` email address in the commit. \|<br />\| `unverified_email` \| The `committer` email address in the commit was associated with a user, but the email address is not verified on her/his account. \|<br />\| `bad_email` \| The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. \|<br />\| `unknown_key` \| The key that made the signature has not been registered with any user's account. \|<br />\| `malformed_signature` \| There was an error parsing the signature. \|<br />\| `invalid` \| The signature could not be cryptographically verified using the key whose key-id was found in the signature. \|<br />\| `valid` \| None of the above errors applied, so the signature is considered to be verified. \| |
