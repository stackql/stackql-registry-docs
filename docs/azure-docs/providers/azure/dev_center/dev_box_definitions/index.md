---
title: dev_box_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_box_definitions
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>dev_box_definitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dev_box_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.dev_box_definitions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dev_box_definitions', value: 'view', },
        { label: 'dev_box_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="active_image_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="devBoxDefinitionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hibernate_support" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_reference" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_validation_error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_validation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="os_storage_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="validation_status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a Dev Box definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devBoxDefinitionName, devCenterName, resourceGroupName, subscriptionId" /> | Gets a Dev Box definition |
| <CopyableCode code="get_by_project" /> | `SELECT` | <CopyableCode code="devBoxDefinitionName, projectName, resourceGroupName, subscriptionId" /> | Gets a Dev Box definition configured for a project |
| <CopyableCode code="list_by_dev_center" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | List Dev Box definitions for a devcenter. |
| <CopyableCode code="list_by_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List Dev Box definitions configured for a project. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devBoxDefinitionName, devCenterName, resourceGroupName, subscriptionId" /> | Creates or updates a Dev Box definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devBoxDefinitionName, devCenterName, resourceGroupName, subscriptionId" /> | Deletes a Dev Box definition |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="devBoxDefinitionName, devCenterName, resourceGroupName, subscriptionId" /> | Partially updates a Dev Box definition. |

## `SELECT` examples

List Dev Box definitions configured for a project.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dev_box_definitions', value: 'view', },
        { label: 'dev_box_definitions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
active_image_reference,
devBoxDefinitionName,
devCenterName,
hibernate_support,
image_reference,
image_validation_error_details,
image_validation_status,
location,
os_storage_type,
projectName,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
validation_status
FROM azure.dev_center.vw_dev_box_definitions
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.dev_center.dev_box_definitions
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dev_box_definitions</code> resource.

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
INSERT INTO azure.dev_center.dev_box_definitions (
devBoxDefinitionName,
devCenterName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ devBoxDefinitionName }}',
'{{ devCenterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: imageReference
          value:
            - name: id
              value: string
            - name: exactVersion
              value: string
        - name: sku
          value:
            - name: name
              value: string
            - name: tier
              value: []
            - name: size
              value: string
            - name: family
              value: string
            - name: capacity
              value: integer
        - name: osStorageType
          value: string
        - name: hibernateSupport
          value: []
        - name: provisioningState
          value: []
        - name: imageValidationStatus
          value: []
        - name: imageValidationErrorDetails
          value:
            - name: code
              value: string
            - name: message
              value: string
        - name: validationStatus
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dev_box_definitions</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.dev_box_definitions
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}'
WHERE 
devBoxDefinitionName = '{{ devBoxDefinitionName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dev_box_definitions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.dev_box_definitions
WHERE devBoxDefinitionName = '{{ devBoxDefinitionName }}'
AND devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
