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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_issuance_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.certificatemanager.certificate_issuance_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | A user-defined name of the certificate issuance config. CertificateIssuanceConfig names must be unique globally and match pattern `projects/*/locations/*/certificateIssuanceConfigs/*`. |
| `description` | `string` | One or more paragraphs of text description of a CertificateIssuanceConfig. |
| `createTime` | `string` | Output only. The creation timestamp of a CertificateIssuanceConfig. |
| `labels` | `object` | Set of labels associated with a CertificateIssuanceConfig. |
| `updateTime` | `string` | Output only. The last update timestamp of a CertificateIssuanceConfig. |
| `certificateAuthorityConfig` | `object` | The CA that issues the workload certificate. It includes CA address, type, authentication to CA service, etc. |
| `rotationWindowPercentage` | `integer` | Required. Specifies the percentage of elapsed time of the certificate lifetime to wait before renewing the certificate. Must be a number between 1-99, inclusive. |
| `keyAlgorithm` | `string` | Required. The key algorithm to use when generating the private key. |
| `lifetime` | `string` | Required. Workload certificate lifetime requested. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateIssuanceConfigsId, locationsId, projectsId` | Gets details of a single CertificateIssuanceConfig. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists CertificateIssuanceConfigs in a given project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a new CertificateIssuanceConfig in a given project and location. |
| `delete` | `DELETE` | `certificateIssuanceConfigsId, locationsId, projectsId` | Deletes a single CertificateIssuanceConfig. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists CertificateIssuanceConfigs in a given project and location. |
