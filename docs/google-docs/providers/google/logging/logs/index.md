---
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - logs
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

Creates, updates, deletes, gets or lists a <code>logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_buckets_views_logs_list" /> | `SELECT` | <CopyableCode code="billingAccountsId, bucketsId, locationsId, viewsId" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="billing_accounts_logs_list" /> | `SELECT` | <CopyableCode code="billingAccountsId" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="folders_locations_buckets_views_logs_list" /> | `SELECT` | <CopyableCode code="bucketsId, foldersId, locationsId, viewsId" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="folders_logs_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="logs_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="organizations_locations_buckets_views_logs_list" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, organizationsId, viewsId" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="organizations_logs_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="projects_locations_buckets_views_logs_list" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, projectsId, viewsId" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="projects_logs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| <CopyableCode code="billing_accounts_logs_delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, logsId" /> | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| <CopyableCode code="folders_logs_delete" /> | `DELETE` | <CopyableCode code="foldersId, logsId" /> | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| <CopyableCode code="logs_delete" /> | `DELETE` | <CopyableCode code="logName" /> | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| <CopyableCode code="organizations_logs_delete" /> | `DELETE` | <CopyableCode code="logsId, organizationsId" /> | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| <CopyableCode code="projects_logs_delete" /> | `DELETE` | <CopyableCode code="logsId, projectsId" /> | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |

## `SELECT` examples

Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed.

```sql
SELECT
column_anon
FROM google.logging.logs
WHERE foldersId = '{{ foldersId }}';
```

## `DELETE` example

Deletes the specified <code>logs</code> resource.

```sql
/*+ delete */
DELETE FROM google.logging.logs
WHERE logName = '{{ logName }}';
```
