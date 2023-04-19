---
title: container_registry
hide_title: false
hide_table_of_contents: false
keywords:
  - container_registry
  - container_registry
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_registry</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.container_registry.container_registry</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A globally unique name for the container registry. Must be lowercase and be composed only of numbers, letters and `-`, up to a limit of 63 characters. |
| `region` | `string` | Slug of the region where registry data is stored |
| `storage_usage_bytes` | `integer` | The amount of storage used in the registry in bytes. |
| `storage_usage_bytes_updated_at` | `string` | The time at which the storage usage was updated. Storage usage is calculated asynchronously, and may not immediately reflect pushes to the registry. |
| `subscription` | `object` |  |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the registry was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `registry_get` | `SELECT` |  | To get information about your container registry, send a GET request to `/v2/registry`. |
| `registry_create` | `INSERT` | `data__name, data__subscription_tier_slug` | To create your container registry, send a POST request to `/v2/registry`.<br /><br />The `name` becomes part of the URL for images stored in the registry. For<br />example, if your registry is called `example`, an image in it will have the<br />URL `registry.digitalocean.com/example/image:tag`.<br /> |
| `registry_delete` | `DELETE` |  | To delete your container registry, destroying all container image data stored in it, send a DELETE request to `/v2/registry`. |
| `_registry_get` | `EXEC` |  | To get information about your container registry, send a GET request to `/v2/registry`. |
| `registry_validate_name` | `EXEC` | `data__name` | To validate that a container registry name is available for use, send a POST<br />request to `/v2/registry/validate-name`.<br /><br />If the name is both formatted correctly and available, the response code will<br />be 204 and contain no body. If the name is already in use, the response will<br />be a 409 Conflict.<br /> |
