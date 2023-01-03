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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorized_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.authorized_certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Relative name of the certificate. This is a unique value autogenerated on AuthorizedCertificate resource creation. Example: 12345.@OutputOnly |
| `name` | `string` | Full path to the AuthorizedCertificate resource in the API. Example: apps/myapp/authorizedCertificates/12345.@OutputOnly |
| `displayName` | `string` | The user-specified display name of the certificate. This is not guaranteed to be unique. Example: My Certificate. |
| `domainMappingsCount` | `integer` | Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have VIEWER permissions.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly |
| `expireTime` | `string` | The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using AuthorizedCertificates.UpdateAuthorizedCertificate.@OutputOnly |
| `managedCertificate` | `object` | A certificate managed by App Engine. |
| `visibleDomainMappings` | `array` | The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: apps/myapp/domainMappings/example.com.This may not represent the full list of mapped domain mappings if the user does not have VIEWER permissions on all of the applications that have this certificate mapped. See domain_mappings_count for a complete count.Only returned by GET or LIST requests when specifically requested by the view=FULL_CERTIFICATE option.@OutputOnly |
| `certificateRawData` | `object` | An SSL certificate obtained from a certificate authority. |
| `domainNames` | `array` | Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: example.com.@OutputOnly |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `apps_authorizedCertificates_get` | `SELECT` | `appsId, authorizedCertificatesId` | Gets the specified SSL certificate. |
| `apps_authorizedCertificates_list` | `SELECT` | `appsId` | Lists all SSL certificates the user is authorized to administer. |
| `apps_authorizedCertificates_create` | `INSERT` | `appsId` | Uploads the specified SSL certificate. |
| `apps_authorizedCertificates_delete` | `DELETE` | `appsId, authorizedCertificatesId` | Deletes the specified SSL certificate. |
| `apps_authorizedCertificates_patch` | `EXEC` | `appsId, authorizedCertificatesId` | Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated. |