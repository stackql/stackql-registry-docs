---
title: data_types_data
hide_title: false
hide_table_of_contents: false
keywords:
  - data_types_data
  - network_analytics
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

Creates, updates, deletes, gets or lists a <code>data_types_data</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_types_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_analytics.data_types_data" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataProductName, dataTypeName, resourceGroupName, subscriptionId" /> | Delete data for data type. |

## `DELETE` example

Deletes the specified <code>data_types_data</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network_analytics.data_types_data
WHERE dataProductName = '{{ dataProductName }}'
AND dataTypeName = '{{ dataTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
