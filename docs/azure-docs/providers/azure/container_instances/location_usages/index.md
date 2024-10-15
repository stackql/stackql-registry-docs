---
title: location_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - location_usages
  - container_instances
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

Creates, updates, deletes, gets or lists a <code>location_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_instances.location_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the usage result |
| <CopyableCode code="name" /> | `object` | The name object of the resource |
| <CopyableCode code="currentValue" /> | `integer` | The current usage of the resource |
| <CopyableCode code="limit" /> | `integer` | The maximum permitted usage of the resource. |
| <CopyableCode code="unit" /> | `string` | Unit of the usage result |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get the usage for a subscription |

## `SELECT` examples

Get the usage for a subscription


```sql
SELECT
id,
name,
currentValue,
limit,
unit
FROM azure.container_instances.location_usages
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```