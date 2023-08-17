---
title: appgroups
hide_title: false
hide_table_of_contents: false
keywords:
  - appgroups
  - apigee
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
<tr><td><b>Name</b></td><td><code>appgroups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.appgroups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Name of the AppGroup. Characters you can use in the name are restricted to: A-Z0-9._\-$ %. |
| `attributes` | `array` | A list of attributes |
| `createdAt` | `string` | Output only. Created time as milliseconds since epoch. |
| `channelId` | `string` | channel identifier identifies the owner maintaing this grouping. |
| `lastModifiedAt` | `string` | Output only. Modified time as milliseconds since epoch. |
| `organization` | `string` | Immutable. the org the app group is created |
| `channelUri` | `string` | A reference to the associated storefront/marketplace. |
| `displayName` | `string` | app group name displayed in the UI |
| `status` | `string` | Valid values are `active` or `inactive`. Note that the status of the AppGroup should be updated via UpdateAppGroupRequest by setting the action as `active` or `inactive`. |
| `appGroupId` | `string` | Output only. Internal identifier that cannot be edited |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_appgroups_get` | `SELECT` | `appgroupsId, organizationsId` | Returns the AppGroup details for the provided AppGroup name in the request URI. |
| `organizations_appgroups_list` | `SELECT` | `organizationsId` | Lists all AppGroups in an organization. A maximum of 1000 AppGroups are returned in the response if PageSize is not specified, or if the PageSize is greater than 1000. |
| `organizations_appgroups_create` | `INSERT` | `organizationsId` | Creates an AppGroup. Once created, user can register apps under the AppGroup to obtain secret key and password. At creation time, the AppGroup's state is set as `active`. The attribute `Attribute` with key `attribute_name` as `__apigee_reserved__developer_details` can be used to store developers and their roles. The JSON format expected is: [ &#123; "developer_id":"", "roles":[ "" ] &#125; ] and is dealt in base64encoded format. Etag will be available in attribute `Attribute` with key `attribute_name` as `__apigee_reserved__developer_details_etag` for that AppGroup. |
| `organizations_appgroups_delete` | `DELETE` | `appgroupsId, organizationsId` | Deletes an AppGroup. All app and API keys associations with the AppGroup are also removed. **Warning**: This API will permanently delete the AppGroup and related artifacts. **Note**: The delete operation is asynchronous. The AppGroup app is deleted immediately, but its associated resources, such as apps and API keys, may take anywhere from a few seconds to a few minutes to be deleted. |
| `_organizations_appgroups_list` | `EXEC` | `organizationsId` | Lists all AppGroups in an organization. A maximum of 1000 AppGroups are returned in the response if PageSize is not specified, or if the PageSize is greater than 1000. |
| `organizations_appgroups_update` | `EXEC` | `appgroupsId, organizationsId` | Updates an appGroup. This API replaces the existing appGroup details with those specified in the request. Include or exclude any existing details that you want to retain or delete, respectively. Note that the state of the AppGroup should be updated using `action`, and not via AppGroup. The custom attribute limit is 1000, and is how `__apigee_reserved__developer_details` can be updated. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
