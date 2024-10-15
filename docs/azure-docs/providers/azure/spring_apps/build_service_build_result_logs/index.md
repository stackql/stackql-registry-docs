---
title: build_service_build_result_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - build_service_build_result_logs
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>build_service_build_result_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>build_service_build_result_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.build_service_build_result_logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobUrl" /> | `string` | The public download URL of this build result log |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="buildName, buildResultName, buildServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get a KPack build result log download URL. |

## `SELECT` examples

Get a KPack build result log download URL.


```sql
SELECT
blobUrl
FROM azure.spring_apps.build_service_build_result_logs
WHERE buildName = '{{ buildName }}'
AND buildResultName = '{{ buildResultName }}'
AND buildServiceName = '{{ buildServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```