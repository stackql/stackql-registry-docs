---
title: hyperv_machines_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - hyperv_machines_controllers
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

Creates, updates, deletes, gets or lists a <code>hyperv_machines_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hyperv_machines_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.hyperv_machines_controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hyperv_machines_controllers', value: 'view', },
        { label: 'hyperv_machines_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allocated_memory_in_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="appliance_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="apps_and_roles" /> | `text` | field from the `properties` object |
| <CopyableCode code="bios_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="bios_serial_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_protection_requested" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_map_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="encrypt_state_and_vm_migration_traffic" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="firmware" /> | `text` | field from the `properties` object |
| <CopyableCode code="generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_details_discovery_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_os_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="high_availability" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="iis_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_uuid" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_dynamic_memory_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_guest_details_discovery_in_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="ksd_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="machineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_server_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_memory_mb" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_adapters" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_applications" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_processor_core" /> | `text` | field from the `properties` object |
| <CopyableCode code="operating_system_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="oracle_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_support_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="secure_boot_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="secure_boot_template" /> | `text` | field from the `properties` object |
| <CopyableCode code="secure_boot_template_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="shielding_requested" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spring_boot_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="sql_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="static_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="tomcat_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="tpm_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualization_based_security_opt_out" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_configuration_file_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_app_discovery" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of AddressResource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Get a HypervMachine |
| <CopyableCode code="list_by_hyperv_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List HypervMachine resources by HypervSite |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Update a HypervMachine |

## `SELECT` examples

List HypervMachine resources by HypervSite

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hyperv_machines_controllers', value: 'view', },
        { label: 'hyperv_machines_controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allocated_memory_in_mb,
appliance_names,
application_discovery,
apps_and_roles,
bios_guid,
bios_serial_number,
cluster_fqdn,
cluster_id,
created_timestamp,
data_protection_requested,
dependency_map_discovery,
dependency_mapping,
dependency_mapping_end_time,
dependency_mapping_start_time,
disks,
display_name,
encrypt_state_and_vm_migration_traffic,
errors,
firmware,
generation,
guest_details_discovery_timestamp,
guest_os_details,
high_availability,
host_fqdn,
host_id,
iis_discovery,
instance_uuid,
is_deleted,
is_dynamic_memory_enabled,
is_guest_details_discovery_in_progress,
ksd_enabled,
machineName,
management_server_type,
max_memory_mb,
network_adapters,
number_of_applications,
number_of_processor_core,
operating_system_details,
oracle_discovery,
power_status,
product_support_status,
provisioning_state,
resourceGroupName,
run_as_account_id,
secure_boot_enabled,
secure_boot_template,
secure_boot_template_id,
shielding_requested,
siteName,
spring_boot_discovery,
sql_discovery,
static_discovery,
subscriptionId,
tags,
tomcat_discovery,
tpm_enabled,
updated_timestamp,
version,
virtualization_based_security_opt_out,
vm_configuration_file_location,
vm_fqdn,
web_app_discovery
FROM azure.migrate.vw_hyperv_machines_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.hyperv_machines_controllers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>hyperv_machines_controllers</code> resource.

```sql
/*+ update */
UPDATE azure.migrate.hyperv_machines_controllers
SET 
properties = '{{ properties }}'
WHERE 
machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
