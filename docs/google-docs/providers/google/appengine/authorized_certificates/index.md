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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>authorized_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.authorized_certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Continuation token for fetching the next page of results. |
| `certificates` | `array` | The SSL certificates the user is authorized to administer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appsId, authorizedCertificatesId` | Gets the specified SSL certificate. |
| `list` | `SELECT` | `appsId` | Lists all SSL certificates the user is authorized to administer. |
| `create` | `INSERT` | `appsId` | Uploads the specified SSL certificate. |
| `delete` | `DELETE` | `appsId, authorizedCertificatesId` | Deletes the specified SSL certificate. |
| `patch` | `EXEC` | `appsId, authorizedCertificatesId` | Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update certificate_data with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate display_name may also be updated. |
