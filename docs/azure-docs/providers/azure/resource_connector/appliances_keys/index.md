---
title: appliances_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances_keys
  - resource_connector
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
<tr><td><b>Name</b></td><td><code>appliances_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_connector.appliances_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `artifactProfiles` | `object` | Map of artifacts that contains a list of ArtifactProfile used to upload artifacts such as logs. |
| `kubeconfigs` | `array` | The list of appliance kubeconfigs. |
| `sshKeys` | `object` | Map of Customer User Public, Private SSH Keys and Certificate when available. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
