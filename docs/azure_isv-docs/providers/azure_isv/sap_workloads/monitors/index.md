---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - sap_workloads
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

Creates, updates, deletes, gets or lists a <code>monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.monitors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitors', value: 'view', },
        { label: 'monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="app_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_analytics_workspace_arm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resource_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitor_subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="msi_arm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routing_preference" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_arm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="zone_redundancy_preference" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a SAP monitor. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Gets properties of a SAP monitor for the specified subscription, resource group, and resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of SAP monitors in the specified resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Creates a SAP monitor for the specified subscription, resource group, and resource name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Deletes a SAP monitor with the specified subscription, resource group, and SAP monitor name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Patches the Tags field of a SAP monitor for the specified subscription, resource group, and SAP monitor name. |

## `SELECT` examples

Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitors', value: 'view', },
        { label: 'monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
app_location,
errors,
identity,
location,
log_analytics_workspace_arm_id,
managed_resource_group_configuration,
monitorName,
monitor_subnet,
msi_arm_id,
provisioning_state,
resourceGroupName,
routing_preference,
storage_account_arm_id,
subscriptionId,
tags,
zone_redundancy_preference
FROM azure_isv.sap_workloads.vw_monitors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure_isv.sap_workloads.monitors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>monitors</code> resource.

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
INSERT INTO azure_isv.sap_workloads.monitors (
monitorName,
resourceGroupName,
subscriptionId,
identity,
properties,
tags,
location
)
SELECT 
'{{ monitorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ identity }}',
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
    - name: identity
      value:
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: errors
          value: string
        - name: appLocation
          value: string
        - name: routingPreference
          value: string
        - name: zoneRedundancyPreference
          value: string
        - name: managedResourceGroupConfiguration
          value:
            - name: name
              value: string
        - name: logAnalyticsWorkspaceArmId
          value: string
        - name: monitorSubnet
          value: string
        - name: msiArmId
          value: string
        - name: storageAccountArmId
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>monitors</code> resource.

```sql
/*+ update */
UPDATE azure_isv.sap_workloads.monitors
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>monitors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.sap_workloads.monitors
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
