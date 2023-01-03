---
title: keyvaluemaps
hide_title: false
hide_table_of_contents: false
keywords:
  - keyvaluemaps
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
<tr><td><b>Name</b></td><td><code>keyvaluemaps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.keyvaluemaps</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_apis_keyvaluemaps_create` | `INSERT` | `apisId, organizationsId` | Creates a key value map in an API proxy. |
| `organizations_environments_keyvaluemaps_create` | `INSERT` | `environmentsId, organizationsId` | Creates a key value map in an environment. |
| `organizations_keyvaluemaps_create` | `INSERT` | `organizationsId` | Creates a key value map in an organization. |
| `organizations_apis_keyvaluemaps_delete` | `DELETE` | `apisId, keyvaluemapsId, organizationsId` | Deletes a key value map from an API proxy. |
| `organizations_environments_keyvaluemaps_delete` | `DELETE` | `environmentsId, keyvaluemapsId, organizationsId` | Deletes a key value map from an environment. |
| `organizations_keyvaluemaps_delete` | `DELETE` | `keyvaluemapsId, organizationsId` | Deletes a key value map from an organization. |
