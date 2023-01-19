---
title: activities
hide_title: false
hide_table_of_contents: false
keywords:
  - activities
  - admin
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>activities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.admin.activities</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `object` | Unique identifier for each activity record. |
| `ipAddress` | `string` | IP address of the user doing the action. This is the Internet Protocol (IP) address of the user when logging into Google Workspace, which may or may not reflect the user's physical location. For example, the IP address can be the user's proxy server's address or a virtual private network (VPN) address. The API supports IPv4 and IPv6. |
| `kind` | `string` | The type of API resource. For an activity report, the value is `audit#activity`. |
| `ownerDomain` | `string` | This is the domain that is affected by the report's event. For example domain of Admin console or the Drive application's document owner. |
| `actor` | `object` | User doing the action. |
| `etag` | `string` | ETag of the entry. |
| `events` | `array` | Activity events in the report. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `reports_activities_list` | `SELECT` | `applicationName, userKey` | Retrieves a list of activities for a specific customer's account and application such as the Admin console application or the Google Drive application. For more information, see the guides for administrator and Google Drive activity reports. For more information about the activity report's parameters, see the activity parameters reference guides.  |
| `reports_activities_watch` | `EXEC` | `applicationName, userKey` | Start receiving notifications for account activities. For more information, see Receiving Push Notifications. |
