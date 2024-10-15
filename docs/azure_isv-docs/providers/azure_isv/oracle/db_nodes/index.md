---
title: db_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - db_nodes
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

Creates, updates, deletes, gets or lists a <code>db_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.db_nodes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_db_nodes', value: 'view', },
        { label: 'db_nodes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="additional_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_ip_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_vnic2_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="backup_vnic_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudvmclustername" /> | `text` | field from the `properties` object |
| <CopyableCode code="cpu_core_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_node_storage_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_server_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="db_system_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="dbnodeocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="fault_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_ip_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostname" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="lifecycle_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="maintenance_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="memory_size_in_gbs" /> | `text` | field from the `properties` object |
| <CopyableCode code="ocid" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="software_storage_size_in_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_maintenance_window_end" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_maintenance_window_start" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnic2_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnic_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of DbNodeResource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudvmclustername, dbnodeocid, resourceGroupName, subscriptionId" /> | Get a DbNode |
| <CopyableCode code="list_by_cloud_vm_cluster" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | List DbNode resources by CloudVmCluster |
| <CopyableCode code="action" /> | `EXEC` | <CopyableCode code="cloudvmclustername, dbnodeocid, resourceGroupName, subscriptionId, data__action" /> | VM actions on DbNode of VM Cluster by the provided filter |

## `SELECT` examples

List DbNode resources by CloudVmCluster

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_db_nodes', value: 'view', },
        { label: 'db_nodes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
additional_details,
backup_ip_id,
backup_vnic2_id,
backup_vnic_id,
cloudvmclustername,
cpu_core_count,
db_node_storage_size_in_gbs,
db_server_id,
db_system_id,
dbnodeocid,
fault_domain,
host_ip_id,
hostname,
lifecycle_details,
lifecycle_state,
maintenance_type,
memory_size_in_gbs,
ocid,
provisioning_state,
resourceGroupName,
software_storage_size_in_gb,
subscriptionId,
time_created,
time_maintenance_window_end,
time_maintenance_window_start,
vnic2_id,
vnic_id
FROM azure_isv.oracle.vw_db_nodes
WHERE cloudvmclustername = '{{ cloudvmclustername }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.db_nodes
WHERE cloudvmclustername = '{{ cloudvmclustername }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

