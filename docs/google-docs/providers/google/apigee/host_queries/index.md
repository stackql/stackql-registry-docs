---
title: host_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - host_queries
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.host_queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Asynchronous Query Name. |
| `result` | `object` |  |
| `resultFileSize` | `string` | ResultFileSize is available only after the query is completed. |
| `queryParams` | `object` |  |
| `resultRows` | `string` | ResultRows is available only after the query is completed. |
| `envgroupHostname` | `string` | Hostname is available only when query is executed at host level. |
| `error` | `string` | Error is set when query fails. |
| `created` | `string` | Creation time of the query. |
| `self` | `string` | Self link of the query. Example: `/organizations/myorg/environments/myenv/queries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` or following format if query is running at host level: `/organizations/myorg/hostQueries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` |
| `updated` | `string` | Last updated timestamp for the query. |
| `reportDefinitionId` | `string` | Asynchronous Report ID. |
| `state` | `string` | Query state could be "enqueued", "running", "completed", "failed". |
| `executionTime` | `string` | ExecutionTime is available only after the query is completed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_host_queries_get` | `SELECT` | `hostQueriesId, organizationsId` | Get status of a query submitted at host level. If the query is still in progress, the `state` is set to "running" After the query has completed successfully, `state` is set to "completed" |
| `organizations_host_queries_list` | `SELECT` | `organizationsId` | Return a list of Asynchronous Queries at host level. |
| `organizations_host_queries_create` | `INSERT` | `organizationsId` | Submit a query at host level to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the `state` of "enqueued" means that the request succeeded. |
