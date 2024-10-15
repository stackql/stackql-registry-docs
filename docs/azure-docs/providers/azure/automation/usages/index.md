---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - automation
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the id of the resource. |
| <CopyableCode code="name" /> | `object` | Definition of usage counter name. |
| <CopyableCode code="currentValue" /> | `number` | Gets or sets the current usage value. |
| <CopyableCode code="limit" /> | `integer` | Gets or sets max limit. -1 for unlimited |
| <CopyableCode code="throttleStatus" /> | `string` | Gets or sets the throttle status. |
| <CopyableCode code="unit" /> | `string` | Gets or sets the usage unit name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve the usage for the account id. |

## `SELECT` examples

Retrieve the usage for the account id.


```sql
SELECT
id,
name,
currentValue,
limit,
throttleStatus,
unit
FROM azure.automation.usages
WHERE automationAccountName = '{{ automationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```