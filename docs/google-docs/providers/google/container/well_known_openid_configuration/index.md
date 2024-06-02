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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>well_known_openid_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="container.well_known_openid_configuration" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cacheHeader" /> | `object` | RFC-2616: cache control support |
| <CopyableCode code="claims_supported" /> | `array` | Supported claims. |
| <CopyableCode code="grant_types" /> | `array` | Supported grant types. |
| <CopyableCode code="id_token_signing_alg_values_supported" /> | `array` | supported ID Token signing Algorithms. |
| <CopyableCode code="issuer" /> | `string` | OIDC Issuer. |
| <CopyableCode code="jwks_uri" /> | `string` | JSON Web Key uri. |
| <CopyableCode code="response_types_supported" /> | `array` | Supported response types. |
| <CopyableCode code="subject_types_supported" /> | `array` | Supported subject types. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_locations_clusters_well-known_get_openid-configuration" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, projectsId" /> |
