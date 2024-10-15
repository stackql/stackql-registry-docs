---
title: vh_ds
hide_title: false
hide_table_of_contents: false
keywords:
  - vh_ds
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

Creates, updates, deletes, gets or lists a <code>vh_ds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vh_ds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.vh_ds" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vh_ds', value: 'view', },
        { label: 'vh_ds', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="path" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vhdName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Test Base VHD properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName, vhdName" /> | Gets a Test Base VHD. |
| <CopyableCode code="list_by_test_base_account" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the VHDs under a test base account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName, vhdName" /> | Deletes a Test Base VHD. |

## `SELECT` examples

Lists all the VHDs under a test base account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vh_ds', value: 'view', },
        { label: 'vh_ds', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
creation_time,
file_name,
file_size,
path,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
testBaseAccountName,
vhdName
FROM azure_extras.test_base.vw_vh_ds
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.vh_ds
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>vh_ds</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.vh_ds
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}'
AND vhdName = '{{ vhdName }}';
```
