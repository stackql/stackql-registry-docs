---
title: active_session_host_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - active_session_host_configurations
  - desktop_virtualization
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

Creates, updates, deletes, gets or lists a <code>active_session_host_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>active_session_host_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.active_session_host_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_active_session_host_configurations', value: 'view', },
        { label: 'active_session_host_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="availability_zones" /> | `text` | field from the `properties` object |
| <CopyableCode code="boot_diagnostics_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_configuration_script_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hostPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_admin_credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_name_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_size_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_tags" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Session host configurations of HostPool. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Get the ActiveSessionHostConfiguration for the hostPool that is currently being used for update operations. |
| <CopyableCode code="list_by_host_pool" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List activeSessionHostConfigurations. |

## `SELECT` examples

Get the ActiveSessionHostConfiguration for the hostPool that is currently being used for update operations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_active_session_host_configurations', value: 'view', },
        { label: 'active_session_host_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
availability_zones,
boot_diagnostics_info,
custom_configuration_script_url,
disk_info,
domain_info,
friendly_name,
hostPoolName,
image_info,
network_info,
resourceGroupName,
security_info,
subscriptionId,
system_data,
type,
version,
vm_admin_credentials,
vm_location,
vm_name_prefix,
vm_resource_group,
vm_size_id,
vm_tags
FROM azure.desktop_virtualization.vw_active_session_host_configurations
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.desktop_virtualization.active_session_host_configurations
WHERE hostPoolName = '{{ hostPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

