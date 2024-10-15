---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - peering
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation. |
| <CopyableCode code="display" /> | `object` | The information related to the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | The flag that indicates whether the operation applies to data plane. |
| <CopyableCode code="properties" /> | `object` | The properties of the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available API operations for peering resources. |
| <CopyableCode code="check_service_provider_availability" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Checks if the peering service provider is present within 1000 miles of customer's location |

## `SELECT` examples

Lists all of the available API operations for peering resources.


```sql
SELECT
name,
display,
isDataAction,
properties
FROM azure.peering.operations
;
```