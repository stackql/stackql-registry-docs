---
title: monitors_vm_host_payload
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_vm_host_payload
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>monitors_vm_host_payload</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.dynatrace.monitors_vm_host_payload</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `environmentId` | `string` | Id of the environment created |
| `ingestionKey` | `string` | Ingestion key of the environment |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
