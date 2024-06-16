---
title: provider_resource_types
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_resource_types
  - resources
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
<tr><td><b>Name</b></td><td><code>provider_resource_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.provider_resource_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aliases" /> | `array` | The aliases that are supported by this resource type. |
| <CopyableCode code="apiProfiles" /> | `array` | The API profiles for the resource provider. |
| <CopyableCode code="apiVersions" /> | `array` | The API version. |
| <CopyableCode code="capabilities" /> | `string` | The additional capabilities offered by this resource type. |
| <CopyableCode code="defaultApiVersion" /> | `string` | The default API version. |
| <CopyableCode code="locationMappings" /> | `array` | The location mappings that are supported by this resource type. |
| <CopyableCode code="locations" /> | `array` | The collection of locations where this resource type can be created. |
| <CopyableCode code="properties" /> | `object` | The properties. |
| <CopyableCode code="resourceType" /> | `string` | The resource type. |
| <CopyableCode code="zoneMappings" /> | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceProviderNamespace, subscriptionId" /> |
