---
title: factories_data_plane_access
hide_title: false
hide_table_of_contents: false
keywords:
  - factories_data_plane_access
  - data_factory
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
<tr><td><b>Name</b></td><td><code>factories_data_plane_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.factories_data_plane_access</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accessToken` | `string` | Data Plane read only access token. |
| `dataPlaneUrl` | `string` | Data Plane service base URL. |
| `policy` | `object` | Get Data Plane read only token request definition. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` |
