---
title: vpn_gateways_status
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways_status
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

Creates, updates, deletes, gets or lists a <code>vpn_gateways_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpn_gateways_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.vpn_gateways_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="result" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_status" /> | `SELECT` | <CopyableCode code="project, region, vpnGateway" /> | Returns the status for the specified VPN gateway. |

## `SELECT` examples

Returns the status for the specified VPN gateway.

```sql
SELECT
result
FROM google.compute.vpn_gateways_status
WHERE project = '{{ project }}'
AND region = '{{ region }}'
AND vpnGateway = '{{ vpnGateway }}';
```
