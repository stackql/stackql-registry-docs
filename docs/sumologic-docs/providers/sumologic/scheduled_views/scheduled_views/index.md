---
title: scheduled_views
hide_title: false
hide_table_of_contents: false
keywords:
  - scheduled_views
  - scheduled_views
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scheduled_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.scheduled_views.scheduled_views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier for the scheduled view. |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the scheduled view. |
| <CopyableCode code="createdByOptimizeIt" /> | `boolean` | If the scheduled view is created by OptimizeIt. |
| <CopyableCode code="dataForwardingId" /> | `string` | An optional ID of a data forwarding configuration to be used by the scheduled view. |
| <CopyableCode code="error" /> | `string` | Errors related to the scheduled view. |
| <CopyableCode code="filledRanges" /> | `array` | List of the different units of filled ranges since the autoview has been created. |
| <CopyableCode code="indexId" /> | `string` | The `id` of the Index where the output from Scheduled view is stored. |
| <CopyableCode code="indexName" /> | `string` | Name of the index for the scheduled view. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="newRetentionPeriod" /> | `integer` | If the retention period is scheduled to be updated in the future (i.e., if retention period is previously reduced with value of reduceRetentionPeriodImmediately as false), this property gives the future value of retention period while retentionPeriod gives the current value. retentionPeriod will take up the value of newRetentionPeriod after the scheduled time. |
| <CopyableCode code="parsingMode" /> | `string` | Define the parsing mode to scan the JSON format log messages. Possible values are:<br />  1. `AutoParse`<br />  2. `Manual`<br />In AutoParse mode, the system automatically figures out fields to parse based on the search query. While in the Manual mode, no fields are parsed out automatically. For more information see [Dynamic Parsing](https://help.sumologic.com/?cid=0011). |
| <CopyableCode code="query" /> | `string` | The query that defines the data to be included in the scheduled view. |
| <CopyableCode code="retentionEffectiveAt" /> | `string` | When the newRetentionPeriod will become effective in UTC format. |
| <CopyableCode code="retentionPeriod" /> | `integer` | The number of days to retain data in the scheduled view, or -1 to use the default value for your account. Only relevant if your account has multi-retention enabled. |
| <CopyableCode code="startTime" /> | `string` | Start timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="status" /> | `string` | Status of the scheduled view. |
| <CopyableCode code="totalBytes" /> | `integer` | Total storage consumed by the scheduled view. |
| <CopyableCode code="totalMessageCount" /> | `integer` | Total number of messages for the scheduled view. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getScheduledView" /> | `SELECT` | <CopyableCode code="id, region" /> | Get a scheduled view with the given identifier. |
| <CopyableCode code="listScheduledViews" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of all scheduled views in the organization. The response is paginated with a default limit of 100 scheduled views per page. |
| <CopyableCode code="createScheduledView" /> | `INSERT` | <CopyableCode code="data__indexName, data__query, data__startTime, region" /> | Creates a new scheduled view in the organization. |
| <CopyableCode code="updateScheduledView" /> | `EXEC` | <CopyableCode code="id, region" /> | Update an existing scheduled view. |
