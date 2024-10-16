---
title: endpoints_managed_proxy_details
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints_managed_proxy_details
  - hybrid_connectivity
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

Creates, updates, deletes, gets or lists a <code>endpoints_managed_proxy_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints_managed_proxy_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.endpoints_managed_proxy_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expiresOn" /> | `integer` | The expiration time of short lived proxy name in unix epoch. |
| <CopyableCode code="proxy" /> | `string` | The short lived proxy name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri, data__service" /> | Fetches the managed proxy details |

## `SELECT` examples

Fetches the managed proxy details


```sql
SELECT
expiresOn,
proxy
FROM azure.hybrid_connectivity.endpoints_managed_proxy_details
WHERE endpointName = '{{ endpointName }}'
AND resourceUri = '{{ resourceUri }}'
AND data__service = '{{ data__service }}';
```