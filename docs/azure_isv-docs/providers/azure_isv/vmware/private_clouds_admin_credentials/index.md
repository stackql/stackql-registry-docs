---
title: private_clouds_admin_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds_admin_credentials
  - vmware
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>private_clouds_admin_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware.private_clouds_admin_credentials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nsxtPassword` | `string` | NSX-T Manager password |
| `nsxtUsername` | `string` | NSX-T Manager username |
| `vcenterPassword` | `string` | vCenter admin password |
| `vcenterUsername` | `string` | vCenter admin username |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |
