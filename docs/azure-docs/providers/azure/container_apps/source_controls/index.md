---
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>source_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.source_controls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | SourceControl resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, sourceControlName, subscriptionId" /> |  |
| <CopyableCode code="list_by_container_app" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerAppName, resourceGroupName, sourceControlName, subscriptionId, x-ms-github-auxiliary" /> | Create or update the SourceControl for a Container App. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerAppName, resourceGroupName, sourceControlName, subscriptionId, x-ms-github-auxiliary" /> | Delete a Container App SourceControl. |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.container_apps.source_controls
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>source_controls</code> resource.

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
INSERT INTO azure.container_apps.source_controls (
containerAppName,
resourceGroupName,
sourceControlName,
subscriptionId,
x-ms-github-auxiliary,
properties
)
SELECT 
'{{ containerAppName }}',
'{{ resourceGroupName }}',
'{{ sourceControlName }}',
'{{ subscriptionId }}',
'{{ x-ms-github-auxiliary }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: operationState
          value: string
        - name: repoUrl
          value: string
        - name: branch
          value: string
        - name: githubActionConfiguration
          value:
            - name: registryInfo
              value:
                - name: registryUrl
                  value: string
                - name: registryUserName
                  value: string
                - name: registryPassword
                  value: string
            - name: azureCredentials
              value:
                - name: clientId
                  value: string
                - name: clientSecret
                  value: string
                - name: tenantId
                  value: string
                - name: kind
                  value: string
                - name: subscriptionId
                  value: string
            - name: contextPath
              value: string
            - name: githubPersonalAccessToken
              value: string
            - name: image
              value: string
            - name: publishType
              value: string
            - name: os
              value: string
            - name: runtimeStack
              value: string
            - name: runtimeVersion
              value: string
            - name: buildEnvironmentVariables
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>source_controls</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.source_controls
WHERE containerAppName = '{{ containerAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlName = '{{ sourceControlName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND x-ms-github-auxiliary = '{{ x-ms-github-auxiliary }}';
```
