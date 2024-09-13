
---
title: workloads_ekm_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads_ekm_connections
  - cloudcontrolspartner
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

Creates, updates, deletes or gets an <code>workloads_ekm_connection</code> resource or lists <code>workloads_ekm_connections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workloads_ekm_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.workloads_ekm_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/ekmConnections` |
| <CopyableCode code="ekmConnections" /> | `array` | The EKM connections associated with the workload |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_ekm_connections" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> | Gets the EKM connections associated with a workload |

## `SELECT` examples

Gets the EKM connections associated with a workload

```sql
SELECT
name,
ekmConnections
FROM google.cloudcontrolspartner.workloads_ekm_connections
WHERE customersId = '{{ customersId }}'
AND locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND workloadsId = '{{ workloadsId }}'; 
```
