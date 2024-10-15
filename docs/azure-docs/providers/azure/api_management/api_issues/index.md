---
title: api_issues
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issues
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

Creates, updates, deletes, gets or lists a <code>api_issues</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_issues" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_issues', value: 'view', },
        { label: 'api_issues', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="issueId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Issue contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the Issue for an API specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId" /> | Lists all issues associated with the specified API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Issue for an API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified Issue from an API. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, apiId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Updates an existing issue for an API. |

## `SELECT` examples

Lists all issues associated with the specified API.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_issues', value: 'view', },
        { label: 'api_issues', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
apiId,
api_id,
created_date,
issueId,
resourceGroupName,
serviceName,
state,
subscriptionId,
title,
user_id
FROM azure.api_management.vw_api_issues
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.api_issues
WHERE apiId = '{{ apiId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_issues</code> resource.

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
INSERT INTO azure.api_management.api_issues (
apiId,
issueId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiId }}',
'{{ issueId }}',
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
        - name: title
          value: string
        - name: description
          value: string
        - name: userId
          value: string
        - name: createdDate
          value: string
        - name: state
          value: string
        - name: apiId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>api_issues</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.api_issues
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND issueId = '{{ issueId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>api_issues</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.api_issues
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND issueId = '{{ issueId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
