---
title: custom_host_name_analysis
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_host_name_analysis
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
<tr><td><b>Name</b></td><td><code>custom_host_name_analysis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.custom_host_name_analysis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `aRecords` | `array` | A records visible for this hostname. |
| `alternateCNameRecords` | `array` | Alternate CName records visible for this hostname. |
| `alternateTxtRecords` | `array` | Alternate TXT records visible for this hostname. |
| `cNameRecords` | `array` | CName records visible for this hostname. |
| `conflictWithEnvironmentCustomDomain` | `boolean` | &lt;code&gt;true&lt;/code&gt; if there is a conflict on the Container App's managed environment level custom domain; otherwise, &lt;code&gt;false&lt;/code&gt;. |
| `conflictingContainerAppResourceId` | `string` | Name of the conflicting Container App on the Managed Environment if it's within the same subscription. |
| `customDomainVerificationFailureInfo` | `object` | Raw failure information if DNS verification fails. |
| `customDomainVerificationTest` | `string` | DNS verification test result. |
| `hasConflictOnManagedEnvironment` | `boolean` | &lt;code&gt;true&lt;/code&gt; if there is a conflict on the Container App's managed environment; otherwise, &lt;code&gt;false&lt;/code&gt;. |
| `hostName` | `string` | Host name that was analyzed |
| `isHostnameAlreadyVerified` | `boolean` | &lt;code&gt;true&lt;/code&gt; if hostname is already verified; otherwise, &lt;code&gt;false&lt;/code&gt;. |
| `txtRecords` | `array` | TXT records visible for this hostname. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `containerAppName, resourceGroupName, subscriptionId` |
