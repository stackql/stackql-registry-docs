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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `tier` | `string` | Required. Immutable. The Tier of this CaPool. |
| `issuancePolicy` | `object` | Defines controls over all certificate issuance within a CaPool. |
| `labels` | `object` | Optional. Labels with user-defined metadata. |
| `publishingOptions` | `object` | Options relating to the publication of each CertificateAuthority's CA certificate and CRLs and their inclusion as extensions in issued Certificates. The options set here apply to certificates issued by any CertificateAuthority in the CaPool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `caPoolsId, locationsId, projectsId` | Returns a CaPool. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists CaPools. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a CaPool. |
| `delete` | `DELETE` | `caPoolsId, locationsId, projectsId` | Delete a CaPool. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists CaPools. |
| `patch` | `EXEC` | `caPoolsId, locationsId, projectsId` | Update a CaPool. |
