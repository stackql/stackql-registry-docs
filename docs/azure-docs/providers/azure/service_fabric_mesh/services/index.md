---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - service_fabric_mesh
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified identifier for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_scaling_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="code_packages" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_refs" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replica_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |
| <CopyableCode code="unhealthy_evaluation" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | This type describes properties of a service resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationResourceName, resourceGroupName, serviceResourceName, subscriptionId" /> | Gets the information about the service resource with the given name. The information include the description and other properties of the service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationResourceName, resourceGroupName, subscriptionId" /> | Gets the information about all services of an application resource. The information include the description and other properties of the Service. |

## `SELECT` examples

Gets the information about all services of an application resource. The information include the description and other properties of the Service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
applicationResourceName,
auto_scaling_policies,
code_packages,
diagnostics,
health_state,
network_refs,
os_type,
provisioning_state,
replica_count,
resourceGroupName,
serviceResourceName,
status,
status_details,
subscriptionId,
type,
unhealthy_evaluation
FROM azure.service_fabric_mesh.vw_services
WHERE applicationResourceName = '{{ applicationResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.service_fabric_mesh.services
WHERE applicationResourceName = '{{ applicationResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

