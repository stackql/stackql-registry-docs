---
title: deployment_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_operations
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>deployment_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployment_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.deployment_operations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployment_operations', value: 'view', },
        { label: 'deployment_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Full deployment operation ID. |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | Deployment operation ID. |
| <CopyableCode code="operation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_operation" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="response" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_request_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource" /> | `text` | field from the `properties` object |
| <CopyableCode code="timestamp" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Full deployment operation ID. |
| <CopyableCode code="operationId" /> | `string` | Deployment operation ID. |
| <CopyableCode code="properties" /> | `object` | Deployment operation properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentName, operationId, resourceGroupName, subscriptionId" /> | Gets a deployments operation. |
| <CopyableCode code="get_at_management_group_scope" /> | `SELECT` | <CopyableCode code="deploymentName, groupId, operationId" /> | Gets a deployments operation. |
| <CopyableCode code="get_at_scope" /> | `SELECT` | <CopyableCode code="deploymentName, operationId, scope" /> | Gets a deployments operation. |
| <CopyableCode code="get_at_subscription_scope" /> | `SELECT` | <CopyableCode code="deploymentName, operationId, subscriptionId" /> | Gets a deployments operation. |
| <CopyableCode code="get_at_tenant_scope" /> | `SELECT` | <CopyableCode code="deploymentName, operationId" /> | Gets a deployments operation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> | Gets all deployments operations for a deployment. |
| <CopyableCode code="list_at_management_group_scope" /> | `SELECT` | <CopyableCode code="deploymentName, groupId" /> | Gets all deployments operations for a deployment. |
| <CopyableCode code="list_at_scope" /> | `SELECT` | <CopyableCode code="deploymentName, scope" /> | Gets all deployments operations for a deployment. |
| <CopyableCode code="list_at_subscription_scope" /> | `SELECT` | <CopyableCode code="deploymentName, subscriptionId" /> | Gets all deployments operations for a deployment. |
| <CopyableCode code="list_at_tenant_scope" /> | `SELECT` | <CopyableCode code="deploymentName" /> | Gets all deployments operations for a deployment. |

## `SELECT` examples

Gets all deployments operations for a deployment.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployment_operations', value: 'view', },
        { label: 'deployment_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
deploymentName,
duration,
operationId,
operation_id,
provisioning_operation,
provisioning_state,
request,
resourceGroupName,
response,
service_request_id,
status_code,
status_message,
subscriptionId,
target_resource,
timestamp
FROM azure.resources.vw_deployment_operations
WHERE deploymentName = '{{ deploymentName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
operationId,
properties
FROM azure.resources.deployment_operations
WHERE deploymentName = '{{ deploymentName }}';
```
</TabItem></Tabs>

