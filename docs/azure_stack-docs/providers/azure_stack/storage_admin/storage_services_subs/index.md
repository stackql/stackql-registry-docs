---
title: storage_services_subs
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_services_subs
  - storage_admin
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

Creates, updates, deletes, gets or lists a <code>storage_services_subs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>storage_services_subs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.storage_services_subs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="location" /> | `string` | Resource Location. |
| <CopyableCode code="properties" /> | `object` | The properties for service name. |
| <CopyableCode code="type" /> | `string` | Resource Type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns the storage services list under the specified subscription. |

## `SELECT` examples

Returns the storage services list under the specified subscription.


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_stack.storage_admin.storage_services_subs
WHERE subscriptionId = '{{ subscriptionId }}';
```