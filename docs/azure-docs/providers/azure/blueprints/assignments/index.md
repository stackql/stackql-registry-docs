---
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
  - blueprints
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

Creates, updates, deletes, gets or lists a <code>assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assignments', value: 'view', },
        { label: 'assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="blueprint_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed identity generic object. |
| <CopyableCode code="location" /> | `text` | The location of this blueprint assignment. |
| <CopyableCode code="locks" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceScope" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed identity generic object. |
| <CopyableCode code="location" /> | `string` | The location of this blueprint assignment. |
| <CopyableCode code="properties" /> | `object` | Detailed properties for a blueprint assignment. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assignmentName, resourceScope" /> | Get a blueprint assignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceScope" /> | List blueprint assignments within a subscription or a management group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="assignmentName, resourceScope, data__identity, data__properties" /> | Create or update a blueprint assignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assignmentName, resourceScope" /> | Delete a blueprint assignment. |
| <CopyableCode code="who_is_blueprint" /> | `EXEC` | <CopyableCode code="assignmentName, resourceScope" /> | Get Blueprints service SPN objectId |

## `SELECT` examples

List blueprint assignments within a subscription or a management group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assignments', value: 'view', },
        { label: 'assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
assignmentName,
blueprint_id,
display_name,
identity,
location,
locks,
parameters,
provisioning_state,
resourceScope,
resource_groups,
scope,
status
FROM azure.blueprints.vw_assignments
WHERE resourceScope = '{{ resourceScope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties
FROM azure.blueprints.assignments
WHERE resourceScope = '{{ resourceScope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assignments</code> resource.

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
INSERT INTO azure.blueprints.assignments (
assignmentName,
resourceScope,
data__identity,
data__properties,
identity,
properties,
location
)
SELECT 
'{{ assignmentName }}',
'{{ resourceScope }}',
'{{ data__identity }}',
'{{ data__properties }}',
'{{ identity }}',
'{{ properties }}',
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
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: object
    - name: properties
      value:
        - name: blueprintId
          value: string
        - name: scope
          value: string
        - name: parameters
          value: object
        - name: resourceGroups
          value: object
        - name: status
          value:
            - name: managedResources
              value:
                - string
            - name: timeCreated
              value: string
            - name: lastModified
              value: string
        - name: locks
          value:
            - name: mode
              value: string
            - name: excludedPrincipals
              value:
                - string
            - name: excludedActions
              value:
                - string
        - name: provisioningState
          value: string
        - name: displayName
          value: string
        - name: description
          value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.blueprints.assignments
WHERE assignmentName = '{{ assignmentName }}'
AND resourceScope = '{{ resourceScope }}';
```
