---
title: import_machines_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - import_machines_controllers
  - migrate
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

Creates, updates, deletes, gets or lists a <code>import_machines_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_machines_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.import_machines_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_import_machines_controllers', value: 'view', },
        { label: 'import_machines_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allocated_memory_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="bios_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="bios_serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="firmware" /> | `text` | field from the `properties` object |
| <CopyableCode code="hypervisor" /> | `text` | field from the `properties` object |
| <CopyableCode code="hypervisor_version_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="mac_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="machineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_manager_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_in_throughput" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_out_throughput" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_network_adapters" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_processor_core" /> | `text` | field from the `properties` object |
| <CopyableCode code="operating_system_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="percentage_cpu_utilization" /> | `text` | field from the `properties` object |
| <CopyableCode code="percentage_memory_utilization" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_in_use_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_disk_read_operations_per_second" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_disk_read_throughput" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_disk_write_operations_per_second" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_disk_write_throughput" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_fqdn" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for machine properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Get a ImportMachine |
| <CopyableCode code="list_by_import_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List ImportMachine resources by ImportSite |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Delete a ImportMachine |

## `SELECT` examples

List ImportMachine resources by ImportSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_import_machines_controllers', value: 'view', },
        { label: 'import_machines_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allocated_memory_in_mb,
bios_guid,
bios_serial_number,
created_timestamp,
disks,
display_name,
firmware,
hypervisor,
hypervisor_version_number,
ip_addresses,
is_deleted,
mac_address,
machineName,
machine_id,
machine_manager_id,
network_in_throughput,
network_out_throughput,
number_of_disks,
number_of_network_adapters,
number_of_processor_core,
operating_system_details,
percentage_cpu_utilization,
percentage_memory_utilization,
provisioning_state,
resourceGroupName,
server_type,
siteName,
storage_in_use_gb,
subscriptionId,
tags,
total_disk_read_operations_per_second,
total_disk_read_throughput,
total_disk_write_operations_per_second,
total_disk_write_throughput,
updated_timestamp,
vm_fqdn
FROM azure.migrate.vw_import_machines_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.import_machines_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>import_machines_controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.import_machines_controllers
WHERE machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
