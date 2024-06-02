---
title: saved_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_queries
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saved_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="logging.saved_queries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the saved query.In the format: "projects/[PROJECT_ID]/locations/[LOCATION_ID]/savedQueries/[QUERY_ID]" For a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support#bucket-regions)After the saved query is created, the location cannot be changed.If the user doesn't provide a QUERY_ID, the system will generate an alphanumeric ID. |
| <CopyableCode code="description" /> | `string` | Optional. A human readable description of the saved query. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the saved query was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The user specified title for the SavedQuery. |
| <CopyableCode code="loggingQuery" /> | `object` | Describes a Cloud Logging query that can be run in Logs Explorer UI or via the logging API.In addition to the query itself, additional information may be stored to capture the display configuration and other UI state used in association with analysis of query results. |
| <CopyableCode code="opsAnalyticsQuery" /> | `object` | Describes an analytics query that can be run in the Log Analytics page of Google Cloud console.Preview: This is a preview feature and may be subject to change before final release. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the saved query was last updated. |
| <CopyableCode code="visibility" /> | `string` | Required. The visibility status of this query, which determines its ownership. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_saved_queries_list" /> | `SELECT` | <CopyableCode code="billingAccountsId, locationsId" /> | Lists the SavedQueries that were created by the user making the request. |
| <CopyableCode code="folders_locations_saved_queries_list" /> | `SELECT` | <CopyableCode code="foldersId, locationsId" /> | Lists the SavedQueries that were created by the user making the request. |
| <CopyableCode code="organizations_locations_saved_queries_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists the SavedQueries that were created by the user making the request. |
| <CopyableCode code="projects_locations_saved_queries_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the SavedQueries that were created by the user making the request. |
| <CopyableCode code="billing_accounts_locations_saved_queries_create" /> | `INSERT` | <CopyableCode code="billingAccountsId, locationsId" /> | Creates a new SavedQuery for the user making the request. |
| <CopyableCode code="folders_locations_saved_queries_create" /> | `INSERT` | <CopyableCode code="foldersId, locationsId" /> | Creates a new SavedQuery for the user making the request. |
| <CopyableCode code="organizations_locations_saved_queries_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a new SavedQuery for the user making the request. |
| <CopyableCode code="projects_locations_saved_queries_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new SavedQuery for the user making the request. |
| <CopyableCode code="billing_accounts_locations_saved_queries_delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, locationsId, savedQueriesId" /> | Deletes an existing SavedQuery that was created by the user making the request. |
| <CopyableCode code="folders_locations_saved_queries_delete" /> | `DELETE` | <CopyableCode code="foldersId, locationsId, savedQueriesId" /> | Deletes an existing SavedQuery that was created by the user making the request. |
| <CopyableCode code="organizations_locations_saved_queries_delete" /> | `DELETE` | <CopyableCode code="locationsId, organizationsId, savedQueriesId" /> | Deletes an existing SavedQuery that was created by the user making the request. |
| <CopyableCode code="projects_locations_saved_queries_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, savedQueriesId" /> | Deletes an existing SavedQuery that was created by the user making the request. |
| <CopyableCode code="_billing_accounts_locations_saved_queries_list" /> | `EXEC` | <CopyableCode code="billingAccountsId, locationsId" /> | Lists the SavedQueries that were created by the user making the request. |
| <CopyableCode code="_folders_locations_saved_queries_list" /> | `EXEC` | <CopyableCode code="foldersId, locationsId" /> | Lists the SavedQueries that were created by the user making the request. |
| <CopyableCode code="_organizations_locations_saved_queries_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists the SavedQueries that were created by the user making the request. |
| <CopyableCode code="_projects_locations_saved_queries_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists the SavedQueries that were created by the user making the request. |
