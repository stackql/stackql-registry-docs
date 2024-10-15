---
title: runbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - runbooks
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

Creates, updates, deletes, gets or lists a <code>runbooks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runbooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.runbooks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_runbooks', value: 'view', },
        { label: 'runbooks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="draft" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Gets or sets the etag of the resource. |
| <CopyableCode code="job_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="log_activity_trace" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_progress" /> | `text` | field from the `properties` object |
| <CopyableCode code="log_verbose" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publish_content_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runbookName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runbook_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Gets or sets the etag of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Definition of the runbook property type. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Retrieve the runbook identified by runbook name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of runbooks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId, data__properties" /> | Create the runbook identified by runbook name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Delete the runbook by name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Update the runbook identified by runbook name. |
| <CopyableCode code="publish" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, runbookName, subscriptionId" /> | Publish runbook draft. |

## `SELECT` examples

Retrieve a list of runbooks.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_runbooks', value: 'view', },
        { label: 'runbooks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
automationAccountName,
creation_time,
draft,
etag,
job_count,
last_modified_by,
last_modified_time,
location,
log_activity_trace,
log_progress,
log_verbose,
output_types,
parameters,
provisioning_state,
publish_content_link,
resourceGroupName,
runbookName,
runbook_type,
state,
subscriptionId,
tags
FROM azure.automation.vw_runbooks
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure.automation.runbooks
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>runbooks</code> resource.

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
INSERT INTO azure.automation.runbooks (
automationAccountName,
resourceGroupName,
runbookName,
subscriptionId,
data__properties,
properties,
name,
location,
tags
)
SELECT 
'{{ automationAccountName }}',
'{{ resourceGroupName }}',
'{{ runbookName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ name }}',
'{{ location }}',
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
        - name: logVerbose
          value: boolean
        - name: logProgress
          value: boolean
        - name: runbookType
          value: string
        - name: draft
          value:
            - name: inEdit
              value: boolean
            - name: draftContentLink
              value:
                - name: uri
                  value: string
                - name: contentHash
                  value:
                    - name: algorithm
                      value: string
                    - name: value
                      value: string
                - name: version
                  value: string
            - name: creationTime
              value: string
            - name: lastModifiedTime
              value: string
            - name: parameters
              value: object
            - name: outputTypes
              value:
                - string
        - name: description
          value: string
        - name: logActivityTrace
          value: integer
    - name: name
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>runbooks</code> resource.

```sql
/*+ update */
UPDATE azure.automation.runbooks
SET 
properties = '{{ properties }}',
name = '{{ name }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runbookName = '{{ runbookName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>runbooks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automation.runbooks
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runbookName = '{{ runbookName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
