---
title: revision_replicas_replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - revision_replicas_replicas
  - container_apps
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
<tr><td><b>Name</b></td><td><code>revision_replicas_replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.revision_replicas_replicas</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `containerAppName, resourceGroupName, revisionName, subscriptionId` |
| `_list` | `EXEC` | `containerAppName, resourceGroupName, revisionName, subscriptionId` |
