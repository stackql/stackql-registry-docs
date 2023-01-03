---
title: references
hide_title: false
hide_table_of_contents: false
keywords:
  - references
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
<tr><td><b>Name</b></td><td><code>references</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.references</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource id of this reference. Values must match the regular expression [\w\s\-.]+. |
| `description` | `string` | Optional. A human-readable description of this reference. |
| `refers` | `string` | Required. The id of the resource to which this reference refers. Must be the id of a resource that exists in the parent environment and is of the given resource_type. |
| `resourceType` | `string` | The type of resource referred to by this reference. Valid values are 'KeyStore' or 'TrustStore'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_references_get` | `SELECT` | `environmentsId, organizationsId, referencesId` | Gets a Reference resource. |
| `organizations_environments_references_create` | `INSERT` | `environmentsId, organizationsId` | Creates a Reference in the specified environment. |
| `organizations_environments_references_delete` | `DELETE` | `environmentsId, organizationsId, referencesId` | Deletes a Reference from an environment. Returns the deleted Reference resource. |
| `organizations_environments_references_update` | `EXEC` | `environmentsId, organizationsId, referencesId` | Updates an existing Reference. Note that this operation has PUT semantics; it will replace the entirety of the existing Reference with the resource in the request body. |
