---
title: sinks
hide_title: false
hide_table_of_contents: false
keywords:
  - sinks
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
<tr><td><b>Name</b></td><td><code>sinks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.sinks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The client-assigned sink identifier, unique within the project.For example: "my-syslog-errors-to-pubsub". Sink identifiers are limited to 100 characters and can include only the following characters: upper and lower-case alphanumeric characters, underscores, hyphens, and periods. First character has to be alphanumeric. |
| `description` | `string` | Optional. A description of this sink.The maximum length of the description is 8000 characters. |
| `filter` | `string` | Optional. An advanced logs filter (https://cloud.google.com/logging/docs/view/advanced-queries). The only exported log entries are those that are in the resource owning the sink and that match the filter.For example:logName="projects/[PROJECT_ID]/logs/[LOG_ID]" AND severity&gt;=ERROR |
| `includeChildren` | `boolean` | Optional. This field applies only to sinks owned by organizations and folders. If the field is false, the default, only the logs owned by the sink's parent resource are available for export. If the field is true, then log entries from all the projects, folders, and billing accounts contained in the sink's parent resource are also available for export. Whether a particular log entry from the children is exported depends on the sink's filter expression.For example, if this field is true, then the filter resource.type=gce_instance would export all Compute Engine VM instance log entries from all projects in the sink's parent.To only export entries from certain child projects, filter on the project part of the log name:logName:("projects/test-project1/" OR "projects/test-project2/") AND resource.type=gce_instance |
| `destination` | `string` | Required. The export destination: "storage.googleapis.com/[GCS_BUCKET]" "bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]" "pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]" "logging.googleapis.com/projects/[PROJECT_ID]" "logging.googleapis.com/projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]" The sink's writer_identity, set when the sink is created, must have permission to write to the destination or else the log entries are not exported. For more information, see Exporting Logs with Sinks (https://cloud.google.com/logging/docs/api/tasks/exporting-logs). |
| `bigqueryOptions` | `object` | Options that change functionality of a sink exporting data to BigQuery. |
| `updateTime` | `string` | Output only. The last update timestamp of the sink.This field may not be present for older sinks. |
| `createTime` | `string` | Output only. The creation timestamp of the sink.This field may not be present for older sinks. |
| `exclusions` | `array` | Optional. Log entries that match any of these exclusion filters will not be exported.If a log entry is matched by both filter and one of exclusion_filters it will not be exported. |
| `writerIdentity` | `string` | Output only. An IAM identity—a service account or group—under which Cloud Logging writes the exported log entries to the sink's destination. This field is either set by specifying custom_writer_identity or set automatically by sinks.create and sinks.update based on the value of unique_writer_identity in those methods.Until you grant this identity write-access to the destination, log entry exports from this sink will fail. For more information, see Granting Access for a Resource (https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource). Consult the destination service's documentation to determine the appropriate IAM roles to assign to the identity.Sinks that have a destination that is a log bucket in the same project as the sink cannot have a writer_identity and no additional permissions are required. |
| `disabled` | `boolean` | Optional. If set to true, then this sink is disabled and it does not export any log entries. |
| `outputVersionFormat` | `string` | Deprecated. This field is unused. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_sinks_get` | `SELECT` | `billingAccountsId, sinksId` | Gets a sink. |
| `billing_accounts_sinks_list` | `SELECT` | `billingAccountsId` | Lists sinks. |
| `folders_sinks_get` | `SELECT` | `foldersId, sinksId` | Gets a sink. |
| `folders_sinks_list` | `SELECT` | `foldersId` | Lists sinks. |
| `organizations_sinks_get` | `SELECT` | `organizationsId, sinksId` | Gets a sink. |
| `organizations_sinks_list` | `SELECT` | `organizationsId` | Lists sinks. |
| `projects_sinks_get` | `SELECT` | `projectsId, sinksId` | Gets a sink. |
| `projects_sinks_list` | `SELECT` | `projectsId` | Lists sinks. |
| `sinks_get` | `SELECT` | `sinkName` | Gets a sink. |
| `sinks_list` | `SELECT` | `parent, parentType` | Lists sinks. |
| `billing_accounts_sinks_create` | `INSERT` | `billingAccountsId` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `folders_sinks_create` | `INSERT` | `foldersId` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `organizations_sinks_create` | `INSERT` | `organizationsId` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `projects_sinks_create` | `INSERT` | `projectsId` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `sinks_create` | `INSERT` | `parent, parentType` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `billing_accounts_sinks_delete` | `DELETE` | `billingAccountsId, sinksId` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `folders_sinks_delete` | `DELETE` | `foldersId, sinksId` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `organizations_sinks_delete` | `DELETE` | `organizationsId, sinksId` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `projects_sinks_delete` | `DELETE` | `projectsId, sinksId` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `sinks_delete` | `DELETE` | `sinkName` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `_billing_accounts_sinks_list` | `EXEC` | `billingAccountsId` | Lists sinks. |
| `_folders_sinks_list` | `EXEC` | `foldersId` | Lists sinks. |
| `_organizations_sinks_list` | `EXEC` | `organizationsId` | Lists sinks. |
| `_projects_sinks_list` | `EXEC` | `projectsId` | Lists sinks. |
| `_sinks_list` | `EXEC` | `parent, parentType` | Lists sinks. |
| `billing_accounts_sinks_patch` | `EXEC` | `billingAccountsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `billing_accounts_sinks_update` | `EXEC` | `billingAccountsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `folders_sinks_patch` | `EXEC` | `foldersId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `folders_sinks_update` | `EXEC` | `foldersId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `organizations_sinks_patch` | `EXEC` | `organizationsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `organizations_sinks_update` | `EXEC` | `organizationsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `projects_sinks_patch` | `EXEC` | `projectsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `projects_sinks_update` | `EXEC` | `projectsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `sinks_update` | `EXEC` | `sinkName` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
