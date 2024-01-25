---
title: runtime_versions_runtime_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - runtime_versions_runtime_versions
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>runtime_versions_runtime_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.runtime_versions_runtime_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `platform` | `string` | The platform of this runtime version (possible values: "Java" or ".NET"). |
| `value` | `string` | The raw value which could be passed to deployment CRUD operations. |
| `version` | `string` | The detailed version (major.minor) of the platform. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
