---
title: web_apps__config
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps__config
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_apps__config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebase.web_apps__config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiKey" /> | `string` | The [`keyString`](https://cloud.google.com/api-keys/docs/reference/rest/v2/projects.locations.keys#Key.FIELDS.key_string) of the API key associated with the `WebApp`. Note that this value is _not_ the [`apiKeyId`](../projects.webApps#WebApp.FIELDS.api_key_id) (the UID) of the API key associated with the `WebApp`. |
| <CopyableCode code="appId" /> | `string` | Immutable. The globally unique, Firebase-assigned identifier for the `WebApp`. |
| <CopyableCode code="authDomain" /> | `string` | The domain Firebase Auth configures for OAuth redirects, in the format: PROJECT_ID.firebaseapp.com |
| <CopyableCode code="databaseURL" /> | `string` | The default Firebase Realtime Database URL. |
| <CopyableCode code="locationId" /> | `string` | The ID of the Project's default GCP resource location. The location is one of the available [GCP resource locations](https://firebase.google.com/docs/projects/locations). This field is omitted if the default GCP resource location has not been finalized yet. To set a Project's default GCP resource location, call [`FinalizeDefaultLocation`](../projects.defaultLocation/finalize) after you add Firebase resources to the Project. |
| <CopyableCode code="measurementId" /> | `string` | The unique Google-assigned identifier of the Google Analytics web stream associated with the `WebApp`. Firebase SDKs use this ID to interact with Google Analytics APIs. This field is only present if the `WebApp` is linked to a web stream in a Google Analytics App + Web property. Learn more about this ID and Google Analytics web streams in the [Analytics documentation](https://support.google.com/analytics/answer/9304153). To generate a `measurementId` and link the `WebApp` with a Google Analytics web stream, call [`AddGoogleAnalytics`](../../v1beta1/projects/addGoogleAnalytics). For apps using the Firebase JavaScript SDK v7.20.0 and later, Firebase dynamically fetches the `measurementId` when your app initializes Analytics. Having this ID in your config object is optional, but it does serve as a fallback in the rare case that the dynamic fetch fails. |
| <CopyableCode code="messagingSenderId" /> | `string` | The sender ID for use with Firebase Cloud Messaging. |
| <CopyableCode code="projectId" /> | `string` | Immutable. A user-assigned unique identifier for the `FirebaseProject`. |
| <CopyableCode code="storageBucket" /> | `string` | The default Cloud Storage for Firebase storage bucket name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_webApps_getConfig" /> | `SELECT` | <CopyableCode code="projectsId, webAppsId" /> |
