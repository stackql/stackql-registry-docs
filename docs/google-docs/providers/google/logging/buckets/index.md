---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
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
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.buckets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the bucket.For example:projects/my-project/locations/global/buckets/my-bucketFor a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support)For the location of global it is unspecified where log entries are actually stored.After a bucket has been created, the location cannot be changed. |
| `description` | `string` | Describes this bucket. |
| `locked` | `boolean` | Whether the bucket is locked.The retention period on a locked bucket cannot be changed. Locked buckets may only be deleted if they are empty. |
| `lifecycleState` | `string` | Output only. The bucket lifecycle state. |
| `indexConfigs` | `array` | A list of indexed fields and related configuration data. |
| `restrictedFields` | `array` | Log entry field paths that are denied access in this bucket.The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation.Restricting a repeated field will restrict all values. Adding a parent will block all child fields. (e.g. foo.bar will block foo.bar.baz) |
| `cmekSettings` | `object` | Describes the customer-managed encryption key (CMEK) settings associated with a project, folder, organization, billing account, or flexible resource.Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |
| `updateTime` | `string` | Output only. The last update timestamp of the bucket. |
| `createTime` | `string` | Output only. The creation timestamp of the bucket. This is not set for any of the default buckets. |
| `retentionDays` | `integer` | Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAccounts_locations_buckets_get` | `SELECT` | `billingAccountsId, bucketsId, locationsId` | Gets a log bucket. |
| `billingAccounts_locations_buckets_list` | `SELECT` | `billingAccountsId, locationsId` | Lists log buckets. |
| `folders_locations_buckets_get` | `SELECT` | `bucketsId, foldersId, locationsId` | Gets a log bucket. |
| `folders_locations_buckets_list` | `SELECT` | `foldersId, locationsId` | Lists log buckets. |
| `locations_buckets_list` | `SELECT` | `parent` | Lists log buckets. |
| `organizations_locations_buckets_get` | `SELECT` | `bucketsId, locationsId, organizationsId` | Gets a log bucket. |
| `organizations_locations_buckets_list` | `SELECT` | `locationsId, organizationsId` | Lists log buckets. |
| `projects_locations_buckets_get` | `SELECT` | `bucketsId, locationsId, projectsId` | Gets a log bucket. |
| `projects_locations_buckets_list` | `SELECT` | `locationsId, projectsId` | Lists log buckets. |
| `billingAccounts_locations_buckets_create` | `INSERT` | `billingAccountsId, locationsId` | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| `folders_locations_buckets_create` | `INSERT` | `foldersId, locationsId` | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| `locations_buckets_create` | `INSERT` | `parent` | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| `organizations_locations_buckets_create` | `INSERT` | `locationsId, organizationsId` | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| `projects_locations_buckets_create` | `INSERT` | `locationsId, projectsId` | Creates a log bucket that can be used to store log entries. After a bucket has been created, the bucket's location cannot be changed. |
| `billingAccounts_locations_buckets_delete` | `DELETE` | `billingAccountsId, bucketsId, locationsId` | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| `folders_locations_buckets_delete` | `DELETE` | `bucketsId, foldersId, locationsId` | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| `locations_buckets_delete` | `DELETE` | `name` | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| `organizations_locations_buckets_delete` | `DELETE` | `bucketsId, locationsId, organizationsId` | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| `projects_locations_buckets_delete` | `DELETE` | `bucketsId, locationsId, projectsId` | Deletes a log bucket.Changes the bucket's lifecycle_state to the DELETE_REQUESTED state. After 7 days, the bucket will be purged and all log entries in the bucket will be permanently deleted. |
| `billingAccounts_locations_buckets_patch` | `EXEC` | `billingAccountsId, bucketsId, locationsId` | Updates a log bucket. This method replaces the following fields in the existing bucket with values from the new bucket: retention_periodIf the retention period is decreased and the bucket is locked, FAILED_PRECONDITION will be returned.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| `billingAccounts_locations_buckets_undelete` | `EXEC` | `billingAccountsId, bucketsId, locationsId` | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
| `folders_locations_buckets_patch` | `EXEC` | `bucketsId, foldersId, locationsId` | Updates a log bucket. This method replaces the following fields in the existing bucket with values from the new bucket: retention_periodIf the retention period is decreased and the bucket is locked, FAILED_PRECONDITION will be returned.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| `folders_locations_buckets_undelete` | `EXEC` | `bucketsId, foldersId, locationsId` | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
| `locations_buckets_patch` | `EXEC` | `name` | Updates a log bucket. This method replaces the following fields in the existing bucket with values from the new bucket: retention_periodIf the retention period is decreased and the bucket is locked, FAILED_PRECONDITION will be returned.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| `organizations_locations_buckets_patch` | `EXEC` | `bucketsId, locationsId, organizationsId` | Updates a log bucket. This method replaces the following fields in the existing bucket with values from the new bucket: retention_periodIf the retention period is decreased and the bucket is locked, FAILED_PRECONDITION will be returned.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| `organizations_locations_buckets_undelete` | `EXEC` | `bucketsId, locationsId, organizationsId` | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
| `projects_locations_buckets_patch` | `EXEC` | `bucketsId, locationsId, projectsId` | Updates a log bucket. This method replaces the following fields in the existing bucket with values from the new bucket: retention_periodIf the retention period is decreased and the bucket is locked, FAILED_PRECONDITION will be returned.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| `projects_locations_buckets_undelete` | `EXEC` | `bucketsId, locationsId, projectsId` | Undeletes a log bucket. A bucket that has been deleted can be undeleted within the grace period of 7 days. |
