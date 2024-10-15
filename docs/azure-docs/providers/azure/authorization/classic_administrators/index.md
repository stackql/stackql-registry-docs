---
title: classic_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - classic_administrators
  - authorization
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

Creates, updates, deletes, gets or lists a <code>classic_administrators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>classic_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.classic_administrators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the administrator. |
| <CopyableCode code="name" /> | `string` | The name of the administrator. |
| <CopyableCode code="properties" /> | `object` | Classic Administrator properties. |
| <CopyableCode code="type" /> | `string` | The type of the administrator. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets service administrator, account administrator, and co-administrators for the subscription. |

## `SELECT` examples

Gets service administrator, account administrator, and co-administrators for the subscription.


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.classic_administrators
WHERE subscriptionId = '{{ subscriptionId }}';
```