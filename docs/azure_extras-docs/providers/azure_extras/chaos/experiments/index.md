---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
  - chaos
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
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.chaos.experiments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The identity of a resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Model that represents the Experiment properties model. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, experimentName, resourceGroupName, subscriptionId" /> | Get a Experiment resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get a list of Experiment resources in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, experimentName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a Experiment resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, experimentName, resourceGroupName, subscriptionId" /> | Delete a Experiment resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get a list of Experiment resources in a resource group. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="api-version, experimentName, resourceGroupName, subscriptionId" /> | Cancel a running Experiment resource. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="api-version, experimentName, resourceGroupName, subscriptionId" /> | Start a Experiment resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, experimentName, resourceGroupName, subscriptionId" /> | The operation to update an experiment. |
