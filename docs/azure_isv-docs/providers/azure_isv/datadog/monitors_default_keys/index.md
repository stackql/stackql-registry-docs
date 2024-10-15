---
title: monitors_default_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_default_keys
  - datadog
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

Creates, updates, deletes, gets or lists a <code>monitors_default_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_default_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.monitors_default_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the API key. |
| <CopyableCode code="created" /> | `string` | The time of creation of the API key. |
| <CopyableCode code="createdBy" /> | `string` | The user that created the API key. |
| <CopyableCode code="key" /> | `string` | The value of the API key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
created,
createdBy,
key
FROM azure_isv.datadog.monitors_default_keys
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```