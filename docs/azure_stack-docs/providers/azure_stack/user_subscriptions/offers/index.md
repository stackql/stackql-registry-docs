---
title: offers
hide_title: false
hide_table_of_contents: false
keywords:
  - offers
  - user_subscriptions
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

Creates, updates, deletes, gets or lists a <code>offers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>offers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.user_subscriptions.offers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The offer ID |
| <CopyableCode code="name" /> | `string` | The name of the offer. |
| <CopyableCode code="description" /> | `string` | Description of offer. |
| <CopyableCode code="displayName" /> | `string` | Display name of offer. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get the list of public offers for the root provider. |

## `SELECT` examples

Get the list of public offers for the root provider.


```sql
SELECT
id,
name,
description,
displayName
FROM azure_stack.user_subscriptions.offers
;
```