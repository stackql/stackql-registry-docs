---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.artifacts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `properties` | `object` | Properties of an artifact. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Artifacts_Get` | `SELECT` | `api-version, artifactSourceName, labName, name, resourceGroupName, subscriptionId` | Get artifact. |
| `Artifacts_List` | `SELECT` | `api-version, artifactSourceName, labName, resourceGroupName, subscriptionId` | List artifacts in a given artifact source. |
| `Artifacts_GenerateArmTemplate` | `EXEC` | `api-version, artifactSourceName, labName, name, resourceGroupName, subscriptionId` | Generates an ARM template for the given artifact, uploads the required files to a storage account, and validates the generated artifact. |
