---
title: configuration_snapshot_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_snapshot_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>configuration_snapshot_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_snapshot_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.configuration_snapshot_slots" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_snapshot_slots', value: 'view', },
        { label: 'configuration_snapshot_slots', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="acr_use_managed_identity_creds" /> | `text` | field from the `properties` object |
| <CopyableCode code="acr_user_managed_identity_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="always_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_management_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_command_line" /> | `text` | field from the `properties` object |
| <CopyableCode code="app_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_heal_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_heal_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_swap_slot_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_storage_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_strings" /> | `text` | field from the `properties` object |
| <CopyableCode code="cors" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_documents" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_error_logging_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="document_root" /> | `text` | field from the `properties` object |
| <CopyableCode code="elastic_web_app_scale_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="experiments" /> | `text` | field from the `properties` object |
| <CopyableCode code="ftps_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="function_app_scale_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="functions_runtime_scale_monitoring_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="handler_mappings" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_check_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="http20_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="http_logging_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_security_restrictions" /> | `text` | field from the `properties` object |
| <CopyableCode code="ip_security_restrictions_default_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="java_container" /> | `text` | field from the `properties` object |
| <CopyableCode code="java_container_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="java_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_reference_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of resource. |
| <CopyableCode code="limits" /> | `text` | field from the `properties` object |
| <CopyableCode code="linux_fx_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancing" /> | `text` | field from the `properties` object |
| <CopyableCode code="local_my_sql_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="logs_directory_size_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="machine_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_pipeline_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_service_identity_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_tls_cipher_suite" /> | `text` | field from the `properties` object |
| <CopyableCode code="min_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="minimum_elastic_instance_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="net_framework_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="node_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_workers" /> | `text` | field from the `properties` object |
| <CopyableCode code="php_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="power_shell_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="pre_warmed_instance_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="publishing_username" /> | `text` | field from the `properties` object |
| <CopyableCode code="push" /> | `text` | field from the `properties` object |
| <CopyableCode code="python_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_debugging_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_debugging_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_tracing_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_tracing_expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scm_ip_security_restrictions" /> | `text` | field from the `properties` object |
| <CopyableCode code="scm_ip_security_restrictions_default_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="scm_ip_security_restrictions_use_main" /> | `text` | field from the `properties` object |
| <CopyableCode code="scm_min_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="scm_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="slot" /> | `text` | field from the `properties` object |
| <CopyableCode code="snapshotId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tracing_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="use32_bit_worker_process" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_applications" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_private_ports_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="vnet_route_all_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_sockets_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="website_time_zone" /> | `text` | field from the `properties` object |
| <CopyableCode code="windows_fx_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="x_managed_service_identity_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Configuration of an App Service app. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, snapshotId, subscriptionId" /> | Description for Gets a snapshot of the configuration of an app at a previous point in time. |

## `SELECT` examples

Description for Gets a snapshot of the configuration of an app at a previous point in time.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_snapshot_slots', value: 'view', },
        { label: 'configuration_snapshot_slots', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
acr_use_managed_identity_creds,
acr_user_managed_identity_id,
always_on,
api_definition,
api_management_config,
app_command_line,
app_settings,
auto_heal_enabled,
auto_heal_rules,
auto_swap_slot_name,
azure_storage_accounts,
connection_strings,
cors,
default_documents,
detailed_error_logging_enabled,
document_root,
elastic_web_app_scale_limit,
experiments,
ftps_state,
function_app_scale_limit,
functions_runtime_scale_monitoring_enabled,
handler_mappings,
health_check_path,
http20_enabled,
http_logging_enabled,
ip_security_restrictions,
ip_security_restrictions_default_action,
java_container,
java_container_version,
java_version,
key_vault_reference_identity,
kind,
limits,
linux_fx_version,
load_balancing,
local_my_sql_enabled,
logs_directory_size_limit,
machine_key,
managed_pipeline_mode,
managed_service_identity_id,
metadata,
min_tls_cipher_suite,
min_tls_version,
minimum_elastic_instance_count,
net_framework_version,
node_version,
number_of_workers,
php_version,
power_shell_version,
pre_warmed_instance_count,
public_network_access,
publishing_username,
push,
python_version,
remote_debugging_enabled,
remote_debugging_version,
request_tracing_enabled,
request_tracing_expiration_time,
resourceGroupName,
scm_ip_security_restrictions,
scm_ip_security_restrictions_default_action,
scm_ip_security_restrictions_use_main,
scm_min_tls_version,
scm_type,
slot,
snapshotId,
subscriptionId,
tracing_options,
type,
use32_bit_worker_process,
virtual_applications,
vnet_name,
vnet_private_ports_count,
vnet_route_all_enabled,
web_sockets_enabled,
website_time_zone,
windows_fx_version,
x_managed_service_identity_id
FROM azure.app_service.vw_configuration_snapshot_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND snapshotId = '{{ snapshotId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.configuration_snapshot_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND snapshotId = '{{ snapshotId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

