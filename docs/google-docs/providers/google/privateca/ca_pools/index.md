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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ca_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.privateca.ca_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name for this CaPool in the format `projects/*/locations/*/caPools/*`. |
| <CopyableCode code="issuancePolicy" /> | `object` | Defines controls over all certificate issuance within a CaPool. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels with user-defined metadata. |
| <CopyableCode code="publishingOptions" /> | `object` | Options relating to the publication of each CertificateAuthority's CA certificate and CRLs and their inclusion as extensions in issued Certificates. The options set here apply to certificates issued by any CertificateAuthority in the CaPool. |
| <CopyableCode code="tier" /> | `string` | Required. Immutable. The Tier of this CaPool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Returns a CaPool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CaPools. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a CaPool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Delete a CaPool. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists CaPools. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="caPoolsId, locationsId, projectsId" /> | Update a CaPool. |
