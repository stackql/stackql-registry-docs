---
title: jobs_query_results
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_query_results
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

Creates, updates, deletes, gets or lists a <code>jobs_query_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_query_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigquery.jobs_query_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cacheHit" /> | `boolean` | Whether the query result was fetched from the query cache. |
| <CopyableCode code="errors" /> | `array` | Output only. The first errors or warnings encountered during the running of the job. The final message includes the number of errors that caused the process to stop. Errors here do not necessarily mean that the job has completed or was unsuccessful. For more information about error messages, see [Error messages](https://cloud.google.com/bigquery/docs/error-messages). |
| <CopyableCode code="etag" /> | `string` | A hash of this response. |
| <CopyableCode code="jobComplete" /> | `boolean` | Whether the query has completed or not. If rows or totalRows are present, this will always be true. If this is false, totalRows will not be available. |
| <CopyableCode code="jobReference" /> | `object` | A job reference is a fully qualified identifier for referring to a job. |
| <CopyableCode code="kind" /> | `string` | The resource type of the response. |
| <CopyableCode code="numDmlAffectedRows" /> | `string` | Output only. The number of rows affected by a DML statement. Present only for DML statements INSERT, UPDATE or DELETE. |
| <CopyableCode code="pageToken" /> | `string` | A token used for paging results. When this token is non-empty, it indicates additional results are available. |
| <CopyableCode code="rows" /> | `array` | An object with as many results as can be contained within the maximum permitted reply size. To get any additional rows, you can call GetQueryResults and specify the jobReference returned above. Present only when the query completes successfully. The REST-based representation of this data leverages a series of JSON f,v objects for indicating fields and values. |
| <CopyableCode code="schema" /> | `object` | Schema of a table |
| <CopyableCode code="totalBytesProcessed" /> | `string` | The total number of bytes processed for this query. |
| <CopyableCode code="totalRows" /> | `string` | The total number of rows in the complete query result set, which can be more than the number of rows in this single page of results. Present only when the query completes successfully. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_query_results" /> | `SELECT` | <CopyableCode code="+jobId, projectId" /> | RPC to get the results of a query job. |

## `SELECT` examples

RPC to get the results of a query job.

```sql
SELECT
cacheHit,
errors,
etag,
jobComplete,
jobReference,
kind,
numDmlAffectedRows,
pageToken,
rows,
schema,
totalBytesProcessed,
totalRows
FROM google.bigquery.jobs_query_results
WHERE +jobId = '{{ +jobId }}'
AND projectId = '{{ projectId }}'; 
```
