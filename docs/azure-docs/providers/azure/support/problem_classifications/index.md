---
title: problem_classifications
hide_title: false
hide_table_of_contents: false
keywords:
  - problem_classifications
  - support
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
<tr><td><b>Name</b></td><td><code>problem_classifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.support.problem_classifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Id of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Details about a problem classification available for an Azure service. |
| `type` | `string` | Type of the resource 'Microsoft.Support/problemClassification'. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProblemClassifications_Get` | `SELECT` | `problemClassificationName, serviceName` | Get problem classification details for a specific Azure service. |
| `ProblemClassifications_List` | `SELECT` | `serviceName` | Lists all the problem classifications (categories) available for a specific Azure service. Always use the service and problem classifications obtained programmatically. This practice ensures that you always have the most recent set of service and problem classification Ids. |
