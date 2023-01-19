---
title: enterprises
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprises
  - androidenterprise
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enterprises</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.enterprises</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID for the enterprise. |
| `name` | `string` | The name of the enterprise, for example, "Example, Inc". |
| `googleAuthenticationSettings` | `object` | Contains settings for Google-provided user authentication. |
| `primaryDomain` | `string` | The enterprise's primary domain, such as "example.com". |
| `administrator` | `array` | Admins of the enterprise. This is only supported for enterprises created via the EMM-initiated flow. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `enterpriseId` | Retrieves the name and domain of an enterprise. |
| `list` | `SELECT` | `domain` | Looks up an enterprise by domain name. This is only supported for enterprises created via the Google-initiated creation flow. Lookup of the id is not needed for enterprises created via the EMM-initiated flow since the EMM learns the enterprise ID in the callback specified in the Enterprises.generateSignupUrl call. |
| `acknowledgeNotificationSet` | `EXEC` |  | Acknowledges notifications that were received from Enterprises.PullNotificationSet to prevent subsequent calls from returning the same notifications. |
| `completeSignup` | `EXEC` |  | Completes the signup flow, by specifying the Completion token and Enterprise token. This request must not be called multiple times for a given Enterprise Token. |
| `enroll` | `EXEC` | `token` | Enrolls an enterprise with the calling EMM. |
| `generateSignupUrl` | `EXEC` |  | Generates a sign-up URL. |
| `pullNotificationSet` | `EXEC` |  | Pulls and returns a notification set for the enterprises associated with the service account authenticated for the request. The notification set may be empty if no notification are pending. A notification set returned needs to be acknowledged within 20 seconds by calling Enterprises.AcknowledgeNotificationSet, unless the notification set is empty. Notifications that are not acknowledged within the 20 seconds will eventually be included again in the response to another PullNotificationSet request, and those that are never acknowledged will ultimately be deleted according to the Google Cloud Platform Pub/Sub system policy. Multiple requests might be performed concurrently to retrieve notifications, in which case the pending notifications (if any) will be split among each caller, if any are pending. If no notifications are present, an empty notification list is returned. Subsequent requests may return more notifications once they become available. |
| `sendTestPushNotification` | `EXEC` | `enterpriseId` | Sends a test notification to validate the EMM integration with the Google Cloud Pub/Sub service for this enterprise. |
| `setAccount` | `EXEC` | `enterpriseId` | Sets the account that will be used to authenticate to the API as the enterprise. |
| `setStoreLayout` | `EXEC` | `enterpriseId` | Sets the store layout for the enterprise. By default, storeLayoutType is set to "basic" and the basic store layout is enabled. The basic layout only contains apps approved by the admin, and that have been added to the available product set for a user (using the setAvailableProductSet call). Apps on the page are sorted in order of their product ID value. If you create a custom store layout (by setting storeLayoutType = "custom" and setting a homepage), the basic store layout is disabled. |
| `unenroll` | `EXEC` | `enterpriseId` | Unenrolls an enterprise from the calling EMM. |
