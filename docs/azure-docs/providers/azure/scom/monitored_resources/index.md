---
title: monitored_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_resources
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

Creates, updates, deletes, gets or lists a <code>monitored_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitored_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scom.monitored_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitored_resources', value: 'view', },
        { label: 'monitored_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="agent_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="computer_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="install_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="management_server_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitoredResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of a monitored resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceName, monitoredResourceName, resourceGroupName, subscriptionId" /> | Retrieve the details of the monitored resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceName, monitoredResourceName, resourceGroupName, subscriptionId" /> | Create or update a monitored resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceName, monitoredResourceName, resourceGroupName, subscriptionId" /> | Delete a monitored resource. |

## `SELECT` examples

Retrieve the details of the monitored resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_monitored_resources', value: 'view', },
        { label: 'monitored_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agent_version,
computer_name,
connection_status,
domain_name,
health_status,
install_type,
instanceName,
management_server_endpoint,
monitoredResourceName,
provisioning_state,
resourceGroupName,
resource_id,
resource_location,
subscriptionId,
type
FROM azure.scom.vw_monitored_resources
WHERE instanceName = '{{ instanceName }}'
AND monitoredResourceName = '{{ monitoredResourceName }}'
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
FROM azure.scom.monitored_resources
WHERE instanceName = '{{ instanceName }}'
AND monitoredResourceName = '{{ monitoredResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>monitored_resources</code> resource.

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
INSERT INTO azure.scom.monitored_resources (
instanceName,
monitoredResourceName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ instanceName }}',
'{{ monitoredResourceName }}',
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

Deletes the specified <code>monitored_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.scom.monitored_resources
WHERE instanceName = '{{ instanceName }}'
AND monitoredResourceName = '{{ monitoredResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
