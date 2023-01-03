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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs_query_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.jobs_query_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cacheHit` | `boolean` | Whether the query result was fetched from the query cache. |
| `etag` | `string` | A hash of this response. |
| `jobReference` | `object` |  |
| `pageToken` | `string` | A token used for paging results. |
| `numDmlAffectedRows` | `string` | [Output-only] The number of rows affected by a DML statement. Present only for DML statements INSERT, UPDATE or DELETE. |
| `totalBytesProcessed` | `string` | The total number of bytes processed for this query. |
| `schema` | `object` |  |
| `errors` | `array` | [Output-only] The first errors or warnings encountered during the running of the job. The final message includes the number of errors that caused the process to stop. Errors here do not necessarily mean that the job has completed or was unsuccessful. |
| `kind` | `string` | The resource type of the response. |
| `rows` | `array` | An object with as many results as can be contained within the maximum permitted reply size. To get any additional rows, you can call GetQueryResults and specify the jobReference returned above. Present only when the query completes successfully. |
| `jobComplete` | `boolean` | Whether the query has completed or not. If rows or totalRows are present, this will always be true. If this is false, totalRows will not be available. |
| `totalRows` | `string` | The total number of rows in the complete query result set, which can be more than the number of rows in this single page of results. Present only when the query completes successfully. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `jobs_getQueryResults` | `SELECT` | `jobId, projectId` |
