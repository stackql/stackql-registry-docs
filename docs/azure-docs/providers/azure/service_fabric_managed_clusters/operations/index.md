---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - service_fabric_managed_clusters
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation. |
| <CopyableCode code="display" /> | `object` | Operation supported by the Service Fabric resource provider |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation is a data action |
| <CopyableCode code="nextLink" /> | `string` | The URL to use for getting the next set of results. |
| <CopyableCode code="origin" /> | `string` | Origin result |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get the list of available Service Fabric resource provider API operations. |

## `SELECT` examples

Get the list of available Service Fabric resource provider API operations.


```sql
SELECT
name,
display,
isDataAction,
nextLink,
origin
FROM azure.service_fabric_managed_clusters.operations
;
```