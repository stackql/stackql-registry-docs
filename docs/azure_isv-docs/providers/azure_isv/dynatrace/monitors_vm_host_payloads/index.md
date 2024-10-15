---
title: monitors_vm_host_payloads
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_vm_host_payloads
  - dynatrace
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

Creates, updates, deletes, gets or lists a <code>monitors_vm_host_payloads</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_vm_host_payloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.dynatrace.monitors_vm_host_payloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="environmentId" /> | `string` | Id of the environment created |
| <CopyableCode code="ingestionKey" /> | `string` | Ingestion key of the environment |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
environmentId,
ingestionKey
FROM azure_isv.dynatrace.monitors_vm_host_payloads
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```