---
title: vm_instance_hybrid_identity_metadatas
hide_title: false
hide_table_of_contents: false
keywords:
  - vm_instance_hybrid_identity_metadatas
  - system_center_vm_manager
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

Creates, updates, deletes, gets or lists a <code>vm_instance_hybrid_identity_metadatas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vm_instance_hybrid_identity_metadatas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.vm_instance_hybrid_identity_metadatas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vm_instance_hybrid_identity_metadatas', value: 'view', },
        { label: 'vm_instance_hybrid_identity_metadatas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_uid" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of Hybrid Identity Metadata for a Virtual Machine. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Implements HybridIdentityMetadata GET method. |

## `SELECT` examples

Implements HybridIdentityMetadata GET method.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vm_instance_hybrid_identity_metadatas', value: 'view', },
        { label: 'vm_instance_hybrid_identity_metadatas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
provisioning_state,
public_key,
resourceUri,
resource_uid
FROM azure.system_center_vm_manager.vw_vm_instance_hybrid_identity_metadatas
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.system_center_vm_manager.vm_instance_hybrid_identity_metadatas
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>

