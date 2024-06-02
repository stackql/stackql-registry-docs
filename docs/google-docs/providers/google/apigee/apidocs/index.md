---
title: apidocs
hide_title: false
hide_table_of_contents: false
keywords:
  - apidocs
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apidocs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apigee.apidocs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. The ID of the catalog item. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the catalog item. Max length is 10,000 characters. |
| <CopyableCode code="anonAllowed" /> | `boolean` | Optional. Boolean flag that manages user access to the catalog item. When true, the catalog item has public visibility and can be viewed anonymously; otherwise, only registered users may view it. Note: when the parent portal is enrolled in the [audience management feature](https://cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#enrolling_in_the_beta_release_of_the_audience_management_feature), and this flag is set to false, visibility is set to an indeterminate state and must be explicitly specified in the management UI (see [Manage the visibility of an API in your portal](https://cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#visibility)). Additionally, when enrolled in the audience management feature, updates to this flag will be ignored as visibility permissions must be updated in the management UI. |
| <CopyableCode code="apiProductName" /> | `string` | Required. Immutable. The `name` field of the associated [API product](/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts). A portal may have only one catalog item associated with a given API product. |
| <CopyableCode code="categoryIds" /> | `array` | Optional. The IDs of the API categories to which this catalog item belongs. |
| <CopyableCode code="edgeAPIProductName" /> | `string` | Optional. Immutable. DEPRECATED: use the `apiProductName` field instead |
| <CopyableCode code="graphqlEndpointUrl" /> | `string` | Optional. DEPRECATED: manage documentation through the `getDocumentation` and `updateDocumentation` methods |
| <CopyableCode code="graphqlSchema" /> | `string` | Optional. DEPRECATED: manage documentation through the `getDocumentation` and `updateDocumentation` methods |
| <CopyableCode code="graphqlSchemaDisplayName" /> | `string` | Optional. DEPRECATED: manage documentation through the `getDocumentation` and `updateDocumentation` methods |
| <CopyableCode code="imageUrl" /> | `string` | Optional. Location of the image used for the catalog item in the catalog. This can be either an image with an external URL or a file path for [image files stored in the portal](/apigee/docs/api-platform/publish/portal/portal-files"), for example, `/files/book-tree.jpg`. When specifying the URL of an external image, the image won't be uploaded to your assets; additionally, loading the image in the integrated portal will be subject to its availability, which may be blocked or restricted by [content security policies](/apigee/docs/api-platform/publish/portal/csp). Max length of file path is 2,083 characters. |
| <CopyableCode code="modified" /> | `string` | Output only. Time the catalog item was last modified in milliseconds since epoch. |
| <CopyableCode code="published" /> | `boolean` | Optional. Denotes whether the catalog item is published to the portal or is in a draft state. When the parent portal is enrolled in the [audience management feature](https://cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#enrolling_in_the_beta_release_of_the_audience_management_feature), the visibility can be set to public on creation by setting the anonAllowed flag to true or further managed in the management UI (see [Manage the visibility of an API in your portal](https://cloud.google.com/apigee/docs/api-platform/publish/portal/publish-apis#visibility)) before it can be visible to any users. If not enrolled in the audience management feature, the visibility is managed by the `anonAllowed` flag. |
| <CopyableCode code="requireCallbackUrl" /> | `boolean` | Optional. Whether a callback URL is required when this catalog item's API product is enabled in a developer app. When true, a portal user will be required to input a URL when managing the app (this is typically used for the app's OAuth flow). |
| <CopyableCode code="siteId" /> | `string` | Output only. The ID of the parent portal. |
| <CopyableCode code="specId" /> | `string` | Optional. DEPRECATED: DO NOT USE |
| <CopyableCode code="title" /> | `string` | Required. The user-facing name of the catalog item. `title` must be a non-empty string with a max length of 255 characters. |
| <CopyableCode code="visibility" /> | `boolean` | Optional. DEPRECATED: use the `published` field instead |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_sites_apidocs_get" /> | `SELECT` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Gets a catalog item. |
| <CopyableCode code="organizations_sites_apidocs_list" /> | `SELECT` | <CopyableCode code="organizationsId, sitesId" /> | Returns the catalog items associated with a portal. |
| <CopyableCode code="organizations_sites_apidocs_create" /> | `INSERT` | <CopyableCode code="organizationsId, sitesId" /> | Creates a new catalog item. |
| <CopyableCode code="organizations_sites_apidocs_delete" /> | `DELETE` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Deletes a catalog item. |
| <CopyableCode code="_organizations_sites_apidocs_list" /> | `EXEC` | <CopyableCode code="organizationsId, sitesId" /> | Returns the catalog items associated with a portal. |
| <CopyableCode code="organizations_sites_apidocs_update" /> | `EXEC` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Updates a catalog item. |
