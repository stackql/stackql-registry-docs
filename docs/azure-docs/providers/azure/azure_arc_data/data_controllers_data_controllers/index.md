---
title: data_controllers_data_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_controllers_data_controllers
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>data_controllers_data_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_controllers_data_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.data_controllers_data_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_controllers_data_controllers', value: 'view', },
        { label: 'data_controllers_data_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="basic_login_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataControllerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="extension_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="infrastructure" /> | `text` | field from the `properties` object |
| <CopyableCode code="k8s_raw" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_uploaded_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_analytics_workspace_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="logs_dashboard_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="metrics_dashboard_credential" /> | `text` | field from the `properties` object |
| <CopyableCode code="on_premise_property" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="upload_service_principal" /> | `text` | field from the `properties` object |
| <CopyableCode code="upload_watermark" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The data controller properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataControllerName, resourceGroupName, subscriptionId" /> | Retrieves a dataController resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataControllerName, resourceGroupName, subscriptionId" /> | Deletes a dataController resource |

## `SELECT` examples

Retrieves a dataController resource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_controllers_data_controllers', value: 'view', },
        { label: 'data_controllers_data_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
basic_login_information,
cluster_id,
dataControllerName,
extended_location,
extension_id,
infrastructure,
k8s_raw,
last_uploaded_date,
location,
log_analytics_workspace_config,
logs_dashboard_credential,
metrics_dashboard_credential,
on_premise_property,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
upload_service_principal,
upload_watermark
FROM azure.azure_arc_data.vw_data_controllers_data_controllers
WHERE dataControllerName = '{{ dataControllerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.azure_arc_data.data_controllers_data_controllers
WHERE dataControllerName = '{{ dataControllerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>data_controllers_data_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.azure_arc_data.data_controllers_data_controllers
WHERE dataControllerName = '{{ dataControllerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
