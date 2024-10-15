---
title: incident_relations
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_relations
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>incident_relations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>incident_relations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incident_relations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_incident_relations', value: 'view', },
        { label: 'incident_relations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `text` | Etag of the azure resource |
| <CopyableCode code="incidentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="related_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="related_resource_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="related_resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="related_resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="relationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Relation property bag. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentId, relationName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a relation for a given incident. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets all relations for a given incident. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="incidentId, relationName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a relation for a given incident. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="incidentId, relationName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a relation for a given incident. |

## `SELECT` examples

Gets all relations for a given incident.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_incident_relations', value: 'view', },
        { label: 'incident_relations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
etag,
incidentId,
related_resource_id,
related_resource_kind,
related_resource_name,
related_resource_type,
relationName,
resourceGroupName,
subscriptionId,
workspaceName
FROM azure.sentinel.vw_incident_relations
WHERE incidentId = '{{ incidentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties
FROM azure.sentinel.incident_relations
WHERE incidentId = '{{ incidentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>incident_relations</code> resource.

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
INSERT INTO azure.sentinel.incident_relations (
incidentId,
relationName,
resourceGroupName,
subscriptionId,
workspaceName,
etag,
properties
)
SELECT 
'{{ incidentId }}',
'{{ relationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ etag }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: relatedResourceId
          value: string
        - name: relatedResourceName
          value: string
        - name: relatedResourceType
          value: string
        - name: relatedResourceKind
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>incident_relations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.incident_relations
WHERE incidentId = '{{ incidentId }}'
AND relationName = '{{ relationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
