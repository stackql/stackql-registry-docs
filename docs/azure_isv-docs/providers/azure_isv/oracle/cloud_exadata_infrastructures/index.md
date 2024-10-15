---
title: cloud_exadata_infrastructures
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_exadata_infrastructures
  - oracle
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

Creates, updates, deletes, gets or lists a <code>cloud_exadata_infrastructures</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_exadata_infrastructures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.cloud_exadata_infrastructures" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_exadata_infrastructures', value: 'view', },
        { label: 'cloud_exadata_infrastructures', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activated_storage_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="additional_storage_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudexadatainfrastructurename" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_contacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_storage_size_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_node_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_server_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="estimated_patching_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_maintenance_run_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="maintenance_window" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_cpu_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_data_storage_in_tbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_db_node_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_memory_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="memory_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="monthly_db_server_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="monthly_storage_server_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_maintenance_run_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="oci_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shape" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_server_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="zones" /> | `text` | CloudExadataInfrastructure zones |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | CloudExadataInfrastructure resource model |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | CloudExadataInfrastructure zones |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | Get a CloudExadataInfrastructure |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List CloudExadataInfrastructure resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List CloudExadataInfrastructure resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId, data__zones" /> | Create a CloudExadataInfrastructure |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | Delete a CloudExadataInfrastructure |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | Update a CloudExadataInfrastructure |
| <CopyableCode code="add_storage_capacity" /> | `EXEC` | <CopyableCode code="cloudexadatainfrastructurename, resourceGroupName, subscriptionId" /> | Perform add storage capacity on exadata infra |

## `SELECT` examples

List CloudExadataInfrastructure resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_exadata_infrastructures', value: 'view', },
        { label: 'cloud_exadata_infrastructures', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
activated_storage_count,
additional_storage_count,
available_storage_size_in_gbs,
cloudexadatainfrastructurename,
compute_count,
cpu_count,
customer_contacts,
data_storage_size_in_tbs,
db_node_storage_size_in_gbs,
db_server_version,
display_name,
estimated_patching_time,
last_maintenance_run_id,
lifecycle_details,
lifecycle_state,
location,
maintenance_window,
max_cpu_count,
max_data_storage_in_tbs,
max_db_node_storage_size_in_gbs,
max_memory_in_gbs,
memory_size_in_gbs,
monthly_db_server_version,
monthly_storage_server_version,
next_maintenance_run_id,
oci_url,
ocid,
provisioning_state,
resourceGroupName,
shape,
storage_count,
storage_server_version,
subscriptionId,
tags,
time_created,
total_storage_size_in_gbs,
zones
FROM azure_isv.oracle.vw_cloud_exadata_infrastructures
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags,
zones
FROM azure_isv.oracle.cloud_exadata_infrastructures
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_exadata_infrastructures</code> resource.

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
INSERT INTO azure_isv.oracle.cloud_exadata_infrastructures (
cloudexadatainfrastructurename,
resourceGroupName,
subscriptionId,
data__zones,
properties,
zones,
tags,
location
)
SELECT 
'{{ cloudexadatainfrastructurename }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__zones }}',
'{{ properties }}',
'{{ zones }}',
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
        - name: ocid
          value: []
        - name: computeCount
          value: integer
        - name: storageCount
          value: integer
        - name: totalStorageSizeInGbs
          value: integer
        - name: availableStorageSizeInGbs
          value: integer
        - name: timeCreated
          value: string
        - name: lifecycleDetails
          value: string
        - name: maintenanceWindow
          value:
            - name: preference
              value: []
            - name: months
              value:
                - - name: name
                    value: []
            - name: weeksOfMonth
              value:
                - integer
            - name: daysOfWeek
              value:
                - - name: name
                    value: []
            - name: hoursOfDay
              value:
                - integer
            - name: leadTimeInWeeks
              value: integer
            - name: patchingMode
              value: []
            - name: customActionTimeoutInMins
              value: integer
            - name: isCustomActionTimeoutEnabled
              value: boolean
            - name: isMonthlyPatchingEnabled
              value: boolean
        - name: estimatedPatchingTime
          value:
            - name: estimatedDbServerPatchingTime
              value: integer
            - name: estimatedNetworkSwitchesPatchingTime
              value: integer
            - name: estimatedStorageServerPatchingTime
              value: integer
            - name: totalEstimatedPatchingTime
              value: integer
        - name: customerContacts
          value:
            - - name: email
                value: string
        - name: provisioningState
          value: []
        - name: lifecycleState
          value: []
        - name: shape
          value: string
        - name: ociUrl
          value: string
        - name: cpuCount
          value: integer
        - name: maxCpuCount
          value: integer
        - name: memorySizeInGbs
          value: integer
        - name: maxMemoryInGbs
          value: integer
        - name: dbNodeStorageSizeInGbs
          value: integer
        - name: maxDbNodeStorageSizeInGbs
          value: integer
        - name: dataStorageSizeInTbs
          value: number
        - name: maxDataStorageInTbs
          value: number
        - name: dbServerVersion
          value: string
        - name: storageServerVersion
          value: string
        - name: activatedStorageCount
          value: integer
        - name: additionalStorageCount
          value: integer
        - name: displayName
          value: string
        - name: monthlyDbServerVersion
          value: string
        - name: monthlyStorageServerVersion
          value: string
    - name: zones
      value:
        - string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>cloud_exadata_infrastructures</code> resource.

```sql
/*+ update */
UPDATE azure_isv.oracle.cloud_exadata_infrastructures
SET 
zones = '{{ zones }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>cloud_exadata_infrastructures</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.oracle.cloud_exadata_infrastructures
WHERE cloudexadatainfrastructurename = '{{ cloudexadatainfrastructurename }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
