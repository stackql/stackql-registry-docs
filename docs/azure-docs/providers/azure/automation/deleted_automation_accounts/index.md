---
title: deleted_automation_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_automation_accounts
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

Creates, updates, deletes, gets or lists a <code>deleted_automation_accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deleted_automation_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.deleted_automation_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets or sets name of the resource. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location of the resource. |
| <CopyableCode code="properties" /> | `object` | Definition of the deleted automation account properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieve deleted automation account. |

## `SELECT` examples

Retrieve deleted automation account.


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.automation.deleted_automation_accounts
WHERE subscriptionId = '{{ subscriptionId }}';
```