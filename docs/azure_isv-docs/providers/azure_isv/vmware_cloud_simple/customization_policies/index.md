---
title: customization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - customization_policies
  - vmware_cloud_simple
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>customization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.customization_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Customization policy azure id |
| <CopyableCode code="name" /> | `string` | Customization policy name |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | The properties of Customization policy |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, customizationPolicyName, pcName, regionId, subscriptionId" /> | Returns customization policy by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, pcName, regionId, subscriptionId" /> | Returns list of customization policies in region for private cloud |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, pcName, regionId, subscriptionId" /> | Returns list of customization policies in region for private cloud |
