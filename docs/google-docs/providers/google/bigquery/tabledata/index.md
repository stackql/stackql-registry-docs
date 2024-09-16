---
title: tabledata
hide_title: false
hide_table_of_contents: false
keywords:
  - tabledata
  - bigquery
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

Creates, updates, deletes, gets or lists a <code>tabledata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tabledata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.tabledata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A hash of this page of results. |
| <CopyableCode code="kind" /> | `string` | The resource type of the response. |
| <CopyableCode code="pageToken" /> | `string` | A token used for paging results. Providing this token instead of the startIndex parameter can help you retrieve stable results when an underlying table is changing. |
| <CopyableCode code="rows" /> | `array` | Rows of results. |
| <CopyableCode code="totalRows" /> | `string` | Total rows of the entire table. In order to show default value 0 we have to present it as string. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="+datasetId, +tableId, projectId" /> | List the content of a table in rows. |
| <CopyableCode code="insert_all" /> | `INSERT` | <CopyableCode code="+datasetId, +tableId, projectId" /> | Streams data into BigQuery one record at a time without needing to run a load job. |

## `SELECT` examples

List the content of a table in rows.

```sql
SELECT
etag,
kind,
pageToken,
rows,
totalRows
FROM google.bigquery.tabledata
WHERE +datasetId = '{{ +datasetId }}'
AND +tableId = '{{ +tableId }}'
AND projectId = '{{ projectId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tabledata</code> resource.

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
INSERT INTO google.bigquery.tabledata (
+datasetId,
+tableId,
projectId,
ignoreUnknownValues,
rows,
skipInvalidRows,
templateSuffix,
traceId
)
SELECT 
'{{ +datasetId }}',
'{{ +tableId }}',
'{{ projectId }}',
true|false,
'{{ rows }}',
true|false,
'{{ templateSuffix }}',
'{{ traceId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: ignoreUnknownValues
      value: '{{ ignoreUnknownValues }}'
    - name: rows
      value:
        - name: insertId
          value: '{{ insertId }}'
        - name: json
          value: []
    - name: skipInvalidRows
      value: '{{ skipInvalidRows }}'
    - name: templateSuffix
      value: '{{ templateSuffix }}'
    - name: traceId
      value: '{{ traceId }}'

```
</TabItem>
</Tabs>
