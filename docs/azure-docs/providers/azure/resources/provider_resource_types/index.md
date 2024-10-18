---
title: provider_resource_types
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_resource_types
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>provider_resource_types</code> resource.

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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceProviderNamespace, subscriptionId" /> | List the resource types for a specified resource provider. |

## `SELECT` examples

List the resource types for a specified resource provider.


```sql
SELECT
aliases,
apiProfiles,
apiVersions,
capabilities,
defaultApiVersion,
locationMappings,
locations,
properties,
resourceType,
zoneMappings
FROM azure.resources.provider_resource_types
WHERE resourceProviderNamespace = '{{ resourceProviderNamespace }}'
AND subscriptionId = '{{ subscriptionId }}';
```