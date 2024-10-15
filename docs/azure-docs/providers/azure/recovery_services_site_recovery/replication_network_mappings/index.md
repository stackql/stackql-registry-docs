---
title: replication_network_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_network_mappings
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_network_mappings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_network_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_network_mappings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_network_mappings', value: 'view', },
        { label: 'replication_network_mappings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_specific_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="networkMappingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="networkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_network_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_network_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_fabric_arm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_network_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_network_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Network Mapping Properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an ASR network mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists all ASR network mappings in the vault. |
| <CopyableCode code="list_by_replication_networks" /> | `SELECT` | <CopyableCode code="fabricName, networkName, resourceGroupName, resourceName, subscriptionId" /> | Lists all ASR network mappings for the specified network. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to create an ASR network mapping. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete a network mapping. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fabricName, networkMappingName, networkName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update an ASR network mapping. |

## `SELECT` examples

Lists all ASR network mappings in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_network_mappings', value: 'view', },
        { label: 'replication_network_mappings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
fabricName,
fabric_specific_settings,
location,
networkMappingName,
networkName,
primary_fabric_friendly_name,
primary_network_friendly_name,
primary_network_id,
recovery_fabric_arm_id,
recovery_fabric_friendly_name,
recovery_network_friendly_name,
recovery_network_id,
resourceGroupName,
resourceName,
state,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_replication_network_mappings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.recovery_services_site_recovery.replication_network_mappings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_network_mappings</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_network_mappings (
fabricName,
networkMappingName,
networkName,
resourceGroupName,
resourceName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ fabricName }}',
'{{ networkMappingName }}',
'{{ networkName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: recoveryFabricName
          value: string
        - name: recoveryNetworkId
          value: string
        - name: fabricSpecificDetails
          value:
            - name: instanceType
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replication_network_mappings</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services_site_recovery.replication_network_mappings
SET 
properties = '{{ properties }}'
WHERE 
fabricName = '{{ fabricName }}'
AND networkMappingName = '{{ networkMappingName }}'
AND networkName = '{{ networkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>replication_network_mappings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_network_mappings
WHERE fabricName = '{{ fabricName }}'
AND networkMappingName = '{{ networkMappingName }}'
AND networkName = '{{ networkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
