---
title: private_link_resources_supported
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources_supported
  - search
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>private_link_resources_supported</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_link_resources_supported</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.private_link_resources_supported" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a supported private link resource for the Azure AI Search service. For a given API version, this represents the 'supported' groupIds when creating a shared private link resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Gets a list of all supported private link resource types for the given service. |

## `SELECT` examples

Gets a list of all supported private link resource types for the given service.


```sql
SELECT
id,
name,
properties,
type
FROM azure.search.private_link_resources_supported
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND searchServiceName = '{{ searchServiceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```