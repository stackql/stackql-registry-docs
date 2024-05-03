---
title: org_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - org_secrets
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
<tr><td><b>Name</b></td><td><code>org_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.dependabot.org_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the secret. |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="selected_repositories_url" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="visibility" /> | `string` | Visibility of a secret |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_org_secret" /> | `SELECT` | <CopyableCode code="org, secret_name" /> | Gets a single organization secret without revealing its encrypted value. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| <CopyableCode code="list_org_secrets" /> | `SELECT` | <CopyableCode code="org" /> | Lists all secrets available in an organization without revealing their encrypted values. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
| <CopyableCode code="create_or_update_org_secret" /> | `INSERT` | <CopyableCode code="org, secret_name, data__visibility" /> | Creates or updates an organization secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access<br />token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization<br />permission to use this endpoint. |
| <CopyableCode code="delete_org_secret" /> | `DELETE` | <CopyableCode code="org, secret_name" /> | Deletes a secret in an organization using the secret name. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `dependabot_secrets` organization permission to use this endpoint. |
