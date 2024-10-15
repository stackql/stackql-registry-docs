---
title: system_assigned_identities
hide_title: false
hide_table_of_contents: false
keywords:
  - system_assigned_identities
  - managed_identity
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

Creates, updates, deletes, gets or lists a <code>system_assigned_identities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>system_assigned_identities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_identity.system_assigned_identities" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_system_assigned_identities', value: 'view', },
        { label: 'system_assigned_identities', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_secret_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties associated with the system assigned identity. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets the systemAssignedIdentity available under the specified RP scope. |

## `SELECT` examples

Gets the systemAssignedIdentity available under the specified RP scope.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_system_assigned_identities', value: 'view', },
        { label: 'system_assigned_identities', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
client_id,
client_secret_url,
location,
principal_id,
scope,
tags,
tenant_id
FROM azure.managed_identity.vw_system_assigned_identities
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.managed_identity.system_assigned_identities
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

