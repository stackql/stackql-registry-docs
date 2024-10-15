---
title: orchestrator_instance_service_details
hide_title: false
hide_table_of_contents: false
keywords:
  - orchestrator_instance_service_details
  - delegated_network
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

Creates, updates, deletes, gets or lists a <code>orchestrator_instance_service_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orchestrator_instance_service_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.delegated_network.orchestrator_instance_service_details" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_orchestrator_instance_service_details', value: 'view', },
        { label: 'orchestrator_instance_service_details', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | An identifier that represents the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="api_server_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_root_ca" /> | `text` | field from the `properties` object |
| <CopyableCode code="controller_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of workbook. Choices are user and shared. |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="orchestrator_app_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="orchestrator_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | The type of resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | The kind of workbook. Choices are user and shared. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of orchestrator |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets details about the orchestrator instance. |

## `SELECT` examples

Gets details about the orchestrator instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_orchestrator_instance_service_details', value: 'view', },
        { label: 'orchestrator_instance_service_details', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
api_server_endpoint,
cluster_root_ca,
controller_details,
identity,
kind,
location,
orchestrator_app_id,
orchestrator_tenant_id,
private_link_resource_id,
provisioning_state,
resourceGroupName,
resourceName,
resource_guid,
subscriptionId,
tags,
type
FROM azure.delegated_network.vw_orchestrator_instance_service_details
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
kind,
location,
properties,
tags,
type
FROM azure.delegated_network.orchestrator_instance_service_details
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

