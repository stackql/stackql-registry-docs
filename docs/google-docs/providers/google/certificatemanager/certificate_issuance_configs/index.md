---
title: certificate_issuance_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_issuance_configs
  - certificatemanager
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
<tr><td><b>Name</b></td><td><code>certificate_issuance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.certificatemanager.certificate_issuance_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A user-defined name of the certificate issuance config. CertificateIssuanceConfig names must be unique globally and match pattern `projects/*/locations/*/certificateIssuanceConfigs/*`. |
| <CopyableCode code="description" /> | `string` | One or more paragraphs of text description of a CertificateIssuanceConfig. |
| <CopyableCode code="certificateAuthorityConfig" /> | `object` | The CA that issues the workload certificate. It includes CA address, type, authentication to CA service, etc. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of a CertificateIssuanceConfig. |
| <CopyableCode code="keyAlgorithm" /> | `string` | Required. The key algorithm to use when generating the private key. |
| <CopyableCode code="labels" /> | `object` | Set of labels associated with a CertificateIssuanceConfig. |
| <CopyableCode code="lifetime" /> | `string` | Required. Workload certificate lifetime requested. |
| <CopyableCode code="rotationWindowPercentage" /> | `integer` | Required. Specifies the percentage of elapsed time of the certificate lifetime to wait before renewing the certificate. Must be a number between 1-99, inclusive. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update timestamp of a CertificateIssuanceConfig. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateIssuanceConfigsId, locationsId, projectsId" /> | Gets details of a single CertificateIssuanceConfig. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CertificateIssuanceConfigs in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new CertificateIssuanceConfig in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateIssuanceConfigsId, locationsId, projectsId" /> | Deletes a single CertificateIssuanceConfig. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists CertificateIssuanceConfigs in a given project and location. |
