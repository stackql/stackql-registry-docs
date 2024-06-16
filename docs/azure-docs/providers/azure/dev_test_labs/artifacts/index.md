---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an artifact. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, artifactSourceName, labName, name, resourceGroupName, subscriptionId" /> | Get artifact. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, artifactSourceName, labName, resourceGroupName, subscriptionId" /> | List artifacts in a given artifact source. |
| <CopyableCode code="generate_arm_template" /> | `EXEC` | <CopyableCode code="api-version, artifactSourceName, labName, name, resourceGroupName, subscriptionId" /> | Generates an ARM template for the given artifact, uploads the required files to a storage account, and validates the generated artifact. |
