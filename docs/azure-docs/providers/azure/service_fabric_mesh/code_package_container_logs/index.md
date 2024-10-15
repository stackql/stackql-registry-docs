---
title: code_package_container_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - code_package_container_logs
  - service_fabric_mesh
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

Creates, updates, deletes, gets or lists a <code>code_package_container_logs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>code_package_container_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.code_package_container_logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="content" /> | `string` | Container logs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationResourceName, codePackageName, replicaName, resourceGroupName, serviceResourceName, subscriptionId" /> | Gets the logs for the container of the specified code package of the service replica. |

## `SELECT` examples

Gets the logs for the container of the specified code package of the service replica.


```sql
SELECT
content
FROM azure.service_fabric_mesh.code_package_container_logs
WHERE applicationResourceName = '{{ applicationResourceName }}'
AND codePackageName = '{{ codePackageName }}'
AND replicaName = '{{ replicaName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceResourceName = '{{ serviceResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```