---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - lab_services
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

Creates, updates, deletes, gets or lists a <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_images', value: 'view', },
        { label: 'images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="author" /> | `text` | field from the `properties` object |
| <CopyableCode code="available_regions" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="icon_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="labPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_gallery_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="terms_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an image resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageName, labPlanName, resourceGroupName, subscriptionId" /> | Gets an image resource. |
| <CopyableCode code="list_by_lab_plan" /> | `SELECT` | <CopyableCode code="labPlanName, resourceGroupName, subscriptionId" /> | Gets all images from galleries attached to a lab plan. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="imageName, labPlanName, resourceGroupName, subscriptionId, data__properties" /> | Updates an image resource via PUT. Creating new resources via PUT will not function. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="imageName, labPlanName, resourceGroupName, subscriptionId" /> | Updates an image resource. |

## `SELECT` examples

Gets all images from galleries attached to a lab plan.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_images', value: 'view', },
        { label: 'images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
author,
available_regions,
display_name,
enabled_state,
icon_url,
imageName,
labPlanName,
offer,
os_state,
os_type,
plan,
provisioning_state,
publisher,
resourceGroupName,
shared_gallery_id,
sku,
subscriptionId,
system_data,
terms_status,
version
FROM azure.lab_services.vw_images
WHERE labPlanName = '{{ labPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.lab_services.images
WHERE labPlanName = '{{ labPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>images</code> resource.

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
INSERT INTO azure.lab_services.images (
imageName,
labPlanName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ imageName }}',
'{{ labPlanName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: properties
      value:
        - name: enabledState
          value: []
        - name: provisioningState
          value: []
        - name: displayName
          value: string
        - name: description
          value: string
        - name: iconUrl
          value: string
        - name: author
          value: string
        - name: osType
          value: []
        - name: plan
          value: string
        - name: offer
          value: string
        - name: publisher
          value: string
        - name: sku
          value: string
        - name: version
          value: string
        - name: sharedGalleryId
          value: []
        - name: availableRegions
          value:
            - string
        - name: osState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>images</code> resource.

```sql
/*+ update */
UPDATE azure.lab_services.images
SET 
properties = '{{ properties }}'
WHERE 
imageName = '{{ imageName }}'
AND labPlanName = '{{ labPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
