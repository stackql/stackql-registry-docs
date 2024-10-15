---
title: machines_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - machines_controllers
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

Creates, updates, deletes, gets or lists a <code>machines_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>machines_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.machines_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_machines_controllers', value: 'view', },
        { label: 'machines_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="allocated_memory_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="alt_guest_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="appliance_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="apps_and_roles" /> | `text` | field from the `properties` object |
| <CopyableCode code="bios_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="bios_serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="change_tracking_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="change_tracking_supported" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_center_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_map_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_enabled_uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="firmware" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_details_discovery_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_os_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_in_maintenance_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_power_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="iis_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_guest_details_discovery_in_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="machineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_snapshots" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_adapters" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_applications" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_processor_core" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_snapshots" /> | `text` | field from the `properties` object |
| <CopyableCode code="operating_system_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="oracle_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_support_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spring_boot_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="static_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="tomcat_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_center_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_center_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_mware_tools_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="v_mware_tools_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_configuration_file_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_app_discovery" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Class for machine properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Get a MachineResource |
| <CopyableCode code="list_by_vmware_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List MachineResource resources by VmwareSite |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Update a MachineResource |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Method to start a machine. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Method to stop a machine. |

## `SELECT` examples

List MachineResource resources by VmwareSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_machines_controllers', value: 'view', },
        { label: 'machines_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
allocated_memory_in_mb,
alt_guest_name,
appliance_names,
application_discovery,
apps_and_roles,
bios_guid,
bios_serial_number,
change_tracking_enabled,
change_tracking_supported,
created_timestamp,
data_center_scope,
dependency_map_discovery,
dependency_mapping,
dependency_mapping_end_time,
dependency_mapping_start_time,
disk_enabled_uuid,
disks,
display_name,
errors,
firmware,
guest_details_discovery_timestamp,
guest_os_details,
host_in_maintenance_mode,
host_name,
host_power_state,
host_version,
iis_discovery,
instance_uuid,
is_deleted,
is_guest_details_discovery_in_progress,
machineName,
max_snapshots,
network_adapters,
number_of_applications,
number_of_processor_core,
number_of_snapshots,
operating_system_details,
oracle_discovery,
power_status,
product_support_status,
provisioning_state,
resourceGroupName,
run_as_account_id,
siteName,
spring_boot_discovery,
sql_discovery,
static_discovery,
subscriptionId,
tags,
tomcat_discovery,
updated_timestamp,
v_center_fqdn,
v_center_id,
v_mware_tools_status,
v_mware_tools_version,
vm_configuration_file_location,
vm_fqdn,
web_app_discovery
FROM azure.migrate.vw_machines_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.machines_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>machines_controllers</code> resource.

```sql
/*+ update */
UPDATE azure.migrate.machines_controllers
SET 
properties = '{{ properties }}'
WHERE 
machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
