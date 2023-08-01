---
title: certificate_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate_templates
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>certificate_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.certificate_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListCertificateTemplatesRequest.next_page_token to retrieve the next page of results. |
| `unreachable` | `array` | A list of locations (e.g. "us-west1") that could not be reached. |
| `certificateTemplates` | `array` | The list of CertificateTemplates. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `certificateTemplatesId, locationsId, projectsId` | Returns a CertificateTemplate. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists CertificateTemplates. |
| `create` | `INSERT` | `locationsId, projectsId` | Create a new CertificateTemplate in a given Project and Location. |
| `delete` | `DELETE` | `certificateTemplatesId, locationsId, projectsId` | DeleteCertificateTemplate deletes a CertificateTemplate. |
| `patch` | `EXEC` | `certificateTemplatesId, locationsId, projectsId` | Update a CertificateTemplate. |
