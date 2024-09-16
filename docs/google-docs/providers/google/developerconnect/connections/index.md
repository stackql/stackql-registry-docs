---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
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

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.developerconnect.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the connection, in the format `projects/{project}/locations/{location}/connections/{connection_id}`. |
| <CopyableCode code="annotations" /> | `object` | Optional. Allows clients to store small amounts of arbitrary data. |
| <CopyableCode code="createTime" /> | `string` | Output only. [Output only] Create timestamp |
| <CopyableCode code="deleteTime" /> | `string` | Output only. [Output only] Delete timestamp |
| <CopyableCode code="disabled" /> | `boolean` | Optional. If disabled is set to true, functionality is disabled for this connection. Repository based API methods and webhooks processing for repositories in this connection will be disabled. |
| <CopyableCode code="etag" /> | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="githubConfig" /> | `object` | Configuration for connections to github.com. |
| <CopyableCode code="installationState" /> | `object` | Describes stage and necessary actions to be taken by the user to complete the installation. Used for GitHub and GitHub Enterprise based connections. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels as key value pairs |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Set to true when the connection is being set up or updated in the background. |
| <CopyableCode code="uid" /> | `string` | Output only. A system-assigned unique identifier for a the GitRepositoryLink. |
| <CopyableCode code="updateTime" /> | `string` | Output only. [Output only] Update timestamp |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Gets details of a single Connection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Connections in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Connection in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Deletes a single Connection. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="connectionsId, locationsId, projectsId" /> | Updates the parameters of a single Connection. |

## `SELECT` examples

Lists Connections in a given project and location.

```sql
SELECT
name,
annotations,
createTime,
deleteTime,
disabled,
etag,
githubConfig,
installationState,
labels,
reconciling,
uid,
updateTime
FROM google.developerconnect.connections
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connections</code> resource.

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
INSERT INTO google.developerconnect.connections (
locationsId,
projectsId,
githubConfig,
name,
labels,
disabled,
annotations,
etag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ githubConfig }}',
'{{ name }}',
'{{ labels }}',
true|false,
'{{ annotations }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: githubConfig
      value:
        - name: githubApp
          value: '{{ githubApp }}'
        - name: authorizerCredential
          value:
            - name: oauthTokenSecretVersion
              value: '{{ oauthTokenSecretVersion }}'
        - name: appInstallationId
          value: '{{ appInstallationId }}'
    - name: name
      value: '{{ name }}'
    - name: labels
      value: '{{ labels }}'
    - name: disabled
      value: '{{ disabled }}'
    - name: annotations
      value: '{{ annotations }}'
    - name: etag
      value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connections</code> resource.

```sql
/*+ update */
UPDATE google.developerconnect.connections
SET 
githubConfig = '{{ githubConfig }}',
name = '{{ name }}',
labels = '{{ labels }}',
disabled = true|false,
annotations = '{{ annotations }}',
etag = '{{ etag }}'
WHERE 
connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>connections</code> resource.

```sql
/*+ delete */
DELETE FROM google.developerconnect.connections
WHERE connectionsId = '{{ connectionsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
