---
title: server_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - server_keys
  - sql
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

Creates, updates, deletes, gets or lists a <code>server_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_keys', value: 'view', },
        { label: 'server_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_rotation_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="keyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_key_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subregion" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="thumbprint" /> | `text` | field from the `properties` object |
| <CopyableCode code="uri" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of encryption protector. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties for a server key execution. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="keyName, resourceGroupName, serverName, subscriptionId" /> | Gets a server key. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of server keys. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="keyName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a server key. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyName, resourceGroupName, serverName, subscriptionId" /> | Deletes the server key with the given name. |

## `SELECT` examples

Gets a list of server keys.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_keys', value: 'view', },
        { label: 'server_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_rotation_enabled,
creation_date,
keyName,
kind,
location,
resourceGroupName,
serverName,
server_key_type,
subregion,
subscriptionId,
thumbprint,
uri
FROM azure.sql.vw_server_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.sql.server_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_keys</code> resource.

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
INSERT INTO azure.sql.server_keys (
keyName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ keyName }}',
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
    - name: kind
      value: string
    - name: location
      value: string
    - name: properties
      value:
        - name: subregion
          value: string
        - name: serverKeyType
          value: string
        - name: uri
          value: string
        - name: thumbprint
          value: string
        - name: creationDate
          value: string
        - name: autoRotationEnabled
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>server_keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.server_keys
WHERE keyName = '{{ keyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
