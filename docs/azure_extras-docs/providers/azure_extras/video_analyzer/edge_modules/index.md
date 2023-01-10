---
title: edge_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - edge_modules
  - video_analyzer
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>edge_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.video_analyzer.edge_modules</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EdgeModules_Get` | `SELECT` | `accountName, edgeModuleName, resourceGroupName, subscriptionId` | Retrieves an existing edge module resource with the given name. |
| `EdgeModules_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List all existing edge module resources, along with their JSON representations. |
| `EdgeModules_CreateOrUpdate` | `INSERT` | `accountName, edgeModuleName, resourceGroupName, subscriptionId` | Creates a new edge module or updates an existing one. An edge module resource enables a single instance of an Azure Video Analyzer IoT edge module to interact with the Video Analyzer Account. This is used for authorization and also to make sure that the particular edge module instance only has access to the data it requires from the Azure Video Analyzer service. A new edge module resource should be created for every new instance of an Azure Video Analyzer edge module deployed to you Azure IoT edge environment. Edge module resources can be deleted if the specific module is not in use anymore. |
| `EdgeModules_Delete` | `DELETE` | `accountName, edgeModuleName, resourceGroupName, subscriptionId` | Deletes an existing edge module resource. Deleting the edge module resource will prevent an Azure Video Analyzer IoT edge module which was previously initiated with the module provisioning token from communicating with the cloud. |
| `EdgeModules_ListProvisioningToken` | `EXEC` | `accountName, edgeModuleName, resourceGroupName, subscriptionId, data__expirationDate` | Creates a new provisioning token. A provisioning token allows for a single instance of Azure Video analyzer IoT edge module to be initialized and authorized to the cloud account. The provisioning token itself is short lived and it is only used for the initial handshake between IoT edge module and the cloud. After the initial handshake, the IoT edge module will agree on a set of authentication keys which will be auto-rotated as long as the module is able to periodically connect to the cloud. A new provisioning token can be generated for the same IoT edge module in case the module state lost or reset. |
