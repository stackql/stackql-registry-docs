---
title: key_rings
hide_title: false
hide_table_of_contents: false
keywords:
  - key_rings
  - cloudkms
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
<tr><td><b>Name</b></td><td><code>key_rings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.key_rings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for the KeyRing in the format `projects/*/locations/*/keyRings/*`. |
| `createTime` | `string` | Output only. The time at which this KeyRing was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_keyRings_get` | `SELECT` | `keyRingsId, locationsId, projectsId` | Returns metadata for a given KeyRing. |
| `projects_locations_keyRings_list` | `SELECT` | `locationsId, projectsId` | Lists KeyRings. |
| `projects_locations_keyRings_create` | `INSERT` | `locationsId, projectsId` | Create a new KeyRing in a given Project and Location. |
