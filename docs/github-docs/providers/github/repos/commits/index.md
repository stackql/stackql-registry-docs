---
title: commits
hide_title: false
hide_table_of_contents: false
keywords:
  - commits
  - repos
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `url` | `string` |  |
| `commit` | `object` |  |
| `committer` | `object` | A GitHub user. |
| `html_url` | `string` |  |
| `author` | `object` | A GitHub user. |
| `parents` | `array` |  |
| `stats` | `object` |  |
| `files` | `array` |  |
| `node_id` | `string` |  |
| `comments_url` | `string` |  |
| `sha` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_commit` | `SELECT` | `owner, ref, repo` | Returns the contents of a single commit reference. You must have `read` access for the repository to use this endpoint.<br /><br />**Note:** If there are more than 300 files in the commit diff, the response will include pagination link headers for the remaining files, up to a limit of 3000 files. Each page contains the static commit information, and the only changes are to the file listing.<br /><br />You can pass the appropriate [media type](https://docs.github.com/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to  fetch `diff` and `patch` formats. Diffs with binary data will have no `patch` property.<br /><br />To return only the SHA-1 hash of the commit reference, you can provide the `sha` custom [media type](https://docs.github.com/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) in the `Accept` header. You can use this endpoint to check if a remote reference's SHA-1 hash is the same as your local reference's SHA-1 hash by providing the local SHA-1 reference as the ETag.<br /><br />**Signature verification object**<br /><br />The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:<br /><br />\| Name \| Type \| Description \|<br />\| ---- \| ---- \| ----------- \|<br />\| `verified` \| `boolean` \| Indicates whether GitHub considers the signature in this commit to be verified. \|<br />\| `reason` \| `string` \| The reason for verified value. Possible values and their meanings are enumerated in table below. \|<br />\| `signature` \| `string` \| The signature that was extracted from the commit. \|<br />\| `payload` \| `string` \| The value that was signed. \|<br /><br />These are the possible values for `reason` in the `verification` object:<br /><br />\| Value \| Description \|<br />\| ----- \| ----------- \|<br />\| `expired_key` \| The key that made the signature is expired. \|<br />\| `not_signing_key` \| The "signing" flag is not among the usage flags in the GPG key that made the signature. \|<br />\| `gpgverify_error` \| There was an error communicating with the signature verification service. \|<br />\| `gpgverify_unavailable` \| The signature verification service is currently unavailable. \|<br />\| `unsigned` \| The object does not include a signature. \|<br />\| `unknown_signature_type` \| A non-PGP signature was found in the commit. \|<br />\| `no_user` \| No user was associated with the `committer` email address in the commit. \|<br />\| `unverified_email` \| The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. \|<br />\| `bad_email` \| The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. \|<br />\| `unknown_key` \| The key that made the signature has not been registered with any user's account. \|<br />\| `malformed_signature` \| There was an error parsing the signature. \|<br />\| `invalid` \| The signature could not be cryptographically verified using the key whose key-id was found in the signature. \|<br />\| `valid` \| None of the above errors applied, so the signature is considered to be verified. \| |
| `list_commits` | `SELECT` | `owner, repo` | **Signature verification object**<br /><br />The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:<br /><br />\| Name \| Type \| Description \|<br />\| ---- \| ---- \| ----------- \|<br />\| `verified` \| `boolean` \| Indicates whether GitHub considers the signature in this commit to be verified. \|<br />\| `reason` \| `string` \| The reason for verified value. Possible values and their meanings are enumerated in table below. \|<br />\| `signature` \| `string` \| The signature that was extracted from the commit. \|<br />\| `payload` \| `string` \| The value that was signed. \|<br /><br />These are the possible values for `reason` in the `verification` object:<br /><br />\| Value \| Description \|<br />\| ----- \| ----------- \|<br />\| `expired_key` \| The key that made the signature is expired. \|<br />\| `not_signing_key` \| The "signing" flag is not among the usage flags in the GPG key that made the signature. \|<br />\| `gpgverify_error` \| There was an error communicating with the signature verification service. \|<br />\| `gpgverify_unavailable` \| The signature verification service is currently unavailable. \|<br />\| `unsigned` \| The object does not include a signature. \|<br />\| `unknown_signature_type` \| A non-PGP signature was found in the commit. \|<br />\| `no_user` \| No user was associated with the `committer` email address in the commit. \|<br />\| `unverified_email` \| The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. \|<br />\| `bad_email` \| The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. \|<br />\| `unknown_key` \| The key that made the signature has not been registered with any user's account. \|<br />\| `malformed_signature` \| There was an error parsing the signature. \|<br />\| `invalid` \| The signature could not be cryptographically verified using the key whose key-id was found in the signature. \|<br />\| `valid` \| None of the above errors applied, so the signature is considered to be verified. \| |
