---
title: cloud_service_operating_systems
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_service_operating_systems
  - compute
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
<tr><td><b>Name</b></td><td><code>cloud_service_operating_systems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.cloud_service_operating_systems</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CloudServiceOperatingSystems_GetOSFamily` | `EXEC` | `location, osFamilyName, subscriptionId` | Gets properties of a guest operating system family that can be specified in the XML service configuration (.cscfg) for a cloud service. |
| `CloudServiceOperatingSystems_GetOSVersion` | `EXEC` | `location, osVersionName, subscriptionId` | Gets properties of a guest operating system version that can be specified in the XML service configuration (.cscfg) for a cloud service. |
| `CloudServiceOperatingSystems_ListOSFamilies` | `EXEC` | `location, subscriptionId` | Gets a list of all guest operating system families available to be specified in the XML service configuration (.cscfg) for a cloud service. Use nextLink property in the response to get the next page of OS Families. Do this till nextLink is null to fetch all the OS Families. |
| `CloudServiceOperatingSystems_ListOSVersions` | `EXEC` | `location, subscriptionId` | Gets a list of all guest operating system versions available to be specified in the XML service configuration (.cscfg) for a cloud service. Use nextLink property in the response to get the next page of OS versions. Do this till nextLink is null to fetch all the OS versions. |
