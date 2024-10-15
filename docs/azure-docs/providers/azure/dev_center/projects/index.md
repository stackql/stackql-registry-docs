---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
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

Creates, updates, deletes, gets or lists a <code>projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.projects" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_projects', value: 'view', },
        { label: 'projects', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="catalog_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="dev_center_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="dev_center_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="max_dev_boxes_per_user" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a project. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Gets a specific project. |
| <CopyableCode code="get_inherited_settings" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Gets applicable inherited settings for this project. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all projects in the resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all projects in the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Creates or updates a project. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Deletes a project resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Partially updates a project. |

## `SELECT` examples

Lists all projects in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_projects', value: 'view', },
        { label: 'projects', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
catalog_settings,
dev_center_id,
dev_center_uri,
display_name,
identity,
location,
max_dev_boxes_per_user,
projectName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.dev_center.vw_projects
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.dev_center.projects
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>projects</code> resource.

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
INSERT INTO azure.dev_center.projects (
projectName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
identity
)
SELECT 
'{{ projectName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}'
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
        - name: devCenterId
          value: string
        - name: description
          value: string
        - name: maxDevBoxesPerUser
          value: integer
        - name: displayName
          value: string
        - name: catalogSettings
          value:
            - name: catalogItemSyncTypes
              value:
                - []
        - name: provisioningState
          value: []
        - name: devCenterUri
          value: []
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>projects</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.projects
SET 
tags = '{{ tags }}',
location = '{{ location }}',
properties = '{{ properties }}',
identity = '{{ identity }}'
WHERE 
projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>projects</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.projects
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
