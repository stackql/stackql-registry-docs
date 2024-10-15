---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - app_service
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

Creates, updates, deletes, gets or lists a <code>usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | Localizable string object containing the name and a localized value. |
| <CopyableCode code="currentValue" /> | `integer` | The current value of the resource counter. |
| <CopyableCode code="limit" /> | `integer` | The resource limit. |
| <CopyableCode code="nextResetTime" /> | `string` | Next reset time for the resource counter. |
| <CopyableCode code="unit" /> | `string` | Units of measurement for the quota resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the quota usage information of an app (or deployment slot, if specified). |

## `SELECT` examples

Description for Gets the quota usage information of an app (or deployment slot, if specified).


```sql
SELECT
name,
currentValue,
limit,
nextResetTime,
unit
FROM azure.app_service.usages
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```