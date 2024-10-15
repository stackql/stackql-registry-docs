---
title: managed_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_gateways
  - scom
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

Creates, updates, deletes, gets or lists a <code>managed_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scom.managed_gateways" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_gateways', value: 'view', },
        { label: 'managed_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="computer_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="install_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managedGatewayName" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_server_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of a gateway resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceName, managedGatewayName, resourceGroupName, subscriptionId" /> | Retrieve the details of the gateway resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceName, managedGatewayName, resourceGroupName, subscriptionId" /> | Create or update a gateway resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceName, managedGatewayName, resourceGroupName, subscriptionId" /> | Remove a gateway resource. |

## `SELECT` examples

Retrieve the details of the gateway resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_managed_gateways', value: 'view', },
        { label: 'managed_gateways', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
computer_name,
connection_status,
domain_name,
health_status,
install_type,
instanceName,
managedGatewayName,
management_server_endpoint,
provisioning_state,
resourceGroupName,
resource_id,
resource_location,
subscriptionId,
type,
version
FROM azure.scom.vw_managed_gateways
WHERE instanceName = '{{ instanceName }}'
AND managedGatewayName = '{{ managedGatewayName }}'
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
FROM azure.scom.managed_gateways
WHERE instanceName = '{{ instanceName }}'
AND managedGatewayName = '{{ managedGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>managed_gateways</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.scom.managed_gateways (
instanceName,
managedGatewayName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ instanceName }}',
'{{ managedGatewayName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>managed_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM azure.scom.managed_gateways
WHERE instanceName = '{{ instanceName }}'
AND managedGatewayName = '{{ managedGatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
