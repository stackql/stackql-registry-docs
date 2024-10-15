---
title: custom_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_locations
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

Creates, updates, deletes, gets or lists a <code>custom_locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.custom_locations.custom_locations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_locations', value: 'view', },
        { label: 'custom_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authentication" /> | `text` | field from the `properties` object |
| <CopyableCode code="cluster_extension_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="namespace" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties for a custom location. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the details of the customLocation with a specified resource group and name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Custom Locations in the specified subscription and resource group. The operation returns properties of each Custom Location. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of Custom Locations in the specified subscription. The operation returns properties of each Custom Location |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Creates or updates a Custom Location in the specified Subscription and Resource Group |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes the Custom Location with the specified Resource Name, Resource Group, and Subscription Id. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a Custom Location with the specified Resource Name in the specified Resource Group and Subscription. |
| <CopyableCode code="find_target_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns the target resource group associated with the resource sync rules of the Custom Location that match the rules passed in with the Find Target Resource Group Request. |

## `SELECT` examples

Gets a list of Custom Locations in the specified subscription. The operation returns properties of each Custom Location

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_custom_locations', value: 'view', },
        { label: 'custom_locations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authentication,
cluster_extension_ids,
display_name,
host_resource_id,
host_type,
identity,
location,
namespace,
provisioning_state,
resourceGroupName,
resourceName,
subscriptionId,
system_data,
tags
FROM azure.custom_locations.vw_custom_locations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure.custom_locations.custom_locations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_locations</code> resource.

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
INSERT INTO azure.custom_locations.custom_locations (
resourceGroupName,
resourceName,
subscriptionId,
identity,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ identity }}',
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
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: authentication
          value:
            - name: type
              value: string
            - name: value
              value: string
        - name: clusterExtensionIds
          value:
            - string
        - name: displayName
          value: string
        - name: hostResourceId
          value: string
        - name: hostType
          value: string
        - name: namespace
          value: string
        - name: provisioningState
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

Updates a <code>custom_locations</code> resource.

```sql
/*+ update */
UPDATE azure.custom_locations.custom_locations
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>custom_locations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.custom_locations.custom_locations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
