---
title: region_ssl_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - region_ssl_certificates
  - compute
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
<tr><td><b>Name</b></td><td><code>region_ssl_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_ssl_certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#sslCertificate for SSL certificates. |
| `region` | `string` | [Output Only] URL of the region where the regional SSL Certificate resides. This field is not applicable to global SSL Certificate. |
| `type` | `string` | (Optional) Specifies the type of SSL certificate, either "SELF_MANAGED" or "MANAGED". If not specified, the certificate is self-managed and the fields certificate and private_key are used. |
| `selfManaged` | `object` | Configuration and status of a self-managed SSL certificate. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `managed` | `object` | Configuration and status of a managed SSL certificate. |
| `selfLink` | `string` | [Output only] Server-defined URL for the resource. |
| `expireTime` | `string` | [Output Only] Expire time of the certificate. RFC3339 |
| `subjectAlternativeNames` | `array` | [Output Only] Domains associated with the certificate via Subject Alternative Name. |
| `privateKey` | `string` | A value read into memory from a write-only private key file. The private key file must be in PEM format. For security, only insert requests include this field. |
| `certificate` | `string` | A value read into memory from a certificate file. The certificate file must be in PEM format. The certificate chain must be no greater than 5 certs long. The chain must include at least one intermediate cert. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionSslCertificates_get` | `SELECT` | `project, region, sslCertificate` | Returns the specified SslCertificate resource in the specified region. Get a list of available SSL certificates by making a list() request. |
| `regionSslCertificates_list` | `SELECT` | `project, region` | Retrieves the list of SslCertificate resources available to the specified project in the specified region. |
| `regionSslCertificates_insert` | `INSERT` | `project, region` | Creates a SslCertificate resource in the specified project and region using the data included in the request |
| `regionSslCertificates_delete` | `DELETE` | `project, region, sslCertificate` | Deletes the specified SslCertificate resource in the region. |
