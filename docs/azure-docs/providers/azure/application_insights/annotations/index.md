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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.annotations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="AnnotationName" /> | `string` | Name of annotation |
| <CopyableCode code="Category" /> | `string` | Category of annotation, free form |
| <CopyableCode code="EventTime" /> | `string` | Time when event occurred |
| <CopyableCode code="Id" /> | `string` | Unique Id for annotation |
| <CopyableCode code="Properties" /> | `string` | Serialized JSON object for detailed properties |
| <CopyableCode code="RelatedAnnotation" /> | `string` | Related parent annotation if any |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="annotationId, resourceGroupName, resourceName, subscriptionId" /> | Get the annotation for given id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="end, resourceGroupName, resourceName, start, subscriptionId" /> | Gets the list of annotations for a component for given time range |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create an Annotation of an Application Insights component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="annotationId, resourceGroupName, resourceName, subscriptionId" /> | Delete an Annotation of an Application Insights component. |
