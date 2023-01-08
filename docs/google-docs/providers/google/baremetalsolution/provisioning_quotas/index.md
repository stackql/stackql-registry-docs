---
title: provisioning_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioning_quotas
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
<tr><td><b>Name</b></td><td><code>provisioning_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.baremetalsolution.provisioning_quotas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the provisioning quota. |
| `instanceQuota` | `object` | A resource budget. |
| `gcpService` | `string` | The gcp service of the provisioning quota. |
| `serverCount` | `string` | Server count. |
| `availableCount` | `integer` | The available count of the provisioning quota. |
| `location` | `string` | The specific location of the provisioining quota. |
| `networkBandwidth` | `string` | Network bandwidth, Gbps |
| `storageGib` | `string` | Storage size (GB). |
| `assetType` | `string` | The asset type of this provisioning quota. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_provisioningQuotas_list` | `SELECT` | `locationsId, projectsId` |
