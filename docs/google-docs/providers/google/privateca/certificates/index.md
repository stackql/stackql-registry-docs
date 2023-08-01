---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.privateca.certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token to retrieve next page of results. Pass this value in ListCertificatesRequest.next_page_token to retrieve the next page of results. |
| `unreachable` | `array` | A list of locations (e.g. "us-west1") that could not be reached. |
| `certificates` | `array` | The list of Certificates. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `caPoolsId, certificatesId, locationsId, projectsId` | Returns a Certificate. |
| `list` | `SELECT` | `caPoolsId, locationsId, projectsId` | Lists Certificates. |
| `create` | `INSERT` | `caPoolsId, locationsId, projectsId` | Create a new Certificate in a given Project, Location from a particular CaPool. |
| `patch` | `EXEC` | `caPoolsId, certificatesId, locationsId, projectsId` | Update a Certificate. Currently, the only field you can update is the labels field. |
| `revoke` | `EXEC` | `caPoolsId, certificatesId, locationsId, projectsId` | Revoke a Certificate. |
