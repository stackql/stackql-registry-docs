
---
title: recent_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - recent_queries
  - logging
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

Creates, updates, deletes or gets an <code>recent_query</code> resource or lists <code>recent_queries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recent_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.recent_queries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the recent query.In the format: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/recentQueries/[QUERY_ID]" For a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support)The QUERY_ID is a system generated alphanumeric ID. |
| <CopyableCode code="lastRunTime" /> | `string` | Output only. The timestamp when this query was last run. |
| <CopyableCode code="loggingQuery" /> | `object` | Describes a Cloud Logging query that can be run in Logs Explorer UI or via the logging API.In addition to the query itself, additional information may be stored to capture the display configuration and other UI state used in association with analysis of query results. |
| <CopyableCode code="opsAnalyticsQuery" /> | `object` | Describes an analytics query that can be run in the Log Analytics page of Google Cloud console.Preview: This is a preview feature and may be subject to change before final release. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_recent_queries_list" /> | `SELECT` | <CopyableCode code="billingAccountsId, locationsId" /> | Lists the RecentQueries that were created by the user making the request. |
| <CopyableCode code="folders_locations_recent_queries_list" /> | `SELECT` | <CopyableCode code="foldersId, locationsId" /> | Lists the RecentQueries that were created by the user making the request. |
| <CopyableCode code="organizations_locations_recent_queries_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists the RecentQueries that were created by the user making the request. |
| <CopyableCode code="projects_locations_recent_queries_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the RecentQueries that were created by the user making the request. |

## `SELECT` examples

Lists the RecentQueries that were created by the user making the request.

```sql
SELECT
name,
lastRunTime,
loggingQuery,
opsAnalyticsQuery
FROM google.logging.recent_queries
WHERE foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}'; 
```
