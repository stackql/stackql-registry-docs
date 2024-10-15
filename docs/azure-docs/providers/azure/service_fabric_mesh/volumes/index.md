---
title: volumes
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes
  - service_fabric_mesh
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

Creates, updates, deletes, gets or lists a <code>volumes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.volumes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_file_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="volumeResourceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | This type describes properties of a volume resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, volumeResourceName" /> | Gets the information about the volume resource with the given name. The information include the description and other properties of the volume. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the information about all volume resources in a given resource group. The information include the description and other properties of the volume. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, volumeResourceName, data__properties" /> | Creates a volume resource with the specified name, description and properties. If a volume resource with the same name exists, then it is updated with the specified description and properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, volumeResourceName" /> | Deletes the volume resource identified by the name. |

## `SELECT` examples

Gets the information about all volume resources in a given resource group. The information include the description and other properties of the volume.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_volumes', value: 'view', },
        { label: 'volumes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
azure_file_parameters,
location,
provider,
provisioning_state,
resourceGroupName,
status,
status_details,
subscriptionId,
tags,
volumeResourceName
FROM azure.service_fabric_mesh.vw_volumes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.service_fabric_mesh.volumes
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>volumes</code> resource.

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
INSERT INTO azure.service_fabric_mesh.volumes (
resourceGroupName,
subscriptionId,
volumeResourceName,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ volumeResourceName }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: description
          value: string
        - name: status
          value: []
        - name: statusDetails
          value: string
        - name: provider
          value: []
        - name: azureFileParameters
          value:
            - name: accountName
              value: string
            - name: accountKey
              value: string
            - name: shareName
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>volumes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_mesh.volumes
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND volumeResourceName = '{{ volumeResourceName }}';
```
