---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - redhat_openshift
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.redhat_openshift.secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | SecretProperties represents the properties of a Secret |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a Secret. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of each Secret. |
| `create_or_update` | `INSERT` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a Secret. |
| `delete` | `DELETE` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns nothing. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | The operation returns properties of each Secret. |
| `update` | `EXEC` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | The operation returns properties of a Secret. |
