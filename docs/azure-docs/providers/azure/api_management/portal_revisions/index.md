---
title: portal_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - portal_revisions
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

Creates, updates, deletes, gets or lists a <code>portal_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>portal_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.portal_revisions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_portal_revisions', value: 'view', },
        { label: 'portal_revisions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_current" /> | `text` | field from the `properties` object |
| <CopyableCode code="portalRevisionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_date_time" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="portalRevisionId, resourceGroupName, serviceName, subscriptionId" /> | Gets the developer portal's revision specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists developer portal's revisions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="portalRevisionId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new developer portal's revision by running the portal's publishing. The `isCurrent` property indicates if the revision is publicly accessible. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, portalRevisionId, resourceGroupName, serviceName, subscriptionId" /> | Updates the description of specified portal revision or makes it current. |

## `SELECT` examples

Lists developer portal's revisions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_portal_revisions', value: 'view', },
        { label: 'portal_revisions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
created_date_time,
is_current,
portalRevisionId,
provisioning_state,
resourceGroupName,
serviceName,
status,
status_details,
subscriptionId,
updated_date_time
FROM azure.api_management.vw_portal_revisions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.portal_revisions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>portal_revisions</code> resource.

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
INSERT INTO azure.api_management.portal_revisions (
portalRevisionId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ portalRevisionId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: description
          value: string
        - name: statusDetails
          value: string
        - name: status
          value: string
        - name: isCurrent
          value: boolean
        - name: createdDateTime
          value: string
        - name: updatedDateTime
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>portal_revisions</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.portal_revisions
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND portalRevisionId = '{{ portalRevisionId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
