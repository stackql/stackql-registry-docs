---
title: slices
hide_title: false
hide_table_of_contents: false
keywords:
  - slices
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>slices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>slices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.slices" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_slices', value: 'view', },
        { label: 'slices', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mobileNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sliceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="snssai" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network slice properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, sliceName, subscriptionId" /> | Gets information about the specified network slice. |
| <CopyableCode code="list_by_mobile_network" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Lists all slices in the mobile network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mobileNetworkName, resourceGroupName, sliceName, subscriptionId, data__properties" /> | Creates or updates a network slice. Must be created in the same location as its parent mobile network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mobileNetworkName, resourceGroupName, sliceName, subscriptionId" /> | Deletes the specified network slice. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="mobileNetworkName, resourceGroupName, sliceName, subscriptionId" /> | Updates slice tags. |

## `SELECT` examples

Lists all slices in the mobile network.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_slices', value: 'view', },
        { label: 'slices', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
location,
mobileNetworkName,
provisioning_state,
resourceGroupName,
sliceName,
snssai,
subscriptionId,
tags
FROM azure.mobile_network.vw_slices
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.mobile_network.slices
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>slices</code> resource.

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
INSERT INTO azure.mobile_network.slices (
mobileNetworkName,
resourceGroupName,
sliceName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ mobileNetworkName }}',
'{{ resourceGroupName }}',
'{{ sliceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: snssai
          value:
            - name: sst
              value: integer
            - name: sd
              value: string
        - name: description
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>slices</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.slices
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sliceName = '{{ sliceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
