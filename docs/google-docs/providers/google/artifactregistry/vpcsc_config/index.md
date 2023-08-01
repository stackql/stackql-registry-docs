---
title: vpcsc_config
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcsc_config
  - artifactregistry
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
<tr><td><b>Name</b></td><td><code>vpcsc_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.artifactregistry.vpcsc_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the project's VPC SC Config. Always of the form: projects/&#123;projectID&#125;/locations/&#123;location&#125;/vpcscConfig In update request: never set In response: always set |
| `vpcscPolicy` | `string` | The project per location VPC SC policy that defines the VPC SC behavior for the Remote Repository (Allow/Deny). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_vpcsc_config` | `SELECT` | `locationsId, projectsId` | Retrieves the VPCSC Config for the Project. |
| `update_vpcsc_config` | `EXEC` | `locationsId, projectsId` | Updates the VPCSC Config for the Project. |
