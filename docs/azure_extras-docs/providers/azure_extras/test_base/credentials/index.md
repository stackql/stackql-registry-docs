---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - credentials
  - test_base
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
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.credentials</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `create` | `INSERT` | `credentialName, resourceGroupName, subscriptionId, testBaseAccountName` | Creates or replaces a Test Base Credential. |
| `delete` | `DELETE` | `credentialName, resourceGroupName, subscriptionId, testBaseAccountName` | Deletes an existing test base credential. |
| `update` | `EXEC` | `credentialName, resourceGroupName, subscriptionId, testBaseAccountName` | Updates an existing test base credential. |
