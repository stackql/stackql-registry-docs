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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Required if the policy exists. The resource name for this policy. The format is: projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID] [ALERT_POLICY_ID] is assigned by Cloud Monitoring when the policy is created. When calling the alertPolicies.create method, do not include the name field in the alerting policy passed as part of the request. |
| `documentation` | `object` | A content string and a MIME type that describes the content string's format. |
| `mutationRecord` | `object` | Describes a change made to a configuration. |
| `combiner` | `string` | How to combine the results of multiple conditions to determine if an incident should be opened. If condition_time_series_query_language is present, this must be COMBINE_UNSPECIFIED. |
| `conditions` | `array` | A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions. If condition_time_series_query_language is present, it must be the only condition. |
| `notificationChannels` | `array` | Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of the NotificationChannel objects that are returned from the ListNotificationChannels method. The format of the entries in this field is: projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]  |
| `enabled` | `boolean` | Whether or not the policy is enabled. On write, the default interpretation if unset is that the policy is enabled. On read, clients should not make any assumption about the state if it has not been populated. The field should always be populated on List and Get operations, unless a field projection has been specified that strips it out. |
| `creationRecord` | `object` | Describes a change made to a configuration. |
| `displayName` | `string` | A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion, don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode characters. |
| `validity` | `object` | The Status type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by gRPC (https://github.com/grpc). Each Status message contains three pieces of data: error code, error message, and error details.You can find out more about this error model and how to work with it in the API Design Guide (https://cloud.google.com/apis/design/errors). |
| `userLabels` | `object` | User-supplied key/value data to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter. |
| `alertStrategy` | `object` | Control over how the notification channels in notification_channels are notified when this alert fires. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_alertPolicies_get` | `SELECT` | `alertPoliciesId, projectsId` | Gets a single alerting policy. |
| `projects_alertPolicies_list` | `SELECT` | `projectsId` | Lists the existing alerting policies for the workspace. |
| `projects_alertPolicies_create` | `INSERT` | `projectsId` | Creates a new alerting policy. |
| `projects_alertPolicies_delete` | `DELETE` | `alertPoliciesId, projectsId` | Deletes an alerting policy. |
| `projects_alertPolicies_patch` | `EXEC` | `alertPoliciesId, projectsId` | Updates an alerting policy. You can either replace the entire policy with a new one or replace only certain fields in the current alerting policy by specifying the fields to be updated via updateMask. Returns the updated alerting policy. |
