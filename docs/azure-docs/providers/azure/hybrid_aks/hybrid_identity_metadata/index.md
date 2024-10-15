---
title: hybrid_identity_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_identity_metadata
  - hybrid_aks
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

Creates, updates, deletes, gets or lists a <code>hybrid_identity_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hybrid_identity_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.hybrid_identity_metadata" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hybrid_identity_metadata', value: 'view', },
        { label: 'hybrid_identity_metadata', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectedClusterResourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_uid" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Defines the resource properties for the hybrid identity metadata. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Get the hybrid identity metadata proxy resource. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Lists the hybrid identity metadata proxy resource in a provisioned cluster instance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedClusterResourceUri" /> | Deletes the hybrid identity metadata proxy resource. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="connectedClusterResourceUri, data__properties" /> | Creates the hybrid identity metadata proxy resource that facilitates the managed identity provisioning. |

## `SELECT` examples

Get the hybrid identity metadata proxy resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hybrid_identity_metadata', value: 'view', },
        { label: 'hybrid_identity_metadata', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connectedClusterResourceUri,
provisioning_state,
public_key,
resource_uid,
system_data
FROM azure.hybrid_aks.vw_hybrid_identity_metadata
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.hybrid_aks.hybrid_identity_metadata
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>hybrid_identity_metadata</code> resource.

```sql
/*+ update */
REPLACE azure.hybrid_aks.hybrid_identity_metadata
SET 
properties = '{{ properties }}',
systemData = '{{ systemData }}'
WHERE 
connectedClusterResourceUri = '{{ connectedClusterResourceUri }}'
AND data__properties = '{{ data__properties }}';
```

## `DELETE` example

Deletes the specified <code>hybrid_identity_metadata</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_aks.hybrid_identity_metadata
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```
