---
title: managed_hsm_keys_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsm_keys_versions
  - key_vault
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

Creates, updates, deletes, gets or lists a <code>managed_hsm_keys_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_hsm_keys_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.managed_hsm_keys_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_hsm_keys_versions', value: 'view', },
        { label: 'managed_hsm_keys_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="attributes" /> | `text` | field from the `properties` object |
| <CopyableCode code="curve_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="keyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="keyVersion" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_ops" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_uri_with_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="kty" /> | `text` | field from the `properties` object |
| <CopyableCode code="release_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rotation_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of the key. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, keyVersion, name, resourceGroupName, subscriptionId" /> | Gets the specified version of the specified key in the specified managed HSM. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="keyName, name, resourceGroupName, subscriptionId" /> | Lists the versions of the specified key in the specified managed HSM. |

## `SELECT` examples

Lists the versions of the specified key in the specified managed HSM.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_hsm_keys_versions', value: 'view', },
        { label: 'managed_hsm_keys_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
attributes,
curve_name,
keyName,
keyVersion,
key_ops,
key_size,
key_uri,
key_uri_with_version,
kty,
release_policy,
resourceGroupName,
rotation_policy,
subscriptionId,
tags,
type
FROM azure.key_vault.vw_managed_hsm_keys_versions
WHERE keyName = '{{ keyName }}'
AND name = '{{ name }}'
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
tags,
type
FROM azure.key_vault.managed_hsm_keys_versions
WHERE keyName = '{{ keyName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

