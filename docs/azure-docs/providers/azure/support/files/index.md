---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - support
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

Creates, updates, deletes, gets or lists a <code>files</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.files" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_files', value: 'view', },
        { label: 'files', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="chunk_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="fileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="fileWorkspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_of_chunks" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of a file. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fileName, fileWorkspaceName, subscriptionId" /> | Returns details of a specific file in a work space. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="fileWorkspaceName, subscriptionId" /> | Lists all the Files information under a workspace for an Azure subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="fileName, fileWorkspaceName, subscriptionId" /> | Creates a new file under a workspace for the specified subscription. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="fileName, fileWorkspaceName, subscriptionId" /> | This API allows you to upload content to a file |

## `SELECT` examples

Lists all the Files information under a workspace for an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_files', value: 'view', },
        { label: 'files', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
chunk_size,
created_on,
fileName,
fileWorkspaceName,
file_size,
number_of_chunks,
subscriptionId
FROM azure.support.vw_files
WHERE fileWorkspaceName = '{{ fileWorkspaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.support.files
WHERE fileWorkspaceName = '{{ fileWorkspaceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>files</code> resource.

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
INSERT INTO azure.support.files (
fileName,
fileWorkspaceName,
subscriptionId,
properties
)
SELECT 
'{{ fileName }}',
'{{ fileWorkspaceName }}',
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
        - name: createdOn
          value: string
        - name: chunkSize
          value: integer
        - name: fileSize
          value: integer
        - name: numberOfChunks
          value: integer

```
</TabItem>
</Tabs>
