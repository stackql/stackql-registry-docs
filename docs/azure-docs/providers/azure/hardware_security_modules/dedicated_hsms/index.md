---
title: dedicated_hsms
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hsms
  - hardware_security_modules
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

Creates, updates, deletes, gets or lists a <code>dedicated_hsms</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_hsms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.dedicated_hsms" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_hsms', value: 'view', },
        { label: 'dedicated_hsms', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="management_network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="stamp_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="zones" /> | `text` | The Dedicated Hsm zones. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the dedicated hsm |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | The Dedicated Hsm zones. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Gets the specified Azure dedicated HSM. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the dedicated hsms associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the dedicated HSMs associated with the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__location, data__properties, data__sku" /> | Create or Update a dedicated HSM in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Deletes the specified Azure Dedicated HSM. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Update a dedicated HSM in the specified subscription. |

## `SELECT` examples

The List operation gets information about the dedicated HSMs associated with the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dedicated_hsms', value: 'view', },
        { label: 'dedicated_hsms', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
location,
management_network_profile,
network_profile,
provisioning_state,
resourceGroupName,
sku,
stamp_id,
status_message,
subscriptionId,
tags,
zones
FROM azure.hardware_security_modules.vw_dedicated_hsms
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags,
zones
FROM azure.hardware_security_modules.dedicated_hsms
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dedicated_hsms</code> resource.

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
INSERT INTO azure.hardware_security_modules.dedicated_hsms (
name,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
data__sku,
sku,
zones,
properties,
tags,
location
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ sku }}',
'{{ zones }}',
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
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: zones
      value:
        - string
    - name: properties
      value:
        - name: networkProfile
          value:
            - name: subnet
              value:
                - name: resourceId
                  value: string
            - name: networkInterfaces
              value:
                - - name: resourceId
                    value: string
                  - name: privateIpAddress
                    value: string
        - name: stampId
          value: string
        - name: statusMessage
          value: string
        - name: provisioningState
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dedicated_hsms</code> resource.

```sql
/*+ update */
UPDATE azure.hardware_security_modules.dedicated_hsms
SET 
tags = '{{ tags }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dedicated_hsms</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hardware_security_modules.dedicated_hsms
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
