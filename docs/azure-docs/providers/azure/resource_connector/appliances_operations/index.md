---
title: appliances_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances_operations
  - resource_connector
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

Creates, updates, deletes, gets or lists a <code>appliances_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>appliances_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_connector.appliances_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the compute operation. |
| <CopyableCode code="display" /> | `object` | Describes the properties of an Appliances Operation Value Display. |
| <CopyableCode code="isDataAction" /> | `boolean` | Is this Operation a data plane operation |
| <CopyableCode code="origin" /> | `string` | The origin of the compute operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all available Appliances operations. |

## `SELECT` examples

Lists all available Appliances operations.


```sql
SELECT
name,
display,
isDataAction,
origin
FROM azure.resource_connector.appliances_operations
;
```