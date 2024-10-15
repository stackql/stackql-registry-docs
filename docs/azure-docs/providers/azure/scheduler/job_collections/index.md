---
title: job_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - job_collections
  - scheduler
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

Creates, updates, deletes, gets or lists a <code>job_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.scheduler.job_collections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_collections', value: 'view', },
        { label: 'job_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets the job collection resource identifier. |
| <CopyableCode code="name" /> | `text` | Gets or sets the job collection resource name. |
| <CopyableCode code="jobCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Gets or sets the storage account location. |
| <CopyableCode code="quota" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Gets or sets the tags. |
| <CopyableCode code="type" /> | `text` | Gets the job collection resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the job collection resource identifier. |
| <CopyableCode code="name" /> | `string` | Gets or sets the job collection resource name. |
| <CopyableCode code="location" /> | `string` | Gets or sets the storage account location. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Gets or sets the tags. |
| <CopyableCode code="type" /> | `string` | Gets the job collection resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobCollectionName, resourceGroupName, subscriptionId" /> | Gets a job collection. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all job collections under specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all job collections under specified subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="jobCollectionName, resourceGroupName, subscriptionId" /> | Provisions a new job collection or updates an existing job collection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobCollectionName, resourceGroupName, subscriptionId" /> | Deletes a job collection. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="jobCollectionName, resourceGroupName, subscriptionId" /> | Patches an existing job collection. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="jobCollectionName, resourceGroupName, subscriptionId" /> | Disables all of the jobs in the job collection. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="jobCollectionName, resourceGroupName, subscriptionId" /> | Enables all of the jobs in the job collection. |

## `SELECT` examples

Gets all job collections under specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_job_collections', value: 'view', },
        { label: 'job_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
jobCollectionName,
location,
quota,
resourceGroupName,
sku,
state,
subscriptionId,
tags,
type
FROM azure.scheduler.vw_job_collections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.scheduler.job_collections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_collections</code> resource.

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
INSERT INTO azure.scheduler.job_collections (
jobCollectionName,
resourceGroupName,
subscriptionId,
name,
location,
tags,
properties
)
SELECT 
'{{ jobCollectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ name }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: type
      value: string
    - name: name
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: sku
          value:
            - name: name
              value: string
        - name: state
          value: string
        - name: quota
          value:
            - name: maxJobCount
              value: integer
            - name: maxJobOccurrence
              value: integer
            - name: maxRecurrence
              value:
                - name: frequency
                  value: string
                - name: interval
                  value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>job_collections</code> resource.

```sql
/*+ update */
UPDATE azure.scheduler.job_collections
SET 
name = '{{ name }}',
location = '{{ location }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
jobCollectionName = '{{ jobCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>job_collections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.scheduler.job_collections
WHERE jobCollectionName = '{{ jobCollectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
