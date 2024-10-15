---
title: connected_environments_dapr_components
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_dapr_components
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

Creates, updates, deletes, gets or lists a <code>connected_environments_dapr_components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connected_environments_dapr_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments_dapr_components" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Dapr Component resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="componentName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="componentName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Creates or updates a Dapr Component in a connected environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="componentName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Delete a Dapr Component from a connected environment. |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.container_apps.connected_environments_dapr_components
WHERE connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connected_environments_dapr_components</code> resource.

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
INSERT INTO azure.container_apps.connected_environments_dapr_components (
componentName,
connectedEnvironmentName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ componentName }}',
'{{ connectedEnvironmentName }}',
'{{ resourceGroupName }}',
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
        - name: componentType
          value: string
        - name: version
          value: string
        - name: ignoreErrors
          value: boolean
        - name: initTimeout
          value: string
        - name: secrets
          value:
            - - name: name
                value: string
              - name: value
                value: string
              - name: identity
                value: string
              - name: keyVaultUrl
                value: string
        - name: secretStoreComponent
          value: string
        - name: metadata
          value:
            - - name: name
                value: string
              - name: value
                value: string
              - name: secretRef
                value: string
        - name: scopes
          value:
            - string
        - name: serviceComponentBind
          value:
            - - name: name
                value: string
              - name: serviceId
                value: string
              - name: metadata
                value:
                  - name: name
                    value: string
                  - name: value
                    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connected_environments_dapr_components</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.connected_environments_dapr_components
WHERE componentName = '{{ componentName }}'
AND connectedEnvironmentName = '{{ connectedEnvironmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
