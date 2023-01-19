---
title: managedconfigurationsforuser
hide_title: false
hide_table_of_contents: false
keywords:
  - managedconfigurationsforuser
  - androidenterprise
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managedconfigurationsforuser</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.managedconfigurationsforuser</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `configurationVariables` | `object` | A configuration variables resource contains the managed configuration settings ID to be applied to a single user, as well as the variable set that is attributed to the user. The variable set will be used to replace placeholders in the managed configuration settings. |
| `kind` | `string` | Deprecated. |
| `managedProperty` | `array` | The set of managed properties for this configuration. |
| `productId` | `string` | The ID of the product that the managed configuration is for, e.g. "app:com.google.android.gm". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `enterpriseId, managedConfigurationForUserId, userId` | Retrieves details of a per-user managed configuration for an app for the specified user. |
| `list` | `SELECT` | `enterpriseId, userId` | Lists all the per-user managed configurations for the specified user. Only the ID is set. |
| `delete` | `DELETE` | `enterpriseId, managedConfigurationForUserId, userId` | Removes a per-user managed configuration for an app for the specified user. |
| `update` | `EXEC` | `enterpriseId, managedConfigurationForUserId, userId` | Adds or updates the managed configuration settings for an app for the specified user. If you support the Managed configurations iframe, you can apply managed configurations to a user by specifying an mcmId and its associated configuration variables (if any) in the request. Alternatively, all EMMs can apply managed configurations by passing a list of managed properties. |
