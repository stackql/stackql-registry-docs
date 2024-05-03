---
title: web_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - web_tests
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
<tr><td><b>Name</b></td><td><code>web_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.web_tests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="kind" /> | `string` | The kind of WebTest that this web test watches. Choices are ping, multistep and standard. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Metadata describing a web test for an Azure resource. |
| <CopyableCode code="tags" /> | `` | Resource tags |
| <CopyableCode code="type" /> | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, webTestName" /> | Get a specific Application Insights web test definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all Application Insights web test definitions for the specified subscription. |
| <CopyableCode code="list_by_component" /> | `SELECT` | <CopyableCode code="componentName, resourceGroupName, subscriptionId" /> | Get all Application Insights web tests defined for the specified component. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all Application Insights web tests defined for the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, webTestName" /> | Creates or updates an Application Insights web test definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, webTestName" /> | Deletes an Application Insights web test. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get all Application Insights web test definitions for the specified subscription. |
| <CopyableCode code="_list_by_component" /> | `EXEC` | <CopyableCode code="componentName, resourceGroupName, subscriptionId" /> | Get all Application Insights web tests defined for the specified component. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all Application Insights web tests defined for the specified resource group. |
