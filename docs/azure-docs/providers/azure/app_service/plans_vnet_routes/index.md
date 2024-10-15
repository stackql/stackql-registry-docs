---
title: plans_vnet_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - plans_vnet_routes
  - app_service
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

Creates, updates, deletes, gets or lists a <code>plans_vnet_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans_vnet_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.plans_vnet_routes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, routeName, subscriptionId, vnetName" /> | Description for Create or update a Virtual Network route in an App Service plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, routeName, subscriptionId, vnetName" /> | Description for Delete a Virtual Network route in an App Service plan. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, routeName, subscriptionId, vnetName" /> | Description for Create or update a Virtual Network route in an App Service plan. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>plans_vnet_routes</code> resource.

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
INSERT INTO azure.app_service.plans_vnet_routes (
name,
resourceGroupName,
routeName,
subscriptionId,
vnetName,
kind,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ routeName }}',
'{{ subscriptionId }}',
'{{ vnetName }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: startAddress
          value: string
        - name: endAddress
          value: string
        - name: routeType
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>plans_vnet_routes</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.plans_vnet_routes
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND routeName = '{{ routeName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```

## `DELETE` example

Deletes the specified <code>plans_vnet_routes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.plans_vnet_routes
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND routeName = '{{ routeName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vnetName = '{{ vnetName }}';
```
