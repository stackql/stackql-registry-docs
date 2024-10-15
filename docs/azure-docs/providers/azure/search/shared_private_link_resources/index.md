---
title: shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_private_link_resources
  - search
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

Creates, updates, deletes, gets or lists a <code>shared_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shared_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.shared_private_link_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_private_link_resources', value: 'view', },
        { label: 'shared_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_region" /> | `text` | field from the `properties` object |
| <CopyableCode code="searchServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sharedPrivateLinkResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an existing shared private link resource managed by the Azure AI Search service. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, sharedPrivateLinkResourceName, subscriptionId" /> | Gets the details of the shared private link resource managed by the search service in the given resource group. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Gets a list of all shared private link resources managed by the given service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, searchServiceName, sharedPrivateLinkResourceName, subscriptionId" /> | Initiates the creation or update of a shared private link resource managed by the search service in the given resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, searchServiceName, sharedPrivateLinkResourceName, subscriptionId" /> | Initiates the deletion of the shared private link resource from the search service. |

## `SELECT` examples

Gets a list of all shared private link resources managed by the given service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_private_link_resources', value: 'view', },
        { label: 'shared_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
group_id,
private_link_resource_id,
provisioning_state,
request_message,
resourceGroupName,
resource_region,
searchServiceName,
sharedPrivateLinkResourceName,
status,
subscriptionId,
type
FROM azure.search.vw_shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
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
FROM azure.search.shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>shared_private_link_resources</code> resource.

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
INSERT INTO azure.search.shared_private_link_resources (
resourceGroupName,
searchServiceName,
sharedPrivateLinkResourceName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ searchServiceName }}',
'{{ sharedPrivateLinkResourceName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: privateLinkResourceId
          value: string
        - name: groupId
          value: string
        - name: requestMessage
          value: string
        - name: resourceRegion
          value: string
        - name: status
          value: string
        - name: provisioningState
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>shared_private_link_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.search.shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND sharedPrivateLinkResourceName = '{{ sharedPrivateLinkResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
