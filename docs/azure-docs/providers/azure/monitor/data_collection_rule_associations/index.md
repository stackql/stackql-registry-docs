---
title: data_collection_rule_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rule_associations
  - monitor
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
<tr><td><b>Name</b></td><td><code>data_collection_rule_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.data_collection_rule_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID of the resource. |
| `name` | `string` | The name of the resource. |
| `type` | `string` | The type of the resource. |
| `etag` | `string` | Resource entity tag (ETag). |
| `properties` | `object` | Resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `DataCollectionRuleAssociations_Get` | `SELECT` | `associationName, resourceUri` |
| `DataCollectionRuleAssociations_ListByDataCollectionEndpoint` | `SELECT` | `dataCollectionEndpointName, resourceGroupName, subscriptionId` |
| `DataCollectionRuleAssociations_ListByResource` | `SELECT` | `resourceUri` |
| `DataCollectionRuleAssociations_ListByRule` | `SELECT` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
| `DataCollectionRuleAssociations_Create` | `INSERT` | `associationName, resourceUri` |
| `DataCollectionRuleAssociations_Delete` | `DELETE` | `associationName, resourceUri` |
