---
title: annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - annotations
  - application_insights
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
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.annotations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `AnnotationName` | `string` | Name of annotation |
| `Category` | `string` | Category of annotation, free form |
| `EventTime` | `string` | Time when event occurred |
| `Id` | `string` | Unique Id for annotation |
| `Properties` | `string` | Serialized JSON object for detailed properties |
| `RelatedAnnotation` | `string` | Related parent annotation if any |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `annotationId, resourceGroupName, resourceName, subscriptionId` | Get the annotation for given id. |
| `list` | `SELECT` | `end, resourceGroupName, resourceName, start, subscriptionId` | Gets the list of annotations for a component for given time range |
| `create` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create an Annotation of an Application Insights component. |
| `delete` | `DELETE` | `annotationId, resourceGroupName, resourceName, subscriptionId` | Delete an Annotation of an Application Insights component. |
| `_list` | `EXEC` | `end, resourceGroupName, resourceName, start, subscriptionId` | Gets the list of annotations for a component for given time range |
