---
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>private_clouds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.private_clouds" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_clouds', value: 'view', },
        { label: 'private_clouds', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure Id, e.g. "/subscriptions/4da99247-a172-4ed6-8ae9-ebed2d12f839/providers/Microsoft.VMwareCloudSimple/privateClouds/cloud123" |
| <CopyableCode code="name" /> | `text` | Private cloud name |
| <CopyableCode code="availability_zone_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_zone_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusters_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_servers" /> | `text` | field from the `properties` object |
| <CopyableCode code="expires" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location where private cloud created, e.g "westus" |
| <CopyableCode code="nsx_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="pcName" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="placement_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="regionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_pools" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_cpu_cores" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_nodes" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_ram" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_storage" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure Resource type |
| <CopyableCode code="v_sphere_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vcenter_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="vcenter_refid" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine_templates" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_networks" /> | `text` | field from the `properties` object |
| <CopyableCode code="vr_ops_enabled" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure Id, e.g. "/subscriptions/4da99247-a172-4ed6-8ae9-ebed2d12f839/providers/Microsoft.VMwareCloudSimple/privateClouds/cloud123" |
| <CopyableCode code="name" /> | `string` | Private cloud name |
| <CopyableCode code="location" /> | `string` | Location where private cloud created, e.g "westus" |
| <CopyableCode code="properties" /> | `object` | Properties of private |
| <CopyableCode code="type" /> | `string` | Azure Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pcName, regionId, subscriptionId" /> | Returns private cloud by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="regionId, subscriptionId" /> | Returns list of private clouds in particular region |

## `SELECT` examples

Returns list of private clouds in particular region

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_private_clouds', value: 'view', },
        { label: 'private_clouds', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
availability_zone_id,
availability_zone_name,
clusters_number,
created_by,
created_on,
dns_servers,
expires,
location,
nsx_type,
pcName,
placement_group_id,
placement_group_name,
private_cloud_id,
regionId,
resource_pools,
state,
subscriptionId,
total_cpu_cores,
total_nodes,
total_ram,
total_storage,
type,
v_sphere_version,
vcenter_fqdn,
vcenter_refid,
virtual_machine_templates,
virtual_networks,
vr_ops_enabled
FROM azure_isv.vmware_cloud_simple.vw_private_clouds
WHERE regionId = '{{ regionId }}'
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
FROM azure_isv.vmware_cloud_simple.private_clouds
WHERE regionId = '{{ regionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

