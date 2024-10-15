---
title: app_setting_key_vault_reference_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - app_setting_key_vault_reference_slots
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

Creates, updates, deletes, gets or lists a <code>app_setting_key_vault_reference_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_setting_key_vault_reference_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.app_setting_key_vault_reference_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | ApiKVReference resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appSettingKey, name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the config reference and status of an app |

## `SELECT` examples

Description for Gets the config reference and status of an app


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.app_setting_key_vault_reference_slots
WHERE appSettingKey = '{{ appSettingKey }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```