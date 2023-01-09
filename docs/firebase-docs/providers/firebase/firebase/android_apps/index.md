---
title: android_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - android_apps
  - firebase
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>android_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebase.android_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the AndroidApp, in the format: projects/ PROJECT_IDENTIFIER/androidApps/APP_ID * PROJECT_IDENTIFIER: the parent Project's [`ProjectNumber`](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the `ProjectId`. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [`appId`](../projects.androidApps#AndroidApp.FIELDS.app_id)). |
| `state` | `string` | Output only. The lifecycle state of the App. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and it may be sent with update requests to ensure the client has an up-to-date value before proceeding. Learn more about `etag` in Google's [AIP-154 standard](https://google.aip.dev/154#declarative-friendly-resources). This etag is strongly validated. |
| `apiKeyId` | `string` | The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the `AndroidApp`. Be aware that this value is the UID of the API key, _not_ the [`keyString`](https://cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys#Key.FIELDS.key_string) of the API key. The `keyString` is the value that can be found in the App's [configuration artifact](../../rest/v1beta1/projects.androidApps/getConfig). If `api_key_id` is not set in requests to [`androidApps.Create`](../../rest/v1beta1/projects.androidApps/create), then Firebase automatically associates an `api_key_id` with the `AndroidApp`. This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned. In patch requests, `api_key_id` cannot be set to an empty value, and the new UID must have no restrictions or only have restrictions that are valid for the associated `AndroidApp`. We recommend using the [Google Cloud Console](https://console.cloud.google.com/apis/credentials) to manage API keys. |
| `appId` | `string` | Output only. Immutable. The globally unique, Firebase-assigned identifier for the `AndroidApp`. This identifier should be treated as an opaque token, as the data format is not specified. |
| `packageName` | `string` | Immutable. The canonical package name of the Android app as would appear in the Google Play Developer Console. |
| `sha1Hashes` | `array` | The SHA1 certificate hashes for the AndroidApp. |
| `sha256Hashes` | `array` | The SHA256 certificate hashes for the AndroidApp. |
| `displayName` | `string` | The user-assigned display name for the `AndroidApp`. |
| `projectId` | `string` | Output only. Immutable. A user-assigned unique identifier of the parent FirebaseProject for the `AndroidApp`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_androidApps_get` | `SELECT` | `androidAppsId, projectsId` | Gets the specified AndroidApp. |
| `projects_androidApps_list` | `SELECT` | `projectsId` | Lists each AndroidApp associated with the specified FirebaseProject. The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a `pageToken`. |
| `projects_androidApps_create` | `INSERT` | `projectsId` | Requests the creation of a new AndroidApp in the specified FirebaseProject. The result of this call is an `Operation` which can be used to track the provisioning process. The `Operation` is automatically deleted after completion, so there is no need to call `DeleteOperation`. |
| `projects_androidApps_patch` | `EXEC` | `androidAppsId, projectsId` | Updates the attributes of the specified AndroidApp. |
| `projects_androidApps_remove` | `EXEC` | `androidAppsId, projectsId` | Removes the specified AndroidApp from the FirebaseProject. |
| `projects_androidApps_undelete` | `EXEC` | `androidAppsId, projectsId` | Restores the specified AndroidApp to the FirebaseProject. |
