---
title: certificate_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_maps
  - certificatemanager
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
<tr><td><b>Name</b></td><td><code>certificate_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.certificate_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the Certificate Map. Certificate Map names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*`. |
| `description` | `string` | One or more paragraphs of text description of a certificate map. |
| `createTime` | `string` | Output only. The creation timestamp of a Certificate Map. |
| `gclbTargets` | `array` | Output only. A list of GCLB targets which use this Certificate Map. |
| `labels` | `object` | Set of labels associated with a Certificate Map. |
| `updateTime` | `string` | Output only. The update timestamp of a Certificate Map. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_certificateMaps_get` | `SELECT` | `certificateMapsId, locationsId, projectsId` | Gets details of a single CertificateMap. |
| `projects_locations_certificateMaps_list` | `SELECT` | `locationsId, projectsId` | Lists CertificateMaps in a given project and location. |
| `projects_locations_certificateMaps_create` | `INSERT` | `locationsId, projectsId` | Creates a new CertificateMap in a given project and location. |
| `projects_locations_certificateMaps_delete` | `DELETE` | `certificateMapsId, locationsId, projectsId` | Deletes a single CertificateMap. A Certificate Map can't be deleted if it contains Certificate Map Entries. Remove all the entries from the map before calling this method. |
| `projects_locations_certificateMaps_patch` | `EXEC` | `certificateMapsId, locationsId, projectsId` | Updates a CertificateMap. |
