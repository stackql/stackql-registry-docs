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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `name` | `string` | Output only. The system-generated name of the provisioning config. This follows the UUID format. |
| `volumes` | `array` | Volumes to be created. |
| `location` | `string` | Optional. Location name of this ProvisioningConfig. It is optional only for Intake UI transition period. |
| `statusMessage` | `string` | Optional status messages associated with the FAILED state. |
| `customId` | `string` | Optional. The user-defined identifier of the provisioning config. |
| `cloudConsoleUri` | `string` | Output only. URI to Cloud Console UI view of this provisioning config. |
| `ticketId` | `string` | A generated ticket id to track provisioning request. |
| `handoverServiceAccount` | `string` | A service account to enable customers to access instance credentials upon handover. |
| `updateTime` | `string` | Output only. Last update timestamp. |
| `vpcScEnabled` | `boolean` | If true, VPC SC is enabled for the cluster. |
| `networks` | `array` | Networks to be created. |
| `instances` | `array` | Instances to be created. |
| `email` | `string` | Email provided to send a confirmation with provisioning config to. Deprecated in favour of email field in request messages. |
| `state` | `string` | Output only. State of ProvisioningConfig. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, provisioningConfigsId` | Get ProvisioningConfig by name. |
| `create` | `INSERT` | `locationsId, projectsId` | Create new ProvisioningConfig. |
| `patch` | `EXEC` | `locationsId, projectsId, provisioningConfigsId` | Update existing ProvisioningConfig. |
| `submit` | `EXEC` | `locationsId, projectsId` | Submit a provisiong configuration for a given project. |
