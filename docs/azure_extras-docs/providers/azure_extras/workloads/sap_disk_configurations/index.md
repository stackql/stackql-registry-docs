---
title: sap_disk_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_disk_configurations
  - workloads
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
<tr><td><b>Name</b></td><td><code>sap_disk_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.workloads.sap_disk_configurations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SAPDiskConfigurations` | `EXEC` | `location, subscriptionId, data__appLocation, data__databaseType, data__dbVmSku, data__deploymentType, data__environment, data__sapProduct` |
