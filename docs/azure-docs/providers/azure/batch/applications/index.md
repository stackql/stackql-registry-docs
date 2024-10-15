---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - batch
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

Creates, updates, deletes, gets or lists a <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.applications" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="allow_updates" /> | `text` | field from the `properties` object |
| <CopyableCode code="applicationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="properties" /> | `object` | The properties associated with the Application. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Gets information about the specified application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all of the applications in the specified account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Adds an application to the specified Batch account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Deletes an application. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, applicationName, resourceGroupName, subscriptionId" /> | Updates settings for the specified application. |

## `SELECT` examples

Lists all of the applications in the specified account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_applications', value: 'view', },
        { label: 'applications', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
allow_updates,
applicationName,
default_version,
display_name,
etag,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.batch.vw_applications
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
tags,
type
FROM azure.batch.applications
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>applications</code> resource.

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
INSERT INTO azure.batch.applications (
accountName,
applicationName,
resourceGroupName,
subscriptionId,
properties,
tags
)
SELECT 
'{{ accountName }}',
'{{ applicationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: displayName
          value: string
        - name: allowUpdates
          value: boolean
        - name: defaultVersion
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>applications</code> resource.

```sql
/*+ update */
UPDATE azure.batch.applications
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
accountName = '{{ accountName }}'
AND applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>applications</code> resource.

```sql
/*+ delete */
DELETE FROM azure.batch.applications
WHERE accountName = '{{ accountName }}'
AND applicationName = '{{ applicationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
