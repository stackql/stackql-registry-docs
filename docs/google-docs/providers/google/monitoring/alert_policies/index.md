---
title: alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_policies
  - monitoring
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
<tr><td><b>Name</b></td><td><code>alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.monitoring.alert_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there might be more results than were returned, then this field is set to a non-empty value. To see the additional results, use that value as page_token in the next call to this method. |
| `totalSize` | `integer` | The total number of alert policies in all pages. This number is only an estimate, and may change in subsequent pages. https://aip.dev/158 |
| `alertPolicies` | `array` | The returned alert policies. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_alert_policies_list` | `SELECT` | `projectsId` | Lists the existing alerting policies for the workspace. |
| `projects_alert_policies_create` | `INSERT` | `projectsId` | Creates a new alerting policy.Design your application to single-thread API calls that modify the state of alerting policies in a single project. This includes calls to CreateAlertPolicy, DeleteAlertPolicy and UpdateAlertPolicy. |
| `projects_alert_policies_delete` | `DELETE` | `alertPoliciesId, projectsId` | Deletes an alerting policy.Design your application to single-thread API calls that modify the state of alerting policies in a single project. This includes calls to CreateAlertPolicy, DeleteAlertPolicy and UpdateAlertPolicy. |
| `projects_alert_policies_get` | `EXEC` | `alertPoliciesId, projectsId` | Gets a single alerting policy. |
| `projects_alert_policies_patch` | `EXEC` | `alertPoliciesId, projectsId` | Updates an alerting policy. You can either replace the entire policy with a new one or replace only certain fields in the current alerting policy by specifying the fields to be updated via updateMask. Returns the updated alerting policy.Design your application to single-thread API calls that modify the state of alerting policies in a single project. This includes calls to CreateAlertPolicy, DeleteAlertPolicy and UpdateAlertPolicy. |
