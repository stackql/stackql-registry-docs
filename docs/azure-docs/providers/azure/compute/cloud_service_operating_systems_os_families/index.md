---
title: cloud_service_operating_systems_os_families
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_operating_systems_os_families
  - compute
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

Creates, updates, deletes, gets or lists a <code>cloud_service_operating_systems_os_families</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_service_operating_systems_os_families</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_service_operating_systems_os_families" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_service_operating_systems_os_families', value: 'view', },
        { label: 'cloud_service_operating_systems_os_families', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="label" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="osFamilyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="versions" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | OS family properties. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, osFamilyName, subscriptionId" /> | Gets properties of a guest operating system family that can be specified in the XML service configuration (.cscfg) for a cloud service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets a list of all guest operating system families available to be specified in the XML service configuration (.cscfg) for a cloud service. Use nextLink property in the response to get the next page of OS Families. Do this till nextLink is null to fetch all the OS Families. |

## `SELECT` examples

Gets a list of all guest operating system families available to be specified in the XML service configuration (.cscfg) for a cloud service. Use nextLink property in the response to get the next page of OS Families. Do this till nextLink is null to fetch all the OS Families.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_service_operating_systems_os_families', value: 'view', },
        { label: 'cloud_service_operating_systems_os_families', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
label,
location,
osFamilyName,
subscriptionId,
type,
versions
FROM azure.compute.vw_cloud_service_operating_systems_os_families
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.compute.cloud_service_operating_systems_os_families
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

