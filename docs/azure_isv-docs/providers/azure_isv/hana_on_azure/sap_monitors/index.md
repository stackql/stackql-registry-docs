---
title: sap_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_monitors
  - hana_on_azure
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

Creates, updates, deletes, gets or lists a <code>sap_monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sap_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.hana_on_azure.sap_monitors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_monitors', value: 'view', },
        { label: 'sap_monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="enable_customer_analytics" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_analytics_workspace_arm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_analytics_workspace_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_analytics_workspace_shared_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_resource_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitor_subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sapMonitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sap_monitor_collector_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a SAP monitor. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapMonitorName, subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sapMonitorName, subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sapMonitorName, subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sapMonitorName, subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |

## `SELECT` examples

The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_monitors', value: 'view', },
        { label: 'sap_monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
enable_customer_analytics,
location,
log_analytics_workspace_arm_id,
log_analytics_workspace_id,
log_analytics_workspace_shared_key,
managed_resource_group_name,
monitor_subnet,
provisioning_state,
resourceGroupName,
sapMonitorName,
sap_monitor_collector_version,
subscriptionId,
tags
FROM azure_isv.hana_on_azure.vw_sap_monitors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure_isv.hana_on_azure.sap_monitors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sap_monitors</code> resource.

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
INSERT INTO azure_isv.hana_on_azure.sap_monitors (
resourceGroupName,
sapMonitorName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ sapMonitorName }}',
'{{ subscriptionId }}',
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
        - name: provisioningState
          value: string
        - name: managedResourceGroupName
          value: string
        - name: logAnalyticsWorkspaceArmId
          value: string
        - name: enableCustomerAnalytics
          value: boolean
        - name: logAnalyticsWorkspaceId
          value: string
        - name: logAnalyticsWorkspaceSharedKey
          value: string
        - name: sapMonitorCollectorVersion
          value: string
        - name: monitorSubnet
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sap_monitors</code> resource.

```sql
/*+ update */
UPDATE azure_isv.hana_on_azure.sap_monitors
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sapMonitorName = '{{ sapMonitorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sap_monitors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.hana_on_azure.sap_monitors
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sapMonitorName = '{{ sapMonitorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
