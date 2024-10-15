---
title: fabric_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - fabric_locations
  - fabric_admin
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

Creates, updates, deletes, gets or lists a <code>fabric_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fabric_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.fabric_admin.fabric_locations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fabric_locations', value: 'view', },
        { label: 'fabric_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="data_geo_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="exclusive_admin_operation_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="exclusive_admin_operation_running" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_dnsip_address01" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_dnsip_address02" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricLocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The region where the resource is located. |
| <CopyableCode code="pep_ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shut_down_action_plan_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="shut_down_action_plan_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="stamp_cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="stamp_information_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_up_action_plan_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_up_action_plan_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key-value pairs. |
| <CopyableCode code="time_server" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | The region where the resource is located. |
| <CopyableCode code="properties" /> | `object` | All properties of a fabric location resource. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fabricLocation, resourceGroupName, subscriptionId" /> | Returns the requested fabric location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns a list of all fabric locations. |

## `SELECT` examples

Returns a list of all fabric locations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_fabric_locations', value: 'view', },
        { label: 'fabric_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
data_geo_location,
exclusive_admin_operation_name,
exclusive_admin_operation_running,
external_dnsip_address01,
external_dnsip_address02,
fabricLocation,
location,
pep_ip_addresses,
resourceGroupName,
shut_down_action_plan_end_time,
shut_down_action_plan_start_time,
stamp_cloud_id,
stamp_information_id,
start_up_action_plan_end_time,
start_up_action_plan_start_time,
subscriptionId,
tags,
time_server,
type
FROM azure_stack.fabric_admin.vw_fabric_locations
WHERE resourceGroupName = '{{ resourceGroupName }}'
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
tags,
type
FROM azure_stack.fabric_admin.fabric_locations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

