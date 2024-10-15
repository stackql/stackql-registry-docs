---
title: transparent_data_encryptions
hide_title: false
hide_table_of_contents: false
keywords:
  - transparent_data_encryptions
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

Creates, updates, deletes, gets or lists a <code>transparent_data_encryptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transparent_data_encryptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.transparent_data_encryptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_transparent_data_encryptions', value: 'view', },
        { label: 'transparent_data_encryptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tdeName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a transparent data encryption. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, tdeName" /> | Gets a logical database's transparent data encryption. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of the logical database's transparent data encryption. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, tdeName" /> | Updates a logical database's transparent data encryption configuration. |

## `SELECT` examples

Gets a list of the logical database's transparent data encryption.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_transparent_data_encryptions', value: 'view', },
        { label: 'transparent_data_encryptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
databaseName,
resourceGroupName,
serverName,
state,
subscriptionId,
tdeName
FROM azure.sql.vw_transparent_data_encryptions
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.transparent_data_encryptions
WHERE databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transparent_data_encryptions</code> resource.

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
INSERT INTO azure.sql.transparent_data_encryptions (
databaseName,
resourceGroupName,
serverName,
subscriptionId,
tdeName,
properties
)
SELECT 
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ tdeName }}',
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
        - name: state
          value: string

```
</TabItem>
</Tabs>
