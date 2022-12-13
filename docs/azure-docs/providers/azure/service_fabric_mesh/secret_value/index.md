---
title: secret_value
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_value
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>secret_value</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_mesh.secret_value</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | This type describes properties of a secret value resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecretValue_Get` | `SELECT` | `api-version, resourceGroupName, secretResourceName, secretValueResourceName, subscriptionId` | Get the information about the specified named secret value resources. The information does not include the actual value of the secret. |
| `SecretValue_List` | `SELECT` | `api-version, resourceGroupName, secretResourceName, subscriptionId` | Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values. |
| `SecretValue_Create` | `INSERT` | `api-version, resourceGroupName, secretResourceName, secretValueResourceName, subscriptionId, data__properties` | Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed. |
| `SecretValue_Delete` | `DELETE` | `api-version, resourceGroupName, secretResourceName, secretValueResourceName, subscriptionId` | Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use. |
| `SecretValue_ListValue` | `EXEC` | `api-version, resourceGroupName, secretResourceName, secretValueResourceName, subscriptionId` | Lists the decrypted value of the specified named value of the secret resource. This is a privileged operation. |
