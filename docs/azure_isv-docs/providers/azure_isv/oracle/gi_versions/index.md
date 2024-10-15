---
title: gi_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - gi_versions
  - oracle
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

Creates, updates, deletes, gets or lists a <code>gi_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gi_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.gi_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gi_versions', value: 'view', },
        { label: 'gi_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="giversionname" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | GiVersion resource model |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="giversionname, location, subscriptionId" /> | Get a GiVersion |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List GiVersion resources by Location |

## `SELECT` examples

List GiVersion resources by Location

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gi_versions', value: 'view', },
        { label: 'gi_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
giversionname,
location,
subscriptionId,
version
FROM azure_isv.oracle.vw_gi_versions
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.gi_versions
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

