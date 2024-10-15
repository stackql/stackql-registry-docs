---
title: cloud_service_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_roles
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

Creates, updates, deletes, gets or lists a <code>cloud_service_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_service_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_service_roles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_service_roles', value: 'view', },
        { label: 'cloud_service_roles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="cloudServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Describes the cloud service role sku. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="unique_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | The cloud service role properties. |
| <CopyableCode code="sku" /> | `object` | Describes the cloud service role sku. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, roleName, subscriptionId" /> | Gets a role from a cloud service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Gets a list of all roles in a cloud service. Use nextLink property in the response to get the next page of roles. Do this till nextLink is null to fetch all the roles. |

## `SELECT` examples

Gets a list of all roles in a cloud service. Use nextLink property in the response to get the next page of roles. Do this till nextLink is null to fetch all the roles.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_service_roles', value: 'view', },
        { label: 'cloud_service_roles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cloudServiceName,
location,
resourceGroupName,
roleName,
sku,
subscriptionId,
type,
unique_id
FROM azure.compute.vw_cloud_service_roles
WHERE cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
sku,
type
FROM azure.compute.cloud_service_roles
WHERE cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

