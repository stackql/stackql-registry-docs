---
title: well_known_openid_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - well_known_openid_configuration
  - container
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
<tr><td><b>Name</b></td><td><code>well_known_openid_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.container.well_known_openid_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `subject_types_supported` | `array` | Supported subject types. |
| `cacheHeader` | `object` | RFC-2616: cache control support |
| `claims_supported` | `array` | Supported claims. |
| `grant_types` | `array` | Supported grant types. |
| `id_token_signing_alg_values_supported` | `array` | supported ID Token signing Algorithms. |
| `issuer` | `string` | OIDC Issuer. |
| `jwks_uri` | `string` | JSON Web Key uri. |
| `response_types_supported` | `array` | Supported response types. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_clusters_well-known_get_openid-configuration` | `SELECT` | `clustersId, locationsId, projectsId` |
