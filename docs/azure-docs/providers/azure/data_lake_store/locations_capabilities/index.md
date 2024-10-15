---
title: locations_capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_capabilities
  - data_lake_store
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

Creates, updates, deletes, gets or lists a <code>locations_capabilities</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_store.locations_capabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountCount" /> | `integer` | The current number of accounts under this subscription. |
| <CopyableCode code="maxAccountCount" /> | `integer` | The maximum supported number of accounts under this subscription. |
| <CopyableCode code="migrationState" /> | `boolean` | The Boolean value of true or false to indicate the maintenance state. |
| <CopyableCode code="state" /> | `string` | The subscription state. |
| <CopyableCode code="subscriptionId" /> | `string` | The subscription credentials that uniquely identifies the subscription. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Gets subscription-level properties and limits for Data Lake Store specified by resource location. |

## `SELECT` examples

Gets subscription-level properties and limits for Data Lake Store specified by resource location.


```sql
SELECT
accountCount,
maxAccountCount,
migrationState,
state,
subscriptionId
FROM azure.data_lake_store.locations_capabilities
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```