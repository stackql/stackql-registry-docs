---
title: associations_interfaces
hide_title: false
hide_table_of_contents: false
keywords:
  - associations_interfaces
  - service_networking
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

Creates, updates, deletes, gets or lists a <code>associations_interfaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>associations_interfaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_networking.associations_interfaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_associations_interfaces', value: 'view', },
        { label: 'associations_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="associationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="association_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="trafficControllerName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Association Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="associationName, resourceGroupName, subscriptionId, trafficControllerName" /> | Get a Association |
| <CopyableCode code="list_by_traffic_controller" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, trafficControllerName" /> | List Association resources by TrafficController |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="associationName, resourceGroupName, subscriptionId, trafficControllerName" /> | Create a Association |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="associationName, resourceGroupName, subscriptionId, trafficControllerName" /> | Delete a Association |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="associationName, resourceGroupName, subscriptionId, trafficControllerName" /> | Update a Association |

## `SELECT` examples

List Association resources by TrafficController

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_associations_interfaces', value: 'view', },
        { label: 'associations_interfaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
associationName,
association_type,
location,
provisioning_state,
resourceGroupName,
subnet,
subscriptionId,
tags,
trafficControllerName
FROM azure.service_networking.vw_associations_interfaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.service_networking.associations_interfaces
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>associations_interfaces</code> resource.

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
INSERT INTO azure.service_networking.associations_interfaces (
associationName,
resourceGroupName,
subscriptionId,
trafficControllerName,
properties,
tags,
location
)
SELECT 
'{{ associationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ trafficControllerName }}',
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
        - name: associationType
          value: []
        - name: subnet
          value:
            - name: id
              value: string
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>associations_interfaces</code> resource.

```sql
/*+ update */
UPDATE azure.service_networking.associations_interfaces
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
associationName = '{{ associationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```

## `DELETE` example

Deletes the specified <code>associations_interfaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_networking.associations_interfaces
WHERE associationName = '{{ associationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trafficControllerName = '{{ trafficControllerName }}';
```
