---
title: organization_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_secrets
  - codespaces
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
<tr><td><b>Name</b></td><td><code>organization_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.codespaces.organization_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the secret |
| <CopyableCode code="created_at" /> | `string` | The date and time at which the secret was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| <CopyableCode code="selected_repositories_url" /> | `string` | The API URL at which the list of repositories this secret is visible to can be retrieved |
| <CopyableCode code="updated_at" /> | `string` | The date and time at which the secret was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| <CopyableCode code="visibility" /> | `string` | The type of repositories in the organization that the secret is visible to |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_org_secret" /> | `SELECT` | <CopyableCode code="org, secret_name" /> | Gets an organization secret without revealing its encrypted value.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="list_org_secrets" /> | `SELECT` | <CopyableCode code="org" /> | Lists all Codespaces secrets available at the organization-level without revealing their encrypted values.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="create_or_update_org_secret" /> | `INSERT` | <CopyableCode code="org, secret_name, data__visibility" /> | Creates or updates an organization secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access<br />token with the `admin:org` scope to use this endpoint. |
| <CopyableCode code="delete_org_secret" /> | `DELETE` | <CopyableCode code="org, secret_name" /> | Deletes an organization secret using the secret name. You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
