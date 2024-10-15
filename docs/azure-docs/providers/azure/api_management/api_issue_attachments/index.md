---
title: api_issue_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issue_attachments
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

Creates, updates, deletes, gets or lists a <code>api_issue_attachments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_issue_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_issue_attachments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_issue_attachments', value: 'view', },
        { label: 'api_issue_attachments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiId" /> | `text` | field from the `properties` object |
| <CopyableCode code="attachmentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_format" /> | `text` | field from the `properties` object |
| <CopyableCode code="issueId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Issue Attachment contract Properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the issue Attachment for an API specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Lists all attachments for the Issue associated with the specified API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Attachment for the Issue in an API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified comment from an Issue. |

## `SELECT` examples

Lists all attachments for the Issue associated with the specified API.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_issue_attachments', value: 'view', },
        { label: 'api_issue_attachments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiId,
attachmentId,
content,
content_format,
issueId,
resourceGroupName,
serviceName,
subscriptionId,
title
FROM azure.api_management.vw_api_issue_attachments
WHERE apiId = '{{ apiId }}'
AND issueId = '{{ issueId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.api_issue_attachments
WHERE apiId = '{{ apiId }}'
AND issueId = '{{ issueId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_issue_attachments</code> resource.

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
INSERT INTO azure.api_management.api_issue_attachments (
apiId,
attachmentId,
issueId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ apiId }}',
'{{ attachmentId }}',
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
        - name: contentFormat
          value: string
        - name: content
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_issue_attachments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.api_issue_attachments
WHERE If-Match = '{{ If-Match }}'
AND apiId = '{{ apiId }}'
AND attachmentId = '{{ attachmentId }}'
AND issueId = '{{ issueId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
