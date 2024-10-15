---
title: profiles_supported_optimization_types
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles_supported_optimization_types
  - cdn
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

Creates, updates, deletes, gets or lists a <code>profiles_supported_optimization_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles_supported_optimization_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.profiles_supported_optimization_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="supportedOptimizationTypes" /> | `array` | Supported optimization types for a profile. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Gets the supported optimization types for the current profile. A user can create an endpoint with an optimization type from the listed values. |

## `SELECT` examples

Gets the supported optimization types for the current profile. A user can create an endpoint with an optimization type from the listed values.


```sql
SELECT
supportedOptimizationTypes
FROM azure.cdn.profiles_supported_optimization_types
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```