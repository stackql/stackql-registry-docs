---
title: certificate_map_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_map_entries
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
<tr><td><b>Name</b></td><td><code>certificate_map_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.certificate_map_entries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the Certificate Map Entry. Certificate Map Entry names must be unique globally and match pattern `projects/*/locations/*/certificateMaps/*/certificateMapEntries/*`. |
| `description` | `string` | One or more paragraphs of text description of a certificate map entry. |
| `certificates` | `array` | A set of Certificates defines for the given `hostname`. There can be defined up to fifteen certificates in each Certificate Map Entry. Each certificate must match pattern `projects/*/locations/*/certificates/*`. |
| `createTime` | `string` | Output only. The creation timestamp of a Certificate Map Entry. |
| `hostname` | `string` | A Hostname (FQDN, e.g. `example.com`) or a wildcard hostname expression (`*.example.com`) for a set of hostnames with common suffix. Used as Server Name Indication (SNI) for selecting a proper certificate. |
| `labels` | `object` | Set of labels associated with a Certificate Map Entry. |
| `matcher` | `string` | A predefined matcher for particular cases, other than SNI selection. |
| `state` | `string` | Output only. A serving state of this Certificate Map Entry. |
| `updateTime` | `string` | Output only. The update timestamp of a Certificate Map Entry. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_certificateMaps_certificateMapEntries_get` | `SELECT` | `certificateMapEntriesId, certificateMapsId, locationsId, projectsId` | Gets details of a single CertificateMapEntry. |
| `projects_locations_certificateMaps_certificateMapEntries_list` | `SELECT` | `certificateMapsId, locationsId, projectsId` | Lists CertificateMapEntries in a given project and location. |
| `projects_locations_certificateMaps_certificateMapEntries_create` | `INSERT` | `certificateMapsId, locationsId, projectsId` | Creates a new CertificateMapEntry in a given project and location. |
| `projects_locations_certificateMaps_certificateMapEntries_delete` | `DELETE` | `certificateMapEntriesId, certificateMapsId, locationsId, projectsId` | Deletes a single CertificateMapEntry. |
| `projects_locations_certificateMaps_certificateMapEntries_patch` | `EXEC` | `certificateMapEntriesId, certificateMapsId, locationsId, projectsId` | Updates a CertificateMapEntry. |
