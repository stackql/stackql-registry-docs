---
title: linked_services
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_services
  - log_analytics
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

Creates, updates, deletes, gets or lists a <code>linked_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>linked_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.linked_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linked_services', value: 'view', },
        { label: 'linked_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="linkedServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="write_access_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Linked service properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="linkedServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a linked service instance. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the linked services instances in a workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="linkedServiceName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Create or update a linked service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="linkedServiceName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a linked service instance. |

## `SELECT` examples

Gets the linked services instances in a workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linked_services', value: 'view', },
        { label: 'linked_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
linkedServiceName,
provisioning_state,
resourceGroupName,
resource_id,
subscriptionId,
tags,
workspaceName,
write_access_resource_id
FROM azure.log_analytics.vw_linked_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.log_analytics.linked_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>linked_services</code> resource.

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
INSERT INTO azure.log_analytics.linked_services (
linkedServiceName,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties,
tags
)
SELECT 
'{{ linkedServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__properties }}',
'{{ properties }}',
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
        - name: resourceId
          value: string
        - name: writeAccessResourceId
          value: string
        - name: provisioningState
          value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>linked_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.log_analytics.linked_services
WHERE linkedServiceName = '{{ linkedServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
