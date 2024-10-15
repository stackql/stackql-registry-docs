---
title: azure_traffic_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_traffic_collectors
  - network_function
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

Creates, updates, deletes, gets or lists a <code>azure_traffic_collectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>azure_traffic_collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_function.azure_traffic_collectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_traffic_collectors', value: 'view', },
        { label: 'azure_traffic_collectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="azureTrafficCollectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="collector_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_hub" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Azure Traffic Collector resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureTrafficCollectorName, resourceGroupName, subscriptionId" /> | Gets the specified Azure Traffic Collector in a specified resource group |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="azureTrafficCollectorName, resourceGroupName, subscriptionId" /> | Creates or updates a Azure Traffic Collector resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureTrafficCollectorName, resourceGroupName, subscriptionId" /> | Deletes a specified Azure Traffic Collector resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="azureTrafficCollectorName, resourceGroupName, subscriptionId" /> | Updates the specified Azure Traffic Collector tags. |

## `SELECT` examples

Gets the specified Azure Traffic Collector in a specified resource group

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_azure_traffic_collectors', value: 'view', },
        { label: 'azure_traffic_collectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
azureTrafficCollectorName,
collector_policies,
etag,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
tags,
type,
virtual_hub
FROM azure.network_function.vw_azure_traffic_collectors
WHERE azureTrafficCollectorName = '{{ azureTrafficCollectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.network_function.azure_traffic_collectors
WHERE azureTrafficCollectorName = '{{ azureTrafficCollectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>azure_traffic_collectors</code> resource.

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
INSERT INTO azure.network_function.azure_traffic_collectors (
azureTrafficCollectorName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ azureTrafficCollectorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: collectorPolicies
          value:
            - - name: id
                value: string
        - name: virtualHub
          value:
            - name: id
              value: string
        - name: provisioningState
          value: []
    - name: etag
      value: string
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
    - name: systemData
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>azure_traffic_collectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network_function.azure_traffic_collectors
WHERE azureTrafficCollectorName = '{{ azureTrafficCollectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
