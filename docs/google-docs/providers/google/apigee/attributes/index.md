---
title: attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - attributes
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
<tr><td><b>Name</b></td><td><code>attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.attributes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | API key of the attribute. |
| `value` | `string` | Value of the attribute. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_apiproducts_attributes_get` | `SELECT` | `apiproductsId, attributesId, organizationsId` | Gets the value of an API product attribute. |
| `organizations_apiproducts_attributes_list` | `SELECT` | `apiproductsId, organizationsId` | Lists all API product attributes. |
| `organizations_developers_apps_attributes_get` | `SELECT` | `appsId, attributesId, developersId, organizationsId` | Returns a developer app attribute. |
| `organizations_developers_apps_attributes_list` | `SELECT` | `appsId, developersId, organizationsId` | Returns a list of all developer app attributes. |
| `organizations_developers_attributes_get` | `SELECT` | `attributesId, developersId, organizationsId` | Returns the value of the specified developer attribute. |
| `organizations_developers_attributes_list` | `SELECT` | `developersId, organizationsId` | Returns a list of all developer attributes. |
| `organizations_apiproducts_attributes_delete` | `DELETE` | `apiproductsId, attributesId, organizationsId` | Deletes an API product attribute. |
| `organizations_developers_apps_attributes_delete` | `DELETE` | `appsId, attributesId, developersId, organizationsId` | Deletes a developer app attribute. |
| `organizations_developers_attributes_delete` | `DELETE` | `attributesId, developersId, organizationsId` | Deletes a developer attribute. |
| `organizations_apiproducts_attributes_updateApiProductAttribute` | `EXEC` | `apiproductsId, attributesId, organizationsId` | Updates the value of an API product attribute. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with entities also get cached for at least 180 seconds after entity is accessed during runtime. In this case, the `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
| `organizations_developers_apps_attributes_updateDeveloperAppAttribute` | `EXEC` | `appsId, attributesId, developersId, organizationsId` | Updates a developer app attribute. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (current default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
| `organizations_developers_attributes_updateDeveloperAttribute` | `EXEC` | `attributesId, developersId, organizationsId` | Updates a developer attribute. **Note**: OAuth access tokens and Key Management Service (KMS) entities (apps, developers, and API products) are cached for 180 seconds (default). Any custom attributes associated with these entities are cached for at least 180 seconds after the entity is accessed at runtime. Therefore, an `ExpiresIn` element on the OAuthV2 policy won't be able to expire an access token in less than 180 seconds. |
