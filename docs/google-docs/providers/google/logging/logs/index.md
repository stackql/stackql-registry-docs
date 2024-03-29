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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.logs</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_locations_buckets_views_logs_list` | `SELECT` | `billingAccountsId, bucketsId, locationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `billing_accounts_logs_list` | `SELECT` | `billingAccountsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `folders_locations_buckets_views_logs_list` | `SELECT` | `bucketsId, foldersId, locationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `folders_logs_list` | `SELECT` | `foldersId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `logs_list` | `SELECT` | `parent, parentType` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `organizations_locations_buckets_views_logs_list` | `SELECT` | `bucketsId, locationsId, organizationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `organizations_logs_list` | `SELECT` | `organizationsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `projects_locations_buckets_views_logs_list` | `SELECT` | `bucketsId, locationsId, projectsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `projects_logs_list` | `SELECT` | `projectsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `billing_accounts_logs_delete` | `DELETE` | `billingAccountsId, logsId` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `folders_logs_delete` | `DELETE` | `foldersId, logsId` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `logs_delete` | `DELETE` | `logName` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `organizations_logs_delete` | `DELETE` | `logsId, organizationsId` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `projects_logs_delete` | `DELETE` | `logsId, projectsId` | Deletes all the log entries in a log for the _Default Log Bucket. The log reappears if it receives new entries. Log entries written shortly before the delete operation might not be deleted. Entries received after the delete operation with a timestamp before the operation will be deleted. |
| `_billing_accounts_locations_buckets_views_logs_list` | `EXEC` | `billingAccountsId, bucketsId, locationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `_billing_accounts_logs_list` | `EXEC` | `billingAccountsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `_folders_locations_buckets_views_logs_list` | `EXEC` | `bucketsId, foldersId, locationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `_folders_logs_list` | `EXEC` | `foldersId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `_logs_list` | `EXEC` | `parent, parentType` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `_organizations_locations_buckets_views_logs_list` | `EXEC` | `bucketsId, locationsId, organizationsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `_organizations_logs_list` | `EXEC` | `organizationsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `_projects_locations_buckets_views_logs_list` | `EXEC` | `bucketsId, locationsId, projectsId, viewsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
| `_projects_logs_list` | `EXEC` | `projectsId` | Lists the logs in projects, organizations, folders, or billing accounts. Only logs that have entries are listed. |
