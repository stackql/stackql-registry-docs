---
title: encryption_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_scopes
  - storage
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

Creates, updates, deletes, gets or lists a <code>encryption_scopes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>encryption_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.encryption_scopes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_encryption_scopes', value: 'view', },
        { label: 'encryption_scopes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryptionScopeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_vault_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="require_infrastructure_encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the encryption scope. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, encryptionScopeName, resourceGroupName, subscriptionId" /> | Returns the properties for the specified encryption scope. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all the encryption scopes available under the specified storage account. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="accountName, encryptionScopeName, resourceGroupName, subscriptionId" /> | Update encryption scope properties as specified in the request body. Update fails if the specified encryption scope does not already exist. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="accountName, encryptionScopeName, resourceGroupName, subscriptionId" /> | Synchronously creates or updates an encryption scope under the specified storage account. If an encryption scope is already created and a subsequent request is issued with different properties, the encryption scope properties will be updated per the specified request. |

## `SELECT` examples

Lists all the encryption scopes available under the specified storage account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_encryption_scopes', value: 'view', },
        { label: 'encryption_scopes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
creation_time,
encryptionScopeName,
key_vault_properties,
last_modified_time,
require_infrastructure_encryption,
resourceGroupName,
source,
state,
subscriptionId,
type
FROM azure.storage.vw_encryption_scopes
WHERE accountName = '{{ accountName }}'
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
type
FROM azure.storage.encryption_scopes
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>encryption_scopes</code> resource.

```sql
/*+ update */
UPDATE azure.storage.encryption_scopes
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND encryptionScopeName = '{{ encryptionScopeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>encryption_scopes</code> resource.

```sql
/*+ update */
REPLACE azure.storage.encryption_scopes
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND encryptionScopeName = '{{ encryptionScopeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
