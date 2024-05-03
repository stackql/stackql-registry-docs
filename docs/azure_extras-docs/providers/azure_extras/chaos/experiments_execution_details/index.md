---
title: experiments_execution_details
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments_execution_details
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
<tr><td><b>Name</b></td><td><code>experiments_execution_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.chaos.experiments_execution_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String of the fully qualified resource ID. |
| <CopyableCode code="name" /> | `string` | String of the resource name. |
| <CopyableCode code="properties" /> | `object` | Model that represents the Experiment execution details properties model. |
| <CopyableCode code="type" /> | `string` | String of the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, executionDetailsId, experimentName, resourceGroupName, subscriptionId" /> | Get an execution detail of a Experiment resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, experimentName, resourceGroupName, subscriptionId" /> | Get a list of execution details of a Experiment resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, experimentName, resourceGroupName, subscriptionId" /> | Get a list of execution details of a Experiment resource. |
