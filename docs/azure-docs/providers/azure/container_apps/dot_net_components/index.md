---
title: dot_net_components
hide_title: false
hide_table_of_contents: false
keywords:
  - dot_net_components
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

Creates, updates, deletes, gets or lists a <code>dot_net_components</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dot_net_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.dot_net_components" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | .NET Component resource specific properties |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Creates or updates a .NET Component in a Managed Environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Delete a .NET Component. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Patches a .NET Component using JSON Merge Patch |

## `SELECT` examples




```sql
SELECT
properties
FROM azure.container_apps.dot_net_components
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dot_net_components</code> resource.

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
INSERT INTO azure.container_apps.dot_net_components (
environmentName,
name,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ environmentName }}',
'{{ name }}',
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
        - name: provisioningState
          value: string
        - name: configurations
          value:
            - - name: propertyName
                value: string
              - name: value
                value: string
        - name: serviceBinds
          value:
            - - name: name
                value: string
              - name: serviceId
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dot_net_components</code> resource.

```sql
/*+ update */
UPDATE azure.container_apps.dot_net_components
SET 
properties = '{{ properties }}'
WHERE 
environmentName = '{{ environmentName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dot_net_components</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_apps.dot_net_components
WHERE environmentName = '{{ environmentName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
