---
title: service_members_data_freshness
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_data_freshness
  - ad_hybrid_health_service
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

Creates, updates, deletes, gets or lists a <code>service_members_data_freshness</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_members_data_freshness</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.service_members_data_freshness" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key" /> | `string` | The key for the property. |
| <CopyableCode code="value" /> | `string` | The value for the key. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> | Gets the last time when the server uploaded data to Azure Active Directory Connect Health Service. |

## `SELECT` examples

Gets the last time when the server uploaded data to Azure Active Directory Connect Health Service.


```sql
SELECT
key,
value
FROM azure.ad_hybrid_health_service.service_members_data_freshness
WHERE serviceMemberId = '{{ serviceMemberId }}'
AND serviceName = '{{ serviceName }}';
```