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
| `nextPageToken` | `string` | If there might be more results than appear in this response, then nextPageToken is included. To get the next set of results, call the same method again using the value of nextPageToken as pageToken. |
| `sinks` | `array` | A list of sinks. |
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
| `sinks_list` | `SELECT` | `parent` | Lists sinks. |
| `billing_accounts_sinks_create` | `INSERT` | `billingAccountsId` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `folders_sinks_create` | `INSERT` | `foldersId` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `organizations_sinks_create` | `INSERT` | `organizationsId` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `projects_sinks_create` | `INSERT` | `projectsId` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `sinks_create` | `INSERT` | `parent` | Creates a sink that exports specified log entries to a destination. The export begins upon ingress, unless the sink's writer_identity is not permitted to write to the destination. A sink can export log entries only from the resource owning the sink. |
| `billing_accounts_sinks_delete` | `DELETE` | `billingAccountsId, sinksId` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `folders_sinks_delete` | `DELETE` | `foldersId, sinksId` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `organizations_sinks_delete` | `DELETE` | `organizationsId, sinksId` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `projects_sinks_delete` | `DELETE` | `projectsId, sinksId` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `sinks_delete` | `DELETE` | `sinkName` | Deletes a sink. If the sink has a unique writer_identity, then that service account is also deleted. |
| `billing_accounts_sinks_patch` | `EXEC` | `billingAccountsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `billing_accounts_sinks_update` | `EXEC` | `billingAccountsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `folders_sinks_patch` | `EXEC` | `foldersId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `folders_sinks_update` | `EXEC` | `foldersId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `organizations_sinks_patch` | `EXEC` | `organizationsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `organizations_sinks_update` | `EXEC` | `organizationsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `projects_sinks_patch` | `EXEC` | `projectsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `projects_sinks_update` | `EXEC` | `projectsId, sinksId` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
| `sinks_update` | `EXEC` | `sinkName` | Updates a sink. This method replaces the following fields in the existing sink with values from the new sink: destination, and filter.The updated sink might also have a new writer_identity; see the unique_writer_identity field. |
