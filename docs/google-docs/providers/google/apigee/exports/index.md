---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
  - apigee
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

Creates, updates, deletes or gets an <code>export</code> resource or lists <code>exports</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.exports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Display name of the export job. |
| <CopyableCode code="description" /> | `string` | Description of the export job. |
| <CopyableCode code="created" /> | `string` | Output only. Time the export job was created. |
| <CopyableCode code="datastoreName" /> | `string` | Name of the datastore that is the destination of the export job [datastore] |
| <CopyableCode code="error" /> | `string` | Output only. Error is set when export fails |
| <CopyableCode code="executionTime" /> | `string` | Output only. Execution time for this export job. If the job is still in progress, it will be set to the amount of time that has elapsed since`created`, in seconds. Else, it will set to (`updated` - `created`), in seconds. |
| <CopyableCode code="self" /> | `string` | Output only. Self link of the export job. A URI that can be used to retrieve the status of an export job. Example: `/organizations/myorg/environments/myenv/analytics/exports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` |
| <CopyableCode code="state" /> | `string` | Output only. Status of the export job. Valid values include `enqueued`, `running`, `completed`, and `failed`. |
| <CopyableCode code="updated" /> | `string` | Output only. Time the export job was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_analytics_exports_get" /> | `SELECT` | <CopyableCode code="environmentsId, exportsId, organizationsId" /> | Gets the details and status of an analytics export job. If the export job is still in progress, its `state` is set to "running". After the export job has completed successfully, its `state` is set to "completed". If the export job fails, its `state` is set to `failed`. |
| <CopyableCode code="organizations_environments_analytics_exports_list" /> | `SELECT` | <CopyableCode code="environmentsId, organizationsId" /> | Lists the details and status of all analytics export jobs belonging to the parent organization and environment. |
| <CopyableCode code="organizations_environments_analytics_exports_create" /> | `INSERT` | <CopyableCode code="environmentsId, organizationsId" /> | Submit a data export job to be processed in the background. If the request is successful, the API returns a 201 status, a URI that can be used to retrieve the status of the export job, and the `state` value of "enqueued". |

## `SELECT` examples

Lists the details and status of all analytics export jobs belonging to the parent organization and environment.

```sql
SELECT
name,
description,
created,
datastoreName,
error,
executionTime,
self,
state,
updated
FROM google.apigee.exports
WHERE environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>exports</code> resource.

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
INSERT INTO google.apigee.exports (
environmentsId,
organizationsId,
csvDelimiter,
name,
outputFormat,
dateRange,
datastoreName,
description
)
SELECT 
'{{ environmentsId }}',
'{{ organizationsId }}',
'{{ csvDelimiter }}',
'{{ name }}',
'{{ outputFormat }}',
'{{ dateRange }}',
'{{ datastoreName }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: csvDelimiter
        value: '{{ csvDelimiter }}'
      - name: name
        value: '{{ name }}'
      - name: outputFormat
        value: '{{ outputFormat }}'
      - name: dateRange
        value: '{{ dateRange }}'
      - name: datastoreName
        value: '{{ datastoreName }}'
      - name: description
        value: '{{ description }}'

```
</TabItem>
</Tabs>
