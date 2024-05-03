---
title: springbootapps
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootapps
  - off_azure_springboot
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>springbootapps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.off_azure_springboot.springbootapps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The springbootapps resource definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, springbootappsName, subscriptionId" /> | Get a springbootapps resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List springbootapps resource by resourceGroup |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="siteName, subscriptionId" /> | List springbootapps resource by subscription |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List springbootapps resource by resourceGroup |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="siteName, subscriptionId" /> | List springbootapps resource by subscription |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, springbootappsName, subscriptionId" /> | Update a springbootapps resource. |
