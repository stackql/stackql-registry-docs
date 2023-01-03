---
title: security_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - security_reports
  - apigee
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
<tr><td><b>Name</b></td><td><code>security_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.security_reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resultRows` | `string` | ResultRows is available only after the query is completed. |
| `self` | `string` | Self link of the query. Example: `/organizations/myorg/environments/myenv/securityReports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` or following format if query is running at host level: `/organizations/myorg/hostSecurityReports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` |
| `state` | `string` | Query state could be "enqueued", "running", "completed", "failed". |
| `displayName` | `string` | Display Name specified by the user. |
| `queryParams` | `object` | Metadata for the security report. |
| `updated` | `string` | Output only. Last updated timestamp for the query. |
| `result` | `object` | Contains informations about the security report results. |
| `resultFileSize` | `string` | ResultFileSize is available only after the query is completed. |
| `error` | `string` | Error is set when query fails. |
| `envgroupHostname` | `string` | Hostname is available only when query is executed at host level. |
| `reportDefinitionId` | `string` | Report Definition ID. |
| `created` | `string` | Creation time of the query. |
| `executionTime` | `string` | ExecutionTime is available only after the query is completed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_securityReports_get` | `SELECT` | `environmentsId, organizationsId, securityReportsId` | Get security report status If the query is still in progress, the `state` is set to "running" After the query has completed successfully, `state` is set to "completed" |
| `organizations_environments_securityReports_list` | `SELECT` | `environmentsId, organizationsId` | Return a list of Security Reports |
| `organizations_environments_securityReports_create` | `INSERT` | `environmentsId, organizationsId` | Submit a report request to be processed in the background. If the submission succeeds, the API returns a 200 status and an ID that refer to the report request. In addition to the HTTP status 200, the `state` of "enqueued" means that the request succeeded. |
