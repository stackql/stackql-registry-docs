---
title: projects_service_account
hide_title: false
hide_table_of_contents: false
keywords:
  - projects_service_account
  - accessapproval
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
<tr><td><b>Name</b></td><td><code>projects_service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.accessapproval.projects_service_account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the Access Approval service account. Format is one of: * "projects/&#123;project&#125;/serviceAccount" * "folders/&#123;folder&#125;/serviceAccount" * "organizations/&#123;organization&#125;/serviceAccount" |
| `accountEmail` | `string` | Email address of the service account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_getServiceAccount` | `SELECT` | `projectsId` |
