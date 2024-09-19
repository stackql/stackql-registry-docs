---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - artifactregistry
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the repository, for example: `projects/p1/locations/us-central1/repositories/repo1`. For each location in a project, repository names must be unique. |
| <CopyableCode code="description" /> | `string` | The user-provided description of the repository. |
| <CopyableCode code="cleanupPolicies" /> | `object` | Optional. Cleanup policies for this repository. Cleanup policies indicate when certain package versions can be automatically deleted. Map keys are policy IDs supplied by users during policy creation. They must unique within a repository and be under 128 characters in length. |
| <CopyableCode code="cleanupPolicyDryRun" /> | `boolean` | Optional. If true, the cleanup pipeline is prevented from deleting versions in this repository. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the repository was created. |
| <CopyableCode code="disallowUnspecifiedMode" /> | `boolean` | Optional. If this is true, an unspecified repo type will be treated as error rather than defaulting to standard. |
| <CopyableCode code="dockerConfig" /> | `object` | DockerRepositoryConfig is docker related repository details. Provides additional configuration details for repositories of the docker format type. |
| <CopyableCode code="format" /> | `string` | Optional. The format of packages that are stored in the repository. |
| <CopyableCode code="kmsKeyName" /> | `string` | The Cloud KMS resource name of the customer managed encryption key that's used to encrypt the contents of the Repository. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. This value may not be changed after the Repository has been created. |
| <CopyableCode code="labels" /> | `object` | Labels with user-defined metadata. This field may contain up to 64 entries. Label keys and values may be no longer than 63 characters. Label keys must begin with a lowercase letter and may only contain lowercase letters, numeric characters, underscores, and dashes. |
| <CopyableCode code="mavenConfig" /> | `object` | MavenRepositoryConfig is maven related repository details. Provides additional configuration details for repositories of the maven format type. |
| <CopyableCode code="mode" /> | `string` | Optional. The mode of the repository. |
| <CopyableCode code="remoteRepositoryConfig" /> | `object` | Remote repository configuration. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. If set, the repository satisfies physical zone isolation. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. If set, the repository satisfies physical zone separation. |
| <CopyableCode code="sizeBytes" /> | `string` | Output only. The size, in bytes, of all artifact storage in this repository. Repositories that are generally available or in public preview use this to calculate storage costs. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the repository was last updated. |
| <CopyableCode code="virtualRepositoryConfig" /> | `object` | Virtual repository configuration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Gets a repository. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists repositories. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a repository. The returned Operation will finish once the repository has been created. Its response will be the created Repository. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Deletes a repository and all of its contents. The returned Operation will finish once the repository has been deleted. It will not have any Operation metadata and will return a google.protobuf.Empty response. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, repositoriesId" /> | Updates a repository. |

## `SELECT` examples

Lists repositories.

```sql
SELECT
name,
description,
cleanupPolicies,
cleanupPolicyDryRun,
createTime,
disallowUnspecifiedMode,
dockerConfig,
format,
kmsKeyName,
labels,
mavenConfig,
mode,
remoteRepositoryConfig,
satisfiesPzi,
satisfiesPzs,
sizeBytes,
updateTime,
virtualRepositoryConfig
FROM google.artifactregistry.repositories
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
INSERT INTO google.artifactregistry.repositories (
locationsId,
projectsId,
mavenConfig,
dockerConfig,
virtualRepositoryConfig,
remoteRepositoryConfig,
name,
format,
description,
labels,
kmsKeyName,
mode,
cleanupPolicies,
cleanupPolicyDryRun,
disallowUnspecifiedMode
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ mavenConfig }}',
'{{ dockerConfig }}',
'{{ virtualRepositoryConfig }}',
'{{ remoteRepositoryConfig }}',
'{{ name }}',
'{{ format }}',
'{{ description }}',
'{{ labels }}',
'{{ kmsKeyName }}',
'{{ mode }}',
'{{ cleanupPolicies }}',
{{ cleanupPolicyDryRun }},
{{ disallowUnspecifiedMode }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: mavenConfig
      value:
        - name: allowSnapshotOverwrites
          value: boolean
        - name: versionPolicy
          value: string
    - name: dockerConfig
      value:
        - name: immutableTags
          value: boolean
    - name: virtualRepositoryConfig
      value:
        - name: upstreamPolicies
          value:
            - - name: id
                value: string
              - name: repository
                value: string
              - name: priority
                value: integer
    - name: remoteRepositoryConfig
      value:
        - name: dockerRepository
          value:
            - name: publicRepository
              value: string
            - name: customRepository
              value:
                - name: uri
                  value: string
        - name: mavenRepository
          value:
            - name: publicRepository
              value: string
            - name: customRepository
              value:
                - name: uri
                  value: string
        - name: npmRepository
          value:
            - name: publicRepository
              value: string
            - name: customRepository
              value:
                - name: uri
                  value: string
        - name: pythonRepository
          value:
            - name: publicRepository
              value: string
            - name: customRepository
              value:
                - name: uri
                  value: string
        - name: aptRepository
          value:
            - name: publicRepository
              value:
                - name: repositoryBase
                  value: string
                - name: repositoryPath
                  value: string
            - name: customRepository
              value:
                - name: uri
                  value: string
        - name: yumRepository
          value:
            - name: publicRepository
              value:
                - name: repositoryBase
                  value: string
                - name: repositoryPath
                  value: string
            - name: customRepository
              value:
                - name: uri
                  value: string
        - name: commonRepository
          value:
            - name: uri
              value: string
        - name: description
          value: string
        - name: upstreamCredentials
          value:
            - name: usernamePasswordCredentials
              value:
                - name: username
                  value: string
                - name: passwordSecretVersion
                  value: string
        - name: disableUpstreamValidation
          value: boolean
    - name: name
      value: string
    - name: format
      value: string
    - name: description
      value: string
    - name: labels
      value: object
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: kmsKeyName
      value: string
    - name: mode
      value: string
    - name: cleanupPolicies
      value: object
    - name: sizeBytes
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: cleanupPolicyDryRun
      value: boolean
    - name: disallowUnspecifiedMode
      value: boolean
    - name: satisfiesPzi
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>repositories</code> resource.

```sql
/*+ update */
UPDATE google.artifactregistry.repositories
SET 
mavenConfig = '{{ mavenConfig }}',
dockerConfig = '{{ dockerConfig }}',
virtualRepositoryConfig = '{{ virtualRepositoryConfig }}',
remoteRepositoryConfig = '{{ remoteRepositoryConfig }}',
name = '{{ name }}',
format = '{{ format }}',
description = '{{ description }}',
labels = '{{ labels }}',
kmsKeyName = '{{ kmsKeyName }}',
mode = '{{ mode }}',
cleanupPolicies = '{{ cleanupPolicies }}',
cleanupPolicyDryRun = true|false,
disallowUnspecifiedMode = true|false
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```

## `DELETE` example

Deletes the specified <code>repositories</code> resource.

```sql
/*+ delete */
DELETE FROM google.artifactregistry.repositories
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```
