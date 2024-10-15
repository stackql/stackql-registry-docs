---
title: service_members_connector_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_connector_metadata
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

Creates, updates, deletes, gets or lists a <code>service_members_connector_metadata</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_members_connector_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.service_members_connector_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connectors" /> | `array` | The list of connectors. |
| <CopyableCode code="runProfileNames" /> | `array` | The list of run profile names. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="metricName, serviceMemberId, serviceName" /> | Gets the list of connectors and run profile names. |

## `SELECT` examples

Gets the list of connectors and run profile names.


```sql
SELECT
connectors,
runProfileNames
FROM azure.ad_hybrid_health_service.service_members_connector_metadata
WHERE metricName = '{{ metricName }}'
AND serviceMemberId = '{{ serviceMemberId }}'
AND serviceName = '{{ serviceName }}';
```