---
title: allowed_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - allowed_connections
  - security
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

Creates, updates, deletes, gets or lists a <code>allowed_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>allowed_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.allowed_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_allowed_connections', value: 'view', },
        { label: 'allowed_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="ascLocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="calculated_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectable_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionType" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location where the resource is stored |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Location where the resource is stored |
| <CopyableCode code="properties" /> | `object` | Describes the allowed traffic between Azure resources |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ascLocation, connectionType, resourceGroupName, subscriptionId" /> | Gets the list of all possible traffic between resources for the subscription and location, based on connection type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of all possible traffic between resources for the subscription |
| <CopyableCode code="list_by_home_region" /> | `SELECT` | <CopyableCode code="ascLocation, subscriptionId" /> | Gets the list of all possible traffic between resources for the subscription and location. |

## `SELECT` examples

Gets the list of all possible traffic between resources for the subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_allowed_connections', value: 'view', },
        { label: 'allowed_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ascLocation,
calculated_date_time,
connectable_resources,
connectionType,
location,
resourceGroupName,
subscriptionId,
type
FROM azure.security.vw_allowed_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.security.allowed_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

