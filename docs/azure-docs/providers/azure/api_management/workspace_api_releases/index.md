---
title: workspace_api_releases
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_releases
  - api_management
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

Creates, updates, deletes, gets or lists a <code>workspace_api_releases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_api_releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_api_releases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_api_releases', value: 'view', },
        { label: 'workspace_api_releases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="releaseId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API Release details |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Returns the details of an API release. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates a new Release for the API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the specified release in the API. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Updates the details of the release of the API specified by its identifier. |

## `SELECT` examples

Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_api_releases', value: 'view', },
        { label: 'workspace_api_releases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiId,
api_id,
created_date_time,
notes,
releaseId,
resourceGroupName,
serviceName,
subscriptionId,
updated_date_time,
workspaceId
FROM azure.api_management.vw_workspace_api_releases
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.workspace_api_releases
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_api_releases</code> resource.

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
INSERT INTO azure.api_management.workspace_api_releases (
apiId,
releaseId,
resourceGroupName,
serviceName,
subscriptionId,
workspaceId,
properties
)
SELECT 
'{{ apiId }}',
'{{ releaseId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ workspaceId }}',
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
        - name: apiId
          value: string
        - name: createdDateTime
          value: string
        - name: updatedDateTime
          value: string
        - name: notes
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_api_releases</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.workspace_api_releases
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND releaseId = '{{ releaseId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```

## `DELETE` example

Deletes the specified <code>workspace_api_releases</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.workspace_api_releases
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND releaseId = '{{ releaseId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceId = '{{ workspaceId }}';
```
