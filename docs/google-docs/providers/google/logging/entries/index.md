---
title: entries
hide_title: false
hide_table_of_contents: false
keywords:
  - entries
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

Creates, updates, deletes, gets or lists a <code>entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="entries" /> | `array` | A list of log entries. If entries is empty, nextPageToken may still be returned, indicating that more entries may exist. See nextPageToken for more information. |
| <CopyableCode code="nextPageToken" /> | `string` | If there might be more results than those appearing in this response, then nextPageToken is included. To get the next set of results, call this method again using the value of nextPageToken as pageToken.If a value for next_page_token appears and the entries field is empty, it means that the search found no log entries so far but it did not have time to search all the possible log entries. Retry the method with this value for page_token to continue the search. Alternatively, consider speeding up the search by changing your filter to specify a single log name or resource type, or to narrow the time range of the search. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="entries_list" /> | `SELECT` | <CopyableCode code="" /> | Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see Exporting Logs (https://cloud.google.com/logging/docs/export). |
| <CopyableCode code="entries_copy" /> | `EXEC` | <CopyableCode code="" /> | Copies a set of log entries from a log bucket to a Cloud Storage bucket. |
| <CopyableCode code="entries_tail" /> | `EXEC` | <CopyableCode code="" /> | Streaming read of log entries as they are received. Until the stream is terminated, it will continue reading logs. |
| <CopyableCode code="entries_write" /> | `EXEC` | <CopyableCode code="" /> | Writes log entries to Logging. This API method is the only way to send log entries to Logging. This method is used, directly or indirectly, by the Logging agent (fluentd) and all logging libraries configured to use Logging. A single request may contain log entries for a maximum of 1000 different resource names (projects, organizations, billing accounts or folders), where the resource name for a log entry is determined from its logName field. |

## `SELECT` examples

Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account. For ways to export log entries, see Exporting Logs (https://cloud.google.com/logging/docs/export).

```sql
SELECT
entries,
nextPageToken
FROM google.logging.entries
;
```
