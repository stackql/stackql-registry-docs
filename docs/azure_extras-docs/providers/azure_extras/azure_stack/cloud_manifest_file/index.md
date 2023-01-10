---
title: cloud_manifest_file
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_manifest_file
  - azure_stack
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
<tr><td><b>Name</b></td><td><code>cloud_manifest_file</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.azure_stack.cloud_manifest_file</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Cloud specific manifest JSON properties. |
| `type` | `string` | Type of Resource. |
| `etag` | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CloudManifestFile_Get` | `SELECT` | `verificationVersion` | Returns a cloud specific manifest JSON file. |
| `CloudManifestFile_List` | `SELECT` |  | Returns a cloud specific manifest JSON file with latest version. |
