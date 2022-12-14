---
title: afd_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_profiles
  - cdn
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
<tr><td><b>Name</b></td><td><code>afd_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.afd_profiles</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AFDProfiles_CheckHostNameAvailability` | `EXEC` | `profileName, resourceGroupName, subscriptionId, data__hostName` | Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS. |
| `AFDProfiles_ListResourceUsage` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Checks the quota and actual usage of endpoints under the given CDN profile. |
