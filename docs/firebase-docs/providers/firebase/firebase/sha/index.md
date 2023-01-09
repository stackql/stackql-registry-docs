---
title: sha
hide_title: false
hide_table_of_contents: false
keywords:
  - sha
  - firebase
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sha</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>firebase.firebase.sha</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_androidApps_sha_list` | `SELECT` | `androidAppsId, projectsId` | Lists the SHA-1 and SHA-256 certificates for the specified AndroidApp. |
| `projects_androidApps_sha_create` | `INSERT` | `androidAppsId, projectsId` | Adds a ShaCertificate to the specified AndroidApp. |
| `projects_androidApps_sha_delete` | `DELETE` | `androidAppsId, projectsId, shaId` | Removes a ShaCertificate from the specified AndroidApp. |
