---
title: iot_security_solution_analytics
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solution_analytics
  - security
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

Creates, updates, deletes, gets or lists a <code>iot_security_solution_analytics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iot_security_solution_analytics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.iot_security_solution_analytics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Security analytics properties of your IoT Security solution |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Use this method to get IoT Security Analytics metrics. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, solutionName, subscriptionId" /> | Use this method to get IoT security Analytics metrics in an array. |

## `SELECT` examples

Use this method to get IoT Security Analytics metrics.


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.iot_security_solution_analytics
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND solutionName = '{{ solutionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```