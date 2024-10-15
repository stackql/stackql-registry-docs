---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - peering
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="log_analytics_workspace_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="peeringServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_service_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="peering_service_provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_backup_peering_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_primary_peering_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU that defines the type of the peering service. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define connectivity to the Peering Service. |
| <CopyableCode code="sku" /> | `object` | The SKU that defines the type of the peering service. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Gets an existing peering service with the specified name under the given subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the peering services under the given subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the peerings under the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId, data__location" /> | Creates a new peering service or updates an existing peering with the specified name under the given subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Deletes an existing peering service with the specified name under the given subscription and resource group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Updates tags for a peering service with the specified name under the given subscription and resource group. |
| <CopyableCode code="initialize_connection_monitor" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Initialize Peering Service for Connection Monitor functionality |

## `SELECT` examples

Lists all of the peerings under the given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
log_analytics_workspace_properties,
peeringServiceName,
peering_service_location,
peering_service_provider,
provider_backup_peering_location,
provider_primary_peering_location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
type
FROM azure.peering.vw_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
sku,
tags,
type
FROM azure.peering.services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO azure.peering.services (
peeringServiceName,
resourceGroupName,
subscriptionId,
data__location,
sku,
properties,
location,
tags
)
SELECT 
'{{ peeringServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ sku }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: sku
      value:
        - name: name
          value: string
    - name: properties
      value:
        - name: peeringServiceLocation
          value: string
        - name: peeringServiceProvider
          value: string
        - name: provisioningState
          value: string
        - name: providerPrimaryPeeringLocation
          value: string
        - name: providerBackupPeeringLocation
          value: string
        - name: logAnalyticsWorkspaceProperties
          value:
            - name: workspaceID
              value: string
            - name: key
              value: string
            - name: connectedAgents
              value:
                - string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure.peering.services
SET 
tags = '{{ tags }}'
WHERE 
peeringServiceName = '{{ peeringServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.peering.services
WHERE peeringServiceName = '{{ peeringServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
