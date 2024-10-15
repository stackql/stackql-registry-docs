---
title: server_connection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - server_connection_policies
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

Creates, updates, deletes, gets or lists a <code>server_connection_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>server_connection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.server_connection_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_connection_policies', value: 'view', },
        { label: 'server_connection_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectionPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a server connection policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionPolicyName, resourceGroupName, serverName, subscriptionId" /> | Gets a server connection policy |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Lists connection policy |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionPolicyName, resourceGroupName, serverName, subscriptionId" /> | Updates a server connection policy |

## `SELECT` examples

Lists connection policy

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_server_connection_policies', value: 'view', },
        { label: 'server_connection_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connectionPolicyName,
connection_type,
kind,
location,
resourceGroupName,
serverName,
subscriptionId
FROM azure.sql.vw_server_connection_policies
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
FROM azure.sql.server_connection_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server_connection_policies</code> resource.

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
INSERT INTO azure.sql.server_connection_policies (
connectionPolicyName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ connectionPolicyName }}',
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
    - name: location
      value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: connectionType
          value: string

```
</TabItem>
</Tabs>
