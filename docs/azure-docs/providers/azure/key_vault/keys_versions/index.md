---
title: keys_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - keys_versions
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

Creates, updates, deletes, gets or lists a <code>keys_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>keys_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.keys_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_keys_versions', value: 'view', },
        { label: 'keys_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `text` | Name of the key vault resource. |
| <CopyableCode code="attributes" /> | `text` | field from the `properties` object |
| <CopyableCode code="curve_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="keyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="keyVersion" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_ops" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_uri_with_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="kty" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure location of the key vault resource. |
| <CopyableCode code="release_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rotation_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags assigned to the key vault resource. |
| <CopyableCode code="type" /> | `text` | Resource type of the key vault resource. |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `string` | Name of the key vault resource. |
| <CopyableCode code="location" /> | `string` | Azure location of the key vault resource. |
| <CopyableCode code="properties" /> | `object` | The properties of the key. |
| <CopyableCode code="tags" /> | `object` | Tags assigned to the key vault resource. |
| <CopyableCode code="type" /> | `string` | Resource type of the key vault resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, keyVersion, resourceGroupName, subscriptionId, vaultName" /> | Gets the specified version of the specified key in the specified key vault. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="keyName, resourceGroupName, subscriptionId, vaultName" /> | Lists the versions of the specified key in the specified key vault. |

## `SELECT` examples

Lists the versions of the specified key in the specified key vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_keys_versions', value: 'view', },
        { label: 'keys_versions', value: 'resource', },
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
location,
release_policy,
resourceGroupName,
rotation_policy,
subscriptionId,
tags,
type,
vaultName
FROM azure.key_vault.vw_keys_versions
WHERE keyName = '{{ keyName }}'
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
location,
properties,
tags,
type
FROM azure.key_vault.keys_versions
WHERE keyName = '{{ keyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>

