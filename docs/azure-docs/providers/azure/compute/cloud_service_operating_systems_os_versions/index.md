---
title: cloud_service_operating_systems_os_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_operating_systems_os_versions
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

Creates, updates, deletes, gets or lists a <code>cloud_service_operating_systems_os_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_service_operating_systems_os_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_service_operating_systems_os_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_service_operating_systems_os_versions', value: 'view', },
        { label: 'cloud_service_operating_systems_os_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="family" /> | `text` | field from the `properties` object |
| <CopyableCode code="family_label" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_active" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_default" /> | `text` | field from the `properties` object |
| <CopyableCode code="label" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="osVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | OS version properties. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, osVersionName, subscriptionId" /> | Gets properties of a guest operating system version that can be specified in the XML service configuration (.cscfg) for a cloud service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets a list of all guest operating system versions available to be specified in the XML service configuration (.cscfg) for a cloud service. Use nextLink property in the response to get the next page of OS versions. Do this till nextLink is null to fetch all the OS versions. |

## `SELECT` examples

Gets a list of all guest operating system versions available to be specified in the XML service configuration (.cscfg) for a cloud service. Use nextLink property in the response to get the next page of OS versions. Do this till nextLink is null to fetch all the OS versions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_service_operating_systems_os_versions', value: 'view', },
        { label: 'cloud_service_operating_systems_os_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
family,
family_label,
is_active,
is_default,
label,
location,
osVersionName,
subscriptionId,
type,
version
FROM azure.compute.vw_cloud_service_operating_systems_os_versions
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
FROM azure.compute.cloud_service_operating_systems_os_versions
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

