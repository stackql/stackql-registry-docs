---
title: managed_environment_usages
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environment_usages
  - container_apps
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

Creates, updates, deletes, gets or lists a <code>managed_environment_usages</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_environment_usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.managed_environment_usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The Usage Names. |
| <CopyableCode code="currentValue" /> | `number` | The current usage of the resource. |
| <CopyableCode code="limit" /> | `number` | The maximum permitted usage of the resource. |
| <CopyableCode code="unit" /> | `string` | An enum describing the unit of usage measurement. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Gets the current usage information as well as the limits for environment. |

## `SELECT` examples

Gets the current usage information as well as the limits for environment.


```sql
SELECT
name,
currentValue,
limit,
unit
FROM azure.container_apps.managed_environment_usages
WHERE environmentName = '{{ environmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```