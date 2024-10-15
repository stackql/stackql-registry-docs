---
title: dedicated_hosts_available_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hosts_available_sizes
  - compute
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

Creates, updates, deletes, gets or lists a <code>dedicated_hosts_available_sizes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dedicated_hosts_available_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.dedicated_hosts_available_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hostGroupName, hostName, resourceGroupName, subscriptionId" /> | Lists all available dedicated host sizes to which the specified dedicated host can be resized. NOTE: The dedicated host sizes provided can be used to only scale up the existing dedicated host. |

## `SELECT` examples

Lists all available dedicated host sizes to which the specified dedicated host can be resized. NOTE: The dedicated host sizes provided can be used to only scale up the existing dedicated host.


```sql
SELECT
column_anon
FROM azure.compute.dedicated_hosts_available_sizes
WHERE hostGroupName = '{{ hostGroupName }}'
AND hostName = '{{ hostName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```