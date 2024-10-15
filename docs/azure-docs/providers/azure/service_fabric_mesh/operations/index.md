---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - service_fabric_mesh
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation. |
| <CopyableCode code="display" /> | `object` | An operation available at the listed Azure resource provider. |
| <CopyableCode code="nextLink" /> | `string` | The URL to use for getting the next set of results. |
| <CopyableCode code="origin" /> | `string` | Origin result |
| <CopyableCode code="properties" /> | `object` | Properties available for a Microsoft.Web resource provider operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all the available operations provided by Service Fabric SeaBreeze resource provider. |

## `SELECT` examples

Lists all the available operations provided by Service Fabric SeaBreeze resource provider.


```sql
SELECT
name,
display,
nextLink,
origin,
properties
FROM azure.service_fabric_mesh.operations
;
```