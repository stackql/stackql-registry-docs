---
title: repositories
hide_title: false
hide_table_of_contents: false
keywords:
  - repositories
  - cloudbuild
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudbuild.repositories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Resource name of the repository, in the format `projects/*/locations/*/connections/*/repositories/*`. |
| <CopyableCode code="annotations" /> | `object` | Optional. Allows clients to store small amounts of arbitrary data. |
| <CopyableCode code="createTime" /> | `string` | Output only. Server assigned timestamp for when the connection was created. |
| <CopyableCode code="etag" /> | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="remoteUri" /> | `string` | Required. Git Clone HTTPS URI. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Server assigned timestamp for when the connection was updated. |
| <CopyableCode code="webhookId" /> | `string` | Output only. External ID of the webhook created for the repository. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_connections_repositories_get" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId, repositoriesId" /> | Gets details of a single repository. |
| <CopyableCode code="projects_locations_connections_repositories_list" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Lists Repositories in a given connection. |
| <CopyableCode code="projects_locations_connections_repositories_batch_create" /> | `INSERT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Creates multiple repositories inside a connection. |
| <CopyableCode code="projects_locations_connections_repositories_create" /> | `INSERT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Creates a Repository. |
| <CopyableCode code="projects_locations_connections_repositories_delete" /> | `DELETE` | <CopyableCode code="connectionsId, locationsId, projectsId, repositoriesId" /> | Deletes a single repository. |
| <CopyableCode code="projects_locations_connections_repositories_access_read_token" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId, repositoriesId" /> | Fetches read token of a given repository. |
| <CopyableCode code="projects_locations_connections_repositories_access_read_write_token" /> | `EXEC` | <CopyableCode code="connectionsId, locationsId, projectsId, repositoriesId" /> | Fetches read/write token of a given repository. |

## `SELECT` examples

Lists Repositories in a given connection.

```sql
SELECT
name,
annotations,
createTime,
etag,
remoteUri,
updateTime,
webhookId
FROM google.cloudbuild.repositories
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
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
INSERT INTO google.cloudbuild.repositories (
connectionsId,
locationsId,
projectsId,
requests
)
SELECT 
'{{ connectionsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ requests }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: requests
      value:
        - - name: repositoryId
            value: string
          - name: repository
            value:
              - name: updateTime
                value: string
              - name: name
                value: string
              - name: annotations
                value: object
              - name: etag
                value: string
              - name: webhookId
                value: string
              - name: createTime
                value: string
              - name: remoteUri
                value: string
          - name: parent
            value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>repositories</code> resource.

```sql
/*+ delete */
DELETE FROM google.cloudbuild.repositories
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}';
```
