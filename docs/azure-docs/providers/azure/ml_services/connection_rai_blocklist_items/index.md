---
title: connection_rai_blocklist_items
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_rai_blocklist_items
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>connection_rai_blocklist_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connection_rai_blocklist_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.connection_rai_blocklist_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_rai_blocklist_items', value: 'view', },
        { label: 'connection_rai_blocklist_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_regex" /> | `text` | field from the `properties` object |
| <CopyableCode code="pattern" /> | `text` | field from the `properties` object |
| <CopyableCode code="raiBlocklistItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="raiBlocklistName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | RAI Custom Blocklist Item properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectionName, raiBlocklistName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectionName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, raiBlocklistItemName, raiBlocklistName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="add_bulk" /> | `EXEC` | <CopyableCode code="connectionName, raiBlocklistName, resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connection_rai_blocklist_items', value: 'view', },
        { label: 'connection_rai_blocklist_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
connectionName,
is_regex,
pattern,
raiBlocklistItemName,
raiBlocklistName,
resourceGroupName,
subscriptionId,
system_data,
type,
workspaceName
FROM azure.ml_services.vw_connection_rai_blocklist_items
WHERE connectionName = '{{ connectionName }}'
AND raiBlocklistName = '{{ raiBlocklistName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.ml_services.connection_rai_blocklist_items
WHERE connectionName = '{{ connectionName }}'
AND raiBlocklistName = '{{ raiBlocklistName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connection_rai_blocklist_items</code> resource.

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
INSERT INTO azure.ml_services.connection_rai_blocklist_items (
connectionName,
raiBlocklistItemName,
raiBlocklistName,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ connectionName }}',
'{{ raiBlocklistItemName }}',
'{{ raiBlocklistName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: isRegex
          value: boolean
        - name: pattern
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connection_rai_blocklist_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.connection_rai_blocklist_items
WHERE connectionName = '{{ connectionName }}'
AND raiBlocklistItemName = '{{ raiBlocklistItemName }}'
AND raiBlocklistName = '{{ raiBlocklistName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
