---
title: android
hide_title: false
hide_table_of_contents: false
keywords:
  - android
  - chromemanagement
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
<tr><td><b>Name</b></td><td><code>android</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.chromemanagement.android</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Format: name=customers/&#123;customer_id&#125;/apps/&#123;chrome\|android\|web&#125;/&#123;app_id&#125;@&#123;version&#125; |
| `description` | `string` | Output only. App's description. |
| `privacyPolicyUri` | `string` | Output only. The URI pointing to the privacy policy of the app, if it was provided by the developer. Version-specific field that will only be set when the requested app version is found. |
| `reviewNumber` | `string` | Output only. Number of reviews received. Chrome Web Store review information will always be for the latest version of an app. |
| `homepageUri` | `string` | Output only. Home page or Website uri. |
| `androidAppInfo` | `object` | Android app information. |
| `type` | `string` | Output only. App type. |
| `chromeAppInfo` | `object` | Chrome Web Store app information. |
| `revisionId` | `string` | Output only. App version. A new revision is committed whenever a new version of the app is published. |
| `iconUri` | `string` | Output only. A link to an image that can be used as an icon for the product. |
| `serviceError` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `reviewRating` | `number` | Output only. The rating of the app (on 5 stars). Chrome Web Store review information will always be for the latest version of an app. |
| `latestPublishTime` | `string` | Output only. Latest published time. |
| `publisher` | `string` | Output only. The publisher of the item. |
| `appId` | `string` | Output only. Unique store identifier for the item. Examples: "gmbmikajjgmnabiglmofipeabaddhgne" for the Save to Google Drive Chrome extension, "com.google.android.apps.docs" for the Google Drive Android app. |
| `firstPublishTime` | `string` | Output only. First published time. |
| `displayName` | `string` | Output only. App's display name. |
| `isPaidApp` | `boolean` | Output only. Indicates if the app has to be paid for OR has paid content. |
| `detailUri` | `string` | Output only. The uri for the detail page of the item. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `customers_apps_android_get` | `SELECT` | `androidId, customersId` |
