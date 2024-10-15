---
title: disk_accesses
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_accesses
  - compute
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

Creates, updates, deletes, gets or lists a <code>disk_accesses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_accesses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.disk_accesses" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_accesses', value: 'view', },
        { label: 'disk_accesses', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="diskAccessName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | Gets information about a disk access resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the disk access resources under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the disk access resources under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | Creates or updates a disk access resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | Deletes a disk access resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="diskAccessName, resourceGroupName, subscriptionId" /> | Updates (patches) a disk access resource. |

## `SELECT` examples

Lists all the disk access resources under a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disk_accesses', value: 'view', },
        { label: 'disk_accesses', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
diskAccessName,
extended_location,
location,
private_endpoint_connections,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
time_created,
type
FROM azure.compute.vw_disk_accesses
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
extendedLocation,
location,
properties,
tags,
type
FROM azure.compute.disk_accesses
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>disk_accesses</code> resource.

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
INSERT INTO azure.compute.disk_accesses (
diskAccessName,
resourceGroupName,
subscriptionId,
properties,
extendedLocation,
location,
tags
)
SELECT 
'{{ diskAccessName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: []
              - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
        - name: provisioningState
          value: string
        - name: timeCreated
          value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>disk_accesses</code> resource.

```sql
/*+ update */
UPDATE azure.compute.disk_accesses
SET 
tags = '{{ tags }}'
WHERE 
diskAccessName = '{{ diskAccessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>disk_accesses</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.disk_accesses
WHERE diskAccessName = '{{ diskAccessName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
