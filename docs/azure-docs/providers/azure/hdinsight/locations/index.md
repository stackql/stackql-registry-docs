---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.locations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Locations_CheckNameAvailability` | `EXEC` | `location, subscriptionId` | Check the cluster name is available or not. |
| `Locations_GetAzureAsyncOperationStatus` | `EXEC` | `location, operationId, subscriptionId` | Get the async operation status. |
| `Locations_GetCapabilities` | `EXEC` | `location, subscriptionId` | Gets the capabilities for the specified location. |
| `Locations_ListBillingSpecs` | `EXEC` | `location, subscriptionId` | Lists the billingSpecs for the specified subscription and location. |
| `Locations_ListUsages` | `EXEC` | `location, subscriptionId` | Lists the usages for the specified location. |
| `Locations_ValidateClusterCreateRequest` | `EXEC` | `location, subscriptionId` | Validate the cluster create request spec is valid or not. |
