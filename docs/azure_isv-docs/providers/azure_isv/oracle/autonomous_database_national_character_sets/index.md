---
title: autonomous_database_national_character_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - autonomous_database_national_character_sets
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

Creates, updates, deletes, gets or lists a <code>autonomous_database_national_character_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>autonomous_database_national_character_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.autonomous_database_national_character_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_autonomous_database_national_character_sets', value: 'view', },
        { label: 'autonomous_database_national_character_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="adbsncharsetname" /> | `text` | field from the `properties` object |
| <CopyableCode code="character_set" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | AutonomousDatabaseNationalCharacterSet resource model |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="adbsncharsetname, location, subscriptionId" /> | Get a AutonomousDatabaseNationalCharacterSet |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List AutonomousDatabaseNationalCharacterSet resources by Location |

## `SELECT` examples

List AutonomousDatabaseNationalCharacterSet resources by Location

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_autonomous_database_national_character_sets', value: 'view', },
        { label: 'autonomous_database_national_character_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
adbsncharsetname,
character_set,
location,
subscriptionId
FROM azure_isv.oracle.vw_autonomous_database_national_character_sets
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_isv.oracle.autonomous_database_national_character_sets
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

