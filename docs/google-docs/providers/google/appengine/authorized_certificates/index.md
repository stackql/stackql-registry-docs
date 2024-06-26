---
title: authorized_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - authorized_certificates
  - appengine
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
<tr><td><b>Name</b></td><td><code>authorized_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.authorized_certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Relative name of the certificate. This is a unique value autogenerated on AuthorizedCertificate resource creation. Example: 12345.@OutputOnly |
| <CopyableCode code="name" /> | `string` | Full path to the AuthorizedCertificate resource in the API. Example: apps/myapp/authorizedCertificates/12345.@OutputOnly |
| <CopyableCode code="certificateRawData" /> | `object` | An SSL certificate obtained from a certificate authority. |
| <CopyableCode code="displayName" /> | `string` | The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate. |
| <CopyableCode code="domainMappingsCount" /> | `integer` | Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have VIEWER permissions.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly |
| <CopyableCode code="domainNames" /> | `array` | Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: example.com.@OutputOnly |
| <CopyableCode code="expireTime" /> | `string` | The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using AuthorizedCertificates.UpdateAuthorizedCertificate.@OutputOnly |
| <CopyableCode code="managedCertificate" /> | `object` | A certificate managed by App Engine. |
| <CopyableCode code="visibleDomainMappings" /> | `array` | The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: apps/myapp/domainMappings/example.com.This may not represent the full list of mapped domain mappings if the user does not have VIEWER permissions on all of the applications that have this certificate mapped. See domain_mappings_count for a complete count.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appsId, authorizedCertificatesId" /> | Gets the specified SSL certificate. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appsId" /> | Lists all SSL certificates the user is authorized to administer. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="appsId" /> | Uploads the specified SSL certificate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appsId, authorizedCertificatesId" /> | Deletes the specified SSL certificate. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="appsId, authorizedCertificatesId" /> | Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="appsId" /> | Lists all SSL certificates the user is authorized to administer. |
