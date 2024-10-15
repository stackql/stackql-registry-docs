---
title: palo_alto_networks_cloudngfw_cloud_manager_tenants
hide_title: false
hide_table_of_contents: false
keywords:
  - palo_alto_networks_cloudngfw_cloud_manager_tenants
  - paloalto
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

Creates, updates, deletes, gets or lists a <code>palo_alto_networks_cloudngfw_cloud_manager_tenants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>palo_alto_networks_cloudngfw_cloud_manager_tenants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.palo_alto_networks_cloudngfw_cloud_manager_tenants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
column_anon
FROM azure_isv.paloalto.palo_alto_networks_cloudngfw_cloud_manager_tenants
WHERE subscriptionId = '{{ subscriptionId }}';
```