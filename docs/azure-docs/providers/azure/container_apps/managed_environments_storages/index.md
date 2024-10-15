---
title: managed_environments_storages
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environments_storages
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

Creates, updates, deletes, gets or lists a <code>managed_environments_storages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_environments_storages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.managed_environments_storages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Storage properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, storageName, subscriptionId" /> | Get storage for a managedEnvironment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Get all storages for a managedEnvironment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, resourceGroupName, storageName, subscriptionId" /> | Create or update storage for a managedEnvironment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, resourceGroupName, storageName, subscriptionId" /> | Delete storage for a managedEnvironment. |

## `SELECT` examples

Get all storages for a managedEnvironment.


```sql
SELECT
properties
FROM azure.container_apps.managed_environments_storages
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_environments_storages</code> resource.

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
INSERT INTO azure.container_apps.managed_environments_storages (
environmentName,
resourceGroupName,
storageName,
subscriptionId,
properties
)
SELECT 
'{{ environmentName }}',
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
        - name: nfsAzureFile
          value:
            - name: server
              value: string
            - name: accessMode
              value: string
            - name: shareName
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>managed_environments_storages</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.managed_environments_storages
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageName = '{{ storageName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
