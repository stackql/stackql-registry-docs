---
title: resource_guard_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_guard_proxies
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

Creates, updates, deletes, gets or lists a <code>resource_guard_proxies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_guard_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.resource_guard_proxies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_guard_proxies', value: 'view', },
        { label: 'resource_guard_proxies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGuardProxyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_operation_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guard_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> | Returns ResourceGuardProxy under vault and with the name referenced in request |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> | Delete ResourceGuardProxy under vault |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> | Add or Update ResourceGuardProxy under vault
Secures vault critical operations |
| <CopyableCode code="unlock_delete" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName" /> | Secures delete ResourceGuardProxy operations. |

## `SELECT` examples

Returns ResourceGuardProxy under vault and with the name referenced in request

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_guard_proxies', value: 'view', },
        { label: 'resource_guard_proxies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
last_updated_time,
resourceGroupName,
resourceGuardProxyName,
resource_guard_operation_details,
resource_guard_resource_id,
subscriptionId,
type,
vaultName
FROM azure.recovery_services_backup.vw_resource_guard_proxies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardProxyName = '{{ resourceGuardProxyName }}'
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
FROM azure.recovery_services_backup.resource_guard_proxies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardProxyName = '{{ resourceGuardProxyName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>resource_guard_proxies</code> resource.

```sql
/*+ update */
REPLACE azure.recovery_services_backup.resource_guard_proxies
SET 
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardProxyName = '{{ resourceGuardProxyName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```

## `DELETE` example

Deletes the specified <code>resource_guard_proxies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_backup.resource_guard_proxies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceGuardProxyName = '{{ resourceGuardProxyName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
