---
title: cloud_service_role_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_role_instances
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

Creates, updates, deletes, gets or lists a <code>cloud_service_role_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_service_role_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.cloud_service_role_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_service_role_instances', value: 'view', },
        { label: 'cloud_service_role_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name. |
| <CopyableCode code="cloudServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location. |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The role instance SKU. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource Type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | Role instance properties. |
| <CopyableCode code="sku" /> | `object` | The role instance SKU. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource Type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | Gets a role instance from a cloud service. |
| <CopyableCode code="get_instance_view" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | Retrieves information about the run-time state of a role instance in a cloud service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudServiceName, resourceGroupName, subscriptionId" /> | Gets the list of all role instances in a cloud service. Use nextLink property in the response to get the next page of role instances. Do this till nextLink is null to fetch all the role instances. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | Deletes a role instance from a cloud service. |
| <CopyableCode code="rebuild" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | The Rebuild Role Instance asynchronous operation reinstalls the operating system on instances of web roles or worker roles and initializes the storage resources that are used by them. If you do not want to initialize storage resources, you can use Reimage Role Instance. |
| <CopyableCode code="reimage" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | The Reimage Role Instance asynchronous operation reinstalls the operating system on instances of web roles or worker roles. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="cloudServiceName, resourceGroupName, roleInstanceName, subscriptionId" /> | The Reboot Role Instance asynchronous operation requests a reboot of a role instance in the cloud service. |

## `SELECT` examples

Gets the list of all role instances in a cloud service. Use nextLink property in the response to get the next page of role instances. Do this till nextLink is null to fetch all the role instances.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_service_role_instances', value: 'view', },
        { label: 'cloud_service_role_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
cloudServiceName,
instance_view,
location,
network_profile,
resourceGroupName,
roleInstanceName,
sku,
subscriptionId,
tags,
type
FROM azure.compute.vw_cloud_service_role_instances
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
tags,
type
FROM azure.compute.cloud_service_role_instances
WHERE cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `DELETE` example

Deletes the specified <code>cloud_service_role_instances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.cloud_service_role_instances
WHERE cloudServiceName = '{{ cloudServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND roleInstanceName = '{{ roleInstanceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
