---
title: sap_landscape_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_landscape_monitors
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

Creates, updates, deletes, gets or lists a <code>sap_landscape_monitors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sap_landscape_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.sap_workloads.sap_landscape_monitors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_landscape_monitors', value: 'view', },
        { label: 'sap_landscape_monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="grouping" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="top_metrics_thresholds" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Gets or sets the properties for Sap Landscape Monitor Dashboard. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Gets configuration values for Single Pane Of Glass for SAP monitor for the specified subscription, resource group, and resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Gets configuration values for Single Pane Of Glass for SAP monitor for the specified subscription, resource group, and resource name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Creates a SAP Landscape Monitor Dashboard for the specified subscription, resource group, and resource name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Deletes a SAP Landscape Monitor Dashboard with the specified subscription, resource group, and SAP monitor name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> | Patches the SAP Landscape Monitor Dashboard for the specified subscription, resource group, and SAP monitor name. |

## `SELECT` examples

Gets configuration values for Single Pane Of Glass for SAP monitor for the specified subscription, resource group, and resource name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sap_landscape_monitors', value: 'view', },
        { label: 'sap_landscape_monitors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
grouping,
monitorName,
provisioning_state,
resourceGroupName,
subscriptionId,
top_metrics_thresholds
FROM azure_isv.sap_workloads.vw_sap_landscape_monitors
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.sap_workloads.sap_landscape_monitors
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sap_landscape_monitors</code> resource.

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
INSERT INTO azure_isv.sap_workloads.sap_landscape_monitors (
monitorName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ monitorName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: provisioningState
          value: string
        - name: grouping
          value:
            - name: landscape
              value:
                - - name: name
                    value: string
                  - name: topSid
                    value:
                      - string
            - name: sapApplication
              value:
                - - name: name
                    value: string
                  - name: topSid
                    value:
                      - string
        - name: topMetricsThresholds
          value:
            - - name: name
                value: string
              - name: green
                value: number
              - name: yellow
                value: number
              - name: red
                value: number

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sap_landscape_monitors</code> resource.

```sql
/*+ update */
UPDATE azure_isv.sap_workloads.sap_landscape_monitors
SET 
properties = '{{ properties }}'
WHERE 
monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>sap_landscape_monitors</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.sap_workloads.sap_landscape_monitors
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
