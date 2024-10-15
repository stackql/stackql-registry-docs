---
title: services_user_bad_password_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - services_user_bad_password_reports
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

Creates, updates, deletes, gets or lists a <code>services_user_bad_password_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_user_bad_password_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_user_bad_password_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ipAddress" /> | `string` | The IP address corresponding to the last error event. |
| <CopyableCode code="lastUpdated" /> | `string` | The date and time when the last error event was logged. |
| <CopyableCode code="totalErrorAttempts" /> | `integer` | The total count of specific error events. |
| <CopyableCode code="uniqueIpAddresses" /> | `string` | The list of unique IP addresses. |
| <CopyableCode code="userId" /> | `string` | The user ID value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the bad password login attempt report for an user |

## `SELECT` examples

Gets the bad password login attempt report for an user


```sql
SELECT
ipAddress,
lastUpdated,
totalErrorAttempts,
uniqueIpAddresses,
userId
FROM azure.ad_hybrid_health_service.services_user_bad_password_reports
WHERE serviceName = '{{ serviceName }}';
```