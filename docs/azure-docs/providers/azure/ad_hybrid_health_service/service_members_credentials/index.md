---
title: service_members_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_credentials
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

Creates, updates, deletes, gets or lists a <code>service_members_credentials</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_members_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.service_members_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="credentialData" /> | `array` | The credential data. |
| <CopyableCode code="identifier" /> | `string` | The credential identifier. |
| <CopyableCode code="type" /> | `string` | The type of credential. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> | Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service. |

## `SELECT` examples

Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service.


```sql
SELECT
credentialData,
identifier,
type
FROM azure.ad_hybrid_health_service.service_members_credentials
WHERE serviceMemberId = '{{ serviceMemberId }}'
AND serviceName = '{{ serviceName }}';
```