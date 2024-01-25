---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
  - ml_services
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
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.features</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `featureName, featuresetName, featuresetVersion, resourceGroupName, subscriptionId, workspaceName` |
| `list` | `SELECT` | `featuresetName, featuresetVersion, resourceGroupName, subscriptionId, workspaceName` |
| `_list` | `EXEC` | `featuresetName, featuresetVersion, resourceGroupName, subscriptionId, workspaceName` |
