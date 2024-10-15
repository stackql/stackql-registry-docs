---
title: container_apps_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps_secrets
  - app_service
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

Creates, updates, deletes, gets or lists a <code>container_apps_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>container_apps_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.container_apps_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Secret Name. |
| <CopyableCode code="value" /> | `string` | Secret Value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
value
FROM azure.app_service.container_apps_secrets
WHERE name = '{{ name }}'
AND subscriptionId = '{{ subscriptionId }}';
```