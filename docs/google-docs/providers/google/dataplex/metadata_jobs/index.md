---
title: metadata_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_jobs
  - dataplex
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

Creates, updates, deletes, gets or lists a <code>metadata_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataplex.metadata_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The name of the resource that the configuration is applied to, in the format projects/{project_number}/locations/{location_id}/metadataJobs/{metadata_job_id}. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the metadata job was created. |
| <CopyableCode code="importResult" /> | `object` | Results from a metadata import job. |
| <CopyableCode code="importSpec" /> | `object` | Job specification for a metadata import job |
| <CopyableCode code="labels" /> | `object` | Optional. User-defined labels. |
| <CopyableCode code="status" /> | `object` | Metadata job status. |
| <CopyableCode code="type" /> | `string` | Required. Metadata job type. |
| <CopyableCode code="uid" /> | `string` | Output only. A system-generated, globally unique ID for the metadata job. If the metadata job is deleted and then re-created with the same name, this ID is different. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the metadata job was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_metadata_jobs_get" /> | `SELECT` | <CopyableCode code="locationsId, metadataJobsId, projectsId" /> | Gets a metadata job. |
| <CopyableCode code="projects_locations_metadata_jobs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists metadata jobs. |
| <CopyableCode code="projects_locations_metadata_jobs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a metadata job. For example, use a metadata job to import Dataplex Catalog entries and aspects from a third-party system into Dataplex. |
| <CopyableCode code="projects_locations_metadata_jobs_cancel" /> | `EXEC` | <CopyableCode code="locationsId, metadataJobsId, projectsId" /> | Cancels a metadata job.If you cancel a metadata import job that is in progress, the changes in the job might be partially applied. We recommend that you reset the state of the entry groups in your project by running another metadata job that reverts the changes from the canceled job. |

## `SELECT` examples

Lists metadata jobs.

```sql
SELECT
name,
createTime,
importResult,
importSpec,
labels,
status,
type,
uid,
updateTime
FROM google.dataplex.metadata_jobs
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metadata_jobs</code> resource.

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
INSERT INTO google.dataplex.metadata_jobs (
locationsId,
projectsId,
labels,
type,
importSpec
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ type }}',
'{{ importSpec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: uid
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: type
      value: string
    - name: importSpec
      value:
        - name: sourceStorageUri
          value: string
        - name: sourceCreateTime
          value: string
        - name: scope
          value:
            - name: entryGroups
              value:
                - string
            - name: entryTypes
              value:
                - string
            - name: aspectTypes
              value:
                - string
        - name: entrySyncMode
          value: string
        - name: aspectSyncMode
          value: string
        - name: logLevel
          value: string
    - name: importResult
      value:
        - name: deletedEntries
          value: string
        - name: updatedEntries
          value: string
        - name: createdEntries
          value: string
        - name: unchangedEntries
          value: string
        - name: recreatedEntries
          value: string
        - name: updateTime
          value: string
    - name: status
      value:
        - name: state
          value: string
        - name: message
          value: string
        - name: completionPercent
          value: integer
        - name: updateTime
          value: string

```
</TabItem>
</Tabs>
