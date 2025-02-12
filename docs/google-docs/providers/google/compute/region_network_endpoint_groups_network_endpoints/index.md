---
title: region_network_endpoint_groups_network_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - region_network_endpoint_groups_network_endpoints
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

Creates, updates, deletes, gets or lists a <code>region_network_endpoint_groups_network_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_network_endpoint_groups_network_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_network_endpoint_groups_network_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="healths" /> | `array` | [Output only] The health status of network endpoint; |
| <CopyableCode code="networkEndpoint" /> | `object` | The network endpoint. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_network_endpoints" /> | `SELECT` | <CopyableCode code="networkEndpointGroup, project, region" /> | Lists the network endpoints in the specified network endpoint group. |

## `SELECT` examples

Lists the network endpoints in the specified network endpoint group.

```sql
SELECT
healths,
networkEndpoint
FROM google.compute.region_network_endpoint_groups_network_endpoints
WHERE networkEndpointGroup = '{{ networkEndpointGroup }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
