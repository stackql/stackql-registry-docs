---
title: favorite_processes
hide_title: false
hide_table_of_contents: false
keywords:
  - favorite_processes
  - test_base
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

Creates, updates, deletes, gets or lists a <code>favorite_processes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>favorite_processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.favorite_processes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_favorite_processes', value: 'view', },
        { label: 'favorite_processes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actual_process_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="favoriteProcessResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="packageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a favorite process identifier. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a favorite process for a Test Base Package. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists the favorite processes for a specific package. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create or replace a favorite process for a Test Base Package. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="favoriteProcessResourceName, packageName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Deletes a favorite process for a specific package. |

## `SELECT` examples

Lists the favorite processes for a specific package.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_favorite_processes', value: 'view', },
        { label: 'favorite_processes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
actual_process_name,
favoriteProcessResourceName,
packageName,
resourceGroupName,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_favorite_processes
WHERE packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.favorite_processes
WHERE packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>favorite_processes</code> resource.

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
INSERT INTO azure_extras.test_base.favorite_processes (
favoriteProcessResourceName,
packageName,
resourceGroupName,
subscriptionId,
testBaseAccountName,
properties
)
SELECT 
'{{ favoriteProcessResourceName }}',
'{{ packageName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ testBaseAccountName }}',
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
        - name: actualProcessName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>favorite_processes</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.favorite_processes
WHERE favoriteProcessResourceName = '{{ favoriteProcessResourceName }}'
AND packageName = '{{ packageName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
