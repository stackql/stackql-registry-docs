---
title: flighting_rings
hide_title: false
hide_table_of_contents: false
keywords:
  - flighting_rings
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

Creates, updates, deletes, gets or lists a <code>flighting_rings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flighting_rings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.flighting_rings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_flighting_rings', value: 'view', },
        { label: 'flighting_rings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actual_flighting_ring_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="flightingRingResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The Flighting Ring properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="flightingRingResourceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a flighting ring of a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the flighting rings of a Test Base Account. |

## `SELECT` examples

Lists all the flighting rings of a Test Base Account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_flighting_rings', value: 'view', },
        { label: 'flighting_rings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
actual_flighting_ring_name,
flightingRingResourceName,
resourceGroupName,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_flighting_rings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.flighting_rings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

