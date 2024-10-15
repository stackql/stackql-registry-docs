---
title: location_based_capability_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - location_based_capability_sets
  - mysql
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

Creates, updates, deletes, gets or lists a <code>location_based_capability_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_based_capability_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.location_based_capability_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_location_based_capability_sets', value: 'view', },
        { label: 'location_based_capability_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="capabilitySetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="locationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_flexible_server_editions" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_geo_backup_regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_server_versions" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Location capability. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="capabilitySetName, locationName, subscriptionId" /> | Get capabilities at specified location in a given subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | Get capabilities at specified location in a given subscription. |

## `SELECT` examples

Get capabilities at specified location in a given subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_location_based_capability_sets', value: 'view', },
        { label: 'location_based_capability_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
capabilitySetName,
locationName,
subscriptionId,
supported_flexible_server_editions,
supported_geo_backup_regions,
supported_server_versions
FROM azure.mysql.vw_location_based_capability_sets
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.mysql.location_based_capability_sets
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

