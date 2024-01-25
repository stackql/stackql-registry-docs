---
title: registries_build_source_upload_url
hide_title: false
hide_table_of_contents: false
keywords:
  - registries_build_source_upload_url
  - container_registry
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
<tr><td><b>Name</b></td><td><code>registries_build_source_upload_url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.registries_build_source_upload_url</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `relativePath` | `string` | The relative path to the source. This is used to submit the subsequent queue build request. |
| `uploadUrl` | `string` | The URL where the client can upload the source. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `registryName, resourceGroupName, subscriptionId` |
