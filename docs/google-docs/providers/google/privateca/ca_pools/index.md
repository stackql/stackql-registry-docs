---
title: ca_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - ca_pools
  - privateca
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
<tr><td><b>Name</b></td><td><code>ca_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.ca_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for this CaPool in the format `projects/*/locations/*/caPools/*`. |
| `labels` | `object` | Optional. Labels with user-defined metadata. |
| `publishingOptions` | `object` | Options relating to the publication of each CertificateAuthority's CA certificate and CRLs and their inclusion as extensions in issued Certificates. The options set here apply to certificates issued by any CertificateAuthority in the CaPool. |
| `tier` | `string` | Required. Immutable. The Tier of this CaPool. |
| `issuancePolicy` | `object` | Defines controls over all certificate issuance within a CaPool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_caPools_get` | `SELECT` | `caPoolsId, locationsId, projectsId` | Returns a CaPool. |
| `projects_locations_caPools_list` | `SELECT` | `locationsId, projectsId` | Lists CaPools. |
| `projects_locations_caPools_create` | `INSERT` | `locationsId, projectsId` | Create a CaPool. |
| `projects_locations_caPools_delete` | `DELETE` | `caPoolsId, locationsId, projectsId` | Delete a CaPool. |
| `projects_locations_caPools_patch` | `EXEC` | `caPoolsId, locationsId, projectsId` | Update a CaPool. |
