---
title: protection_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_containers
  - recovery_services_backup
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

Creates, updates, deletes, gets or lists a <code>protection_containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.protection_containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protection_containers', value: 'view', },
        { label: 'protection_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="backup_management_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="containerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabricName" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectable_object_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Base class for container with backup items. Containers with specific workloads are derived from this class. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerName, fabricName, resourceGroupName, subscriptionId, vaultName" /> | Gets details of the specific container registered to your Recovery Services Vault. |
| <CopyableCode code="inquire" /> | `EXEC` | <CopyableCode code="containerName, fabricName, resourceGroupName, subscriptionId, vaultName" /> | This is an async operation and the results should be tracked using location header or Azure-async-url. |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="fabricName, resourceGroupName, subscriptionId, vaultName" /> | Discovers all the containers in the subscription that can be backed up to Recovery Services Vault. This is an
asynchronous operation. To know the status of the operation, call GetRefreshOperationResult API. |
| <CopyableCode code="register" /> | `EXEC` | <CopyableCode code="containerName, fabricName, resourceGroupName, subscriptionId, vaultName" /> | Registers the container with Recovery Services vault.
This is an asynchronous operation. To track the operation status, use location header to call get latest status of
the operation. |
| <CopyableCode code="unregister" /> | `EXEC` | <CopyableCode code="containerName, fabricName, resourceGroupName, subscriptionId, vaultName" /> | Unregisters the given container from your Recovery Services Vault. This is an asynchronous operation. To determine
whether the backend service has finished processing the request, call Get Container Operation Result API. |

## `SELECT` examples

Gets details of the specific container registered to your Recovery Services Vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protection_containers', value: 'view', },
        { label: 'protection_containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
backup_management_type,
containerName,
container_type,
fabricName,
friendly_name,
health_status,
protectable_object_type,
registration_status,
resourceGroupName,
subscriptionId,
type,
vaultName
FROM azure.recovery_services_backup.vw_protection_containers
WHERE containerName = '{{ containerName }}'
AND fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.recovery_services_backup.protection_containers
WHERE containerName = '{{ containerName }}'
AND fabricName = '{{ fabricName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

