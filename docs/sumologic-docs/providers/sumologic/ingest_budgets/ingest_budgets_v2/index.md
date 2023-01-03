---
title: ingest_budgets_v2
hide_title: false
hide_table_of_contents: false
keywords:
  - ingest_budgets_v2
  - ingest_budgets
  - sumologic    
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
<tr><td><b>Name</b></td><td><code>ingest_budgets_v2</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.ingest_budgets.ingest_budgets_v2</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the ingest budget. |
| `name` | `string` | Display name of the ingest budget. |
| `description` | `string` | Description of the ingest budget. |
| `modifiedAt` | `string` | The modified timestamp in UTC of the Ingest Budget. |
| `action` | `string` | Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are:<br />  * `stopCollecting`<br />  * `keepCollecting` |
| `usageStatus` | `string` | Status of the current usage. Can be `Normal`, `Approaching`, `Exceeded`, or `Unknown` (unable to retrieve usage). |
| `scope` | `string` | A scope is a constraint that will be used to identify the messages on which budget needs to be applied. A scope is consists of key and value separated by =. The field must be enabled in the fields table. Value supports wildcard. e.g. _sourceCategory=*prod*payment*, cluster=kafka. If the scope is defined _sourceCategory=*nginx* in this budget will be applied on messages having fields _sourceCategory=prod/nginx, _sourceCategory=dev/nginx, or _sourceCategory=dev/nginx/error |
| `createdAt` | `string` | The creation timestamp in UTC of the Ingest Budget. |
| `usageBytes` | `integer` | Current usage since the last reset, in bytes. |
| `auditThreshold` | `integer` | The threshold as a percentage of when an ingest budget's capacity usage is logged in the Audit Index. |
| `createdBy` | `string` | The identifier of the user who created the Ingest Budget. |
| `modifiedBy` | `string` | The identifier of the user who modified the Ingest Budget. |
| `capacityBytes` | `integer` | Capacity of the ingest budget, in bytes. It takes a few minutes for Collectors to stop collecting when capacity is reached. We recommend setting a soft limit that is lower than your needed hard limit. |
| `budgetVersion` | `integer` | The version of the Ingest Budget |
| `timezone` | `string` | Time zone of the reset time for the ingest budget. Follow the format in the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `resetTime` | `string` | Reset time of the ingest budget in HH:MM format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getIngestBudgetV2` | `SELECT` | `id` | Get an ingest budget by the given identifier. |
| `listIngestBudgetsV2` | `SELECT` |  | Get a list of all ingest budgets. The response is paginated with a default limit of 100 budgets per page. |
| `createIngestBudgetV2` | `INSERT` | `data__action, data__capacityBytes, data__name, data__resetTime, data__scope, data__timezone` | Create a new ingest budget. |
| `deleteIngestBudgetV2` | `DELETE` | `id` | Delete an ingest budget with the given identifier. |
| `updateIngestBudgetV2` | `EXEC` | `id, data__action, data__capacityBytes, data__name, data__resetTime, data__scope, data__timezone` | Update an existing ingest budget. All properties specified in the request are required. |
