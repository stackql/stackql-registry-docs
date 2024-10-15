---
title: administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - administrators
  - postgresql
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

Creates, updates, deletes, gets or lists a <code>administrators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.postgresql.administrators" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_administrators', value: 'view', },
        { label: 'administrators', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="objectId" /> | `text` | field from the `properties` object |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an Active Directory administrator. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="objectId, resourceGroupName, serverName, subscriptionId" /> | Gets information about a server. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | List all the AAD administrators for a given server. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="objectId, resourceGroupName, serverName, subscriptionId" /> | Creates a new server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="objectId, resourceGroupName, serverName, subscriptionId" /> | Deletes an Active Directory Administrator associated with the server. |

## `SELECT` examples

List all the AAD administrators for a given server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_administrators', value: 'view', },
        { label: 'administrators', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
objectId,
object_id,
principal_name,
principal_type,
resourceGroupName,
serverName,
subscriptionId,
tenant_id
FROM azure.postgresql.vw_administrators
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.postgresql.administrators
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>administrators</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.postgresql.administrators (
objectId,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ objectId }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: principalType
          value: string
        - name: principalName
          value: string
        - name: tenantId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>administrators</code> resource.

```sql
/*+ delete */
DELETE FROM azure.postgresql.administrators
WHERE objectId = '{{ objectId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
