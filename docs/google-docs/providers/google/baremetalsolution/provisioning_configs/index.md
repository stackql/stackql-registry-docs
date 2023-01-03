---
title: provisioning_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning_configs
  - baremetalsolution
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
<tr><td><b>Name</b></td><td><code>provisioning_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.provisioning_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the provisioning config. |
| `updateTime` | `string` | Output only. Last update timestamp. |
| `networks` | `array` | Networks to be created. |
| `instances` | `array` | Instances to be created. |
| `statusMessage` | `string` | Optional status messages associated with the FAILED state. |
| `volumes` | `array` | Volumes to be created. |
| `cloudConsoleUri` | `string` | Output only. URI to Cloud Console UI view of this provisioning config. |
| `email` | `string` | Email provided to send a confirmation with provisioning config to. Deprecated in favour of email field in request messages. |
| `vpcScEnabled` | `boolean` | If true, VPC SC is enabled for the cluster. |
| `handoverServiceAccount` | `string` | A service account to enable customers to access instance credentials upon handover. |
| `location` | `string` | Optional. Location name of this ProvisioningConfig. It is optional only for Intake UI transition period. |
| `state` | `string` | Output only. State of ProvisioningConfig. |
| `ticketId` | `string` | A generated ticket id to track provisioning request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_provisioningConfigs_get` | `SELECT` | `locationsId, projectsId, provisioningConfigsId` | Get ProvisioningConfig by name. |
| `projects_locations_provisioningConfigs_create` | `INSERT` | `locationsId, projectsId` | Create new ProvisioningConfig. |
| `projects_locations_provisioningConfigs_patch` | `EXEC` | `locationsId, projectsId, provisioningConfigsId` | Update existing ProvisioningConfig. |
| `projects_locations_provisioningConfigs_submit` | `EXEC` | `locationsId, projectsId` | Submit a provisiong configuration for a given project. |
