---
title: ssl_certs
hide_title: false
hide_table_of_contents: false
keywords:
  - ssl_certs
  - sqladmin
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
<tr><td><b>Name</b></td><td><code>ssl_certs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sqladmin.ssl_certs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | This is always `sql#sslCert`. |
| `selfLink` | `string` | The URI of this resource. |
| `cert` | `string` | PEM representation. |
| `sha1Fingerprint` | `string` | Sha1 Fingerprint. |
| `commonName` | `string` | User supplied name. Constrained to [a-zA-Z.-_ ]+. |
| `createTime` | `string` | The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z` |
| `instance` | `string` | Name of the database instance. |
| `certSerialNumber` | `string` | Serial number, as extracted from the certificate. |
| `expirationTime` | `string` | The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `sql_sslCerts_get` | `SELECT` | `instance, project, sha1Fingerprint` | Retrieves a particular SSL certificate. Does not include the private key (required for usage). The private key must be saved from the response to initial creation. |
| `sql_sslCerts_list` | `SELECT` | `instance, project` | Lists all of the current SSL certificates for the instance. |
| `sql_sslCerts_insert` | `INSERT` | `instance, project` | Creates an SSL certificate and returns it along with the private key and server certificate authority. The new certificate will not be usable until the instance is restarted. |
| `sql_sslCerts_delete` | `DELETE` | `instance, project, sha1Fingerprint` | Deletes the SSL certificate. For First Generation instances, the certificate remains valid until the instance is restarted. |
