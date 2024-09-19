---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - dataform
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>repositories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repositories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataform.repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The repository's name. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp of when the repository was created. |
| <CopyableCode code="dataEncryptionState" /> | `object` | Describes encryption state of a resource. |
| <CopyableCode code="displayName" /> | `string` | Optional. The repository's user-friendly name. |
| <CopyableCode code="gitRemoteSettings" /> | `object` | Controls Git remote configuration for a repository. |
| <CopyableCode code="kmsKeyName" /> | `string` | Optional. The reference to a KMS encryption key. If provided, it will be used to encrypt user data in the repository and all child resources. It is not possible to add or update the encryption key after the repository is created. Example: `projects/[kms_project_id]/locations/[region]/keyRings/[key_region]/cryptoKeys/[key]` |
| <CopyableCode code="labels" /> | `object` | Optional. Repository user labels. |
| <CopyableCode code="npmrcEnvironmentVariablesSecretVersion" /> | `string` | Optional. The name of the Secret Manager secret version to be used to interpolate variables into the .npmrc file for package installation operations. Must be in the format `projects/*/secrets/*/versions/*`. The file itself must be in a JSON format. |
| <CopyableCode code="serviceAccount" /> | `string` | Optional. The service account to run workflow invocations under. |
| <CopyableCode code="setAuthenticatedUserAdmin" /> | `boolean` | Optional. Input only. If set to true, the authenticated user will be granted the roles/dataform.admin role on the created repository. To modify access to the created repository later apply setIamPolicy from https://cloud.google.com/dataform/reference/rest#rest-resource:-v1beta1.projects.locations.repositories |
| <CopyableCode code="workspaceCompilationOverrides" /> | `object` | Configures workspace compilation overrides for a repository. Primarily used by the UI (`console.cloud.google.com`). `schema_suffix` and `table_prefix` can have a special expression - `${workspaceName}`, which refers to the workspace name from which the compilation results will be created. API callers are expected to resolve the expression in these overrides and provide them explicitly in `code_compilation_config` (https://cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.repositories.compilationResults#codecompilationconfig) when creating workspace-scoped compilation results. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Fetches a single Repository. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Repositories in a given project and location. |
| <CopyableCode code="query_directory_contents" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Returns the contents of a given Repository directory. The Repository must not have a value for `git_remote_settings.url`. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Repository in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Deletes a single Repository. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Updates a single Repository. |
| <CopyableCode code="commit" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Applies a Git commit to a Repository. The Repository must not have a value for `git_remote_settings.url`. |
| <CopyableCode code="compute_access_token_status" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Computes a Repository's Git access token status. |
| <CopyableCode code="read_file" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Returns the contents of a file (inside a Repository). The Repository must not have a value for `git_remote_settings.url`. |

## `SELECT` examples

Lists Repositories in a given project and location.

```sql
SELECT
name,
createTime,
dataEncryptionState,
displayName,
gitRemoteSettings,
kmsKeyName,
labels,
npmrcEnvironmentVariablesSecretVersion,
serviceAccount,
setAuthenticatedUserAdmin,
workspaceCompilationOverrides
FROM google.dataform.repositories
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>repositories</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.dataform.repositories (
locationsId,
projectsId,
name,
displayName,
gitRemoteSettings,
npmrcEnvironmentVariablesSecretVersion,
workspaceCompilationOverrides,
labels,
setAuthenticatedUserAdmin,
serviceAccount,
kmsKeyName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ gitRemoteSettings }}',
'{{ npmrcEnvironmentVariablesSecretVersion }}',
'{{ workspaceCompilationOverrides }}',
'{{ labels }}',
{{ setAuthenticatedUserAdmin }},
'{{ serviceAccount }}',
'{{ kmsKeyName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: displayName
      value: string
    - name: gitRemoteSettings
      value:
        - name: url
          value: string
        - name: defaultBranch
          value: string
        - name: authenticationTokenSecretVersion
          value: string
        - name: sshAuthenticationConfig
          value:
            - name: userPrivateKeySecretVersion
              value: string
            - name: hostPublicKey
              value: string
        - name: tokenStatus
          value: string
    - name: npmrcEnvironmentVariablesSecretVersion
      value: string
    - name: workspaceCompilationOverrides
      value:
        - name: defaultDatabase
          value: string
        - name: schemaSuffix
          value: string
        - name: tablePrefix
          value: string
    - name: labels
      value: object
    - name: setAuthenticatedUserAdmin
      value: boolean
    - name: serviceAccount
      value: string
    - name: kmsKeyName
      value: string
    - name: dataEncryptionState
      value:
        - name: kmsKeyVersionName
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>repositories</code> resource.

```sql
/*+ update */
UPDATE google.dataform.repositories
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
gitRemoteSettings = '{{ gitRemoteSettings }}',
npmrcEnvironmentVariablesSecretVersion = '{{ npmrcEnvironmentVariablesSecretVersion }}',
workspaceCompilationOverrides = '{{ workspaceCompilationOverrides }}',
labels = '{{ labels }}',
setAuthenticatedUserAdmin = true|false,
serviceAccount = '{{ serviceAccount }}',
kmsKeyName = '{{ kmsKeyName }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```

## `DELETE` example

Deletes the specified <code>repositories</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataform.repositories
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```
