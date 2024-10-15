---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
  - customer_insights
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

Creates, updates, deletes, gets or lists a <code>role_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.role_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_assignments', value: 'view', },
        { label: 'role_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignment_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="conflation_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectors" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="interactions" /> | `text` | field from the `properties` object |
| <CopyableCode code="kpis" /> | `text` | field from the `properties` object |
| <CopyableCode code="links" /> | `text` | field from the `properties` object |
| <CopyableCode code="principals" /> | `text` | field from the `properties` object |
| <CopyableCode code="profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="relationship_links" /> | `text` | field from the `properties` object |
| <CopyableCode code="relationships" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_assignments" /> | `text` | field from the `properties` object |
| <CopyableCode code="sas_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="segments" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="views" /> | `text` | field from the `properties` object |
| <CopyableCode code="widget_types" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The Role Assignment definition. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assignmentName, hubName, resourceGroupName, subscriptionId" /> | Gets the role assignment in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the role assignments for the specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="assignmentName, hubName, resourceGroupName, subscriptionId" /> | Creates or updates a role assignment in the hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assignmentName, hubName, resourceGroupName, subscriptionId" /> | Deletes the role assignment in the hub. |

## `SELECT` examples

Gets all the role assignments for the specified hub.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_assignments', value: 'view', },
        { label: 'role_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
assignmentName,
assignment_name,
conflation_policies,
connectors,
display_name,
hubName,
interactions,
kpis,
links,
principals,
profiles,
provisioning_state,
relationship_links,
relationships,
resourceGroupName,
role,
role_assignments,
sas_policies,
segments,
subscriptionId,
tenant_id,
type,
views,
widget_types
FROM azure_extras.customer_insights.vw_role_assignments
WHERE hubName = '{{ hubName }}'
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
FROM azure_extras.customer_insights.role_assignments
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_assignments</code> resource.

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
INSERT INTO azure_extras.customer_insights.role_assignments (
assignmentName,
hubName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ assignmentName }}',
'{{ hubName }}',
'{{ resourceGroupName }}',
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
        - name: tenantId
          value: string
        - name: assignmentName
          value: string
        - name: displayName
          value: object
        - name: description
          value: object
        - name: provisioningState
          value: []
        - name: role
          value: string
        - name: principals
          value:
            - - name: principalId
                value: string
              - name: principalType
                value: string
              - name: principalMetadata
                value: object
        - name: profiles
          value:
            - name: elements
              value:
                - string
            - name: exceptions
              value:
                - string
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

Deletes the specified <code>role_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.role_assignments
WHERE assignmentName = '{{ assignmentName }}'
AND hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
