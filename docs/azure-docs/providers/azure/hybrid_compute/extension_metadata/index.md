---
title: extension_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - extension_metadata
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>extension_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.extension_metadata</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `extensionType, location, publisher, subscriptionId, version` | Gets an Extension Metadata based on location, publisher, extensionType and version |
| `list` | `SELECT` | `extensionType, location, publisher, subscriptionId` | Gets all Extension versions based on location, publisher, extensionType |
| `_list` | `EXEC` | `extensionType, location, publisher, subscriptionId` | Gets all Extension versions based on location, publisher, extensionType |
