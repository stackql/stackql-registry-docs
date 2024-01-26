---
title: access_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - access_environments
  - confluent
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
<tr><td><b>Name</b></td><td><code>access_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.confluent.access_environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `data` | `array` | Data of the invitations list |
| `kind` | `string` | Type of response |
| `metadata` | `object` | Metadata of the list |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `organizationName, resourceGroupName, subscriptionId` |
