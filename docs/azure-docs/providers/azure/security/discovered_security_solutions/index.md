---
title: discovered_security_solutions
hide_title: false
hide_table_of_contents: false
keywords:
  - discovered_security_solutions
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

Creates, updates, deletes, gets or lists a <code>discovered_security_solutions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discovered_security_solutions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.discovered_security_solutions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_discovered_security_solutions', value: 'view', },
        { label: 'discovered_security_solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="ascLocation" /> | `text` | field from the `properties` object |
| <CopyableCode code="discoveredSecuritySolutionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location where the resource is stored |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_family" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Location where the resource is stored |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ascLocation, discoveredSecuritySolutionName, resourceGroupName, subscriptionId" /> | Gets a specific discovered Security Solution. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of discovered Security Solutions for the subscription. |
| <CopyableCode code="list_by_home_region" /> | `SELECT` | <CopyableCode code="ascLocation, subscriptionId" /> | Gets a list of discovered Security Solutions for the subscription and location. |

## `SELECT` examples

Gets a list of discovered Security Solutions for the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_discovered_security_solutions', value: 'view', },
        { label: 'discovered_security_solutions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
ascLocation,
discoveredSecuritySolutionName,
location,
offer,
publisher,
resourceGroupName,
security_family,
sku,
subscriptionId,
type
FROM azure.security.vw_discovered_security_solutions
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
FROM azure.security.discovered_security_solutions
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

