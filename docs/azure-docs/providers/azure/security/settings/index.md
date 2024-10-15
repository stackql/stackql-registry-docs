---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="kind" /> | `string` | the kind of the settings string |
| <CopyableCode code="type" /> | `string` | Resource type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="settingName, subscriptionId" /> | Settings of different configurations in Microsoft Defender for Cloud |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Settings about different configurations in Microsoft Defender for Cloud |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="settingName, subscriptionId, data__kind" /> | updating settings about different configurations in Microsoft Defender for Cloud |

## `SELECT` examples

Settings about different configurations in Microsoft Defender for Cloud


```sql
SELECT
id,
name,
kind,
type
FROM azure.security.settings
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `REPLACE` example

Replaces all fields in the specified <code>settings</code> resource.

```sql
/*+ update */
REPLACE azure.security.settings
SET 
kind = '{{ kind }}'
WHERE 
settingName = '{{ settingName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__kind = '{{ data__kind }}';
```
