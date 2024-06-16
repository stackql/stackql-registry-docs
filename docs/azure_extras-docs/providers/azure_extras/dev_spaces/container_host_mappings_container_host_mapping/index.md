---
title: container_host_mappings_container_host_mapping
hide_title: false
hide_table_of_contents: false
keywords:
  - container_host_mappings_container_host_mapping
  - dev_spaces
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
<tr><td><b>Name</b></td><td><code>container_host_mappings_container_host_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.dev_spaces.container_host_mappings_container_host_mapping" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="containerHostResourceId" /> | `string` | ARM ID of the Container Host resource |
| <CopyableCode code="mappedControllerResourceId" /> | `string` | ARM ID of the mapped Controller resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> |
