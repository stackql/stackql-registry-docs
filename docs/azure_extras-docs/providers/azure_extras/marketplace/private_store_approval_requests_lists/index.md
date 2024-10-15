---
title: private_store_approval_requests_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_approval_requests_lists
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>private_store_approval_requests_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_store_approval_requests_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store_approval_requests_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Approval request resource properties |
| <CopyableCode code="systemData" /> | `object` | Read only system data |
| <CopyableCode code="type" /> | `string` | The type of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateStoreId" /> | Get all open approval requests of current user |

## `SELECT` examples

Get all open approval requests of current user


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure_extras.marketplace.private_store_approval_requests_lists
WHERE privateStoreId = '{{ privateStoreId }}';
```