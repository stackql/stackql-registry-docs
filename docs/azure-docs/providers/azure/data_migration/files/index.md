---
title: files
hide_title: false
hide_table_of_contents: false
keywords:
  - files
  - data_migration
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.files" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="etag" /> | `text` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="extension" /> | `text` | field from the `properties` object |
| <CopyableCode code="fileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="file_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="media_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="properties" /> | `object` | Base class for file properties. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fileName, groupName, projectName, serviceName, subscriptionId" /> | The files resource is a nested, proxy-only resource representing a file stored under the project resource. This method retrieves information about a file. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupName, projectName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. This method returns a list of files owned by a project resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fileName, groupName, projectName, serviceName, subscriptionId" /> | The PUT method creates a new file or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fileName, groupName, projectName, serviceName, subscriptionId" /> | This method deletes a file. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="fileName, groupName, projectName, serviceName, subscriptionId" /> | This method updates an existing file. |
| <CopyableCode code="read" /> | `EXEC` | <CopyableCode code="fileName, groupName, projectName, serviceName, subscriptionId" /> | This method is used for requesting storage information using which contents of the file can be downloaded. |
| <CopyableCode code="read_write" /> | `EXEC` | <CopyableCode code="fileName, groupName, projectName, serviceName, subscriptionId" /> | This method is used for requesting information for reading and writing the file content. |

## `SELECT` examples

The project resource is a nested resource representing a stored migration project. This method returns a list of files owned by a project resource.

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
id,
name,
etag,
extension,
fileName,
file_path,
groupName,
last_modified,
media_type,
projectName,
serviceName,
size,
subscriptionId,
system_data,
type
FROM azure.data_migration.vw_files
WHERE groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
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
systemData,
type
FROM azure.data_migration.files
WHERE groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
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
INSERT INTO azure.data_migration.files (
fileName,
groupName,
projectName,
serviceName,
subscriptionId,
etag,
properties
)
SELECT 
'{{ fileName }}',
'{{ groupName }}',
'{{ projectName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
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
        - name: extension
          value: string
        - name: filePath
          value: string
        - name: lastModified
          value: string
        - name: mediaType
          value: string
        - name: size
          value: integer
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>files</code> resource.

```sql
/*+ update */
UPDATE azure.data_migration.files
SET 
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
fileName = '{{ fileName }}'
AND groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>files</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_migration.files
WHERE fileName = '{{ fileName }}'
AND groupName = '{{ groupName }}'
AND projectName = '{{ projectName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
