---
title: import_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - import_jobs
  - storage_cache
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

Creates, updates, deletes, gets or lists a <code>import_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.import_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the import job. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="amlFilesystemName, importJobName, resourceGroupName, subscriptionId" /> | Returns an import job. |
| <CopyableCode code="list_by_aml_filesystem" /> | `SELECT` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Returns all import jobs the user has access to under an AML File System. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="amlFilesystemName, importJobName, resourceGroupName, subscriptionId" /> | Create or update an import job. Import jobs are automatically deleted 72 hours after completion. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="amlFilesystemName, importJobName, resourceGroupName, subscriptionId" /> | Schedules an import job for deletion. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="amlFilesystemName, importJobName, resourceGroupName, subscriptionId" /> | Update an import job instance. |

## `SELECT` examples

Returns all import jobs the user has access to under an AML File System.


```sql
SELECT
location,
properties,
tags
FROM azure.storage_cache.import_jobs
WHERE amlFilesystemName = '{{ amlFilesystemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>import_jobs</code> resource.

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
INSERT INTO azure.storage_cache.import_jobs (
amlFilesystemName,
importJobName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ amlFilesystemName }}',
'{{ importJobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: importPrefixes
          value:
            - string
        - name: conflictResolutionMode
          value: string
        - name: maximumErrors
          value: integer
        - name: status
          value:
            - name: state
              value: string
            - name: statusMessage
              value: string
            - name: totalBlobsWalked
              value: integer
            - name: blobsWalkedPerSecond
              value: integer
            - name: totalBlobsImported
              value: integer
            - name: blobsImportedPerSecond
              value: integer
            - name: lastCompletionTime
              value: string
            - name: lastStartedTime
              value: string
            - name: totalErrors
              value: integer
            - name: totalConflicts
              value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>import_jobs</code> resource.

```sql
/*+ update */
UPDATE azure.storage_cache.import_jobs
SET 
tags = '{{ tags }}'
WHERE 
amlFilesystemName = '{{ amlFilesystemName }}'
AND importJobName = '{{ importJobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>import_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_cache.import_jobs
WHERE amlFilesystemName = '{{ amlFilesystemName }}'
AND importJobName = '{{ importJobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
