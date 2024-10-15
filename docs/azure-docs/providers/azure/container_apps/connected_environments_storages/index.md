---
title: connected_environments_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_storages
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

Creates, updates, deletes, gets or lists a <code>connected_environments_storages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_environments_storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments_storages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Storage properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, storageName, subscriptionId" /> | Get storage for a connectedEnvironment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Get all storages for a connectedEnvironment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, storageName, subscriptionId" /> | Create or update storage for a connectedEnvironment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, storageName, subscriptionId" /> | Delete storage for a connectedEnvironment. |

## `SELECT` examples

Get all storages for a connectedEnvironment.


```sql
SELECT
properties
FROM azure.container_apps.connected_environments_storages
WHERE connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connected_environments_storages</code> resource.

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
INSERT INTO azure.container_apps.connected_environments_storages (
connectedEnvironmentName,
resourceGroupName,
storageName,
subscriptionId,
properties
)
SELECT 
'{{ connectedEnvironmentName }}',
'{{ resourceGroupName }}',
'{{ storageName }}',
'{{ subscriptionId }}',
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
        - name: azureFile
          value:
            - name: accountName
              value: string
            - name: accountKey
              value: string
            - name: accessMode
              value: string
            - name: shareName
              value: string
        - name: smb
          value:
            - name: host
              value: string
            - name: shareName
              value: string
            - name: username
              value: string
            - name: domain
              value: string
            - name: password
              value: string
            - name: accessMode
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connected_environments_storages</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.connected_environments_storages
WHERE connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageName = '{{ storageName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
