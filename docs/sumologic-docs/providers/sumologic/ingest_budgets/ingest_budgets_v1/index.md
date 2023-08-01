---
title: ingest_budgets_v1
hide_title: false
hide_table_of_contents: false
keywords:
  - ingest_budgets_v1
  - ingest_budgets
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ingest_budgets_v1</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.ingest_budgets.ingest_budgets_v1</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the ingest budget. |
| `name` | `string` | Display name of the ingest budget. |
| `description` | `string` | Description of the ingest budget. |
| `timezone` | `string` | Time zone of the reset time for the ingest budget. Follow the format in the [IANA Time Zone Database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List). |
| `auditThreshold` | `integer` | The threshold as a percentage of when an ingest budget's capacity usage is logged in the Audit Index. |
| `capacityBytes` | `integer` | Capacity of the ingest budget, in bytes. It takes a few minutes for Collectors to stop collecting when capacity is reached. We recommend setting a soft limit that is lower than your needed hard limit. |
| `usageStatus` | `string` | Status of the current usage. Can be `Normal`, `Approaching`, `Exceeded`, or `Unknown` (unable to retrieve usage). |
| `modifiedAt` | `string` | Last modification timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `action` | `string` | Action to take when ingest budget's capacity is reached. All actions are audited. Supported values are:<br />  * `stopCollecting`<br />  * `keepCollecting` |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `fieldValue` | `string` | Custom field value that is used to assign Collectors to the ingest budget. |
| `numberOfCollectors` | `integer` | Number of collectors assigned to the ingest budget. |
| `modifiedByUser` | `object` |  |
| `usageBytes` | `integer` | Current usage since the last reset, in bytes. |
| `createdByUser` | `object` |  |
| `resetTime` | `string` | Reset time of the ingest budget in HH:MM format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getIngestBudget` | `SELECT` | `id, region` | Get an ingest budget by the given identifier. |
| `listIngestBudgets` | `SELECT` | `region` | Get a list of all ingest budgets. The response is paginated with a default limit of 100 budgets per page. |
| `createIngestBudget` | `INSERT` | `data__action, data__capacityBytes, data__fieldValue, data__name, data__resetTime, data__timezone, region` | Create a new ingest budget. |
| `deleteIngestBudget` | `DELETE` | `id, region` | Delete an ingest budget with the given identifier. |
| `updateIngestBudget` | `EXEC` | `id, data__action, data__capacityBytes, data__fieldValue, data__name, data__resetTime, data__timezone, region` | Update an existing ingest budget. All properties specified in the request are required. |
