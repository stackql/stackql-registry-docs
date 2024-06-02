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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tabledata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="bigquery.tabledata" /></td></tr>
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
