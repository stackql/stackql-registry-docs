---
title: galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - galleries
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

Creates, updates, deletes, gets or lists a <code>galleries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.galleries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_galleries', value: 'view', },
        { label: 'galleries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sharing_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="sharing_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="soft_delete_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Shared Image Gallery. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | Retrieves information about a Shared Image Gallery. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List galleries under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List galleries under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | Create or update a Shared Image Gallery. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | Delete a Shared Image Gallery. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | Update a Shared Image Gallery. |

## `SELECT` examples

List galleries under a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_galleries', value: 'view', },
        { label: 'galleries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
galleryName,
identifier,
location,
provisioning_state,
resourceGroupName,
sharing_profile,
sharing_status,
soft_delete_policy,
subscriptionId,
tags,
type
FROM azure.compute.vw_galleries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.compute.galleries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>galleries</code> resource.

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
INSERT INTO azure.compute.galleries (
galleryName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ galleryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: identifier
          value:
            - name: uniqueName
              value: string
        - name: provisioningState
          value: []
        - name: sharingProfile
          value:
            - name: permissions
              value: string
            - name: groups
              value:
                - - name: type
                    value: string
                  - name: ids
                    value:
                      - string
            - name: communityGalleryInfo
              value:
                - name: publisherUri
                  value: string
                - name: publisherContact
                  value: string
                - name: eula
                  value: string
                - name: publicNamePrefix
                  value: string
                - name: communityGalleryEnabled
                  value: boolean
                - name: publicNames
                  value:
                    - string
        - name: softDeletePolicy
          value:
            - name: isSoftDeleteEnabled
              value: boolean
        - name: sharingStatus
          value:
            - name: aggregatedState
              value: []
            - name: summary
              value:
                - - name: region
                    value: string
                  - name: details
                    value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>galleries</code> resource.

```sql
/*+ update */
UPDATE azure.compute.galleries
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>galleries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.galleries
WHERE galleryName = '{{ galleryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
