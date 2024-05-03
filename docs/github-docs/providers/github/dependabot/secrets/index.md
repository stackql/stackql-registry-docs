---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - dependabot
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.dependabot.secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the secret. |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_repo_secret" /> | `SELECT` | <CopyableCode code="owner, repo, secret_name" /> | Gets a single repository secret without revealing its encrypted value. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` repository permission to use this endpoint. |
| <CopyableCode code="list_repo_secrets" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists all secrets available in a repository without revealing their encrypted values. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` repository permission to use this endpoint. |
| <CopyableCode code="create_or_update_repo_secret" /> | `INSERT` | <CopyableCode code="owner, repo, secret_name" /> | Creates or updates a repository secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access<br />token with the `repo` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` repository<br />permission to use this endpoint. |
| <CopyableCode code="delete_repo_secret" /> | `DELETE` | <CopyableCode code="owner, repo, secret_name" /> | Deletes a secret in a repository using the secret name. You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` repository permission to use this endpoint. |
