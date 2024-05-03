---
title: environment_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_secrets
  - actions
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
<tr><td><b>Name</b></td><td><code>environment_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.actions.environment_secrets" /></td></tr>
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
| <CopyableCode code="get_environment_secret" /> | `SELECT` | <CopyableCode code="environment_name, repository_id, secret_name" /> | Gets a single environment secret without revealing its encrypted value.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| <CopyableCode code="list_environment_secrets" /> | `SELECT` | <CopyableCode code="environment_name, repository_id" /> | Lists all secrets available in an environment without revealing their<br />encrypted values.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| <CopyableCode code="create_or_update_environment_secret" /> | `INSERT` | <CopyableCode code="environment_name, repository_id, secret_name, data__encrypted_value, data__key_id" /> | Creates or updates an environment secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| <CopyableCode code="delete_environment_secret" /> | `DELETE` | <CopyableCode code="environment_name, repository_id, secret_name" /> | Deletes a secret in an environment using the secret name.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
