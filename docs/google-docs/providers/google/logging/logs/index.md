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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.logs</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAccounts_locations_buckets_views_logs_list` | `SELECT` | `billingAccountsId, bucketsId, locationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `billingAccounts_logs_list` | `SELECT` | `billingAccountsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `folders_locations_buckets_views_logs_list` | `SELECT` | `bucketsId, foldersId, locationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `folders_logs_list` | `SELECT` | `foldersId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `list` | `SELECT` | `parent` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `organizations_locations_buckets_views_logs_list` | `SELECT` | `bucketsId, locationsId, organizationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `organizations_logs_list` | `SELECT` | `organizationsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `projects_locations_buckets_views_logs_list` | `SELECT` | `bucketsId, locationsId, projectsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `projects_logs_list` | `SELECT` | `projectsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `billingAccounts_logs_delete` | `DELETE` | `billingAccountsId, logsId` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `delete` | `DELETE` | `logName` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `folders_logs_delete` | `DELETE` | `foldersId, logsId` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `organizations_logs_delete` | `DELETE` | `logsId, organizationsId` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `projects_logs_delete` | `DELETE` | `logsId, projectsId` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
