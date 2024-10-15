---
title: locations_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_usages
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>locations_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.locations_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The details about the localizable name of a type of usage. |
| <CopyableCode code="currentValue" /> | `integer` | The current usage. |
| <CopyableCode code="limit" /> | `integer` | The maximum allowed usage. |
| <CopyableCode code="unit" /> | `string` | The type of measurement for usage. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Lists the usages for the specified location. |

## `SELECT` examples

Lists the usages for the specified location.


```sql
SELECT
name,
currentValue,
limit,
unit
FROM azure.hdinsight.locations_usages
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```