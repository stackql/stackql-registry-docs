---
title: source_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - source_controls
  - automation
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

Creates, updates, deletes, gets or lists a <code>source_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>source_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.source_controls" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_source_controls', value: 'view', },
        { label: 'source_controls', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_sync" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="branch" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="folder_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="publish_runbook" /> | `text` | field from the `properties` object |
| <CopyableCode code="repo_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sourceControlName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Definition of the source control properties |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Retrieve the source control identified by source control name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of source controls. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId, data__properties" /> | Create a source control. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Delete the source control. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, resourceGroupName, sourceControlName, subscriptionId" /> | Update a source control. |

## `SELECT` examples

Retrieve a list of source controls.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_source_controls', value: 'view', },
        { label: 'source_controls', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
auto_sync,
automationAccountName,
branch,
creation_time,
folder_path,
last_modified_time,
publish_runbook,
repo_url,
resourceGroupName,
sourceControlName,
source_type,
subscriptionId
FROM azure.automation.vw_source_controls
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.automation.source_controls
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>source_controls</code> resource.

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
INSERT INTO azure.automation.source_controls (
automationAccountName,
resourceGroupName,
sourceControlName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ sourceControlName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: repoUrl
          value: string
        - name: branch
          value: string
        - name: folderPath
          value: string
        - name: autoSync
          value: boolean
        - name: publishRunbook
          value: boolean
        - name: sourceType
          value: string
        - name: securityToken
          value:
            - name: accessToken
              value: string
            - name: refreshToken
              value: string
            - name: tokenType
              value: string
        - name: description
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>source_controls</code> resource.

```sql
/*+ update */
UPDATE azure.automation.source_controls
SET 
properties = '{{ properties }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlName = '{{ sourceControlName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>source_controls</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.source_controls
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sourceControlName = '{{ sourceControlName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
