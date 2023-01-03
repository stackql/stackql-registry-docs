---
title: developers
hide_title: false
hide_table_of_contents: false
keywords:
  - developers
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
<tr><td><b>Name</b></td><td><code>developers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.developers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `appFamily` | `string` | Developer app family. |
| `organizationName` | `string` | Output only. Name of the Apigee organization in which the developer resides. |
| `firstName` | `string` | Required. First name of the developer. |
| `lastName` | `string` | Required. Last name of the developer. |
| `status` | `string` | Output only. Status of the developer. Valid values are `active` and `inactive`. |
| `userName` | `string` | Required. User name of the developer. Not used by Apigee hybrid. |
| `accessType` | `string` | Access type. |
| `createdAt` | `string` | Output only. Time at which the developer was created in milliseconds since epoch. |
| `email` | `string` | Required. Email address of the developer. This value is used to uniquely identify the developer in Apigee hybrid. Note that the email address has to be in lowercase only. |
| `lastModifiedAt` | `string` | Output only. Time at which the developer was last modified in milliseconds since epoch. |
| `attributes` | `array` | Optional. Developer attributes (name/value pairs). The custom attribute limit is 18. |
| `apps` | `array` | List of apps associated with the developer. |
| `companies` | `array` | List of companies associated with the developer. |
| `developerId` | `string` | ID of the developer. **Note**: IDs are generated internally by Apigee and are not guaranteed to stay the same over time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_developers_get` | `SELECT` | `developersId, organizationsId` | Returns the developer details, including the developer's name, email address, apps, and other information. **Note**: The response includes only the first 100 developer apps. |
| `organizations_developers_list` | `SELECT` | `organizationsId` | Lists all developers in an organization by email address. By default, the response does not include company developers. Set the `includeCompany` query parameter to `true` to include company developers. **Note**: A maximum of 1000 developers are returned in the response. You paginate the list of developers returned using the `startKey` and `count` query parameters. |
| `organizations_developers_create` | `INSERT` | `organizationsId` | Creates a developer. Once created, the developer can register an app and obtain an API key. At creation time, a developer is set as `active`. To change the developer status, use the SetDeveloperStatus API. |
| `organizations_developers_delete` | `DELETE` | `developersId, organizationsId` | Deletes a developer. All apps and API keys associated with the developer are also removed. **Warning**: This API will permanently delete the developer and related artifacts. To avoid permanently deleting developers and their artifacts, set the developer status to `inactive` using the SetDeveloperStatus API. **Note**: The delete operation is asynchronous. The developer app is deleted immediately, but its associated resources, such as apps and API keys, may take anywhere from a few seconds to a few minutes to be deleted. |
| `organizations_developers_attributes` | `EXEC` | `developersId, organizationsId` | Updates developer attributes. This API replaces the existing attributes with those specified in the request. Add new attributes, and include or exclude any existing attributes that you want to retain or remove, respectively. The custom attribute limit is 18. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
| `organizations_developers_setDeveloperStatus` | `EXEC` | `developersId, organizationsId` | Sets the status of a developer. A developer is `active` by default. If you set a developer's status to `inactive`, the API keys assigned to the developer apps are no longer valid even though the API keys are set to `approved`. Inactive developers can still sign in to the developer portal and create apps; however, any new API keys generated during app creation won't work. To set the status of a developer, set the `action` query parameter to `active` or `inactive`, and the `Content-Type` header to `application/octet-stream`. If successful, the API call returns the following HTTP status code: `204 No Content` |
| `organizations_developers_update` | `EXEC` | `developersId, organizationsId` | Updates a developer. This API replaces the existing developer details with those specified in the request. Include or exclude any existing details that you want to retain or delete, respectively. The custom attribute limit is 18. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
| `organizations_developers_updateMonetizationConfig` | `EXEC` | `developersId, organizationsId` | Updates the monetization configuration for the developer. |
