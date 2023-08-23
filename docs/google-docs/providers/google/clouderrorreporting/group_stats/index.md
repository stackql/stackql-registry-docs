---
title: group_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - group_stats
  - clouderrorreporting
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
<tr><td><b>Name</b></td><td><code>group_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.clouderrorreporting.group_stats</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `group` | `object` | Description of a group of similar error events. |
| `timedCounts` | `array` | Approximate number of occurrences over time. Timed counts returned by ListGroups are guaranteed to be: - Inside the requested time interval - Non-overlapping, and - Ordered by ascending time. |
| `firstSeenTime` | `string` | Approximate first occurrence that was ever seen for this group and which matches the given filter criteria, ignoring the time_range that was specified in the request. |
| `affectedUsersCount` | `string` | Approximate number of affected users in the given group that match the filter criteria. Users are distinguished by data in the ErrorContext of the individual error events, such as their login name or their remote IP address in case of HTTP requests. The number of affected users can be zero even if the number of errors is non-zero if no data was provided from which the affected user could be deduced. Users are counted based on data in the request context that was provided in the error report. If more users are implicitly affected, such as due to a crash of the whole service, this is not reflected here. |
| `numAffectedServices` | `integer` | The total number of services with a non-zero error count for the given filter criteria. |
| `representative` | `object` | An error event which is returned by the Error Reporting system. |
| `count` | `string` | Approximate total number of events in the given group that match the filter criteria. |
| `lastSeenTime` | `string` | Approximate last occurrence that was ever seen for this group and which matches the given filter criteria, ignoring the time_range that was specified in the request. |
| `affectedServices` | `array` | Service contexts with a non-zero error count for the given filter criteria. This list can be truncated if multiple services are affected. Refer to `num_affected_services` for the total count. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `projectsId` |
| `_list` | `EXEC` | `projectsId` |
