---
title: resource_sync_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_sync_rules
  - custom_locations
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

Creates, updates, deletes, gets or lists a <code>resource_sync_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_sync_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.custom_locations.resource_sync_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_sync_rules', value: 'view', },
        { label: 'resource_sync_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="childResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="selector" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="target_resource_group" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties for a resource sync rule. For an unmapped custom resource, its labels will be used to find out matching resource sync rules using the selector property of the resource sync rule. If this resource sync rule has highest priority among all matching rules, then the unmapped custom resource will be projected to the target resource group associated with this resource sync rule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of the resourceSyncRule with a specified resource group, subscription id Custom Location resource name and Resource Sync Rule name. |
| <CopyableCode code="list_by_custom_location_id" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets a list of Resource Sync Rules in the specified subscription. The operation returns properties of each Resource Sync Rule |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | Creates or updates a Resource Sync Rule in the parent Custom Location, Subscription Id and Resource Group |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | Deletes the Resource Sync Rule with the specified Resource Sync Rule Name, Custom Location Resource Name, Resource Group, and Subscription Id. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="childResourceName, resourceGroupName, resourceName, subscriptionId" /> | Updates a Resource Sync Rule with the specified Resource Sync Rule name in the specified Resource Group, Subscription and Custom Location name. |

## `SELECT` examples

Gets a list of Resource Sync Rules in the specified subscription. The operation returns properties of each Resource Sync Rule

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_sync_rules', value: 'view', },
        { label: 'resource_sync_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
childResourceName,
location,
priority,
provisioning_state,
resourceGroupName,
resourceName,
selector,
subscriptionId,
system_data,
tags,
target_resource_group
FROM azure.custom_locations.vw_resource_sync_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.custom_locations.resource_sync_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_sync_rules</code> resource.

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
INSERT INTO azure.custom_locations.resource_sync_rules (
childResourceName,
resourceGroupName,
resourceName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ childResourceName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: priority
          value: integer
        - name: provisioningState
          value: string
        - name: selector
          value:
            - name: matchExpressions
              value: []
            - name: matchLabels
              value: object
        - name: targetResourceGroup
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>resource_sync_rules</code> resource.

```sql
/*+ update */
UPDATE azure.custom_locations.resource_sync_rules
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
childResourceName = '{{ childResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>resource_sync_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.custom_locations.resource_sync_rules
WHERE childResourceName = '{{ childResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
