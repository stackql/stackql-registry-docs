---
title: git_repository_links
hide_title: false
hide_table_of_contents: false
keywords:
  - git_repository_links
  - developerconnect
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

Creates, updates, deletes, gets or lists a <code>git_repository_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>git_repository_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.developerconnect.git_repository_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Resource name of the repository, in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`. |
| <CopyableCode code="annotations" /> | `object` | Optional. Allows clients to store small amounts of arbitrary data. |
| <CopyableCode code="cloneUri" /> | `string` | Required. Git Clone URI. |
| <CopyableCode code="createTime" /> | `string` | Output only. [Output only] Create timestamp |
| <CopyableCode code="deleteTime" /> | `string` | Output only. [Output only] Delete timestamp |
| <CopyableCode code="etag" /> | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Set to true when the connection is being set up or updated in the background. |
| <CopyableCode code="uid" /> | `string` | Output only. A system-assigned unique identifier for a the GitRepositoryLink. |
| <CopyableCode code="updateTime" /> | `string` | Output only. [Output only] Update timestamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionsId, gitRepositoryLinksId, locationsId, projectsId" /> | Gets details of a single GitRepositoryLink. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Lists GitRepositoryLinks in a given project, location, and connection. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Creates a GitRepositoryLink. Upon linking a Git Repository, Developer Connect will configure the Git Repository to send webhook events to Developer Connect. Connections that use Firebase GitHub Application will have events forwarded to the Firebase service. All other Connections will have events forwarded to Cloud Build. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionsId, gitRepositoryLinksId, locationsId, projectsId" /> | Deletes a single GitRepositoryLink. |

## `SELECT` examples

Lists GitRepositoryLinks in a given project, location, and connection.

```sql
SELECT
name,
annotations,
cloneUri,
createTime,
deleteTime,
etag,
labels,
reconciling,
uid,
updateTime
FROM google.developerconnect.git_repository_links
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>git_repository_links</code> resource.

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
INSERT INTO google.developerconnect.git_repository_links (
connectionsId,
locationsId,
projectsId,
name,
cloneUri,
createTime,
updateTime,
deleteTime,
labels,
etag,
reconciling,
annotations,
uid
)
SELECT 
'{{ connectionsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ cloneUri }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ labels }}',
'{{ etag }}',
true|false,
'{{ annotations }}',
'{{ uid }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: cloneUri
        value: '{{ cloneUri }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: etag
        value: '{{ etag }}'
      - name: reconciling
        value: '{{ reconciling }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: uid
        value: '{{ uid }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>git_repository_links</code> resource.

```sql
/*+ delete */
DELETE FROM google.developerconnect.git_repository_links
WHERE connectionsId = '{{ connectionsId }}'
AND gitRepositoryLinksId = '{{ gitRepositoryLinksId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
