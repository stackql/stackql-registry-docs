---
title: monitors_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_hosts
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

Creates, updates, deletes, gets or lists a <code>monitors_hosts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.monitors_hosts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the host. |
| <CopyableCode code="aliases" /> | `array` | The aliases for the host installed via the Datadog agent. |
| <CopyableCode code="apps" /> | `array` | The Datadog integrations reporting metrics for the host. |
| <CopyableCode code="meta" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
aliases,
apps,
meta
FROM azure_isv.datadog.monitors_hosts
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```