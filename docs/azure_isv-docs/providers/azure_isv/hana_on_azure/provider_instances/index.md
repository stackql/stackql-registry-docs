---
title: provider_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_instances
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

Creates, updates, deletes, gets or lists a <code>provider_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.hana_on_azure.provider_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provider_instances', value: 'view', },
        { label: 'provider_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Describes the properties of a provider instance. |
| <CopyableCode code="providerInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sapMonitorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of a provider instance. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sapMonitorName, subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerInstanceName, resourceGroupName, sapMonitorName, subscriptionId" /> | The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023. |

## `SELECT` examples

The product Microsoft.Workloads/sapMonitors (AMS Classic) is officially retired as of May 31, 2023.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_provider_instances', value: 'view', },
        { label: 'provider_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
metadata,
properties,
providerInstanceName,
provisioning_state,
resourceGroupName,
sapMonitorName,
subscriptionId,
type
FROM azure_isv.hana_on_azure.vw_provider_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sapMonitorName = '{{ sapMonitorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.hana_on_azure.provider_instances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sapMonitorName = '{{ sapMonitorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_instances</code> resource.

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
INSERT INTO azure_isv.hana_on_azure.provider_instances (
providerInstanceName,
resourceGroupName,
sapMonitorName,
subscriptionId,
properties
)
SELECT 
'{{ providerInstanceName }}',
'{{ resourceGroupName }}',
'{{ sapMonitorName }}',
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
        - name: type
          value: string
        - name: properties
          value: string
        - name: metadata
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>provider_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure_isv.hana_on_azure.provider_instances
WHERE providerInstanceName = '{{ providerInstanceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sapMonitorName = '{{ sapMonitorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
