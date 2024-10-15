---
title: dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - dimensions
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>dimensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dimensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.dimensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | ETag of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Dimension properties. |
| <CopyableCode code="sku" /> | `string` | SKU of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Lists the dimensions by the defined scope. |
| <CopyableCode code="by_external_cloud_provider_type" /> | `EXEC` | <CopyableCode code="externalCloudProviderId, externalCloudProviderType" /> | Lists the dimensions by the external cloud provider type. |

## `SELECT` examples

Lists the dimensions by the defined scope.


```sql
SELECT
id,
name,
eTag,
location,
properties,
sku,
tags,
type
FROM azure.cost_management.dimensions
WHERE scope = '{{ scope }}';
```