---
title: service_members_global_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_global_configurations
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

Creates, updates, deletes, gets or lists a <code>service_members_global_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_members_global_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.service_members_global_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="featureSet" /> | `array` | The list of additional feature sets. |
| <CopyableCode code="numSavedPwdEvent" /> | `integer` | The number of saved password events. |
| <CopyableCode code="passwordSyncEnabled" /> | `boolean` | Indicates if password sync is enabled or not. |
| <CopyableCode code="schemaXml" /> | `string` | The schema for the configuration. |
| <CopyableCode code="version" /> | `integer` | The version for the global configuration. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> | Gets the global configuration. |

## `SELECT` examples

Gets the global configuration.


```sql
SELECT
featureSet,
numSavedPwdEvent,
passwordSyncEnabled,
schemaXml,
version
FROM azure.ad_hybrid_health_service.service_members_global_configurations
WHERE serviceMemberId = '{{ serviceMemberId }}'
AND serviceName = '{{ serviceName }}';
```