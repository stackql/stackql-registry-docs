---
title: servers_controller_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_controller_machines
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

Creates, updates, deletes, gets or lists a <code>servers_controller_machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers_controller_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.servers_controller_machines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers_controller_machines', value: 'view', },
        { label: 'servers_controller_machines', value: 'resource', },
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
| <CopyableCode code="created_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_map_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="dependency_mapping_start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="firmware" /> | `text` | field from the `properties` object |
| <CopyableCode code="fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_details_discovery_timestamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_os_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="hydrated_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="iis_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_deleted" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_guest_details_discovery_in_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="machineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_adapters" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_applications" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_processor_core" /> | `text` | field from the `properties` object |
| <CopyableCode code="operating_system_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="oracle_discovery" /> | `text` | field from the `properties` object |
| <CopyableCode code="processor_info" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="validation_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_app_discovery" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Server REST resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Get a Server |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Delete a Server |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="machineName, resourceGroupName, siteName, subscriptionId" /> | Update a Server machine |

## `SELECT` examples

Get a Server

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers_controller_machines', value: 'view', },
        { label: 'servers_controller_machines', value: 'resource', },
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
created_timestamp,
dependency_map_discovery,
dependency_mapping,
dependency_mapping_end_time,
dependency_mapping_start_time,
disks,
display_name,
errors,
firmware,
fqdn,
guest_details_discovery_timestamp,
guest_os_details,
hydrated_fqdn,
iis_discovery,
is_deleted,
is_guest_details_discovery_in_progress,
machineName,
network_adapters,
number_of_applications,
number_of_processor_core,
operating_system_details,
oracle_discovery,
processor_info,
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
validation_required,
web_app_discovery
FROM azure.migrate.vw_servers_controller_machines
WHERE machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.migrate.servers_controller_machines
WHERE machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>servers_controller_machines</code> resource.

```sql
/*+ update */
UPDATE azure.migrate.servers_controller_machines
SET 
properties = '{{ properties }}'
WHERE 
machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>servers_controller_machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.migrate.servers_controller_machines
WHERE machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
