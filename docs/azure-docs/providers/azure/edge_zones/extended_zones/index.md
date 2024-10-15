---
title: extended_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_zones
  - edge_zones
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

Creates, updates, deletes, gets or lists a <code>extended_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>extended_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.edge_zones.extended_zones" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extended_zones', value: 'view', },
        { label: 'extended_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="extendedZoneName" /> | `text` | field from the `properties` object |
| <CopyableCode code="geography" /> | `text` | field from the `properties` object |
| <CopyableCode code="geography_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="home_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="latitude" /> | `text` | field from the `properties` object |
| <CopyableCode code="longitude" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="region_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="region_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="regional_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an Extended Zone resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="extendedZoneName, subscriptionId" /> | Gets an Azure Extended Zone for a subscription |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the Azure Extended Zones available to a subscription |
| <CopyableCode code="register" /> | `EXEC` | <CopyableCode code="extendedZoneName, subscriptionId" /> | Registers a subscription for an Extended Zone |
| <CopyableCode code="unregister" /> | `EXEC` | <CopyableCode code="extendedZoneName, subscriptionId" /> | Unregisters a subscription for an Extended Zone |

## `SELECT` examples

Lists the Azure Extended Zones available to a subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_extended_zones', value: 'view', },
        { label: 'extended_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
display_name,
extendedZoneName,
geography,
geography_group,
home_location,
latitude,
longitude,
provisioning_state,
region_category,
region_type,
regional_display_name,
registration_state,
subscriptionId
FROM azure.edge_zones.vw_extended_zones
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.edge_zones.extended_zones
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

