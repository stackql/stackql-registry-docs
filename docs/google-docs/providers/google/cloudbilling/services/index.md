---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - cloudbilling
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudbilling.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the service. Example: "services/DA34-426B-A397" |
| `serviceId` | `string` | The identifier for the service. Example: "DA34-426B-A397" |
| `businessEntityName` | `string` | The business under which the service is offered. Ex. "businessEntities/GCP", "businessEntities/Maps" |
| `displayName` | `string` | A human readable display name for this service. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
