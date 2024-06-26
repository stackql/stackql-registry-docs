---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - toolresults
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.toolresults.environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="completionTime" /> | `object` | A Timestamp represents a point in time independent of any time zone or local calendar, encoded as a count of seconds and fractions of seconds at nanosecond resolution. The count is relative to an epoch at UTC midnight on January 1, 1970, in the proleptic Gregorian calendar which extends the Gregorian calendar backwards to year one. All minutes are 60 seconds long. Leap seconds are "smeared" so that no leap second table is needed for interpretation, using a [24-hour linear smear](https://developers.google.com/time/smear). The range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure that we can convert to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) date strings. |
| <CopyableCode code="creationTime" /> | `object` | A Timestamp represents a point in time independent of any time zone or local calendar, encoded as a count of seconds and fractions of seconds at nanosecond resolution. The count is relative to an epoch at UTC midnight on January 1, 1970, in the proleptic Gregorian calendar which extends the Gregorian calendar backwards to year one. All minutes are 60 seconds long. Leap seconds are "smeared" so that no leap second table is needed for interpretation, using a [24-hour linear smear](https://developers.google.com/time/smear). The range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By restricting to that range, we ensure that we can convert to and from [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) date strings. |
| <CopyableCode code="dimensionValue" /> | `array` | Dimension values describing the environment. Dimension values always consist of "Model", "Version", "Locale", and "Orientation". - In response: always set - In create request: always set - In update request: never set |
| <CopyableCode code="displayName" /> | `string` | A short human-readable name to display in the UI. Maximum of 100 characters. For example: Nexus 5, API 27. |
| <CopyableCode code="environmentId" /> | `string` | Output only. An Environment id. |
| <CopyableCode code="environmentResult" /> | `object` | Merged test result for environment. If the environment has only one step (no reruns or shards), then the merged result is the same as the step result. If the environment has multiple shards and/or reruns, then the results of shards and reruns that belong to the same environment are merged into one environment result. |
| <CopyableCode code="executionId" /> | `string` | Output only. An Execution id. |
| <CopyableCode code="historyId" /> | `string` | Output only. A History id. |
| <CopyableCode code="projectId" /> | `string` | Output only. A Project id. |
| <CopyableCode code="resultsStorage" /> | `object` | The storage for test results. |
| <CopyableCode code="shardSummaries" /> | `array` | Output only. Summaries of shards. Only one shard will present unless sharding feature is enabled in TestExecutionService. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_histories_executions_environments_get" /> | `SELECT` | <CopyableCode code="environmentId, executionId, historyId, projectId" /> | Gets an Environment. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Environment does not exist |
| <CopyableCode code="projects_histories_executions_environments_list" /> | `SELECT` | <CopyableCode code="executionId, historyId, projectId" /> | Lists Environments for a given Execution. The Environments are sorted by display name. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the containing Execution does not exist |
