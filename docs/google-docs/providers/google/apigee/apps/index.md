---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - apigee
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the developer app. |
| `attributes` | `array` | List of attributes for the developer app. |
| `callbackUrl` | `string` | Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to developer apps. |
| `scopes` | `array` | Scopes to apply to the developer app. The specified scopes must already exist for the API product that you associate with the developer app. |
| `developerId` | `string` | ID of the developer. |
| `keyExpiresIn` | `string` | Expiration time, in milliseconds, for the consumer key that is generated for the developer app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set. |
| `credentials` | `array` | Output only. Set of credentials for the developer app consisting of the consumer key/secret pairs associated with the API products. |
| `apiProducts` | `array` | List of API products associated with the developer app. |
| `appId` | `string` | ID of the developer app. |
| `appFamily` | `string` | Developer app family. |
| `status` | `string` | Status of the credential. Valid values include `approved` or `revoked`. |
| `lastModifiedAt` | `string` | Output only. Time the developer app was modified in milliseconds since epoch. |
| `createdAt` | `string` | Output only. Time the developer app was created in milliseconds since epoch. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_apps_get` | `SELECT` | `appsId, organizationsId` | Gets the app profile for the specified app ID. |
| `organizations_apps_list` | `SELECT` | `organizationsId` | Lists IDs of apps within an organization that have the specified app status (approved or revoked) or are of the specified app type (developer or company). |
| `organizations_developers_apps_get` | `SELECT` | `appsId, developersId, organizationsId` | Returns the details for a developer app. |
| `organizations_developers_apps_list` | `SELECT` | `developersId, organizationsId` | Lists all apps created by a developer in an Apigee organization. Optionally, you can request an expanded view of the developer apps. A maximum of 100 developer apps are returned per API call. You can paginate the list of deveoper apps returned using the `startKey` and `count` query parameters. |
| `organizations_developers_apps_create` | `INSERT` | `developersId, organizationsId` | Creates an app associated with a developer. This API associates the developer app with the specified API product and auto-generates an API key for the app to use in calls to API proxies inside that API product. The `name` is the unique ID of the app that you can use in API calls. The `DisplayName` (set as an attribute) appears in the UI. If you don't set the `DisplayName` attribute, the `name` appears in the UI. |
| `organizations_developers_apps_delete` | `DELETE` | `appsId, developersId, organizationsId` | Deletes a developer app. **Note**: The delete operation is asynchronous. The developer app is deleted immediately, but its associated resources, such as app keys or access tokens, may take anywhere from a few seconds to a few minutes to be deleted. |
| `organizations_developers_apps_attributes` | `EXEC` | `appsId, developersId, organizationsId` | Updates attributes for a developer app. This API replaces the current attributes with those specified in the request. |
| `organizations_developers_apps_generateKeyPairOrUpdateDeveloperAppStatus` | `EXEC` | `appsId, developersId, organizationsId` | Manages access to a developer app by enabling you to: * Approve or revoke a developer app * Generate a new consumer key and secret for a developer app To approve or revoke a developer app, set the `action` query parameter to `approved` or `revoked`, respectively, and the `Content-Type` header to `application/octet-stream`. If a developer app is revoked, none of its API keys are valid for API calls even though the keys are still `approved`. If successful, the API call returns the following HTTP status code: `204 No Content` To generate a new consumer key and secret for a developer app, pass the new key/secret details. Rather than replace an existing key, this API generates a new key. In this case, multiple key pairs may be associated with a single developer app. Each key pair has an independent status (`approved` or `revoked`) and expiration time. Any approved, non-expired key can be used in an API call. For example, if you're using API key rotation, you can generate new keys with expiration times that overlap keys that are going to expire. You might also generate a new consumer key/secret if the security of the original key/secret is compromised. The `keyExpiresIn` property defines the expiration time for the API key in milliseconds. If you don't set this property or set it to `-1`, the API key never expires. **Notes**: * When generating a new key/secret, this API replaces the existing attributes, notes, and callback URLs with those specified in the request. Include or exclude any existing information that you want to retain or delete, respectively. * To migrate existing consumer keys and secrets to hybrid from another system, see the CreateDeveloperAppKey API. |
| `organizations_developers_apps_update` | `EXEC` | `appsId, developersId, organizationsId` | Updates the details for a developer app. In addition, you can add an API product to a developer app and automatically generate an API key for the app to use when calling APIs in the API product. If you want to use an existing API key for the API product, add the API product to the API key using the UpdateDeveloperAppKey API. Using this API, you cannot update the following: * App name as it is the primary key used to identify the app and cannot be changed. * Scopes associated with the app. Instead, use the ReplaceDeveloperAppKey API. This API replaces the existing attributes with those specified in the request. Include or exclude any existing attributes that you want to retain or delete, respectively. |
