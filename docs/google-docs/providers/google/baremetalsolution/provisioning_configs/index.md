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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioning_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.baremetalsolution.provisioning_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The system-generated name of the provisioning config. This follows the UUID format. |
| <CopyableCode code="cloudConsoleUri" /> | `string` | Output only. URI to Cloud Console UI view of this provisioning config. |
| <CopyableCode code="customId" /> | `string` | Optional. The user-defined identifier of the provisioning config. |
| <CopyableCode code="email" /> | `string` | Email provided to send a confirmation with provisioning config to. Deprecated in favour of email field in request messages. |
| <CopyableCode code="handoverServiceAccount" /> | `string` | A service account to enable customers to access instance credentials upon handover. |
| <CopyableCode code="instances" /> | `array` | Instances to be created. |
| <CopyableCode code="location" /> | `string` | Optional. Location name of this ProvisioningConfig. It is optional only for Intake UI transition period. |
| <CopyableCode code="networks" /> | `array` | Networks to be created. |
| <CopyableCode code="state" /> | `string` | Output only. State of ProvisioningConfig. |
| <CopyableCode code="statusMessage" /> | `string` | Optional status messages associated with the FAILED state. |
| <CopyableCode code="ticketId" /> | `string` | A generated ticket id to track provisioning request. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |
| <CopyableCode code="volumes" /> | `array` | Volumes to be created. |
| <CopyableCode code="vpcScEnabled" /> | `boolean` | If true, VPC SC is enabled for the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, provisioningConfigsId" /> | Get ProvisioningConfig by name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create new ProvisioningConfig. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, provisioningConfigsId" /> | Update existing ProvisioningConfig. |
| <CopyableCode code="submit" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Submit a provisiong configuration for a given project. |
