---
title: standard_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - standard_assignments
  - security
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

Creates, updates, deletes, gets or lists a <code>standard_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standard_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.standard_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_standard_assignments', value: 'view', },
        { label: 'standard_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="assigned_standard" /> | `text` | field from the `properties` object |
| <CopyableCode code="attestation_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="effect" /> | `text` | field from the `properties` object |
| <CopyableCode code="excluded_scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="exemption_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="expires_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="standardAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a standardAssignment |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceId, standardAssignmentName" /> | This operation retrieves a single standard assignment, given its name and the scope it was created at. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of all relevant standard assignments over a scope |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceId, standardAssignmentName" /> | This operation creates or updates a standard assignment with the given scope and name. standard assignments apply to all resources contained within their scope. For example, when you assign a policy at resource group scope, that policy applies to all resources in the group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceId, standardAssignmentName" /> | This operation deletes a standard assignment, given its name and the scope it was created in. The scope of a standard assignment is the part of its ID preceding '/providers/Microsoft.Security/standardAssignments/{standardAssignmentName}'. |

## `SELECT` examples

Get a list of all relevant standard assignments over a scope

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_standard_assignments', value: 'view', },
        { label: 'standard_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
assigned_standard,
attestation_data,
display_name,
effect,
excluded_scopes,
exemption_data,
expires_on,
metadata,
resourceId,
scope,
standardAssignmentName,
type
FROM azure.security.vw_standard_assignments
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.standard_assignments
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>standard_assignments</code> resource.

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
INSERT INTO azure.security.standard_assignments (
resourceId,
standardAssignmentName,
properties
)
SELECT 
'{{ resourceId }}',
'{{ standardAssignmentName }}',
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
        - name: displayName
          value: string
        - name: description
          value: string
        - name: assignedStandard
          value:
            - name: id
              value: string
        - name: effect
          value: string
        - name: excludedScopes
          value:
            - string
        - name: expiresOn
          value: string
        - name: exemptionData
          value:
            - name: exemptionCategory
              value: string
            - name: assignedAssessment
              value:
                - name: assessmentKey
                  value: string
        - name: attestationData
          value:
            - name: complianceState
              value: string
            - name: complianceDate
              value: string
            - name: evidence
              value:
                - - name: description
                    value: string
                  - name: sourceUrl
                    value: string
        - name: metadata
          value:
            - name: createdBy
              value: string
            - name: createdOn
              value: string
            - name: lastUpdatedBy
              value: string
            - name: lastUpdatedOn
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

Deletes the specified <code>standard_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.standard_assignments
WHERE resourceId = '{{ resourceId }}'
AND standardAssignmentName = '{{ standardAssignmentName }}';
```
