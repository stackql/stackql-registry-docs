---
title: ios_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - ios_apps
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
<tr><td><b>Name</b></td><td><code>ios_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebase.ios_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the IosApp, in the format: projects/PROJECT_IDENTIFIER /iosApps/APP_ID * PROJECT_IDENTIFIER: the parent Project's [`ProjectNumber`](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the `ProjectId`. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [`appId`](../projects.iosApps#IosApp.FIELDS.app_id)). |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and it may be sent with update requests to ensure the client has an up-to-date value before proceeding. Learn more about `etag` in Google's [AIP-154 standard](https://google.aip.dev/154#declarative-friendly-resources). This etag is strongly validated. |
| `appId` | `string` | Output only. Immutable. The globally unique, Firebase-assigned identifier for the `IosApp`. This identifier should be treated as an opaque token, as the data format is not specified. |
| `bundleId` | `string` | Immutable. The canonical bundle ID of the iOS app as it would appear in the iOS AppStore. |
| `displayName` | `string` | The user-assigned display name for the `IosApp`. |
| `state` | `string` | Output only. The lifecycle state of the App. |
| `apiKeyId` | `string` | The globally unique, Google-assigned identifier (UID) for the Firebase API key associated with the `IosApp`. Be aware that this value is the UID of the API key, _not_ the [`keyString`](https://cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys#Key.FIELDS.key_string) of the API key. The `keyString` is the value that can be found in the App's [configuration artifact](../../rest/v1beta1/projects.iosApps/getConfig). If `api_key_id` is not set in requests to [`iosApps.Create`](../../rest/v1beta1/projects.iosApps/create), then Firebase automatically associates an `api_key_id` with the `IosApp`. This auto-associated key may be an existing valid key or, if no valid key exists, a new one will be provisioned. In patch requests, `api_key_id` cannot be set to an empty value, and the new UID must have no restrictions or only have restrictions that are valid for the associated `IosApp`. We recommend using the [Google Cloud Console](https://console.cloud.google.com/apis/credentials) to manage API keys. |
| `teamId` | `string` | The Apple Developer Team ID associated with the App in the App Store. |
| `projectId` | `string` | Output only. Immutable. A user-assigned unique identifier of the parent FirebaseProject for the `IosApp`. |
| `appStoreId` | `string` | The automatically generated Apple ID assigned to the iOS app by Apple in the iOS App Store. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_iosApps_get` | `SELECT` | `iosAppsId, projectsId` | Gets the specified IosApp. |
| `projects_iosApps_list` | `SELECT` | `projectsId` | Lists each IosApp associated with the specified FirebaseProject. The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a `pageToken`. |
| `projects_iosApps_create` | `INSERT` | `projectsId` | Requests the creation of a new IosApp in the specified FirebaseProject. The result of this call is an `Operation` which can be used to track the provisioning process. The `Operation` is automatically deleted after completion, so there is no need to call `DeleteOperation`. |
| `projects_iosApps_patch` | `EXEC` | `iosAppsId, projectsId` | Updates the attributes of the specified IosApp. |
| `projects_iosApps_remove` | `EXEC` | `iosAppsId, projectsId` | Removes the specified IosApp from the FirebaseProject. |
| `projects_iosApps_undelete` | `EXEC` | `iosAppsId, projectsId` | Restores the specified IosApp to the FirebaseProject. |
