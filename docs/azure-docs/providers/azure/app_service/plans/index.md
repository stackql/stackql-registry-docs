---
title: plans
hide_title: false
hide_table_of_contents: false
keywords:
  - plans
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

Creates, updates, deletes, gets or lists a <code>plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.plans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="extendedLocation" /> | `object` | Extended Location. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | AppServicePlan resource specific properties |
| <CopyableCode code="sku" /> | `object` | Description of a SKU for a scalable resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Get an App Service plan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all App Service plans for a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get all App Service plans in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates or updates an App Service Plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Delete an App Service plan. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Creates or updates an App Service Plan. |
| <CopyableCode code="get_vnet_route" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, routeName, subscriptionId, vnetName" /> | Description for Get a Virtual Network route in an App Service plan. |
| <CopyableCode code="list_vnet_route" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, vnetName" /> | Description for Get all routes that are associated with a Virtual Network in an App Service plan. |
| <CopyableCode code="reboot_worker" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, workerName" /> | Description for Reboot a worker machine in an App Service plan. |
| <CopyableCode code="restart_web_apps" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Restart all apps in an App Service plan. |

## `SELECT` examples

Description for Get all App Service plans for a subscription.


```sql
SELECT
id,
name,
extendedLocation,
kind,
location,
properties,
sku,
tags,
type
FROM azure.app_service.plans
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>plans</code> resource.

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
INSERT INTO azure.app_service.plans (
name,
resourceGroupName,
subscriptionId,
kind,
location,
tags,
properties,
sku,
extendedLocation
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}',
'{{ sku }}',
'{{ extendedLocation }}'
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
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: workerTierName
          value: string
        - name: status
          value: string
        - name: subscription
          value: string
        - name: hostingEnvironmentProfile
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: type
              value: string
        - name: maximumNumberOfWorkers
          value: integer
        - name: numberOfWorkers
          value: integer
        - name: geoRegion
          value: string
        - name: perSiteScaling
          value: boolean
        - name: elasticScaleEnabled
          value: boolean
        - name: maximumElasticWorkerCount
          value: integer
        - name: numberOfSites
          value: integer
        - name: isSpot
          value: boolean
        - name: spotExpirationTime
          value: string
        - name: freeOfferExpirationTime
          value: string
        - name: resourceGroup
          value: string
        - name: reserved
          value: boolean
        - name: isXenon
          value: boolean
        - name: hyperV
          value: boolean
        - name: targetWorkerCount
          value: integer
        - name: targetWorkerSizeId
          value: integer
        - name: provisioningState
          value: string
        - name: kubeEnvironmentProfile
          value:
            - name: id
              value: string
            - name: name
              value: string
            - name: type
              value: string
        - name: zoneRedundant
          value: boolean
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
        - name: skuCapacity
          value:
            - name: minimum
              value: integer
            - name: maximum
              value: integer
            - name: elasticMaximum
              value: integer
            - name: default
              value: integer
            - name: scaleType
              value: string
        - name: locations
          value:
            - string
        - name: capabilities
          value:
            - - name: name
                value: string
              - name: value
                value: string
              - name: reason
                value: string
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>plans</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.plans
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>plans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.plans
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
