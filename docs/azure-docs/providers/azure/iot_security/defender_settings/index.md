---
title: defender_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - defender_settings
  - iot_security
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>defender_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_security.defender_settings</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DefenderSettings_List` | `SELECT` | `subscriptionId` | List IoT Defender Settings |
| `DefenderSettings_CreateOrUpdate` | `INSERT` | `subscriptionId` | Create or update IoT Defender settings |
| `DefenderSettings_Delete` | `DELETE` | `subscriptionId` | Delete IoT Defender settings |
| `DefenderSettings_DownloadManagerActivation` | `EXEC` | `subscriptionId` | Download manager activation data defined for this subscription |
| `DefenderSettings_Get` | `EXEC` | `subscriptionId` | Get IoT Defender Settings |
| `DefenderSettings_PackageDownloads` | `EXEC` | `subscriptionId` | Information about downloadable packages |
