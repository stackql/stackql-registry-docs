---
title: monitors_app_services
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors_app_services
  - newrelic
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

Creates, updates, deletes, gets or lists a <code>monitors_app_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitors_app_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.newrelic.monitors_app_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="agentStatus" /> | `string` | Status of the NewRelic agent installed on the App service. |
| <CopyableCode code="agentVersion" /> | `string` | Version of the NewRelic agent installed on the App service. |
| <CopyableCode code="azureResourceId" /> | `string` | Azure App service resource ID |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId, data__userEmail" /> | List the app service resources currently being monitored by the NewRelic resource. |

## `SELECT` examples

List the app service resources currently being monitored by the NewRelic resource.


```sql
SELECT
agentStatus,
agentVersion,
azureResourceId
FROM azure_isv.newrelic.monitors_app_services
WHERE monitorName = '{{ monitorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__userEmail = '{{ data__userEmail }}';
```